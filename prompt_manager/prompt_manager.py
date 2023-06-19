from prompt_manager.prompt import Prompt
# prompt manager is a class that manages the prompts for the chatbot
# Prompt manager contain a lists of prompts
# Prompt manager can add, remove, edit, and save prompts
# Prompt manager can also load prompts from a file
# Prompt manager can also save prompts to a file
# Prompt manager can also export prompts to a file
# Prompt manager can also import prompts from a file

class PromptManager:
    def __init__(self):
        self.prompts = []
    
    def add(self, prompt):
        self.prompts.append(prompt)
    
    def remove(self, prompt):
        self.prompts.remove(prompt)
    
    def edit(self, prompt):
        self.remove(prompt)
        self.add(prompt)
    
    def save(self):
        pass
    
    # Load prompts from prompts.csv file
    # prompts.csv file is a csv file that contains the following fields:
    # act,prompt
    # act is a string that contains the action to do
    # prompt is a string that contains the prompt
    # Load prompt = prompt(act, "", prompt, "", "", "", [])
    def loadPromptsFromCSV(self, filename):
        # Open prompts.csv file
        with open(filename, "r") as file:
            # Read all lines from prompts.csv file
            lines = file.readlines()
            # For each line in lines
            for line in lines:
                # Split line by comma
                line = line.split(",")
                # Create a prompt
                prompt = Prompt(line[0], "", line[1], "", "", "", [])
                # Add prompt to prompts
                self.add(prompt)

    def load(self):
        self.loadPromptsFromCSV("prompts.csv")
    
    def export(self):
        pass
    
    def import_(self):
        pass
