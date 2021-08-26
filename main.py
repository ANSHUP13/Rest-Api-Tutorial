'''
comment add for checking
you use this repository form another place  
this is very important

'''

from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests
from requests.api import delete

app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the vedio not given", required=True)
video_put_args.add_argument("likes", type=int, help="likes on the vedio not given", required=True)
video_put_args.add_argument("views", type=int, help="views of the vedio not given", required=True)
videos = {}

class Video(Resource):
    def get(self, video_id):
        try:
            return {video_id:videos[video_id]}
        except:
            return {"msg":"id is not present"}
    
    def put(Self, video_id):
        if video_id in videos:
            return {'msg':'this video_id already exist'}
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {'msg':'video has been added'}

    def delete(self, video_id):
        if video_id not in videos:
            return {'msg':'video_id is not present'}
        videos.pop(video_id)
        return {'msg': 'video_id ' + str(video_id) + ' has been deleted'}
    
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

