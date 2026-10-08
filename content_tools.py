def create_content(topic):
    title = f"{topic} 😂 | Kahani Duniya"

    description = f"""
{topic}

Aisi hi funny aur interesting kahaniyon ke liye
Kahani Duniya ko Subscribe karein. ❤️

#KahaniDuniya #HindiStory #FunnyStory #Shorts #YouTube
"""

    hashtags = [
        "#KahaniDuniya",
        "#HindiStory",
        "#FunnyStory",
        "#Shorts",
        "#YouTube"
    ]

    return {
        "title": title,
        "description": description.strip(),
        "hashtags": hashtags
    }
