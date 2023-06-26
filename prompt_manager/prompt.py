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

class Prompt:
    def __init__(self, act, summary, prompt, describe, author, date, tags):
        self.act = act
        self.summary = summary
        self.prompt = prompt
        self.describe = describe
        self.author = author
        self.date = date
        self.tags = tags

    def GetAct(self):
        return self.act

    def GetSummary(self):
        return self.summary

    def GetPrompt(self):
        return self.prompt

    def GetDescribe(self):
        return self.describe

    def GetAuthor(self):
        return self.author

    def GetDate(self):
        return self.date

    def GetTags(self):
        return self.tags

    def ToJson(self):
        return json.dumps(self.__dict__)
    
    def FromJson(self, json):
        self.__dict__ = json.loads(json)
        return self
    
