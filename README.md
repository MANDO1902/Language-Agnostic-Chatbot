# Language-Agnostic Chatbot 🤖

A bilingual university chatbot built with Flask and JavaScript that provides information about Quantum University in both English and Hindi.

## 🌟 Features

- **Bilingual Support**: Supports both English and Hindi languages
- **University Information**: Comprehensive details about courses, admissions, fees, and facilities
- **Interactive UI**: Modern chatbot interface with smooth animations
- **Language Switching**: Easy toggle between English and Hindi
- **Human Support**: Fallback to human support for unrecognized queries
- **Responsive Design**: Works on desktop and mobile devices

## 🏗️ Project Structure

```
Language-Agnostic-Chatbot/
├── app.py                 # Flask backend server
├── index.html            # Main HTML page
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── css/
│   ├── style.css        # Main website styling
│   └── chatbot.css      # Chatbot interface styling
├── js/
│   └── chatbot.js       # Chatbot frontend logic
└── images/
    └── chatbot-icon.png # Chatbot icon
```

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project**
   ```bash
   cd Language-Agnostic-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

5. **Start chatting!**
   Click the blue chatbot icon in the bottom-right corner

## 💬 Supported Queries

### English Queries
- **Greetings**: "hello", "hi", "hii"
- **Admissions**: "admission", "requirements"
- **Courses**: "course", "computer science", "mechanical", "electronics", "physics", "chemistry", "mathematics", "history", "literature", "philosophy"
- **Fees**: "fee", "cost", "price"
- **University Info**: "contact", "timing", "placement", "scholarship", "hostel"
- **General**: "thank you", "bye", "what is your name", "how are you"

### Hindi Queries  
- **Greetings**: "namaste", "hello"
- **Admissions**: "admission" (प्रवेश)
- **Courses**: "course" (पाठ्यक्रम)
- **And many more in Hindi...**

## 🎯 How It Works

1. **Frontend**: HTML/CSS/JavaScript provides the user interface
2. **Backend**: Flask server handles API requests and responses
3. **Language Detection**: Automatic language switching based on user preference
4. **Keyword Matching**: Simple keyword-based response system
5. **Fallback**: Human support option for unrecognized queries

## 🛠️ Technical Details

### Backend (Flask)
- **Framework**: Flask 3.1.2
- **CORS**: Enabled for cross-origin requests
- **Routes**: 
  - `/` - Serves the main HTML page
  - `/chat` - Handles chatbot API requests
  - `/css/`, `/js/`, `/images/` - Serves static files

### Frontend (JavaScript)
- **Modern ES6+** JavaScript
- **Fetch API** for HTTP requests
- **DOM manipulation** for dynamic UI updates
- **Event handling** for user interactions

### Styling (CSS)
- **Responsive design** with Flexbox
- **CSS animations** for smooth interactions
- **Professional color scheme** (#007bff blue theme)
- **Mobile-friendly** interface

## 🎨 Customization

### Adding New Responses
Edit `app.py` and add new entries to the `dummy_data` dictionary:

```python
dummy_data = {
    "en": {
        "your_keyword": "Your response in English",
        # ... more entries
    },
    "hi": {
        "your_keyword": "आपका हिंदी में उत्तर",
        # ... more entries
    }
}
```

### Styling Changes
- **Main website**: Edit `css/style.css`
- **Chatbot interface**: Edit `css/chatbot.css`
- **Colors**: Update CSS custom properties or color variables

### Adding Languages
1. Add new language data in `dummy_data` dictionary
2. Add new language button in `index.html`
3. Update JavaScript language switching logic

## 🔧 Development

### Running in Development Mode
The Flask app runs in debug mode by default:
```bash
python app.py
```
- **Auto-reload**: Server restarts on file changes
- **Debug info**: Detailed error messages
- **Port**: Runs on `http://localhost:5000`

### API Testing
You can test the API directly:
```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"message":"hello","lang":"en"}' \
     http://localhost:5000/chat
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill existing Python processes
   taskkill /f /im python.exe
   ```

2. **Module not found error**
   ```bash
   pip install -r requirements.txt
   ```

3. **CSS/JS not loading**
   - Make sure you're accessing `http://localhost:5000` (not opening HTML file directly)
   - Check browser console for errors

4. **CORS issues**
   - Flask-CORS is enabled by default
   - If issues persist, check browser network tab

## 📞 Support

For support, please:
1. Check the troubleshooting section
2. Open an issue on the repository
3. Contact the development team

## 📈 Future Enhancements

- [ ] Add more languages (Spanish, French, etc.)
- [ ] Integrate with real university database
- [ ] Add voice input/output capabilities
- [ ] Implement machine learning for better responses
- [ ] Add user authentication
- [ ] Create admin panel for content management

---

**Made with ❤️ for Quantum University**
