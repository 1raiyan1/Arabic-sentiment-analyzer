# Arabic Sentiment Analyzer 🌍🤖

An AI-powered sentiment analysis web application that supports both **Arabic** and **English** text. The application automatically detects language, analyzes sentiment, and provides confidence scores using LLMs.

---

## App Preview
<img width="1911" height="1079" alt="image" src="https://github.com/user-attachments/assets/92092aa5-4c5a-43e9-94a8-293aa22dd24b" />


## 🚀 Features

- Detects Arabic and English text automatically
- Performs sentiment analysis (Positive / Negative / Neutral)
- Shows confidence score
- FastAPI backend
- Streamlit frontend
- Groq LLM integration
- Simple interactive UI

---

## 📌 Demo Example

### Input (Arabic)

أنا سعيد جدا اليوم

### Output

Language: Arabic  
Sentiment: Positive  
Confidence: 96%

---

### Input (English)

I am feeling stressed today.

### Output

Language: English  
Sentiment: Negative  
Confidence: 91%

---

## 🛠 Tech Stack

- Python
- FastAPI
- Streamlit
- Groq API
- Requests
- Uvicorn
- python-dotenv

---

## 📂 Project Structure

```bash
Arabic-sentiment-analyzer/
│
├── app/
│   ├── __init__.py
│   ├── analyzer.py
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/1raiyan1/Arabic-sentiment-analyzer.git
cd Arabic-sentiment-analyzer
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

## ▶️ Run Frontend

```bash
streamlit run streamlit_app.py
```

---

## 🔮 Future Improvements

- Sentiment visualization charts
- Batch sentiment analysis
- Export reports
- Emotion detection
- Support for more languages

---

## 👨‍💻 Author

**Ahmed Raiyan**  
AI & ML Engineer | AI Automation Specialist | Workflow Automation Enthusiast

GitHub:  
https://github.com/1raiyan1

---

## ⭐ Why This Project?

Most beginner sentiment analyzers only focus on English datasets. This project adds **Arabic sentiment analysis support**, making it useful for multilingual applications and potentially relevant for Gulf-region AI markets.

---

## 📄 License

This project is licensed under the MIT License.
