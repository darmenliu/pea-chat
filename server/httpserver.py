# This is RestFul api server for the chatbot
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from brain.openai.openai import OpenAIChatbot
from brain.newbing.newbing import NewbingChatbot

# Create a Restful http server to support the chatbot via flask_restful, it should be run in
# a separate thread, it provide the API post /ask to get the response from the chatbot
# The http server will be run on port 5000 by default, you can change it in config.py
# The http server will be run on localhost by default, you can change it in config.py
# The http server will be run on debug mode by default, you can change it in config.py
# The http server will be run on threaded mode by default, you can change it in config.py
# The http server will be run on ssl mode by default, you can change it in config.py
# The http server recieve the request from the client, and then send the request to backend chatbot
# The http server will return the response from the backend chatbot to the client
# The http server will support the chatbot from openai by default, you can change it in config.py
class ChatbotServer(Resource):
    def __init__(self):
        # Load config from config file
        from config import http_server_port, http_server_host, http_server_debug, http_server_threaded, http_server_ssl, http_server_ssl_context
        self.http_server_port = http_server_port
        self.http_server_host = http_server_host
        self.http_server_debug = http_server_debug
        self.http_server_threaded = http_server_threaded
        self.http_server_ssl = http_server_ssl
        self.http_server_ssl_context = http_server_ssl_context
        # Define a class for openai chatbot
        self.openai_chatbot = OpenAIChatbot()
        # Define a class for newbing chatbot
        self.newbing_chatbot = NewbingChatbot()

    # Post /ask - Get the response from the backend chatbot
    # The http server recieve the request from the client, and then send the request to backend chatbot
    # The http server will return the response from the backend chatbot to the client
    @app.route('/ask', methods=['POST'])
    def ask(self):
        # Get the request from the client
        request_data = request.get_json(force=True)
        # Get the prompt from the request
        prompt = request_data["prompt"]
        # Get the chatbot from the request
        chatbot = request_data["chatbot"]
        # Get the response from the backend chatbot
        response = ""
        if chatbot == "openai":
            response = self.openai_chatbot.ask(prompt=prompt)
        elif chatbot == "newbing":
            response = self.newbing_chatbot.ask(prompt=prompt)
        # Return the response to the client
        return jsonify({"response": response})

    def start(self):
        # Create a flask app
        app = Flask(__name__)
        # Create a flask restful api
        api = Api(app)
        # Create a flask cors
        cors = CORS(app)
        # Add the api resource
        api.add_resource(ChatbotServer, "/ask")
        # Run the flask app
        app.run(host=self.http_server_host, port=self.http_server_port, debug=self.http_server_debug, threaded=self.http_server_threaded, ssl_context=self.http_server_ssl_context)

    def stop(self):
        pass
