import gradio as gr
from brain.openai.openai import OpenAIChatbot

class UIChat:
    def __init__(self):
        self.chatbot = OpenAIChatbot()

    def add_text(self, history, text):
        history = history + [(text, None)]
        return history, gr.update(value="", interactive=False)
    
    def add_file(self, history, file):
        history = history + [((file.name,), None)]
        return history
    
    def bot(self, history):
        response = "**That's cool!**"
        if history[-1][0] != "": # text
            response = self.chatbot.ask(prompt=history[-1][0])
        history[-1][1] = response
        return history

    def chatbot_frame(self):
        with gr.Tab("Chatbot"):
            chatbot = gr.Chatbot([], elem_id="chatbot").style(height=300)

            with gr.Row():
                with gr.Column(scale=0.85):
                    txt = gr.Textbox(
                        show_label=False,
                        placeholder="Enter text and press enter, or upload an image",
                    ).style(container=False)
                with gr.Column(scale=0.15, min_width=0):
                    btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])

            txt_msg = txt.submit(self.add_text, [chatbot, txt], [chatbot, txt], queue=False).then(
                self.bot, chatbot, chatbot
            )
            txt_msg.then(lambda: gr.update(interactive=True), None, [txt], queue=False)
            file_msg = btn.upload(self.add_file, [chatbot, btn], [chatbot], queue=False).then(
                self.bot, chatbot, chatbot
            )
