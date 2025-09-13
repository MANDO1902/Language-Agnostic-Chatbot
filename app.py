from flask import Flask, request, jsonify
from flask_cors import CORS # For handling CORS if frontend and backend are on different ports/domains

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Data for Chatbot
dummy_data = {
    "en": {
        "hello": "Hello! I am the Quantum University chatbot. I can help with admissions, courses, fees, and other university information.",
        "hi": "Hi there! I'm the Quantum University chatbot. How can I assist you today?",
        "admission": "For undergraduate programs at Quantum University, you need to have completed your high school education with a minimum of 75% in Physics, Chemistry, and Mathematics. For postgraduate programs, a bachelor's degree in a relevant field with a CGPA of 6.5 or higher is required. The application deadline is July 31st for all programs.",
        "course": "Quantum University offers a variety of courses. In Engineering, we have Computer Science, Mechanical, and Electronics. In Sciences, we offer Physics, Chemistry, and Mathematics. We also have a strong Arts department with programs in History, Literature, and Philosophy. Which one are you interested in?",
        "computer science": "Our Computer Science program includes courses in Artificial Intelligence, Machine Learning, Data Science, and Cybersecurity. The fee is $10,000 per year.",
        "mechanical": "The Mechanical Engineering program focuses on robotics, thermodynamics, and fluid mechanics. The annual fee is $9,000.",
        "electronics": "Our Electronics Engineering program covers topics like circuit design, signal processing, and embedded systems. The fee is $9,500 per year.",
        "physics": "The Physics program at Quantum University delves into quantum mechanics, relativity, and astrophysics. The annual fee is $8,000.",
        "chemistry": "Our Chemistry program offers specializations in organic, inorganic, and physical chemistry. The fee is $8,500 per year.",
        "mathematics": "The Mathematics program includes courses in algebra, calculus, and statistics. The annual fee is $7,500.",
        "history": "Our History program covers world history, ancient civilizations, and modern history. The fee is $7,000 per year.",
        "literature": "The Literature program explores classic and contemporary literature from around the world. The annual fee is $6,500.",
        "philosophy": "Our Philosophy program covers topics like ethics, metaphysics, and logic. The fee is $6,000 per year.",
        "fee": "The fee structure varies by program. For a specific course's fee, please mention the course name.",
        "timing": "The university is open from 9 AM to 5 PM, Monday to Friday. The library is open until 10 PM on weekdays and is closed on weekends.",
        "contact": "You can contact Quantum University at contact@quantumuniversity.edu or call us at +1-123-456-7890.",
        "thank you": "You're welcome! Let me know if you have any other questions.",
        "bye": "Goodbye! Have a great day.",
        "what is your name": "I am the Quantum University chatbot.",
        "how are you": "I'm a chatbot, so I don't have feelings, but I'm here to help you!",
        "placement": "Quantum University has a 95% placement rate. Our top recruiters include Google, Microsoft, and Amazon. The average salary package is $100,000 per year.",
        "scholarship": "We offer merit-based scholarships to the top 10% of students in each program. There are also need-based scholarships available. Please visit the scholarships page on our website for more details.",
        "hostel": "We have separate hostels for undergraduate and postgraduate students. The hostel fee is $2,000 per year, which includes meals. All rooms are single occupancy and have attached bathrooms."
    },
    "hi": {
        "namaste": "नमस्ते! मैं क्वांटम विश्वविद्यालय चैटबॉट हूँ। मैं प्रवेश, पाठ्यक्रम, शुल्क और विश्वविद्यालय की अन्य जानकारी में आपकी मदद कर सकता हूँ।",
        "hello": "नमस्ते! मैं क्वांटम विश्वविद्यालय चैटबॉट हूँ। मैं आज आपकी कैसे सहायता कर सकता हूँ?",
        "admission": "क्वांटम विश्वविद्यालय में स्नातक कार्यक्रमों के लिए, आपको अपनी उच्च विद्यालय की शिक्षा भौतिकी, रसायन विज्ञान और गणित में न्यूनतम 75% के साथ पूरी करनी होगी। स्नातकोत्तर कार्यक्रमों के लिए, 6.5 या उससे अधिक के सीजीपीए के साथ संबंधित क्षेत्र में स्नातक की डिग्री आवश्यक है। सभी कार्यक्रमों के लिए आवेदन की अंतिम तिथि 31 जुलाई है।",
        "course": "क्वांटम विश्वविद्यालय विभिन्न प्रकार के पाठ्यक्रम प्रदान करता है। इंजीनियरिंग में, हमारे पास कंप्यूटर विज्ञान, मैकेनिकल और इलेक्ट्रॉनिक्स हैं। विज्ञान में, हम भौतिकी, रसायन विज्ञान और गणित प्रदान करते हैं। हमारे पास इतिहास, साहित्य और दर्शनशास्त्र में कार्यक्रमों के साथ एक मजबूत कला विभाग भी है। आप किसमें रुचि रखते हैं?",
        "computer science": "हमारे कंप्यूटर विज्ञान कार्यक्रम में आर्टिफिशियल इंटेलिजेंस, मशीन लर्निंग, डेटा साइंस और साइबर सुरक्षा के पाठ्यक्रम शामिल हैं। शुल्क प्रति वर्ष $10,000 है।",
        "mechanical": "मैकेनिकल इंजीनियरिंग कार्यक्रम रोबोटिक्स, थर्मोडायनामिक्स और द्रव यांत्रिकी पर केंद्रित है। वार्षिक शुल्क $9,000 है।",
        "electronics": "हमारे इलेक्ट्रॉनिक्स इंजीनियरिंग कार्यक्रम में सर्किट डिजाइन, सिग्नल प्रोसेसिंग और एम्बेडेड सिस्टम जैसे विषय शामिल हैं। शुल्क प्रति वर्ष $9,500 है।",
        "physics": "क्वांटम विश्वविद्यालय में भौतिकी कार्यक्रम क्वांटम यांत्रिकी, सापेक्षता और खगोल भौतिकी में delves है। वार्षिक शुल्क $8,000 है।",
        "chemistry": "हमारा रसायन विज्ञान कार्यक्रम कार्बनिक, अकार्बनिक और भौतिक रसायन विज्ञान में विशेषज्ञता प्रदान करता है। शुल्क प्रति वर्ष $8,500 है।",
        "mathematics": "गणित कार्यक्रम में बीजगणित, कलन और सांख्यिकी के पाठ्यक्रम शामिल हैं। वार्षिक शुल्क $7,500 है।",
        "history": "हमारे इतिहास कार्यक्रम में विश्व इतिहास, प्राचीन सभ्यताएं और आधुनिक इतिहास शामिल हैं। शुल्क प्रति वर्ष $7,000 है।",
        "literature": "साहित्य कार्यक्रम दुनिया भर से क्लासिक और समकालीन साहित्य की पड़ताल करता है। वार्षिक शुल्क $6,500 है।",
        "philosophy": "हमारे दर्शनशास्त्र कार्यक्रम में नैतिकता, तत्वमीमांसा और तर्क जैसे विषय शामिल हैं। शुल्क प्रति वर्ष $6,000 है।",
        "fee": "शुल्क संरचना कार्यक्रम के अनुसार भिन्न होती है। किसी विशिष्ट पाठ्यक्रम के शुल्क के लिए, कृपया पाठ्यक्रम का नाम बताएं।",
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