from flask import Flask, jsonify, request, abort
from user_service import UserService

app = Flask(__name__)
user_service = UserService()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user is None:
        abort(404)
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'firstName' in request.json:
        abort(400)
    user = user_service.create_user(request.json)
    return jsonify(user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    if not request.json:
        abort(400)
    user = user_service.update_user(user_id, request.json)
    if user is None:
        abort(404)
    return jsonify(user), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    if not result:
        abort(404)
    return jsonify({'result': True}), 200

if __name__ == '__main__':
    app.run(debug=True)
