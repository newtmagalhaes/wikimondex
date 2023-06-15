from flask_restx import Namespace


class SetupDTO:
    api = Namespace('setup', description='Database setup operations')
