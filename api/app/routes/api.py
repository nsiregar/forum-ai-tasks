from app.gpt.dispatch import GPT4DispatchAPI
from app.http.route import Route
from app.views.main_api import MainView

api_routes = [
    Route.get("/", MainView),
    Route.group(
        "/api",
        routes=[
            Route.post("/gpt4", view=GPT4DispatchAPI),
        ],
    ),
]
