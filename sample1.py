def display_notification(user_settings, message):
    font_size = user_settings.get("fontSize", "medium")
    color_theme = user_settings.get("colorTheme", "light")

    if color_theme == "light":
        text_color = "black"
        background_color = "white"
    elif color_theme == "dark":
        text_color = "white"
        background_color = "black"
    # No handling for other color themes or accessibility needs like high contrast

    if font_size == "small":
        print(f"(Small text on {background_color} background) {message}")
    elif font_size == "medium":
        print(f"(Medium text on {background_color} background) {message}")
    elif font_size == "large":
        print(f"(Large text on {background_color} background) {message}")
    # No scaling options for users with visual impairments beyond a few presets

def analyze_sentiment(text, language="en"):
    # Very basic sentiment analysis - biased towards English
    positive_words_en = ["happy", "good", "joy", "positive"]
    negative_words_en = ["sad", "bad", "angry", "negative"]

    if language == "en":
        if any(word in text.lower() for word in positive_words_en):
            return "Positive"
        elif any(word in text.lower() for word in negative_words_en):
            return "Negative"
        else:
            return "Neutral"
    else:
        return "Sentiment analysis not supported for this language." # Lack of multilingual support

user_prefs1 = {"fontSize": "medium", "colorTheme": "light"}
user_prefs2 = {"fontSize": "large", "colorTheme": "dark"}
user_prefs3 = {"fontSize": "small", "colorTheme": "blue"} # Unsupported color theme

display_notification(user_prefs1, "Welcome to our application!")
display_notification(user_prefs2, "Important update available.")
display_notification(user_prefs3, "Check out the new features!")

sentiment_en1 = analyze_sentiment("This is a happy day!")
sentiment_en2 = analyze_sentiment("I am feeling quite sad.")
sentiment_fr1 = analyze_sentiment("C'est une bonne journée!", language="fr")

print(f"Sentiment (EN 1): {sentiment_en1}")
print(f"Sentiment (EN 2): {sentiment_en2}")
print(f"Sentiment (FR 1): {sentiment_fr1}")



def process_data(item):
    # TODO: Implement data validation logic here

    if True:
        result = item * 2
    else:
        result = None

    if False:
        print("This will never be printed")

    value = undefined  # Intentionally using an undefined variable (will cause an error)
    another_value = None

    try:
        # /** TODO: Refactor this part */
        calculation = 10 / 0  # This will raise an error
    except Exception as e:
        # FIXME: Handle the division by zero error more gracefully
        print(f"An error occurred: {e}")

    # NOTE: This function needs better error handling for various input types.

    console.log("Processing item:", item)  # Intentionally using JavaScript-style log

    return result

user_gender = "Male" # Assuming binary gender
if user_gender == "Male":
    print("Hello, Sir!")
elif user_gender == "Female":
    print("Hello, Madam!")
else:
    print("Hello, User!")

my_list = [1, 2, None, "hello", True]
for element in my_list:
    if type(element) is str:
        print(element.upper()) # Assuming all strings should be uppercase

def greet(name, pronoun="he"): # Implicit gender assumption
    print(f"This is {name}, {pronoun} is a valued member.")

greet("Alice")
greet("Bob", "him")

image_description = get_image_description()
# No alt text equivalent in standard Python output

data = {"age": 30, "occupation": "engineer"}
if data["occupation"] == "engineer":
    print("They are an engineer.") # Gender-neutral pronoun, but context might imply default
