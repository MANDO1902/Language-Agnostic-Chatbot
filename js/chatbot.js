document.addEventListener('DOMContentLoaded', () => {
    const chatbotLogo = document.getElementById('chatbot-logo');
    const chatbotInterface = document.getElementById('chatbot-interface');
    const chatbotMessages = document.getElementById('chatbot-messages');
    const chatbotInput = document.getElementById('chatbot-input');
    const chatbotSendBtn = document.getElementById('chatbot-send-btn');
    const languageSwitcher = document.getElementById('language-switcher');

    let currentLanguage = 'en'; // Default language

    // --- Chatbot Logo Toggle ---
    chatbotLogo.addEventListener('click', () => {
        chatbotInterface.classList.toggle('hidden');
        if (!chatbotInterface.classList.contains('hidden')) {
            // If opening, send a welcome message
            if (chatbotMessages.children.length === 0) {
                sendMessageToBot({ message: "Hello", lang: currentLanguage });
            }
            chatbotInput.focus();
        }
    });

    // --- Language Switching ---
    languageSwitcher.addEventListener('click', (event) => {
        if (event.target.tagName === 'BUTTON') {
            document.querySelectorAll('#language-switcher button').forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');
            currentLanguage = event.target.dataset.lang;
            console.log(`Switched to language: ${currentLanguage}`);
            // Optionally, send a language change message to the bot or clear chat history
            chatbotMessages.innerHTML = ''; // Clear chat on language switch
            sendMessageToBot({ message: "Hello", lang: currentLanguage }); // Send a new welcome message
        }
    });

    // --- Send Message Function ---
    const sendMessage = () => {
        const userMessage = chatbotInput.value.trim();
        if (userMessage) {
            appendMessage(userMessage, 'user');
            sendMessageToBot({ message: userMessage, lang: currentLanguage });
            chatbotInput.value = '';
        }
    };

    chatbotSendBtn.addEventListener('click', sendMessage);
    chatbotInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    // --- Append Message to Chat Interface ---
    const appendMessage = (text, sender) => {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);
        messageDiv.textContent = text;
        chatbotMessages.appendChild(messageDiv);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight; // Scroll to bottom
    };

    // --- Simulate Chatbot Response (Replace with actual API call later) ---
    const sendMessageToBot = async (data) => {
        // Show a "typing" indicator or spinner here if desired
        // For now, let's simulate a delay
        appendMessage('Thinking...', 'bot'); // Temporary placeholder

        try {
            const response = await fetch('/chat', { // This will hit your Flask/Python backend
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });
            const botResponse = await response.json();

            // Remove the "Thinking..." message
            if (chatbotMessages.lastChild && chatbotMessages.lastChild.textContent === 'Thinking...') {
                chatbotMessages.removeChild(chatbotMessages.lastChild);
            }

            appendMessage(botResponse.answer, 'bot');

            if (botResponse.human_support_option) {
                displayHumanSupportOption(botResponse.human_support_message || "I couldn't find an answer. Would you like to talk to a human?");
            }

        } catch (error) {
            console.error('Error communicating with chatbot backend:', error);
            // Remove the "Thinking..." message
            if (chatbotMessages.lastChild && chatbotMessages.lastChild.textContent === 'Thinking...') {
                chatbotMessages.removeChild(chatbotMessages.lastChild);
            }
            appendMessage("Sorry, I'm having trouble connecting right now. Please try again later.", 'bot');
            displayHumanSupportOption("Connection issue. Would you like to talk to a human?");
        }
    };

    // --- Display Human Support Option ---
    const displayHumanSupportOption = (message) => {
        const humanSupportDiv = document.createElement('div');
        humanSupportDiv.classList.add('human-support-option');
        humanSupportDiv.innerHTML = `<p>${message}</p><button id="human-support-btn">Connect to Support</button>`;
        chatbotMessages.appendChild(humanSupportDiv);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;

        document.getElementById('human-support-btn').addEventListener('click', () => {
            alert('Connecting to human support... (This would typically open a new chat window or form)');
            // In a real application, this would trigger a different flow
            // e.g., open a new tab to a live chat system, or send an email.
            humanSupportDiv.remove(); // Remove the option after clicking
            appendMessage("You've requested human support. Please wait while we connect you.", 'bot');
        });
    };

    // Initial welcome message when chatbot loads (hidden state)
    // This will be triggered when the logo is clicked for the first time
});