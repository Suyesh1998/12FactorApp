# 📊 Sentiment Analysis FastAPI App

A lightweight and purposeful web service that analyzes the sentiment of user-provided text using FastAPI. It classifies input as **positive**, **negative**, or **neutral** based on predefined keywords.

---

## 🚀 Features

- Simple REST API with a `/analyze` endpoint
- Accepts JSON input via POST request
- Returns sentiment classification
- ✅ Fully testable via `pytest`
- 🔄 CI/CD setup using GitHub Actions
- 🔍 Testable using Postman

---

## 🛠 How to Run Locally

### 🔹 1. Clone the Repository

```bash
git clone git@github.com:your-username/your-repo-name.git
cd your-repo-name
```

### 🔹 2. Create and Activate a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate        # For Linux/macOS
# OR
venv\Scripts\activate           # For Windows

```

### 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 🔹 4. Run the FastAPI App

```bash
uvicorn app.main:app --reload

```


## 📬 How to Use the API (e.g., in Postman)

### 🔸 Endpoint

```bash
POST http://127.0.0.1:8000/analyze

```

### 🔸 Body → Raw → JSON

```bash
{
  "text": "I love this project!"
}


```

### 🔸 Response

```bash
{
  "sentiment": "positive"
}


```
