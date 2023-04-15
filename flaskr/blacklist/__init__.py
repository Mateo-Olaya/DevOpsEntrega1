from flask import Flask
# from decouple import config

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blacklist'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app 

# def create_app():
#     app = Flask(__name__)
#     #configure postgresql fron env variables
#     if config('ENV') == 'development':
#         app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts'
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     else:
#         app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
#         app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
#     return app

