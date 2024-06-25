from langchain_cohere import ChatCohere
from key import cohere_api_key
api_key = cohere_api_key
chat = ChatCohere(cohere_api_key = api_key)

from langchain.schema.messages import HumanMessage, SystemMessage
messages = [
    SystemMessage(content="You Nandan. You like to swim on saturdays."),
    HumanMessage(content="What do you like to do on weekends?"),
]
response = chat.invoke(messages)
print(response.content)