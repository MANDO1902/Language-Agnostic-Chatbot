from flask import Flask, request, jsonify
from flask_cors import CORS # For handling CORS if frontend and backend are on different ports/domains

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Dummy Data for Chatbot Training (Replace with your actual training data/model)
# This simulates a very basic keyword-based understanding
dummy_data = {
    "en": {
        "hello": "Hello! How can I assist you today? I can help with admissions, courses, and general university information.",
        "hi": "Hello! I'm here to help.",
        "admission": "Our admission requirements vary by program. Please visit our 'Admissions' page on the main website for detailed information, or tell me which program you are interested in.",
        "course": "We offer a wide range of courses in engineering, arts, science, and commerce. Which field are you interested in?",
        "fee": "Fee structures are available on the admissions section of our website. Do you want to know about a specific course fee?",
        "timing": "Our university office hours are Monday to Friday, 9 AM to 5 PM.",
        "contact": "You can reach our administrative office at +91-1234567890 or email info@university.edu.",
        "thank you": "You're welcome! Is there anything else I can help you with?",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "I am the University Chatbot, designed to help students and visitors.",
        "how are you": "I'm doing great, thank you for asking! How can I help you?",
        "placement": "Our university has a dedicated placement cell that works tirelessly to connect students with top companies. Visit our placements page for success stories and details.",
        "scholarship": "We offer various scholarships based on merit and need. You can find detailed information on our 'Scholarships' section on the website.",
        "hostel": "Yes, we provide on-campus hostel facilities for both male and female students. Details about availability and application can be found on the student services portal."
    },
    "hi": {
        "namaste": "नमस्ते! मैं आपकी कैसे सहायता कर सकता हूँ? मैं प्रवेश, पाठ्यक्रमों और विश्वविद्यालय की सामान्य जानकारी में मदद कर सकता हूँ।",
        "hello": "नमस्ते! मैं आपकी कैसे सहायता कर सकता हूँ?",
        "admission": "हमारे प्रवेश के लिए आवश्यकताएँ कार्यक्रम के अनुसार अलग-अलग होती हैं। कृपया विस्तृत जानकारी के लिए मुख्य वेबसाइट पर हमारे 'प्रवेश' पृष्ठ पर जाएँ, या मुझे बताएं कि आप किस कार्यक्रम में रुचि रखते हैं।",
        "course": "हम इंजीनियरिंग, कला, विज्ञान और वाणिज्य में कई प्रकार के पाठ्यक्रम प्रदान करते हैं। आप किस क्षेत्र में रुचि रखते हैं?",
        "fee": "शुल्क संरचनाएँ हमारी वेबसाइट के प्रवेश अनुभाग में उपलब्ध हैं। क्या आप किसी विशिष्ट पाठ्यक्रम के शुल्क के बारे में जानना चाहते हैं?",
        "timing": "हमारे विश्वविद्यालय कार्यालय का समय सोमवार से शुक्रवार, सुबह 9 बजे से शाम 5 बजे तक है।",
        "contact": "आप हमारे प्रशासनिक कार्यालय से +91-1234567890 पर संपर्क कर सकते हैं या info@university.edu पर ईमेल कर सकते हैं।",
        "thank you": "आपका स्वागत है! क्या मैं आपकी और किसी तरह से मदद कर सकता हूँ?",
        "bye": "अलविदा! आपका दिन शुभ हो!",
        "what is your name": "मैं विश्वविद्यालय चैटबॉट हूँ, जिसे छात्रों और आगंतुकों की सहायता के लिए डिज़ाइन किया गया है।",
        "how are you": "मैं बहुत अच्छा हूँ, पूछने के लिए धन्यवाद! मैं आपकी कैसे मदद कर सकता हूँ?",
        "placement": "हमारे विश्वविद्यालय में एक समर्पित प्लेसमेंट सेल है जो छात्रों को शीर्ष कंपनियों से जोड़ने के लिए अथक प्रयास करता है। सफलता की कहानियों और विवरणों के लिए हमारे प्लेसमेंट पेज पर जाएँ।",
        "scholarship": "हम योग्यता और आवश्यकता के आधार पर विभिन्न छात्रवृत्तियाँ प्रदान करते हैं। आप हमारी वेबसाइट के 'छात्रवृत्तियाँ' अनुभाग में विस्तृत जानकारी प्राप्त कर सकते हैं।",
        "hostel": "हाँ, हम पुरुष और महिला दोनों छात्रों के लिए ऑन-कैंपस छात्रावास सुविधाएँ प्रदान करते हैं। उपलब्धता और आवेदन के बारे में विवरण छात्र सेवा पोर्टल पर पाया जा सकता है।"
    }
}

# Fallback messages when no answer is found
fallback_messages = {
    "en": "I'm sorry, I don't have information on that topic. Would you like to talk to a human support agent?",
    "hi": "मुझे क्षमा करें, मेरे पास इस विषय पर जानकारी नहीं है। क्या आप मानव सहायता एजेंट से बात करना चाहेंगे?"
}


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').lower()
    language = request.json.get('lang', 'en') # Default to English

    response_data = {
        "answer": "",
        "human_support_option": False,
        "human_support_message": ""
    }

    # Simulate basic keyword matching
    found_answer = False
    for keyword, answer in dummy_data.get(language, {}).items():
        if keyword in user_message:
            response_data["answer"] = answer
            found_answer = True
            break
    
    # If no direct answer found, use fallback
    if not found_answer:
        response_data["answer"] = fallback_messages[language]
        response_data["human_support_option"] = True
        response_data["human_support_message"] = fallback_messages[language]
    
    # Special handling for "hello" to ensure a good first interaction
    if "hello" in user_message or "hi" in user_message:
        response_data["answer"] = dummy_data[language].get("hello", fallback_messages[language])
        response_data["human_support_option"] = False # No human support for initial greeting

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Run on port 5000