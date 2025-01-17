import os
import subprocess
from datetime import datetime, timedelta
import random

# Set the start date to a recent date, e.g., January 2024
start_date = datetime(2024, 1, 1)

# Set the name of your repository
repo_name = "Saifrazzaq1"  # Your GitHub repository name

# Set the path to your repository folder (current working directory)
repo_path = os.getcwd()  # Get the current working directory

# Function to create fake commits
def create_fake_commits():
    for _ in range(50):  # Create 50 fake commits
        commit_date = start_date + timedelta(days=random.randint(0, 365))  # Random date
        commit_message = f"Fake commit #{_ + 1}"

        # Create or modify a dummy file
        with open("fake_contributions.txt", "a") as f:
            f.write(f"Fake commit message: {commit_message}\n")

        # Add and commit the changes
        subprocess.run(["git", "add", "fake_contributions.txt"])
        subprocess.run(["git", "commit", "--date", commit_date.isoformat(), "-m", commit_message])

# Push changes to GitHub
def push_changes():
    subprocess.run(["git", "push", "--force"])

# Create fake commits and push
create_fake_commits()
push_changes()

print("Fake contributions added successfully!")
