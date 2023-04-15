from blacklist import create_app
from flask_restful import Resource, Api
from flask import Flask, request
from modelos import db
import requests
# from decouple import config

app = create_app("default")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blacklist'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# if config('ENV') == 'development':
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blacklist'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



app_context = app.app_context()
app_context.push()

api = Api(app)
