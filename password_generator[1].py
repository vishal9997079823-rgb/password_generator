"""
========================================
  Smart Password Generator & Strength Checker
  Author : Vishal Bhardwaj
  Tech   : Python, random, string, re
  GitHub : github.com/vishalbhardwaj
========================================

WHAT THIS PROJECT DOES:
  - Generate strong random passwords based on user preferences
  - Check the strength of any existing password
  - Save generated passwords to a text file
  - Allow custom rules: length, uppercase, numbers, symbols
"""

import random
import string
import re
import os
from datetime import datetime


# ── Character sets ──────────────────────────────────────────────────────────
LOWERCASE = string.ascii_lowercase          # a-z
UPPERCASE = string.ascii_uppercase          # A-Z
DIGITS    = string.digits                   # 0-9
SYMBOLS   = "!@#$%^&*()_+-=[]{}|;:,.<>?"  # special characters


# ═══════════════════════════════════════════════════════════
#  GENERATE PASSWORD
# ═══════════════════════════════════════════════════════════
def generate_password(length, use_upper, use_digits, use_symbols):
    """
    Generate a random password based on user preferences.

    Parameters:
        length      (int)  : how many characters long
        use_upper   (bool) : include uppercase letters
        use_digits  (bool) : include numbers
        use_symbols (bool) : include special characters

    Returns:
        str : the generated password
    """

    # Start with lowercase as the base — always included
    character_pool = LOWERCASE

    # Guaranteed characters — ensures at least 1 of each selected type
    guaranteed = []
    guaranteed.append(random.choice(LOWERCASE))   # always add 1 lowercase

    if use_upper:
        character_pool += UPPERCASE
        guaranteed.append(random.choice(UPPERCASE))

    if use_digits:
        character_pool += DIGITS
        guaranteed.append(random.choice(DIGITS))

    if use_symbols:
        character_pool += SYMBOLS
        guaranteed.append(random.choice(SYMBOLS))

    # Fill the rest of the password randomly from the full pool
    remaining_length = length - len(guaranteed)
    random_chars = [random.choice(character_pool) for _ in range(remaining_length)]

    # Combine guaranteed + random, then shuffle so guaranteed chars aren't always first
    all_chars = guaranteed + random_chars
    random.shuffle(all_chars)

    return ''.join(all_chars)


# ═══════════════════════════════════════════════════════════
#  CHECK PASSWORD STRENGTH
# ═══════════════════════════════════════════════════════════
def check_strength(password):
    """
    Analyze a password and return a strength score and feedback.

    Scoring criteria:
        Length >= 8    : +1 point
        Length >= 12   : +1 point
        Has lowercase  : +1 point
        Has uppercase  : +1 point
        Has digits     : +1 point
        Has symbols    : +1 point

    Returns:
        tuple (score, label, suggestions)
    """
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use 12+ characters for stronger security")

    # Check character variety
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z)")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z)")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9)")

    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
        score += 1
    else:
        suggestions.append("Add special characters (!@#$%)")

    # Determine strength label
    if score <= 2:
        label = "WEAK 🔴"
    elif score <= 4:
        label = "MODERATE 🟡"
    else:
        label = "STRONG 🟢"

    return score, label, suggestions


# ═══════════════════════════════════════════════════════════
#  SAVE PASSWORD TO FILE
# ═══════════════════════════════════════════════════════════
def save_password(password, purpose=""):
    """Save a generated password to saved_passwords.txt"""
    filename = "saved_passwords.txt"
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open(filename, 'a') as f:
        f.write(f"[{timestamp}]  Purpose: {purpose if purpose else 'General'}  |  Password: {password}\n")

    print(f"Password saved to '{filename}'")


# ═══════════════════════════════════════════════════════════
#  GENERATE PASSWORD MENU
# ═══════════════════════════════════════════════════════════
def menu_generate():
    print("\n--- GENERATE PASSWORD ---")

    # Get length
    try:
        length = int(input("Enter password length (8-32): "))
        if length < 8 or length > 32:
            print("Length must be between 8 and 32. Setting to 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    # Get preferences
    use_upper   = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits  = input("Include numbers?           (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols?           (y/n): ").strip().lower() == 'y'

    # Generate multiple options so user can choose
    print("\n--- GENERATED PASSWORDS (choose your favourite) ---")
    passwords = []
    for i in range(5):
        pwd = generate_password(length, use_upper, use_digits, use_symbols)
        score, label, _ = check_strength(pwd)
        passwords.append(pwd)
        print(f"  {i+1}. {pwd}   [{label}]")

    # Let user pick one to save
    choice = input("\nEnter number to save (or press Enter to skip): ").strip()
    if choice.isdigit() and 1 <= int(choice) <= 5:
        chosen = passwords[int(choice) - 1]
        purpose = input("What is this password for? (e.g. Gmail, LinkedIn): ").strip()
        save_password(chosen, purpose)
    else:
        print("Password not saved.")


# ═══════════════════════════════════════════════════════════
#  CHECK STRENGTH MENU
# ═══════════════════════════════════════════════════════════
def menu_check_strength():
    print("\n--- CHECK PASSWORD STRENGTH ---")
    password = input("Enter password to check: ").strip()

    if not password:
        print("No password entered.")
        return

    score, label, suggestions = check_strength(password)

    print(f"\nPassword   : {'*' * len(password)}  ({len(password)} characters)")
    print(f"Strength   : {label}  (Score: {score}/6)")

    if suggestions:
        print("\nSuggestions to improve:")
        for tip in suggestions:
            print(f"  - {tip}")
    else:
        print("\nExcellent! This is a very strong password.")


# ═══════════════════════════════════════════════════════════
#  VIEW SAVED PASSWORDS
# ═══════════════════════════════════════════════════════════
def menu_view_saved():
    filename = "saved_passwords.txt"
    print("\n--- SAVED PASSWORDS ---")

    if not os.path.exists(filename):
        print("No passwords saved yet.")
        return

    with open(filename, 'r') as f:
        lines = f.readlines()

    if not lines:
        print("No passwords saved yet.")
    else:
        for line in lines:
            print(" ", line.strip())


# ═══════════════════════════════════════════════════════════
#  MAIN MENU
# ═══════════════════════════════════════════════════════════
def main():
    print("=" * 50)
    print("    SMART PASSWORD GENERATOR & CHECKER")
    print("    Developed by: Vishal Bhardwaj")
    print("=" * 50)

    while True:
        print("\n--- MENU ---")
        print("1. Generate New Password")
        print("2. Check Password Strength")
        print("3. View Saved Passwords")
        print("4. Exit")

        choice = input("\nEnter choice (1-4): ").strip()

        if choice == '1':
            menu_generate()
        elif choice == '2':
            menu_check_strength()
        elif choice == '3':
            menu_view_saved()
        elif choice == '4':
            print("\nStay safe online! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


# ── Entry point ─────────────────────────────────────────────
if __name__ == "__main__":
    main()
