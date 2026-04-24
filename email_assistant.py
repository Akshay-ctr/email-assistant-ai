from groq import Groq
from dotenv import load_dotenv
import os
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
GMAIL_EMAIL = os.getenv("GMAIL_EMAIL")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

seen_ids = set()

def summarise_email(body):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Summarise this email in 2 lines:\n\n{body}"}]
    )
    return response.choices[0].message.content

def draft_reply(body, tone):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": f"Draft a {tone} reply to this email in 3-4 lines. Sign off with the name 'VISON':\n\n{body}"}]
    )
    return response.choices[0].message.content

def fetch_unread_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
    mail.select("inbox")
    
    _, messages = mail.search(None, "UNSEEN")
    email_ids = messages[0].split()
    
    if not email_ids:
        print(".", end="", flush=True)
        mail.logout()
        return []
    
    emails = []
    for eid in email_ids:
        if eid in seen_ids:
            continue
        _, msg_data = mail.fetch(eid, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        subject = msg["subject"]
        sender = msg["from"]
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors="ignore")
                    break
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        emails.append((eid, sender, subject, body))
        seen_ids.add(eid)
    
    mail.logout()
    return emails

def send_reply(to, subject, body):
    msg = MIMEMultipart()
    msg["From"] = GMAIL_EMAIL
    msg["To"] = to
    msg["Subject"] = "Re: " + subject
    msg.attach(MIMEText(body, "plain"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_EMAIL, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_EMAIL, to, msg.as_string())

print("📧 EMAIL ASSISTANT — Watching inbox... (Ctrl+C to stop)")
print("Checking every 30 seconds. Dots = checking...\n")

while True:
    try:
        new_emails = fetch_unread_emails()

        for eid, sender, subject, body in new_emails:
            print(f"\n\n{'='*50}")
            print(f"📨 From: {sender}")
            print(f"📌 Subject: {subject}")
            print(f"\n📧 SUMMARY:")
            print(summarise_email(body))

            print("\n✏️ CHOOSE TONE:")
            print("1. Professional  2. Friendly  3. Assertive  4. Skip")
            choice = input("\nEnter 1, 2, 3 or 4: ")

            if choice == "4":
                print("⏭️ Skipped.")
                continue

            tones = {"1": "professional", "2": "friendly", "3": "assertive"}
            tone = tones.get(choice, "professional")

            reply = draft_reply(body, tone)
            print(f"\n📝 DRAFT REPLY ({tone.upper()}):")
            print(reply)

            send = input("\nSend this reply? (yes/no): ")
            if send.lower() == "yes":
                send_reply(sender, subject, reply)
                print("✅ Reply sent!")
            else:
                print("❌ Reply not sent.")

    except Exception as e:
        print(f"\n⚠️ Error: {e}")

    time.sleep(30)