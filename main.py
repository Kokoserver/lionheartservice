from starlette.requests import Request
from starlette.responses import PlainTextResponse, HTMLResponse, RedirectResponse
from starlette.background import BackgroundTask
from config import template
from model import LionheartUser as User
from model import LionheartContact as Contact
from model import LionheartAdmin as Admin
from config import sendmail

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


async def homeResponse(request):
    context = {
        "request":request,
        "status":"success",
        "message":" Congratulations, you have successfully register to Lionheart."
    }
    return template("pages/index.html", context=context )

async def registerTemplate(request:Request):
    return template("pages/register.html", {"request":request, "categories":CATEGORY})

async def register(request:Request): 
    form = await request.form()
    firstname = form.get("firstname")
    lastname  = form.get("lastname")
    email     = form.get('email')
    category  = form.get('category')
    if category == "Category":
        return template("pages/register.html", { "request":request, "categories":CATEGORY, 
       "status":"error", "message":"Please specify the appropariate category", 
       "email":email, "firstname":firstname, "lastname":lastname, "category":category})
    if User.find({"email":email}):
       return template("pages/register.html", { "request":request, "categories":CATEGORY, 
       "status":"error", "message":"User with this email already exist", 
       "email":email, "firstname":firstname, "lastname":lastname, "category":category})
    new_user = User(firstname, lastname, email, category)
    new_user.save()
    username = f"{firstname} {lastname}"
    BackgroundTask(sendmail, email=email, username=username, category=category)
    return RedirectResponse(url="/homeresponse/23478638726", status_code=301)

async def adminTemplate(request:Request):
    if request.session.get('login', None):
        return RedirectResponse(url="/dashboard", status_code=301)
    return template("pages/admin.html", {"request":request})


async def admin(request:Request):
    form = await request.form()
    email = form.get("email")
    password = form.get("password")
    user = Admin.find(email=email, password=password)
    if user:
       request.session['loginlionheart'] = user["_id"]
       return RedirectResponse("/dashboard", status_code=301)
    return template("pages/admin.html", {"request":request, "email":email, 
    "password":password,"status":"error", "message":"account does not exist"}) 
    

async def logout(request:Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=301)
    # return template("pages/admin.html", { "request":request, "status":"success",
    #  "message":"you have successfully logged out"})

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
    return RedirectResponse(url="/dashboard", status_code=301)
    return template("pages/admin.html", {"request":request})  
   

async def dashboard(request:Request):
    user = request.session.get('loginlionheart', None)
    if user is not None:
        return template("pages/dashboard.html", { "request":request, "user":User.all({})})
    return RedirectResponse(url="/admin", status_code=301)
        


async def contact(request:Request):
    form  = await request.form()
    name = form.get("name")
    email = form.get("email")
    message = form.get("message")
    new_contact = Contact(name, email, message)
    new_contact.save()
    return template("pages/index.html", { "request":request, "status":"success", 
    "message":f"Thanks for contacting us {name}"})
    

