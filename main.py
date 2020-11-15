from starlette.requests import Request
from starlette.responses import PlainTextResponse, HTMLResponse, RedirectResponse
from starlette.background import BackgroundTask
from config import template
from mail import sendmail
from model import LionheartUser as User
from model import LionheartContact as Contact
from model import LionheartAdmin as Admin

CATEGORY:list = [
    "Category",
    "Home services", 
    "Teakwondo Academy", 
    "Lionheart Team", 
    "Sellers Center", 
    "Job Empowerment"
] 


async def home(request:Request):
    request.session['login'] = True
    return template("pages/index.html", {"request":request})


# async def homeResponse(request):
#     context = {
#         "request":request,
#         "status":"success",
#         "message":" Congratulations, you have successfully register to Lionheart."
#     }
#     return template("pages/index.html", context=context )

async def registerTemplate(request:Request):
    return template("pages/register.html", {"request":request, "categories":CATEGORY})

async def register(request:Request): 
    form = await request.form()
    firstname = form.get("firstname")
    lastname  = form.get("lastname")
    email     = form.get('email')
    category  = form.get('category')
    address  = form.get("address")
    phone = form.get("phone")
    if category == "Category":
        return template("pages/register.html", { "request":request, "categories":CATEGORY, 
       "status":"error", "message":"Please specify the appropariate category", 
       "email":email, "firstname":firstname, "lastname":lastname, "category":category,"phone":phone, "address":address})
    if User.find({"email":email}):
       return template("pages/register.html", { "request":request, "categories":CATEGORY, 
       "status":"error", "message":"User with this email already exist", 
       "email":email, "firstname":firstname, "lastname":lastname, "category":category,
        "phone":phone, "address":address})
    new_user = User(firstname, lastname, email, category, phone, address)
    new_user.save()
    username = f"{firstname} {lastname}"
    task = BackgroundTask(sendmail,UserEmail=email, username=username, category="register",conact_message=contact)
    context = {
        "request":request,
        "status":"success",
        "message":f" Congratulations {firstname} , you have successfully register to Lionheart."
    }
    return template("pages/index.html", context=context , background=task)

async def adminTemplate(request:Request):
    user = request.session.get('loginlionheart', None)
    if user:
       return RedirectResponse(url="/dashboard", status_code=303)
    return template("pages/admin.html", {"request":request})


async def admin(request:Request):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    user = Admin.find(email=email, password=password)
    if user:
       request.session['loginlionheart'] = user["_id"]
       return RedirectResponse(url="/dashboard", status_code=303)
    return template("pages/admin.html", {"request":request, "email":email, 
    "password":password,"status":"error", "message":"account does not exist"}) 
    

async def logout(request:Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)


async def adminReg(request:Request):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    if Admin.find(email, password) is None:
       user = Admin(email=email, password=password)
       user.save()
       return template("pages/admin.html", { "request":request, "status":"success", 
       "message":"you have successfully register, Please login below"})
    return template("pages/adminRegister.html", { "request":request, "email":email, 
    "password":password, "status":"error", "message":"account already exist"})
     

async def adminRegTemplate(request:Request):
    return template("pages/adminRegister.html", {"request":request})  

async def delete(request:Request):
    form = await request.form()
    userId = form.get("userId")
    user = User.delete({"_id":userId})
    return RedirectResponse(url="/dashboard", status_code=303)
    return template("pages/admin.html", {"request":request})  
   

async def dashboard(request:Request):
    user = request.session.get('loginlionheart', None)
    if user is not None:
        return template("pages/dashboard.html", { "request":request, "user":User.all({})})
    return RedirectResponse(url="/admin", status_code=303)
        


async def contact(request:Request):
    form  = await request.form()
    name = form.get("name")
    email = form.get("email")
    phone = form.get("phone")
    message = form.get("message")
    new_contact = Contact(name, email, phone, message)
    newContact = new_contact.save()
    contact = f"name:{name}\n\n email:{email}\n\nphone:{phone}\n\n:message:{message}"
    subject = "New contact message"

    task = BackgroundTask(sendmail, UserEmail=email, username=name, category="contact", conact_message=contact)
    return template("pages/index.html", { "request":request, "status":"success", 
    "message":f"Thanks for contacting us {name}"}, background=task)
    

