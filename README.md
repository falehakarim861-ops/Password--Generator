# Password--Generator

Faleha Karim- 25BCE11264 

OVERVIEW 
A small, user-friendly tool that generates strong, random passwords according 
to configurable rules (length, character sets, readability options). It can run as 
a CLI script or a simple GUI (Tkinter) and is designed for everyday users who 
need secure, memorable or strictly-random passwords. 
Goals 
Produce high-entropy passwords quickly and safely. 
Let users choose complexity (letters, digits, symbols, ambiguous-char 
removal). 
Provide both CLI and GUI interfaces. 
Avoid storing generated passwords by default (privacy-first). 
Offer copy-to-clipboard and “regenerate” convenience features. 
Key Features 
Configurable length (e.g., 8–64 chars). 
Toggleable character sets: lowercase, uppercase, digits, punctuation. 
Options: exclude ambiguous characters (O, 0, l, I), include user-chosen 
words, pronounceable mode (limited), and pattern mode (e.g., LdlS = 
Letter-digit-letter-Symbol). 
Uses a cryptographically secure RNG (secrets in Python). 
Copy-to-clipboard button and a “copy confirmation” message in GUI. 
Optional password strength meter (entropy estimate). 
How it works (high level) 
1. User selects options (length, character sets, exclusions). 
2. Program builds a character pool accordingly. 
3. Uses secrets.choice() to pick characters to ensure cryptographically secure 
randomness. 
4. Optionally computes entropy and displays an estimated strength label. 
5. Displays password and offers “Copy” and “Regenerate”. 
Recommended Tech / Stack 
Language: Python 3.8+ 
Core libs: secrets, string, argparse (CLI) 
GUI: tkinter (lightweight) or PySimpleGUI / Qt for richer UI 
Optional: pyperclip for cross-platform clipboard support 
Tests: pytest 
Packaging: simple setup.cfg / pyproject.toml for pip installable script 
 
 
 
 
 
 
 
Security Notes (important) 
 
Use secrets (not random) — secrets is designed for crypto use. 
  
Avoid generating passwords deterministically from low-entropy inputs (no 
insecure seeds). 
 
If you show strength/entropy, explain the estimate and assumptions (character 
pool size × length). 
 
If offering a “save” feature, encrypt before saving (and document risks). 
 
 
 
 
 
Example (compact Python function) 
 
import secrets, string 
 
def generate_password(length=16, use_upper=True, use_digits=True, 
use_symbols=True, exclude_ambiguous=True): 
    pool = list(string.ascii_lowercase) 
    if use_upper: pool += list(string.ascii_uppercase) 
    if use_digits: pool += list(string.digits) 
    if use_symbols: pool += list("!@#$%^&*()-_=+[]{};:,.<>?/") 
    if exclude_ambiguous: 
        for ch in "O0lI|`'\"": 
            pool = [c for c in pool if c != ch] 
    return ''.join(secrets.choice(pool) for _ in range(length)) 
 
# Example 
print(generate_password(16)) 
 
README blurb  
Password Generator is a lightweight Python utility that creates secure, random 
passwords with customizable options for length and character sets. It uses 
Python’s secrets module to ensure cryptographic randomness, provides both 
CLI and GUI usage, and prioritizes privacy by not storing generated 
credentials. Perfect for quickly making strong passwords for accounts, test 
data, or sharing securely with a password manager. 
Testing checklist 
Unit tests for character-pool construction and length. 
Entropy/strength calculation tests. 
Clipboard copy tested across platforms (Windows / macOS / Linux). 
GUI: button behaviors, input validation (min/max length), and no exceptions 
on edge cases. 
Fuzz/generation: run many generations to ensure distribution (smoke test). 
Future enhancements / ideas 
Integration with password managers (e.g., KeePassXC plugin or browser 
extension). 
Export options (encrypted JSON) with user passphrase. 
Pronounceable password generator using syllable lists. 
Patterns and mnemonic helpers. 
Mobile-friendly UI or web front-end (Flask/FastAPI + simple frontend). 
Features of password generator 
1. Generates Strong Random Passwords 
Creates secure passwords using a mix of uppercase letters, lowercase letters, 
numbers, and special symbols. 
2. Customizable Password Length 
User can select the password length (e.g., 8 to 20 characters or more). 
3. One-Click Password Generation 
A single click/button instantly produces a new password. 
4. Copy to Clipboard Option 
Users can copy the generated password with one click. 
5. GUI Interface (Tkinter) 
Simple, clean, and user-friendly graphical interface for easy use. 
6. Uses Secure Random Module 
Uses Python’s random/string (or secrets if added) to ensure randomness. 
7. Includes All Character Types 
Password may include: 
Uppercase letters 
Lowercase letters 
Numbers 
Special characters 
8. No Data Storage 
Your application does not save or store any generated passwords, ensuring 
privacy. 
9. Lightweight & Fast 
Runs smoothly on any device with Python installed. 
10. Simple Code Structure 
Easy for beginners to understand and modify. 
Steps to Install and Run the Project 
1. Install Python 
Go to the official Python website 
Download the latest version (Python 3.x) 
Install it and check “Add Python to PATH” 
2. Install Required Libraries 
Tkinter, random, string are already included with Python. 
So no extra installation needed. 
3. Download or Clone the Project 
Option A: Download ZIP 
Go to your GitHub repository 
Click Code → Download ZIP 
Extract it on your computer 
Option B: Clone Using Git 
git clone https://github.com/your-username/your-repo-name.git 
4. Open the Project in VS Code 
Open VS Code 
Click File → Open Folder 
Select your project folder 
Your Python file (e.g., password_generator.py) will appear in the sidebar 
5. Run the Project 
Option A: Using VS Code 
Open your .py file 
Click the Run ▶ button at the top 
OR 
Press Ctrl + F5 
Option B: Using Terminal 
Open terminal/cmd in your project folder and run: 
python password_generator.py 
6. Use the Application 
The Tkinter window will open 
Click Generate Password to create a strong password 
Click Copy to copy it to your clipboard 
7. (Optional) Commit Changes to GitHub 
If you edit anything: 
git add . 
git commit -m "Updated project" 
git push 
Instructions for Testing the Password Generator 
1. Launch the Application 
Run the Python file using VS Code or terminal: 
python password_generator.py 
Ensure the GUI window opens without errors. 
2. Test Password Generation 
Click the “Generate Password” button. 
Verify that: 
A new password appears each time. 
Password length matches the default value (e.g., 12 characters). 
Password contains letters, digits, and symbols. 
3. Test Multiple Generations 
Click the button several times. 
Check that every password is different and random. 
4. Test Copy to Clipboard Feature 
Click the “Copy” button. 
Open any text box (Notepad, WhatsApp, Browser search bar) and press Ctrl + 
V. 
Confirm the password was copied correctly. 
5. Test Error Handling 
Check if the program behaves correctly when: 
User input is empty (if length field exists). 
Invalid length values are entered (e.g., 0, negative, or non-numeric). 
It should show a message or handle gracefully. 
6. Test UI Elements 
Ensure all buttons work. 
Labels update correctly (e.g., “Password Copied ✔”). 
Window size and layout remain proper. 
7. Test Character Inclusion 
Verify that the password includes: 
Uppercase letters 
Lowercase letters 
Numbers 
Special characters 
8. Security Testing (Basic) 
Ensure the app does not save or display old passwords. 
No errors or crashes occur when generating repeatedly. 
9. Cross-Platform (Optional) 
Test running the program on: 
Windows 
macOS 
Linux 
 
