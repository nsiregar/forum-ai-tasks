from __future__ import annotations

from typing import List, Optional, Type, Union

from flask import Blueprint
from flask.typing import RouteCallable
from flask.views import View


class Route:
    def __init__(
        self,
        url_rule: str,
        view: Type[View],
        method: Optional[str] = None,
        name_alias: Optional[str] = None,
    ) -> None:
        self.url_rule = url_rule
        self.view = view
        self.method = method
        self.name_alias = name_alias

    def view_func(self) -> RouteCallable:
        view_name = self.name_alias or self.view.__name__
        return self.view.as_view(view_name)

    def methods(self) -> List[str]:
        if self.method is None:
            methods = getattr(self.view, "methods", None) or ("GET",)
        else:
            methods = [self.method]
        return methods

    @classmethod
    def get(cls, url_rule: str, view: Type[View], name_alias: Optional[str] = None):
        return cls(url_rule=url_rule, view=view, method="GET", name_alias=name_alias)

    @classmethod
    def post(cls, url_rule: str, view: Type[View], name_alias: Optional[str] = None):
        return cls(url_rule=url_rule, view=view, method="POST", name_alias=name_alias)

    @classmethod
    def put(cls, url_rule: str, view: Type[View], name_alias: Optional[str] = None):
        return cls(url_rule=url_rule, view=view, method="PUT", name_alias=name_alias)

    @classmethod
    def delete(cls, url_rule: str, view: Type[View], name_alias: Optional[str] = None):
        return cls(url_rule=url_rule, view=view, method="DELETE", name_alias=name_alias)

    @staticmethod
    def group(url_prefix_group: str, routes: List[Union[Route, Blueprint]], **kwargs):
        name = kwargs.pop("name", None) or url_prefix_group.replace("/", "")
        url_prefix = kwargs.pop("url_prefix", None) or url_prefix_group
        blueprint = Blueprint(name, __name__, url_prefix=url_prefix, **kwargs)

        for route in routes:
            if isinstance(route, Blueprint):
                blueprint.register_blueprint(route)
            else:
                blueprint.add_url_rule(
                    route.url_rule, view_func=route.view_func(), methods=route.methods()
                )

        return blueprint
