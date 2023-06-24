import gradio as gr
from interface.ui.ui_chat import UIChat

class UIMain: # This class is the main UI class, it's the first thing that runs when the program is launched
    def __init__(self):
        self.chat = UIChat()

    def Launch(self):
        with gr.Blocks() as demo:
            self.chat.chatbot_frame()
        demo.launch()