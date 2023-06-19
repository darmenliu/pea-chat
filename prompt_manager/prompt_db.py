import tinydb

class PromptDb:
    def __init__(self):
        self.db = tinydb.TinyDB("prompts.json")
    
    def add(self, prompt):
        self.db.insert(prompt)
    
    def remove(self, prompt):
        self.db.remove(prompt)
    
    def edit(self, prompt):
        self.remove(prompt)
        self.add(prompt)
    
    # Save prompts to tinydb file
    def save(self, prompts):
        for prompt in prompts:
            self.add(prompt)
    
    def load(self):
        return self.db.all()
    
    def export(self):
        pass
    
    def import_(self):
        pass