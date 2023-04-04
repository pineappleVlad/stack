import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class MessageSendler:
    def send_mes(self, login, password, recipients, subject, message, gmail_smtp):
        msg = MIMEMultipart()
        msg["From"] = login
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(login, password)
        ms.sendmail(login, ms, msg.as_string())
        ms.quit()

    def recieve_mes(self, gmail_imap, login, password, header):
        mail = imaplib.IMAP4_SSL(gmail_imap)
        mail.login(login, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        result, data = mail.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == "__main__":
    gmail_smtp = "smtp.gmail.com"
    gmail_imap = "imap.gmail.com"
    login = "login@gmail.com"
    password = "qwerty"
    subject = "Subject"
    recipients = ["vasya@email.com", "petya@email.com"]
    message = "Message"
    header = None
    send_mes = MessageSendler()
    send_mes.send_mes(login, password, recipients, subject, message, gmail_smtp)
    send_mes.recieve_mes(gmail_imap, login, password, header)
