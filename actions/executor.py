import webbrowser
import os
from core.tts import say


def execute_intent(intent, obj):

    if intent == "exit":
        say("Goodbye")
        return False

    elif intent == "open_website":
        say(f"Opening {obj}")
        webbrowser.open(f"https://www.{obj}.com")

    elif intent == "search":
        say("Searching Google")
        webbrowser.open(f"https://www.google.com/search?q={obj}")

    elif intent == "play_music":
        say("Playing on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={obj}")

    elif intent == "open_app":

        if obj == "calculator":
            say("Opening Calculator")
            os.system("calc")

        elif obj == "chrome":
            say("Opening Chrome")
            os.system("start chrome")

        elif obj == "notepad":
            say("Opening Notepad")
            os.system("notepad")

    else:
        say("Searching on Google")
        webbrowser.open(f"https://www.google.com/search?q={obj}")

    return True