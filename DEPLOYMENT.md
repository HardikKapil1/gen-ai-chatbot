# Deployment Instructions for Streamlit Cloud

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `gen-ai-chatbot` (or your preferred name)
3. Make it **Public** (required for free Streamlit deployment)
4. Don't initialize with README (we already have one)
5. Click "Create repository"

## Step 2: Push Code to GitHub

Run these commands in your terminal:

```bash
git remote add origin https://github.com/YOUR_USERNAME/gen-ai-chatbot.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `gen-ai-chatbot`
5. Main file path: `app.py`
6. Click "Advanced settings"
7. Add your secret:
   - Key: `GEMINI_API_KEY`
   - Value: `AIzaSyCttv16oZI2B_i09Z7UHHlikAk4OOkVTS0`
8. Click "Deploy!"

Your chatbot will be live at: `https://YOUR_USERNAME-gen-ai-chatbot.streamlit.app`

## Notes

- The `.env` file is in `.gitignore` so your API key won't be pushed to GitHub
- You must add the API key in Streamlit Cloud's secrets settings
- Deployment is completely free on Streamlit Community Cloud
