import re
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 14:
        score += 2
    elif len(password) >= 9:
        score += 1
    else:
        feedback.append("Password should be at least 9 characters long.")
    
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Use both uppercase and lowercase letters.")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Include at least one number.")
    
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Include at least one special character (!, @, #, etc.).")

    common_patterns = ["password", "1234567", "qwerty", "letmein", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        feedback.append("Avoid common passwords like 'password' or '1234567'.")
    
    if re.search(r'(.)\1{2,}', password):
        feedback.append("Avoid repeated characters.")
    
    strength_levels = {0: "Very Weak", 1: "Weak", 2: "Moderate", 3: "Strong", 4: "Very Strong", 5: "Excellent"}
    strength = strength_levels.get(score, "Very Weak")
    
    return strength, feedback

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    strength, suggestions = check_password_strength(user_password)
    print(f"Password Strength: {strength}")
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
