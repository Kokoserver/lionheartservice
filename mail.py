import smtplib
from starlette.config import Config
config = Config(".env")
EMAIL = config("EMAIL_ADDRESS", default=None)
PASSWORD = config("EMAIL_PASSWORD", default=None)
def sendmail(UserEmail:str, username:str, category:str, conact_message=None):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        if category == "register": 
            subject = "Complete Registeration"
            body = f"""
            Congratulation {username} you have sucessfully registered to Lionheart service.
            We will keep updating you as soon as possible an if you have any questions?
            please don't hesitate to contact us on our main website.
            """
            message = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAIL, UserEmail, message)
        elif category == "contact":
            subject = "lionheart service reply"
            body = f"""
            Thanks {username} for contacting lionheart service, 
            Your message have been sent sucessfully,
             We will get back to you very soon.
            """
            message = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(EMAIL, UserEmail, message)
            admin_subject = "New message from Customer"
            message = f"Subject: {admin_subject}\n\n{conact_message}"
            smtp.sendmail(EMAIL, EMAIL, message)
           
            
       
    
        