from langchain.chains import LLMChain
from langchain.memory import ChatMessageHistory  # Fixed import
from langchain.prompts import PromptTemplate
from langchain.schema import messages_from_dict, messages_to_dict
from langchain_openai import ChatOpenAI

# Define the prompt
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
Make sure the responses make sense with the context while emulating his style entirely. Be sure to not only emulate the information correct, but also the style of texting. A human should not be able to distinguish between your responses and the tweets you are based on. This may include going on tangents based on the information you know, but do not repeat it verbatim. Please do not tweet out of context or hallucinations.
Please only respond with your answer, no quotations or new lines (please do not include "Answer: ", a newline or anything similar at the beginning).
---
Context:
{context}
---
Question:
{question}
"""
)

# Use ChatOpenAI instead of OpenAI
llm = ChatOpenAI(model="ft:gpt-4o-mini-2024-07-18:personal::BBRCNo7y")

# Create the chain
chain = LLMChain(llm=llm, prompt=prompt)

# Initialize memory
history = ChatMessageHistory()

print("\nType 'exit' to quit.\n")

while True:
    user_input = input("Ask a question: ")
    
    if user_input.lower() == 'exit':
        print("\nLebron: Bye")
        break
    
    # Add user input to memory
    history.add_user_message(user_input)
    
    # Prepare the context by converting messages to a readable format
    context = "\n".join(
        [
            f"{msg['type'].capitalize()}: {msg['data']['content']}"
            for msg in messages_to_dict(history.messages)
        ]
    )
    
    # Invoke the chain with context and new question
    result = chain.invoke({"context": context, "question": user_input})
    
    # Add the model's response to memory
    history.add_ai_message(result['text'])
    
    # Print result
    print(f"Lebron: {result['text']}")
