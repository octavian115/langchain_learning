from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

chain = template | model | parser
final_result = chain.invoke({'topic': 'football'})


print(final_result)
print(type(final_result))