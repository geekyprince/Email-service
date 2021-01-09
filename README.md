install all dependencies using requirement.txt
Modify .env file with your api keys for sendgrid and mailjet.
Then
goto project directory and run commands
python manage.py migrate
python manage.py runserver

then there are two options
either do a post request using postman or django browser console as follows:

method: Post
url:  http://localhost/MailApi/mail/
body: 
{
    "email_ids": ["prince01@gmail.com", "skit@gmail.com"],
    "subject": "hey there Prince this side",
    "content": "welcome to Email service by mailjet and sendgrid"
}

#this is a sample example for body param which need to be in json format


