# starts http server on port 5000 

from flask import Flask

app = Flask(__name__)

class Server():
    def __init__(self,host="0.0.0.0" , port=5000):
        self.host = host
        self.port = port
        self.app = app

    def start(self):
        self.app.run(host=self.host, port=self.port)

    @app.route('/api/', methods=['GET'])
    def api():
        return "Hello World"
