import win32com.client as wc
speaker = wc.Dispatch("SAPI.SpVoice")

def say(text):
    try:
        print("Jarvis:", text)
        speaker.Speak(text)
    except Exception as e:
        print("TTS Error:", e)

def set_speed(rate=150):
    """
    Default = 150
    Lower = slower speech
    Higher = faster speech
    """
    speaker.Rate = rate

def set_voice(index=0):
    voices = speaker.GetVoices()
    speaker.Voice = voices.Item(index)