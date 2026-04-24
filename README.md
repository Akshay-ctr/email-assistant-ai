# AI Email Assistant 📧🤖

An AI-powered Gmail assistant built with Python, Groq, and Gmail that automatically monitors incoming emails, summarizes them, drafts smart replies in different tones, and sends replies only after user approval.

This project uses the **Llama 3.3 70B Versatile** model via Groq API for fast and intelligent email understanding and response generation based on your selected tone. The project details and workflow are based on the implementation shared in your code and setup notes .

---

## Features 🚀

* Fetches unread emails from Gmail inbox
* Summarizes emails in 2 concise lines
* Generates smart AI-based replies
* Multiple reply tones:

  * Professional
  * Friendly
  * Assertive
* Option to skip unwanted emails
* Manual approval before sending replies
* Auto signs replies with **VISON**
* Continuously watches inbox every 30 seconds
* Secure environment variable handling using `.env`

---

## Tech Stack 🛠️

* Python
* Groq API
* Llama 3.3 70B Versatile
* IMAP (for reading emails)
* SMTP (for sending emails)
* Gmail App Password
* python-dotenv

---

## Project Structure 📂

```text
email-assistant/
│
├── email_assistant.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── venv/
```

---

## Environment Variables 🔐

Create a `.env` file in the root folder:

```env
GROQ_API_KEY=your_groq_api_key
GMAIL_APP_PASSWORD=your_gmail_app_password
GMAIL_EMAIL=your_email@gmail.com
```

⚠️ Never push your real `.env` file to GitHub.

Use `.env.example` for safe public sharing.

---

## Installation ⚙️

### 1. Clone the repository

```bash
git clone https://github.com/Akshay-ctr/email-assistant-ai.git
cd email-assistant-ai
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Gmail Setup 📩

### Enable IMAP

* Open Gmail
* Go to Settings
* Click **See all settings**
* Open **Forwarding and POP/IMAP**
* Enable IMAP
* Save changes

### Generate Gmail App Password

* Enable 2-Step Verification
* Generate App Password from Google Account Security settings
* Use that password inside `.env`

---

## Run the Project ▶️

```bash
python email_assistant.py
```

You will see:

```text
📧 EMAIL ASSISTANT — Watching inbox...
Checking every 30 seconds...
```

The assistant checks for new unread emails and helps draft replies.

---

## How It Works 🔄

1. Detects unread emails
2. Shows sender and subject
3. Summarizes email content
4. Lets user choose reply tone
5. Generates AI reply draft
6. Asks final confirmation before sending

Nothing gets sent without your permission.

---

## Example Workflow 💡

```text
📨 From: client@example.com
📌 Subject: Project Update

📧 SUMMARY:
Client is asking for project timeline updates.

✏️ CHOOSE TONE:
1. Professional
2. Friendly
3. Assertive
4. Skip

📝 DRAFT REPLY:
Thank you for reaching out...

Send this reply? (yes/no):
```

---

## Future Improvements 🔥

* Web UI using Flask / React
* Sender-based filtering
* Priority email detection
* WhatsApp notifications
* Email history logs
* True autonomous AI Agent mode

---

## Author 👨‍💻

**Akshay**

Built as a real-world AI automation project using Python + Groq + Gmail integration.

---

## License 📄

This project is for educational and portfolio purposes.
