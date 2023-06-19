import json
# prompt is a struct that contains the following fields:
# prompt = {
#     "act": str,
#     "summary": str,
#     "prompt": str,
#     "describe": str,
#     "author": str,
#     "date": str,
#     "tags": list[str]
# }

class prompt:
    def __init__(self, act, summary, prompt, describe, author, date, tags):
        self.act = act
        self.summary = summary
        self.prompt = prompt
        self.describe = describe
        self.author = author
        self.date = date
        self.tags = tags

    def ToJson(self):
        return json.dumps(self.__dict__)
    
    def FromJson(self, json):
        self.__dict__ = json.loads(json)
        return self
    
