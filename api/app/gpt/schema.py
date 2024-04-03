from marshmallow import Schema, fields


class GPT4RequestSchema(Schema):
    messages = fields.List(fields.Dict(required=True))
