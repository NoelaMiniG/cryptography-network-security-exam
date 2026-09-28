# Cryptography & Network Security Project (Module: ETTCS801)

This project contains a basic Python security toolkit and risk documentation built for the ULK Polytechnic Institute assessment.

## Project Structure
*   `risk_assessment.md` - A Markdown document analyzing network vulnerabilities on campus.
*   `toolkit.py` - The main Python script that handles data encryption, decryption, and file integrity validation.
*   `.gitignore` - A configuration file that tells GitHub to ignore local files like our encryption key so they never get uploaded online.

---

## Technical Overview of the Toolkit

Before running the program, here is an explanation of the core technical concepts used in the code:

1. **Symmetric Encryption (Fernet):** The script uses the `cryptography` library to handle file security. It relies on the **Fernet** standard, which uses a single **secret key** to both encrypt (scramble) and decrypt (unscramble) the student data.
2. **Data Integrity (SHA-256 Hash):** To make sure the data is not altered or corrupted, the script calculates a **SHA-256 checksum** (a unique digital fingerprint) of the file before encryption and after decryption. If the hashes match perfectly, the integrity of the data is verified.
3. **Error Handling:** The code uses `try/except` blocks so that if an input file is missing or a key is invalid, the script prints a helpful error message instead of crashing completely.

---

## How to Setup and Run the Project

### Step 1: Install the External Library
Because Python does not have advanced encryption tools built-in by default, we need to install the external `cryptography` library. Open your terminal or command prompt and run this command:
```bash
pip install cryptography
```

### Step 2: Run the Script
Execute the security toolkit using Python:
```bash
python toolkit.py
```

### Step 3: What Happens Automatically
*   **Key Generation:** On the first run, the script creates a file called `secret.key` on your laptop. Thanks to the `.gitignore` setup, this sensitive key stays safe on your local machine and will not be pushed to GitHub.
*   **Sample Data Setup:** If you don't have a `student_records.csv` file ready, the script will automatically generate a mock file containing sample student identities to test the workflow.
*   **Verification:** The terminal will display the original SHA-256 hash, confirmation of encryption, confirmation of decryption, and the final verification results.
