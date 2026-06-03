# ============================================================
#  Project 1 – Rule-Based AI Chatbot
#  DecodeLabs | Industrial Training Kit | Batch 2026
# ============================================================

# ── KNOWLEDGE BASE (Dictionary – O(1) lookup) ───────────────
responses = {
    # Greetings
    "hello"       : "Hello! How can I assist you today?",
    "hi"          : "Hi there! What can I do for you?",
    "hey"         : "Hey! Great to see you. How can I help?",

    # Identity
    "what is your name" : "I am DecoBot, your rule-based AI assistant.",
    "who are you"       : "I am DecoBot – built at DecodeLabs as Project 1.",
    "what can you do"   : "I can answer your questions using predefined rules. Ask me anything!",

    # General info
    "how are you"       : "I am fully operational and running perfectly, thank you!",
    "what is ai"        : "AI (Artificial Intelligence) is the simulation of human intelligence in machines.",
    "what is decodelabs": "DecodeLabs is an industrial training platform that helps you become a real AI engineer.",
    "tell me a joke"    : "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",

    # Farewells / Exit keywords handled separately below
    "bye"  : "Goodbye! Keep building, keep learning. 🚀",
    "exit" : "EXIT_SIGNAL",
    "quit" : "EXIT_SIGNAL",
}

# ── HELPER FUNCTIONS ────────────────────────────────────────

def sanitize(raw: str) -> str:
    """Phase 1 – Input Sanitization & Normalization."""
    return raw.lower().strip()


def get_response(clean_input: str) -> str:
    """Phase 2 – Intent Matching via Dictionary (.get fallback)."""
    return responses.get(clean_input, "I do not understand that yet. Try asking something else!")


def run_chatbot():
    """Phase 3 – The Infinite Loop (Heartbeat)."""
    print("=" * 50)
    print("  DecoBot – Rule-Based AI Chatbot")
    print("  Type 'exit' or 'quit' to stop.")
    print("=" * 50)

    # ── THE HEARTBEAT: INFINITE LOOP ────────────────────────
    while True:
        # PHASE 1 – INPUT & SANITIZATION
        raw_input   = input("\nYou: ")
        clean_input = sanitize(raw_input)

        # EXIT STRATEGY – Clean break command
        if clean_input in ("exit", "quit"):
            print("DecoBot: Goodbye! Keep building, keep learning. 🚀")
            break

        # PHASE 2 – PROCESS (Intent Matching)
        reply = get_response(clean_input)

        # PHASE 3 – OUTPUT (Response Generation)
        print(f"DecoBot: {reply}")


# ── ENTRY POINT ─────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
