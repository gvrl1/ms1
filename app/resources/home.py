from flask import jsonify, Blueprint, request
from opentelemetry import trace

home = Blueprint('home', __name__)
tracer = trace.get_tracer(__name__)

@home.route('/', methods=['GET'])
@tracer.start_as_current_span("index_route")
def index():
        my_ip = request.remote_addr
        resp = jsonify({"microservicio": my_ip, "status": "ok"})
        resp.status_code = 200
        return resp

@home.route('/health', methods=['GET'])
@tracer.start_as_current_span("health_route")
def health():
        resp = jsonify({"status": "ok"})
        resp.status_code = 200
        return resp

