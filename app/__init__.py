#__init__.py
from flask import Flask, render_template, request

def create_app():
    app = Flask(__name__)
    
    from .routes import main
    app.register_blueprint(main)
    
    return app
