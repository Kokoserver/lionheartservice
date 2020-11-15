
from starlette.routing import Route
from main import (registerTemplate, 
register, contact, adminTemplate, 
dashboard, 
logout,
admin, delete,
adminReg, adminRegTemplate)

routes = [
    Route("/register", registerTemplate, methods=['get']),
    Route("/register", register, methods=['post']),
    Route("/contact", contact, methods=["post"]),
    Route("/admin", adminTemplate, methods=['get']),
    Route("/admin/logout", logout, methods=['get']),
    Route("/admin/login", admin,  methods=['post']),
    Route("/dashboard", dashboard, methods=['get'] ),
    Route("/deleteUser", delete, methods=['post']),
    # Route("/homeresponse/23478638726", homeResponse, methods=["get"] ),
    Route("/admin/register/main/raqueeb", adminReg, methods=['post'] ),
    Route("/admin/register/main/raqueeb", adminRegTemplate, methods=['get']),

]