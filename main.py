from content_tools import create_content

topic = "Ganesh Ji Ki Funny Kahani"

result = create_content(topic)

print("TITLE:", result["title"])
print("DESCRIPTION:", result["description"])
print("HASHTAGS:", " ".join(result["hashtags"]))
