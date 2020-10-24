from starlette.templating import Jinja2Templates
import smtplib
from starlette.config import Config

template = Jinja2Templates(directory="templates").TemplateResponse




def sendmail(email, username, category):
    AdminEmail = 'owonikokoolaoluwa@hotmail.com'
    NewUser = [email]
    message1 = f"""
    Subject: New user registeration
    good day lionheart {username} just register to your server,
    with {email}
    """

    message2 = f"""
    Subject: Registeration succesfull
    Congratulation {username} You have sucessfully register to 
    lionheart under the category of {category} , you will be contacted soon. 
    """
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(AdminEmail, AdminEmail, message1)  
        smtpObj.sendmail(AdminEmail, NewUser, message2)       
        print( "Successfully sent email")
    except 'SMTPException':
        print( "Error: unable to send email")
        