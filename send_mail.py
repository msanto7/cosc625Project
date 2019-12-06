import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '35a39f4efd749e'
    password = '6d40456c116f80'
    message= f"<h3> New Feedback Submission</h3><ul><li>Customer: {customer}</li></ul>"

    sender_email = 'email1@example.com'
    reciever_email = 'email2example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback'
    msg['From'] = sender_email
    msg['To'] = reciever_email

    # Send email 
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, reciever_email, msg.as_string())