import tinydb
from prompt_manager.prompt import Prompt
from prompt_manager.prompt_db import PromptDb

# prompt manager is a class that manages the prompts for the chatbot
# Prompt manager contain a lists of prompts
# Prompt manager can add, remove, edit, and save prompts
# Prompt manager can also load prompts from a file
# Prompt manager can also save prompts to a file
# Prompt manager can also export prompts to a file
# Prompt manager can also import prompts from a file

class PromptManager:
    def __init__(self):
        # awesome prompts with a map
        self.awesome_prompts = {}
        self.prompts_db = {}
        self.db = PromptDb()
    
    def Add(self, prompt):
        self.db.Add(prompt)
    
    def Remove(self, prompt):
        self.db.Remove(prompt)
    
    def Edit(self, prompt):
        self.Remove(prompt)
        self.Add(prompt)
    
    def GetAwesomePrompts(self) -> dict:
        return self.awesome_prompts

    def GetPromptsDb(self) -> dict:
        return self.prompts_db

    def Save(self):
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
                self.awesome_prompts[prompt.act] = prompt

    # Load prompts from tinydb database
    def loadPromptsFromTinyDB(self):
        self.prompts_db = self.db.Load()

    def Load(self):
        self.loadPromptsFromCSV("prompt_manager/data/prompts.csv")
        self.loadPromptsFromTinyDB()
    
    def export(self):
        pass
    
    def import_(self):
        pass
