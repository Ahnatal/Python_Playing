from email.message import EmailMessage
import ssl
import smtplib

email_sender = "dein_Email"
email_kennwort = "Email_kennwort"

email_empfanger = ""

betreff = "Betreff"
body = """Wie war dein Wochenende
"""

em = EmailMessage()
em["Von"] = email_sender
em["An"] = email_empfanger
em["betreff"] = betreff
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as SMTP:
    smtplib.login(email_sender, email_kennwort)
    SMTP.sendmail(email_sender, email_empfanger, em.as_string())
