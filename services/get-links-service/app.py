from flask import Flask
from routes import set_routes

app = Flask(__name__)

set_routes(app)


def main():
    app.run(host='0.0.0.0', port=8080)


if __name__ == '__main__':
    main()
