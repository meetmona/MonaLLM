# monallm.py - Mona LLM placeholder file

class MonaLLM:
    def __init__(self, archetype="Sage"):
        """
        Initialize Mona LLM with a specified archetype.
        """
        self.archetype = archetype
        self.intro_message()

    def intro_message(self):
        """
        Prints a brief introduction message based on archetype.
        """
        print(f"[{self.archetype}] Mona LLM initialized. Awaiting your prompts...")

    def generate(self, prompt):
        """
        Simulates generating a response based on a given prompt.
        """
        # Placeholder responses for each archetype
        responses = {
            "Sage": "Patience reveals the true path.",
            "Trickster": "Expect the unexpected!",
            "Dreamer": "Vision shapes reality.",
            "Visionary": "Embrace what lies beyond the horizon."
        }
        response = responses.get(self.archetype, "Insight loading...")
        return f"[{self.archetype}] Mona says: '{response}'"

    def switch_archetype(self, new_archetype):
        """
        Switches the archetype to a new one.
        """
        self.archetype = new_archetype
        print(f"Archetype switched to {self.archetype}.")
        
# Example usage
if __name__ == "__main__":
    # Initialize Mona with a default archetype
    mona = MonaLLM(archetype="Sage")
    
    # Generate a response to a prompt
    prompt = "What lies ahead?"
    print(mona.generate(prompt))
    
    # Switch archetype and generate another response
    mona.switch_archetype("Trickster")
    print(mona.generate(prompt))
