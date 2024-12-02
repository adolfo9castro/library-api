from marshmallow import Schema, fields, validate

class BooksSchema(Schema):
    #id = fields.UUID(required=True, validate=validate.Length(equal=36))
    title = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(required=True, validate=validate.Length(min=1))
    read = fields.Boolean()