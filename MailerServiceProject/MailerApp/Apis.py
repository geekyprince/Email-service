from MailerService.settings import Sendgrid_API_KEY, Mailjet_API_KEY, Mailjet_API_SECRET
from mailjet_rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail



class SendgridMailApi:
    def __init__(self):
        self.from_email = 'arch.prince01@gmail.com'
    def send_mail(self, recipient, subject, content):
        sg = SendGridAPIClient(Sendgrid_API_KEY)
        message = Mail(
            from_email=self.from_email,
            to_emails=recipient,
            subject=subject,
            html_content=content)
        # print(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        return response

class MailjetApi:
    def __init__(self):
        self.from_email = 'arch.prince01@gmail.com'
    def send_mail(self, recipient, subject, content):
        mailjet = Client(auth=(Mailjet_API_KEY, Mailjet_API_SECRET), version='v3.1')
        list_recipients = []
        for email in recipient:
            temp = {}
            temp['Email'] = email
            list_recipients.append(temp)
        data = {
        'Messages': [
            {
            "From": {
                "Email": "arch.prince01@gmail.com",
            },
            "To": list_recipients,
            "Subject": subject,
            "TextPart": content,
            }
        ]
        }
        response = mailjet.send.create(data=data)
        return response
