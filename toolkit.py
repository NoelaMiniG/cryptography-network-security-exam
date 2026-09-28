import os
import hashlib
from cryptography.fernet import Fernet

# Function to handle the encryption key locally
def get_encryption_key():
    key_filename = "secret.key"
    
    # If the key already exists, open and read it
    if os.path.exists(key_filename):
        with open(key_filename, "rb") as key_file:
            return key_file.read()
    else:
        # Generate a new key and save it locally
        new_key = Fernet.generate_key()
        with open(key_filename, "wb") as key_file:
            key_file.write(new_key)
        print("Generated new key and saved to secret.key")
        return new_key

# Function to get SHA-256 hash of a file
def get_file_hash(filename):
    try:
        with open(filename, "rb") as f:
            file_data = f.read()
            # Calculate and return hex digest
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found for hashing.")
        return None

# Function to encrypt a file
def encrypt_student_records(input_path, output_path, cipher):
    try:
        with open(input_path, "rb") as f:
            original_data = f.read()
            
        encrypted_data = cipher.encrypt(original_data)
        
        with open(output_path, "wb") as f:
            f.write(encrypted_data)
        print(f"Successfully encrypted {input_path} into {output_path}")
    except FileNotFoundError:
        print(f"Error: Cannot encrypt. {input_path} does not exist.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

# Function to decrypt a file
def decrypt_student_records(input_path, output_path, cipher):
    try:
        with open(input_path, "rb") as f:
            encrypted_data = f.read()
            
        decrypted_data = cipher.decrypt(encrypted_data)
        
        with open(output_path, "wb") as f:
            f.write(decrypted_data)
        print(f"Successfully decrypted {input_path} into {output_path}")
    except FileNotFoundError:
        print(f"Error: Cannot decrypt. {input_path} does not exist.")
    except Exception as e:
        print(f"Decryption failed. Check if the key is correct. Error: {e}")

def main():
    print("--- ULK Security Toolkit ---")
    
    # Get or create the secret key
    secret_key = get_encryption_key()
    fernet_cipher = Fernet(secret_key)
    
    source_file = "student_records.csv"
    encrypted_file = "student_records.enc"
    decrypted_file = "student_records_decrypted.csv"
    
    # Setup dummy data if the student records file doesn't exist yet
    if not os.path.exists(source_file):
        print(f"{source_file} not found. Creating a sample file...")
        with open(source_file, "w") as f:
            f.write("StudentID,Name,Course,Grade\n202401,Alice,ETTCS801,A\n202402,Bob,ETTCS801,B\n")
            
    # 1. Calculate original file hash
    hash_before = get_file_hash(source_file)
    print(f"Original File SHA-256: {hash_before}")
    
    # 2. Run encryption
    encrypt_student_records(source_file, encrypted_file, fernet_cipher)
    
    # 3. Run decryption
    decrypt_student_records(encrypted_file, decrypted_file, fernet_cipher)
    
    # 4. Calculate decrypted file hash and verify integrity
    hash_after = get_file_hash(decrypted_file)
    print(f"Decrypted File SHA-256: {hash_after}")
    
    if hash_before == hash_after:
        print("Success: The original file and decrypted file match exactly! Integrity verified.")
    else:
        print("Warning: Hashes do not match! The file has been modified or corrupted.")

if __name__ == "__main__":
    main()
