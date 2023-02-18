from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos = {"tim":{"age":19 , "gender":"male"},
         "John":{"age":21, "gender":"female"},
         }
class Video(Resource):
    def get(self, video_id):
        return videos[video_id]

    def put(self, video_id):
        return(request.form['likes'])
    
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
