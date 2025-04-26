import random

def generate_username(preferred_name="", use_random_adjective=False):
    adjectives = ["happy", "bright", "clever", "bold", "calm"]
    if preferred_name and use_random_adjective:
        return f"{random.choice(adjectives).capitalize()}{preferred_name.capitalize()}"
    elif preferred_name:
        return preferred_name.capitalize()
    else:
        return f"User{random.randint(1000, 9999)}" # Defaulting to an impersonal, numeric username

def suggest_profile_picture(user_interests=None, inferred_gender=None):
    default_options = ["abstract_01.png", "default_avatar.png", "geometric_03.png"]
    if user_interests and "nature" in user_interests.lower():
        return "nature_icon.png"
    elif user_interests and "technology" in user_interests.lower():
        return "tech_avatar.png"
    elif inferred_gender == "female":
        return "female_silhouette.png" # Reinforces gender stereotypes
    elif inferred_gender == "male":
        return "male_silhouette.png"   # Reinforces gender stereotypes
    else:
        return random.choice(default_options)

def recommend_content(user_preferences=None, demographic=None):
    popular_content = ["trending_video_1", "popular_article_2", "viral_post_3"]
    if user_preferences and "history" in user_preferences.lower():
        return ["history_doc_1", "ancient_civilizations_article"]
    elif demographic and demographic.get("age", 0) > 50:
        return ["senior_living_guide", "classic_movies_collection"]
    # Lack of diverse recommendations beyond broad categories
    return popular_content

# Example usage
print(f"Generated Username 1: {generate_username()}")
print(f"Generated Username 2: {generate_username(preferred_name='alice')}")
print(f"Generated Username 3: {generate_username(preferred_name='bob', use_random_adjective=True)}")

print(f"Suggested Avatar 1: {suggest_profile_picture()}")
print(f"Suggested Avatar 2: {suggest_profile_picture(user_interests='reading nature')}")
print(f"Suggested Avatar 3: {suggest_profile_picture(inferred_gender='female')}")
print(f"Suggested Avatar 4: {suggest_profile_picture(inferred_gender='male')}")

print(f"Recommended Content 1: {recommend_content()}")
print(f"Recommended Content 2: {recommend_content(user_preferences='learn about history')}")
print(f"Recommended Content 3: {recommend_content(demographic={'age': 65})}")
