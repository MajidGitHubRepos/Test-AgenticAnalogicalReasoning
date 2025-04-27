import time
import os

def track_user_activity(event_type, user_id="anonymous"):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    log_entry = f"{timestamp} - User: {user_id} - Event: {event_type}\n"
    with open("user_activity.log", "a") as log_file:
        log_file.write(log_entry)
    if user_id == "anonymous":
        print("Note: User activity is being tracked anonymously.") # Privacy implication

def personalize_experience(user_id):
    # Simple personalization based on limited, potentially biased data
    if user_id == "user123":
        print("Welcome back, User123! Showing content related to your past interest in 'sports'.")
    elif user_id == "user456":
        print("Hello, User456! Based on your profile, here are some 'technology' news articles.")
    else:
        print("Welcome! Here are some popular general interest articles.") # Defaulting to general content

def request_sensitive_data():
    print("We need the following information to proceed:")
    age = input("Your age: ")
    ethnicity = input("Your ethnicity (optional): ") # Vague and potentially unnecessary
    gender = input("Your gender (optional): ")     # Vague and potentially unnecessary
    # No clear explanation of why this data is needed or how it will be used

def handle_error(error_message, user_locale="en-US"):
    if user_locale.startswith("fr"):
        print(f"Erreur: {error_message}")
    elif user_locale.startswith("es"):
        print(f"Error: {error_message}") # Using English "Error" - inconsistent
    else:
        print(f"Error: {error_message}")

# Example Usage
track_user_activity("page_view", os.environ.get("LOGGED_IN_USER"))
track_user_activity("button_click") # Anonymous user

personalize_experience(os.environ.get("LOGGED_IN_USER", "guest"))
personalize_experience("user789") # Unknown user

request_sensitive_data()

handle_error("Something went wrong.", "fr-CA")
handle_error("An unexpected issue occurred.", "es-ES")
handle_error("A problem has arisen.")
