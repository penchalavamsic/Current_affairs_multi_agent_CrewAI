
# 🌍 Current Affairs News Summary App

This app fetches and summarizes the top 10 current global and Indian news headlines using AI agents powered by **CrewAI** and **Gemini** (Google's LLM). It runs in **Streamlit** with simple one-click interaction to get one-liner summaries of trending news.

---

## 🚀 Features

- 🔎 **AI Research Agent**: Gathers the top current affairs using Firecrawl.
- 🧠 **AI Summarizer Agent**: Converts complex news into one-liner summaries.
- 📋 **Streamlit UI**: Clean and interactive web interface.
- 🧠 **Powered by Gemini**: Uses Gemini Flash model for quick, accurate insights.

---

## 📁 Project Structure

```
current-affairs-app/
│
├── .env                      # Stores your API keys (not shared)
├── app.py                   # Main Streamlit application
├── README.md                # This file
├── requirements.txt         # Required dependencies
```

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/current-affairs-app.git
cd current-affairs-app
```

### 2. Set up your virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

Create a `.env` file in the root directory and add your API keys:

```env
GEMINI_API_KEY=your_gemini_api_key_here
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to see the app in action.

---

## 🔐 Get API Keys

- **Gemini API**: https://makersuite.google.com/app
- **Firecrawl API**: https://firecrawl.dev

---

## 📦 Requirements

Your `requirements.txt` file should include:

```txt
python-dotenv
streamlit
crewai
crewai-tools
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🧠 Credits

Built using:

- [CrewAI](https://github.com/joaomdmoura/crewai)
- [Gemini](https://ai.google.dev)
- [Streamlit](https://streamlit.io/)
- [Firecrawl Search Tool](https://firecrawl.dev)

---

## 📄 License

MIT License – feel free to fork and improve!
