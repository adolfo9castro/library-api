from flask import request, jsonify

def init_middlewares(app):
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = app.response_class()
            response.headers["Access-Control-Allow-Origin"] = "*"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
            response.headers["Access-Control-Allow-Headers"] = "Authorization, Content-Type"
            return response, 204

    @app.before_request
    def check_headers():
        if request.method in ["POST", "PUT"]:
            if request.headers.get("Content-Type") != "application/json":
                return jsonify({"Error": "Invalid Content Type"}), 400