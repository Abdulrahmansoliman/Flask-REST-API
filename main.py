from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
api = Api(app)


video_put_args = reqparse.RequestParser()
"""
We use reqparse in Flask to parse and validate request data(such as form data, query parameters, and JSON payloads) in a clean and 
consistent way. reqparse is a module provided by the Flask-RESTful extension that allows you to define a set of request arguments 
and apply validation rules to each of them. This helps to ensure that your API only accepts valid and well-formed data from clients.

Here are some reasons why we use reqparse in Flask:
It provides a convenient and consistent way to define request arguments and validation rules.
It automatically handles data type conversion and formatting, so you don't have to write repetitive code for each request argument.
It can handle complex data structures such as nested JSON objects and arrays.
It raises informative errors when validation fails, making it easier to debug issues with incoming requests.
It is well-documented and widely used in the Flask community, so it's easy to find help and examples online
"""

video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video")
video_put_args.add_argument("likes", type=int, help="Likes on the video")

"""
we use the parse_args() method of the RequestParser object to parse the request arguments and validate them according to the rules
we defined earlier. If any validation errors occur (such as a missing required argument or an argument with an invalid data type), 
parse_args() will raise a BadRequest exception.
"""

videos = {"tim":{"age":19 , "gender":"male"},
         "John":{"age":21, "gender":"female"},
         }

def abort_if_video_id_doesnt_exist(video_id):  
    if video_id not in videos:
        abort(404, message="Could not find video...")
        
class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id]=args    
        return(args, 201)
    
    
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)
