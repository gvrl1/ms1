from flask import jsonify, Blueprint, request

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
        my_ip = request.remote_addr
        resp = jsonify({"microservicio": my_ip, "status": "ok"})
        resp.status_code = 200
        return resp
