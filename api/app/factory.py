from typing import List, Type, Union

from flask import Blueprint, Flask
from flask_marshmallow import Marshmallow

from app.config import Config
from app.http.route import Route

ma = Marshmallow()


def create_app(
    app_name: str, config: Type[Config], routes: List[Union[Route, Blueprint]]
):
    app = Flask(app_name)
    app.config.from_object(config)

    ma.init_app(app)

    for route in routes:
        if isinstance(route, Blueprint):
            app.register_blueprint(route)
        else:
            app.add_url_rule(
                route.url_rule, view_func=route.view_func(), methods=route.methods()
            )

    return app
