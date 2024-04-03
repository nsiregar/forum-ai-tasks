from app.config import get_config
from app.factory import create_app
from app.routes.api import api_routes

app = create_app("openai-wrapper", config=get_config(), routes=api_routes)
