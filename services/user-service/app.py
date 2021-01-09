from flask import Flask
from flask import jsonify, request
import models
from models import User, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:root@db/user-service'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

models.init_app(app)
models.create_tables(app)


@app.route('/healthz', methods=['GET'])
def healthz():
    """
    Healthcheck
    """
    if request.method == 'GET':
        return jsonify({'status': 'OK'})

@app.route('/api/users', methods=['GET'])
def get_users():
    data = []
    for row in User.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response

@app.route('/api/user/<username>', methods=['GET'])
def get_username(username):

    item = User.query.filter_by(username=username).first()
    if item is not None:
        response = jsonify(item.to_json)
    else:
        response = jsonify({'message': 'Cannot find username'}), 404

    return response

@app.route('/api/user/create', methods=['POST'])
def create_user():
    user = User()
    user.username = request.form['username']
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.email = request.form['email']

    db.session.add(user)
    db.session.commit()

    response = jsonify({'message': 'User added', 'result': user.to_json()})

    return response

def main():
    app.run(host='0.0.0.0', port=5000, debug=True)


if __name__ == '__main__':
    main()
