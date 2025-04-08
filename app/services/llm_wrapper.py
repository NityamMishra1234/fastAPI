from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory


from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Step 1: Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
)

# Step 2: Create prompt template with history support
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Keep replies short and conversational."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Step 3: In-memory store of per-user histories
user_histories = {}

def get_history(user_id: str):
    if user_id not in user_histories:
        user_histories[user_id] = ChatMessageHistory()
    return user_histories[user_id]

# Step 4: Wrap the chain with memory support
chain_with_memory = RunnableWithMessageHistory(
    prompt | llm,
    get_session_history=get_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Step 5: Exposed function to call from your FastAPI service
def generate_response_with_memory(prompt: str, user_id: str = "default") -> str:
    try:
        print(f"[{user_id}] Prompt: {prompt}")
        response = chain_with_memory.invoke(
            {"input": prompt},
            config={"configurable": {"session_id": user_id}}
        )
        print(f"[{user_id}] Response: {response.content}")
        return response.content
    except Exception as e:
        print(f"LangChain Error for user {user_id}:", e)
        return "I'm sorry, I couldn't think of a response right now."
