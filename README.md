# 🔐 Smart Password Generator & Strength Checker

A Python command-line tool that generates secure random passwords based on custom rules and checks the strength of any existing password with detailed feedback.

## 🛠️ Tech Stack
- **Python 3.8+**
- `random` — secure random character selection
- `string` — character set constants
- `re` — regex for strength validation

## ✨ Features
- 🎲 Generate 5 password options at once — pick your favourite
- 🔒 Custom rules: length (8–32), uppercase, numbers, symbols
- 💪 Strength checker with score out of 6 and improvement tips
- 💾 Save passwords with purpose label to a text file
- 📋 View all previously saved passwords

## 🚀 How to Run

```bash
# No installation needed — uses Python built-in libraries only!
python password_generator.py
```

## 📸 Sample Output

```
--- GENERATED PASSWORDS ---
  1. Kx9#mQpL2!vN   [STRONG 🟢]
  2. r$7TnWq@4mBz   [STRONG 🟢]
  3. Gp2!kLxQ8#mR   [STRONG 🟢]

--- CHECK PASSWORD STRENGTH ---
Password   : ************  (12 characters)
Strength   : STRONG 🟢  (Score: 6/6)
```

## 📁 Project Structure
```
password_generator/
│
├── password_generator.py   # Main application
├── saved_passwords.txt     # Auto-generated when you save a password
└── README.md
```

## 💡 What I Learned
- Using Python's built-in `random` and `string` modules
- **Regex (re module)** for pattern matching and validation
- Designing a **scoring algorithm** with logic conditions
- Writing **modular functions** — each feature in its own function

## 👨‍💻 Author
**Vishal Bhardwaj** — MCA (Graduating March 2026)  
[LinkedIn](https://www.linkedin.com/in/vishalbhardwaj-290bb3386)
