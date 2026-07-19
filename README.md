# MediAura

# Build-a-Complete-Medical-Chatbot-with-Gemini-LangChain-Pinecone-Flask-AWS

## 🚀 How to Run

### Step 1: Clone the repository

```bash
git clone https://github.com/<your-github-username>/MediAura.git
```

Replace `<your-github-username>` with your GitHub username.

---

## Step 2: Create a Conda Environment

```bash
conda create -n medibot python=3.10 -y
```

Activate the environment:

```bash
conda activate medibot
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Create a `.env` File

Create a `.env` file in the root directory and add your API keys.

```ini
PINECONE_API_KEY=your_pinecone_api_key
GOOGLE_API_KEY=your_google_ai_studio_api_key
```

---

## Step 5: Store Embeddings in Pinecone

Run the following command to create embeddings and upload them to Pinecone.

```bash
python store_index.py
```

---

## Step 6: Run the Flask Application

```bash
python app.py
```

---

## Step 7: Open the Application

Open your browser and visit:

```text
http://127.0.0.1:8080
```

---

# 🛠️ Tech Stack

- Python
- Flask
- LangChain
- Google Gemini 2.5 Flash
- HuggingFace Embeddings
- Pinecone Vector Database
- HTML
- CSS
- Bootstrap
- jQuery

---

# ☁️ AWS CI/CD Deployment using GitHub Actions

## 1. Login to AWS Console

---

## 2. Create an IAM User

Grant the following permissions:

- AmazonEC2ContainerRegistryFullAccess
- AmazonEC2FullAccess

---

## 3. Create an Amazon ECR Repository

Example:

```
315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
```

Save the repository URI.

---

## 4. Launch an EC2 Instance (Ubuntu)

---

## 5. Install Docker on EC2

Update packages:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

---

## 6. Configure EC2 as a Self-Hosted GitHub Runner

Go to:

```
GitHub Repository
→ Settings
→ Actions
→ Runners
→ New Self-hosted Runner
```

Follow the commands displayed by GitHub.

---

## 7. Configure GitHub Secrets

Add the following repository secrets:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
- PINECONE_API_KEY
- GOOGLE_API_KEY