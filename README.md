# MediAura

AI-powered Medical Chatbot built using **Flask**, **LangChain**, **Google Gemini**, **Pinecone**, and **HuggingFace Embeddings**.

---

## 🌐 Live Demo

🚀 **Try the chatbot here:**

**https://mediaura-chatbot.onrender.com/**

---

## 🚀 Features

- Medical Question Answering
- Retrieval-Augmented Generation (RAG)
- Google Gemini 2.5 Flash
- Pinecone Vector Database
- Flask Web Interface

# 🚀 Features

- Medical Question Answering
- Retrieval-Augmented Generation (RAG)
- Google Gemini 2.5 Flash
- Pinecone Vector Database
- Flask Web Interface

---

# 🛠 Tech Stack

- Python
- Flask
- LangChain
- Google Gemini
- Pinecone
- HuggingFace Embeddings
- HTML
- CSS
- Bootstrap
- jQuery

---

# ⚙️ Local Setup

## 1. Clone the Repository

```bash
git clone https://github.com/<your-github-username>/MediAura-Chatbot.git
cd MediAura-Chatbot
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create a `.env` File

```env
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## 5. Upload Documents to Pinecone

```bash
python store_index.py
```

Run this command only once after adding your PDFs.

---

## 6. Run the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:8080
```

---

# ☁️ Deploy on Render

## 1. Push the Project to GitHub

```bash
git add .
git commit -m "Initial Commit"
git push origin main
```

---

## 2. Create a Web Service on Render

- New Web Service
- Connect your GitHub repository

---

## 3. Build Command

```bash
pip install -r requirements.txt
```

---

## 4. Start Command

```bash
gunicorn app:app
```

---

## 5. Environment Variables

Add the following variables in Render:

```
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_api_key
```

---

## 6. Deploy

Click **Deploy Web Service**.

Once deployment completes, your chatbot will be available at:

```
https://your-app-name.onrender.com
```

---

# 📂 Project Structure

```
MediAura-Chatbot
│
├── app.py
├── store_index.py
├── requirements.txt
├── runtime.txt
├── .python-version
├── src/
├── templates/
├── static/
└── data/
```

---

# 📜 License

This project is licensed under the MIT License.

# MediAura

AI-powered Medical Chatbot built using **Flask**, **LangChain**, **Google Gemini**, **Pinecone**, and **HuggingFace Embeddings**.

### 👨‍💻 Developed by **Priyam Rai**

