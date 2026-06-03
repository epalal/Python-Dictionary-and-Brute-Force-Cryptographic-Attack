# Python Dictionary and Brute-Force Cryptographic Attack

### Project Overview
This project demonstrates a cryptographic brute-force attack. It targets a specific ciphertext accompanied by a known cryptographic salt. The implementation utilizes systematic string permutations to deduce the original encryption password.

### Cryptographic Primitives
The decryption sequence relies on robust cryptographic standards:
* The script utilizes the `cryptography` Python package for core operations.
* Key derivation employs the PBKDF2HMAC algorithm.
* The key derivation function utilizes SHA256 hashing, a 32-byte length, and 100,000 algorithmic iterations.
* The derived key decrypts data secured with the Fernet symmetric encryption protocol.
* The Base64 encoding converts byte data into ASCII characters to prevent data corruption.

### Attack Methodology
The algorithm constructs password candidates based on predetermined formatting assumptions:
* The attack assumes the sender utilized a foundational dictionary word.
* The foundational dictionary includes predefined strings, such as "gatto", "giulia", "martina", and "sicurezza".
* The script modifies each dictionary string by capitalizing exactly one alphabetical character.
* The script subsequently inserts one numerical digit, ranging from 0 to 9, into any positional index.
* The script finally inserts one of ten specific special characters (`!$%&?^*+@#`) into any positional index.
* The script utilizes iterative nested loops to generate and test all possible permutations systematically.
