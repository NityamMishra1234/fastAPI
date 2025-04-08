from app.services.llm_wrapper import generate_response_with_memory

def generate_response(prompt: str, user_id: str = "default") -> str:
    try:
        return generate_response_with_memory(prompt, user_id)
    except Exception as e:
        print("LLM Service Error:", e)
        return "I'm sorry, something went wrong while generating a response."
