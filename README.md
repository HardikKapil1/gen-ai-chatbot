# Gen AI Chatbot

A conversational AI chatbot powered by Google Gemini and built with Streamlit.

## Features

- 💬 Real-time streaming responses
- 🎨 Clean and intuitive user interface
- 📝 Conversation history management
- 🔄 Easy chat reset functionality

## Setup

1. **Clone or download this project**

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Set up your Google Gemini API key:**
   - Copy `.env.example` to `.env`
   - Add your Gemini API key to the `.env` file:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - Get a free API key at https://makersuite.google.com/app/apikey

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Open your browser to the URL shown in the terminal (usually `http://localhost:8501`)
2. Type your message in the chat input at the bottom
3. Press Enter or click Send
4. Watch as the AI responds in real-time
5. Use the "Clear Chat History" button in the sidebar to start a new conversation

## Requirements

- Python 3.8+
- Google Gemini API key (get one free at https://makersuite.google.com/app/apikey)

## Project Structure

```
.
├── app.py              # Main Streamlit application
├── pyproject.toml      # Project dependencies
├── .env               # Environment variables (create from .env.example)
├── .env.example       # Example environment file
└── README.md          # This file
```

## Customization

You can customize the chatbot by modifying `app.py`:
- Change the AI model (e.g., `gemini-pro`, `gemini-pro-vision`)
- Adjust the page title and icon
- Add system prompts for specific behavior
- Modify the UI layout and styling

## License

MIT License - Feel free to use and modify as needed.
