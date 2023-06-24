import gradio as gr
from interface.ui.ui_chat import UIChat
from interface.ui.ui_prompts_hub import PromptHub

class UIMain: # This class is the main UI class, it's the first thing that runs when the program is launched
    def __init__(self):
        self.chat = UIChat()
        self.prompt_hub = PromptHub()

    def Launch(self):
        with gr.Blocks() as demo:
            self.chat.chatbot_frame()
            self.prompt_hub.prompt_hub_frame()
        demo.launch()