import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from travel_library.routes import pages


load_dotenv()


def create_app():
    """
    Create a Flask application instance with pre-configured settings and routes.

    It initializes a Flask application with MONGODB_URI and SECRET_KEY.
    It used to set up a connection to the MongoDB database and registers the 'pages' blueprint.

    Returns:
        app (Flask): The initialized Flask application instance.
    """
    app = Flask(__name__)
    app.config["MONGODB_URI"] = os.environ.get("MONGODB_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw")
    app.db = MongoClient(app.config["MONGODB_URI"],tlsAllowInvalidCertificates=True).get_default_database()
    app.register_blueprint(pages)
    return app
