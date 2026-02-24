from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

#chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history = []

#load the chat history
#to give llm the full context of the conversation, we can load the previous chat history from a file and include it in the prompt using the MessagesPlaceholder. This allows the model to understand the context of the conversation and provide more relevant responses.
with open('Langchain_prompts/chat_history.txt') as f:
    chat_history.extend(f.readlines())

# print(chat_history)

#create prompt

prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': "where is my refund?"
})
print(prompt)