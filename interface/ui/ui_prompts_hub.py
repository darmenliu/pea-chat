import gradio as gr
from prompt_manager.prompt_manager import PromptManager
from prompt_manager.prompt import Prompt

# Prompts hub provide the page to display prompts, and user can edit,
# add, save, prompts.
# Every prompt show as button in page, button contain the prompt act and summary
# When user click on button, it will show the prompt and to the prompt edit page.
# Prompt edit page include a text box to edit the prompt, and a save button, user
# can also use a try button to try the prompt chat with chatbot.
# Prompt edit page also include a back button to go back to prompts hub page.
# Prompt hub page provide a button to add new prompt, when user click on it, it
# will go to prompt edit page, and user can edit the prompt, try and save it.

class PromptHub:
    def __init__(self):
        self.prompt_manager = PromptManager()
        self.prompt_manager.Load()
        pass
    
    def prompt_box(self, prompt):
        with gr.Box():
            gr.Textbox(label=prompt.GetAct(), lines = 10, value=prompt.GetPrompt(), interactive=True, show_label=True, show_copy_button=True)
            with gr.Row():
                saveButton = gr.Button(value="Save")
                tryButton = gr.Button(Value="Test")

    def prompt_hub_frame(self):
        with gr.Tab("PromptsHub"):
            prompts = self.prompt_manager.GetAwesomePrompts()
            keys = list(prompts.keys())
            length = len(keys)
            for i in range (0, length):
                if i % 4 == 0:
                    with gr.Row():
                        self.prompt_box(prompts[keys[i]])
                        if i + 1 < length :
                            self.prompt_box(prompts[keys[i + 1]])
                        if i + 2 < length :
                            self.prompt_box(prompts[keys[i + 2]])
                        if i + 3 < length :
                            self.prompt_box(prompts[keys[i + 3]])
