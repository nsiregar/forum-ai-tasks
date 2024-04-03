from http import HTTPStatus
from typing import Dict, List

from flask import current_app, jsonify, make_response, request
from flask.typing import ResponseReturnValue
from flask.views import View
from openai import OpenAI, RateLimitError

from app.gpt.schema import GPT4RequestSchema


class GPT4DispatchAPI(View):
    def dispatch_request(self) -> ResponseReturnValue:
        request_schema = GPT4RequestSchema()
        json_data = request.get_json() or dict()
        errors = request_schema.validate(json_data)
        if errors:
            return make_response(jsonify(errors=str(errors)), HTTPStatus.BAD_REQUEST)

        client = OpenAI(api_key=current_app.config.get("OPEN_AI_API_KEY"))
        open_ai_resp = get_open_ai_response(
            client=client, messages=json_data["messages"], model="gpt-3.5-turbo-0125"
        )

        resp = {"data": list(open_ai_resp)}
        return jsonify(resp), HTTPStatus.OK


def get_open_ai_response(client: OpenAI, messages: List[Dict[str, str]], model: str):
    def stream():
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            )

            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                if content:
                    yield content

        except RateLimitError:
            yield "The server is experiencing a high volume of requests. Please try again later."

    return stream()
