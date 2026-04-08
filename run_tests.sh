#!/bin/bash

# ==============================================================================
#                      WELCOME TO THE AUTOMATION HELPER! 🤖
# ==============================================================================
# This is a 'Bash Script'. Think of it as a list of chores that you want the 
# computer to do for you, one by one, without you having to type them manually!
#
# HOW TO LEARN THIS YOURSELF:
# ---------------------------
# 1. 'Shebang' (Line 1): Every bash script starts with #!/bin/bash. It tells the
#    computer: "Hey! Use the Bash language to read this file."
# 2. Variables: We use 'test_status' to remember if the tests passed or failed.
# 3. If/Else: We use 'if' to make decisions, like finding the right folder.
# 4. Exit Codes: 0 means "Success/Hooray!" and 1 means "Error/Oh no!".
# ==============================================================================

# --- STEP 1: WAKE UP THE PROJECT (Activation) ---
# When you work on Python, you usually have a "Virtual Environment" (.venv).
# It's like a special toolbox just for this project.
#
# But Windows and Linux store the 'wake up' (activation) script in different places!
# Windows uses 'Scripts', but Linux (used by CI servers) uses 'bin'.

if [ -d ".venv/Scripts" ]; then
    # If we find a 'Scripts' folder, we are likely on Windows!
    echo "Waking up the Windows toolbox..."
    source .venv/Scripts/activate
else
    # If we don't find 'Scripts', we assume we are on Linux/Mac.
    echo "Waking up the Linux/Mac toolbox..."
    source .venv/bin/activate
fi

# --- STEP 2: RUN THE INSPECTION (Tests) ---
# Now that the project is 'awake', we run our pytest command.
# We use '--headless' so it doesn't try to open a real browser window
# (since CI servers don't have screens!).
pytest --headless test_app.py

# --- STEP 3: REMEMBER THE SCORE ---
# After a command runs, the computer stores a "score" in a secret 
# variable called '$?'. 
# We save that score into our own variable called 'test_status'.
test_status=$?

# --- STEP 4: TELL THE CI SERVER THE RESULT ---
# CI servers are like strict teachers. They look at the 'Exit Code'.
# If the script finishes with 0, the server says: "PASS! You can go play ping pong."
# If the script finishes with 1, the server says: "FAIL! Go back and fix the code."

if [ $test_status -eq 0 ]; then
    echo "========================================"
    echo "✅ ALL TESTS PASSED! YOU ARE A ROCKSTAR!"
    echo "========================================"
    exit 0
else
    echo "========================================"
    echo "❌ TESTS FAILED! PLEASE CHECK THE BUGS."
    echo "========================================"
    exit 1
fi

# ------------------------------------------------------------------------------
# RESOURCES FOR LATER:
# -------------------
# - Want to learn Bash? Check out: https://www.atlassian.com/git/tutorials/dotfiles/bash-scripting
# - Want to learn CI/CD? Look for "GitHub Actions for Beginners" on YouTube.
# - Remember: In Bash, spaces are VERY important! [ $status -eq 0 ] needs spaces!
# ------------------------------------------------------------------------------
