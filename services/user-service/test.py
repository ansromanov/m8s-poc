from flask import Flask
from typing_extensions import get_type_hints
import models
from models import User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:root@localhost:13306/user-service'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
models.init_app(app)
item = User.query.filter_by(username='dbt').first()
test = item.to_json()


print(test)