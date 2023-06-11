# This is backend for OpenAI chatbot
from revChatGPT.V1 import Chatbot
# Load config from config file
from config import access_token_for_openai

# Define a class for openai chatbot
class OpenAIChatbot:
    def __init__(self):
        self.config = {"access_token": access_token_for_openai}
        self.chatbot = Chatbot(config=self.config)

    def ask(self, prompt):
        response = ""
        for data in self.chatbot.ask(prompt=prompt):
            response = data["message"]
        return response
    
