#On the terminal code 'ollama'
#Then code 'ollama pull llama3' to install the Llama3 Model
#To test the model run 'ollama run llama3'
#To set up the virtual environment run 'python3 -m venv primemine'
#The run 'source primemine/bin/activate
#pip install langchain langchain-ollama ollama

#Import langchain
from langchain_ollama import OllamaLLM

#Import for a prompt template
from langchain_core.prompts import ChatPromptTemplate

#Create template
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

#Create the model
model = OllamaLLM(model="llama3")

#Create prompt
prompt = ChatPromptTemplate.from_template(template)

#Chain the prompt and model together using langchain
chain = prompt | model

#Creating a loop to continually be able to speak to the bot
def handle_conversation():
    context = ""
    print("Hi, I'm Primemine! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower()== "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("Primemine: ", result)
        context += f"\nUser:{user_input}\nAI: {result}"


#Call function
if __name__ == "__main__":
    handle_conversation()

