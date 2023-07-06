# ChatBot class is a abstract class for all chatbots
# It contains the basic functions that all chatbots should have
from apc import APC, abstractmethod

class ChatBot(APC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def Ask(self, prompt):
        pass
