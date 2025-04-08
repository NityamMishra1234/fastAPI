from app.services.llm_service import generate_response
from app.utils.system import (
    open_app,
    get_current_time,
    set_alarm,
    create_calendar_event
)

def handle_command(text: str) -> str:
    text_lower = text.lower()

    # Open apps
    if "open instagram" in text_lower:
        open_app("instagram")
        return "Opening Instagram for you."
    elif "open youtube" in text_lower:
        open_app("youtube")
        return "Opening YouTube for you."
    elif "open whatsapp" in text_lower:
        open_app("whatsapp")
        return "Opening WhatsApp for you."
    elif "open gmail" in text_lower:
        open_app("email")
        return "Opening email for you."

    # Tell time
    elif "what is the time" in text_lower or "tell me the time" in text_lower:
        return get_current_time()

    # Set alarm
    elif "set alarm" in text_lower:
        return set_alarm(text)

    # Create calendar event
    elif "create calendar" in text_lower or "add calendar event" in text_lower or "set a meeting" in text_lower:
        return create_calendar_event(text)

    # Fallback to LLM
    return generate_response(text)
