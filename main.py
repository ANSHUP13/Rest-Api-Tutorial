'''
comment add for checking
you use this repository form another place  
this is very important

'''

from flask import Flask, views
from flask_restful import Api, Resource, abort, marshal_with, reqparse, fields
from requests.api import delete
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    views = db.Column(db.Integer,nullable=False)
    likes = db.Column(db.Integer,nullable=False)
    
    def __repr__(self) -> str:
        return f"Video(name={name},views={views},likes={likes})"

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the vedio not given", required=True)
video_put_args.add_argument("likes", type=int, help="likes on the vedio not given", required=True)
video_put_args.add_argument("views", type=int, help="views of the vedio not given", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the vedio not given")
video_update_args.add_argument("likes", type=int, help="likes on the vedio not given")
video_update_args.add_argument("views", type=int, help="views of the vedio not given")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            return result
        else:
            abort(404,message='could not find video')
    
    @marshal_with(resource_fields)
    def put(Self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409,message='already exist')
        args = video_put_args.parse_args()
        video = VideoModel(
            id=video_id,
            name=args['name'],
            views=args['views'],
            likes=args['likes']
            )
        db.session.add(video)
        db.session.commit()
        return video,201

    @marshal_with(resource_fields)
    def patch(self,video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404,message='video_id not found')
        args = video_update_args.parse_args()

        for arg in args:
            if args[arg]:
                print(arg,args[arg])
                result.arg = args[arg]
        
        db.session.commit()
        return result

#    def delete(self, video_id):
#        if video_id not in videos:
#            return {'msg':'video_id is not present'}
#        videos.pop(video_id)
#        return {'msg': 'video_id ' + str(video_id) + ' has been deleted'}
    
api.add_resource(Video,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

