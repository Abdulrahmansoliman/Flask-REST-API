# Flask-REST-API
Python REST API Tutorial 

In this repository, you will find the code for a Flask REST API built using Python. 
The API allows for the creation, retrieval, updating, and deletion of videos.

The repository includes the following files:

```

1. ** app.py **: the main code file for the API

2. requirements.txt: a list of the Python libraries required for the API

3. database.db: a SQLite database used to store video data

4. README.md: a file containing instructions for setting up the API

```

## Installation and Setup

To set up the Flask REST API on your local machine, follow these steps:

```

1. Clone this repository to your machine using git clone.

2. Navigate to the root directory of the repository and create a virtual environment by running python -m venv venv.

3. Activate the virtual environment by running venv\Scripts\activate (Windows) or source venv/bin/activate (Mac/Linux).

4. Install the required Python libraries by running pip install -r requirements.txt.

5. Start the Flask development server by running python app.py.

```

Once the server is running, you can access the API endpoints by sending HTTP requests to http://127.0.0.1:5000/.

## Usage

The API allows for the following HTTP requests:

```

1. GET /video/<int:video_id>: retrieves a video with the specified ID.

2. PUT /video/<int:video_id>: creates a new video with the specified ID and data.

3. PATCH /video/<int:video_id>: updates an existing video with the specified ID and data.

4. DELETE /video/<int:video_id>: deletes the video with the specified ID.

```

To test the API, you can use the requests library in Python or a tool like Postman.
In the app.py file, you will find a section of commented-out code that demonstrates how to use requests to create and retrieve videos.

## Conclusion

With this repository, you now have a fully functioning Flask REST API that can be used to store and retrieve video data.
Feel free to use this code as a starting point for your own API projects!
