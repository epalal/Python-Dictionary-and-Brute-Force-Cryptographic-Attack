import base64
import os
import itertools
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# The salt and ciphertext provided in the hands-on slides
salt = b"\xd2\xffs~\xb4\xf2\xd3\xda\xe3\x16('\xe6\xad\xef\xaf"
cyphertext = b'gAAAAABnE2P-qqJT-HudMbLcykzIx83XqZNEt6UqfyBBzhYKvlF9WSx8FJUvUmatzuY1-io9RHWaj7RVBuAKTWRAVT9GpGC--TZUXk387qeTC2jIJOfUrwSX3eGEb1EVFZBOqALd8EKS1CFWUoF4NpzKsc3eLeCnXihb-w6Boqi835uNzN6mZz4iP-6sSkhNxHP-TbrG-BNgjMIyeRDjSLAZhEAJoUGlz_QuOyyOYHMab9LUrXkHibU='

#dictionary = ["gatto", "giulia", "martina", "password", "pisa", "poesia", "qwerty", "sicurezza", "storia", "tavolo"]
dictionary = ["sicurezza", "storia", "tavolo"]
special_chars = ["!", "$", "%", "&", "?", "^", "*", "+", "@", "#"]
numbers = [str(i) for i in range(10)]

def try_decrypt(passwd_str):
    passwd_bytes = passwd_str.encode('utf-8')
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    # Derive key and attempt decryption
    try:
        key = base64.urlsafe_b64encode(kdf.derive(passwd_bytes))
        f = Fernet(key)
        plaintext = f.decrypt(cyphertext)
        print(f"\n[SUCCESS] Password found: {passwd_str}")
        return True
    except Exception:
        return False


print("Starting Brute Force Attack...")
start_time = time.time()

found = False

# Iterate through each word in the dictionary
for word in dictionary:
    if found: break
    #updates at each iteration to show progress
    print(f"Trying base word: {word}")
    # 1. Capitalize one character (or none, though exercise suggests one)
    # We iterate through the word length to capitalize one char at index i
    for i in range(len(word)):
        # Create base word with one capital letter
        cap_word = word[:i] + word[i].upper() + word[i+1:]
        
        # 2. Insert a Number (0-9) in any position
        # Positions range from 0 (start) to len (end)
        for num in numbers:
            for pos_num in range(len(cap_word) + 1):
                word_with_num = cap_word[:pos_num] + num + cap_word[pos_num:]
                
                # 3. Insert a Special Character in any position
                # Positions range from 0 to len (end of new word)
                for sym in special_chars:
                    for pos_sym in range(len(word_with_num) + 1):
                        candidate = word_with_num[:pos_sym] + sym + word_with_num[pos_sym:]
                        # Attempt to decrypt
                        if try_decrypt(candidate):
                            found = True
                            end_time = time.time()
                            print(f"Time elapsed: {end_time - start_time:.2f} seconds")
                            break
                    if found: break
                if found: break
            if found: break
        if found: break

if not found:
    print("\n[FAILURE] Password not found in the generated set.")