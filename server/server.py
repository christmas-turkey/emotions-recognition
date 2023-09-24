# starts http server on port 5000 

from flask import Flask
from flask_cors import CORS
from routes import routes
app = Flask(__name__)
CORS(app)
routes(app)

class Server():
    def __init__(self, host="0.0.0.0" ,port=5000):
        self.host = host
        self.port = port
        self.app = app

    def start(self):
        self.app.run(host=self.host, port=self.port)

        
