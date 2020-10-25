from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from lionheart.routes import routes
from lionheart.main import home
from lionheart import settings

middleware = [
    Middleware(SessionMiddleware, secret_key=settings.SECRET_KEY),
    # Middleware(TrustedHostMiddleware, allowed_hosts=settings.ALLOWED_HOSTS)
]
routes = [
    Route("/", home),
    Mount("/static", StaticFiles(directory="static"), name="static"),
    Mount("/", routes=routes),

]
app = Starlette(debug=settings.DEBUG, routes=routes, middleware=middleware)
