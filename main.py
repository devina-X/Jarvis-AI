from core.speech import take_command
from core.tts import say
from brain.intent import get_intent
from actions.executor import execute_intent


def main():
    say("Welcome to Jarvis")

    running = True

    while running:
        query, lang = take_command()

        if query == "":
            continue

        print(f"Detected Language: {lang}")

        intent, obj = get_intent(query)

        running = execute_intent(intent, obj)


if __name__ == "__main__":
    main()