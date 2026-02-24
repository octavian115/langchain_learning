from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_input = input('You: ')

    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chatbot. Goodbye!")
        break
    chat_history.append(HumanMessage(content=user_input))
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))

    print(f'Chatbot: {response.content}')

print(chat_history)