from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__, static_folder='../static', static_url_path='')


ENV = "debug"

if ENV == "debug":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123456@localhost:5432/postgres'
    app.debug = True
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qkhusxirwrxtnc:3343256fc71c5934628acfd574b43d375774b169972a6704088ae09f731996b1@ec2-3-213-192-58.compute-1.amazonaws.com:5432/d302ufp80rp2vq'
    app.debug = False
    

@app.route('/')
def index():
    return app.send_static_file('index.html')

# 跨域支持
def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET'
    return resp
app.after_request(after_request)


api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes, schedule_jobs


if __name__ == '__main__':
    app.run()
