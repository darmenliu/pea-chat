import gradio as gr
from interface.ui.ui_chat import UIChat
from interface.ui.ui_prompts_hub import PromptHub
from config import chat_back_end

class UIMain: # This class is the main UI class, it's the first thing that runs when the program is launched
    def __init__(self):
        chatbot = None
        if chat_back_end == "OpenAIChat":
            from brain.openai.openai import OpenAIChatbot
            chatbot = OpenAIChatbot()
        elif chat_back_end == "NewBingChat":
            from brain.newbing.newbing import NewBingChatbot
            chatbot = NewBingChatbot()
        elif chat_back_end == "GoogleBard":
            pass

        self.chat = UIChat(chatbot)
        self.prompt_hub = PromptHub()

    def Launch(self):
        with gr.Blocks() as demo:
            self.chat.ChatbotFrame()
            self.prompt_hub.prompt_hub_frame()
        demo.launch()