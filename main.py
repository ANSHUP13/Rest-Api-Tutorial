'''
comment add for checking
you use this repository form another place  
this is very important

'''

from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

names = {}

class HelloWorld(Resource):
    def get(self, name, mode):
        if mode:
            names[name] = "www.google.com/" + name
            return {"message":"your data has been saved"}
        else:
            return {"details": names[name]}

api.add_resource(HelloWorld,"/helloworld/<string:name>/<int:mode>")

if __name__ == "__main__":
    app.run(debug=True)

