# from brain.openai.openai import OpenAIChatbot

# def main():
#     #Invoke openai chatbot in a for loop, it will run forever, and it will ask for input
#     #from user and then it will print the response from openai chatbot
#     while True:
#         # Ask for input from user
#         prompt = input("You: ")
#         chatbot = OpenAIChatbot()
#         # Print response from openai chatbot
#         print("OpenAI: " + chatbot.ask(prompt=prompt))
#         # Pass
#     pass

# # Run main
# if __name__ == "__main__":
#     main()

from interface.ui.ui_main import UIMain

def main():
    ui = UIMain()
    ui.Launch()

# Run main
if __name__ == "__main__":
    main()
