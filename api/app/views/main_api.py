from flask import jsonify
from flask.typing import ResponseReturnValue
from flask.views import View


class MainView(View):
    def dispatch_request(self) -> ResponseReturnValue:
        resp = {"message": "Application running."}
        return jsonify(resp)
