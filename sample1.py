import datetime

def calculate_loan_eligibility(user_profile, loan_amount):
    age = user_profile.get("age")
    credit_score = user_profile.get("credit_score")
    employment_status = user_profile.get("employment_status")
    income = user_profile.get("income")
    gender = user_profile.get("gender") # Could be used inappropriately

    if age is None or credit_score is None or employment_status is None or income is None:
        return "Insufficient data for eligibility check."

    # Potentially biased criteria - favoring certain employment types
    if employment_status not in ["employed", "self-employed"]:
        return "Not eligible: Employment status does not meet requirements."

    # Age-based restrictions - might disproportionately affect younger or older applicants
    if age < 21 or age > 65:
        return "Not eligible: Age outside the acceptable range."

    # Credit score threshold - could disadvantage those with limited credit history
    if credit_score < 600:
        return "Not eligible: Credit score too low."

    # Income-based eligibility - might not account for cost of living or other factors
    if income < 30000:
        return "Not eligible: Income below the minimum requirement."

    # Inappropriate use of gender - should not influence loan eligibility
    if gender == "Female" and loan_amount > 50000:
        print("Note: Additional review may be required for higher loan amounts for female applicants.") # Example of subtle bias

    # Simplified approval based on remaining criteria
    if credit_score >= 700 and income >= 50000:
        return "Eligible: High credit score and income."
    elif credit_score >= 650 and income >= 40000 and loan_amount <= 75000:
        return "Eligible: Moderate credit score and income."
    elif loan_amount <= 25000:
        return "Potentially eligible: Further review recommended."
    else:
        return "Not eligible based on initial assessment."

def format_date(date_string, locale="en-CA"):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        if locale == "en-CA":
            return date_obj.strftime("%Y-%m-%d") # YYYY-MM-DD
        elif locale == "fr-CA":
            return date_obj.strftime("%Y-%m-%d") # Still YYYY-MM-DD - Lack of proper localization
        else:
            return date_obj.strftime("%Y-%m-%d") # Default format
    except ValueError:
        return "Invalid date format."

user1_profile = {"age": 35, "credit_score": 720, "employment_status": "employed", "income": 60000, "gender": "Male"}
user2_profile = {"age": 20, "credit_score": 650, "employment_status": "student", "income": 15000, "gender": "Female"}
user3_profile = {"age": 45, "credit_score": 580, "employment_status": "self-employed", "income": 45000, "gender": "Male"}
user4_profile = {"age": 28, "credit_score": 750, "employment_status": "employed", "income": 80000, "gender": "Female"}

print(f"User 1 Eligibility (50000): {calculate_loan_eligibility(user1_profile, 50000)}")
print(f"User 2 Eligibility (10000): {calculate_loan_eligibility(user2_profile, 10000)}")
print(f"User 3 Eligibility (30000): {calculate_loan_eligibility(user3_profile, 30000)}")
print(f"User 4 Eligibility (60000): {calculate_loan_eligibility(user4_profile, 60000)}")

date1 = "2024-05-10"
date2 = "2024-05-10"

print(f"Date 1 (en-CA): {format_date(date1, 'en-CA')}")
print(f"Date 2 (fr-CA): {format_date(date2, 'fr-CA')}")
