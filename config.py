# Chat back end is the chatbot engine, you can change it in config.py
chat_back_end="OpenAIChat" # OpenAIChat, NewBingChat, GoogleBard

# Access token for OpenAI chatbot, please configure it in config.py
access_token_for_openai=""

# Access token for newbing chat
access_token_for_newbing=""

# The http server will be run on port 5000 by default, you can change it in config.py
http_server_port=5000

# The http server will be run on localhost by default, you can change it in config.py
http_server_host="localhost"

# The http server will be run on debug mode by default, you can change it in config.py
http_server_debug="True"

# The http server will be run on threaded mode by default, you can change it in config.py
http_server_threaded=True

# The http server will be run on non ssl mode by default, you can change it in config.py
http_server_ssl=False

# The http server will be run on none ssl context by default, you can change it in config.py
http_server_ssl_context=None
