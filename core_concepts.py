"""
LangChain Core Concepts - LCEL & Runnables
"""

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def demo_basic_chain():
    """Demonstrates a basic chain using LCEL and Runnables."""

    # Component 1: Define a prompt template
    prompt_template = ChatPromptTemplate.from_template("You are a helpful assistant. Answer the following question: {question}")

    # Component 2: Define an LLM Runnable (using OpenAI)
    llm_openai = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    # Component 3: Define output parser
    output_parser = StrOutputParser()

    # Component 4: Create a pipeline (chain) that connects the components
    chain = prompt_template | llm_openai | output_parser

    # Execute the chain with an input question
    response = chain.invoke({"question": "What is the capital of France?"})
    print(f"Response from OpenAI: {response}")

    return chain

if __name__ == "__main__":
    demo_basic_chain()