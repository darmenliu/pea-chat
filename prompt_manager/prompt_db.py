import tinydb

class PromptDb:
    def __init__(self):
        self.db = tinydb.TinyDB("prompts.json")
    
    def Add(self, prompt):
        self.db.insert(prompt)
    
    def Remove(self, prompt):
        self.db.remove(prompt)
    
    def Edit(self, prompt):
        self.Remove(prompt)
        self.Add(prompt)
    
    # Save prompts to tinydb file
    def Save(self, prompts):
        for prompt in prompts:
            self.Add(prompt)
    # Load prompts from tinydb file, and return with a dict of prompts
    def Load(self) -> dict:
        prompts = {}
        for prompt in self.db.all():
            prompts[prompt["act"]] = prompt
        return prompts
    
    def export(self):
        pass
    
    def import_(self):
        pass