def extract_search_query(query):
    keywords = ["search", "find", "google", "play"]

    words = query.lower().split()

    for keyword in keywords:
        if keyword in words:
            index = words.index(keyword)

            if index + 1 < len(words):
                return " ".join(words[index + 1:])

    return query