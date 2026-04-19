from dotenv import load_dotenv
load_dotenv()

from importlib.metadata import version
lg_core_version = version("langgraph")
from langchain_core import __version__ as lc_core_version
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

print(f"LangChain Core version: {lc_core_version}")
print(f"LangGraph version: {lg_core_version}")

def main():
    
    # Testing OpenAI
    # llm_openai = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    # response = llm_openai.invoke("Say 'setup complete' if you can read this message.")
    # print(f"Response from OpenAI: {response}")

    # Testing Anthropic
    llm_anthropic = ChatAnthropic(model="claude-3-5-sonnet-20241022", temperature=0)
    response = llm_anthropic.invoke("Say 'setup complete' if you can read this message.")
    print(f"Response from Anthropic: {response}")

    print("Setup complete.")
 
if __name__ == "__main__":
    main()
