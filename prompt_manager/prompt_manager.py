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
    
    def load(self):
        pass
    
    def export(self):
        pass
    
    def import_(self):
        pass
