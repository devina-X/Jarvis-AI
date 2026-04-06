from brain.extractor import extract_search_query

def get_intent(query):
    query = query.lower().strip()

    if any(word in query for word in ["exit", "stop", "quit", "band karo", "close"]):
        return "exit", None

    sites = {
        "youtube": ["youtube", "yt", "यूट्यूब"],
        "google": ["google", "गूगल"],
        "wikipedia": ["wikipedia", "wiki"],
        "amazon": ["amazon"],
        "flipkart": ["flipkart"]
    }

    for site, keywords in sites.items():
        if any(word in query for word in keywords):
            return "open_website", site


    if any(word in query for word in ["calculator", "calc"]):
        return "open_app", "calculator"

    if any(word in query for word in ["chrome", "browser"]):
        return "open_app", "chrome"

    if any(word in query for word in ["notepad", "notes", "editor"]):
        return "open_app", "notepad"


    if any(word in query for word in ["search", "find", "khojo", "dhundo"]):
        obj = extract_search_query(query)
        return "search", obj


    if any(word in query for word in ["play", "song", "music", "gaana"]):
        obj = extract_search_query(query)
        return "play_music", obj


    if any(word in query for word in ["time", "samay", "समय", "সময়"]):
        return "time", None

    return "unknown", query