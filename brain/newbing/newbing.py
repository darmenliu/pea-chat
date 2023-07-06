import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from config import access_token_for_newbing
from brain.chatbot import ChatBot

class NewbingChatbot(Chatbot):
    def __init__(self):
        self.bot = Chatbot.create(access_token_for_newbing)

    async def Ask(self, prompt):
        response = await self.bot.ask(prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
        print(json.dumps(response, indent=2)) # Returns
        """
        {
            "text": str
            "author": str
            "sources": list[dict]
            "sources_text": str
            "suggestions": list[str]
            "messages_left": int
        }
        """
        await self.bot.close()
        return response["text"]