from flask import Flask
from flask import jsonify, request
import models

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
    for row in models.User.query.all():
        data.append(row.to_json())

    response = jsonify(data)

    return response


def main():
    app.run(host='0.0.0.0', port=8080, debug=True)


if __name__ == '__main__':
    main()
