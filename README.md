# cryptography application

# Crypto Tool

## Overview
**Crypto Tool** is a desktop cryptography application built using Python and the `CustomTkinter` GUI framework.  
The application provides multiple cryptographic functionalities through an easy-to-use graphical interface, allowing users to experiment with different encryption, hashing, and digital signature techniques.

The tool is divided into several tabs, each representing a different cryptographic category:

- Symmetric Encryption
- Asymmetric Encryption
- Hashing
- Digital Signature
- Blind Signature

---

# Features

## Symmetric Encryption
Supports:
- AES Encryption/Decryption
- DES Encryption/Decryption

### Functions
- Encrypt plaintext messages
- Decrypt ciphertext messages
- Load text from files
- Save encrypted/decrypted output to files

### Key Validation
- AES keys: 16, 24, or 32 bytes
- DES keys: 8 bytes

---

## Asymmetric Encryption
Supports:
- RSA Encryption/Decryption

### Functions
- Generate RSA keys dynamically
- Encrypt plaintext using RSA
- Decrypt ciphertext
- Load and save files

---

## Hashing
Supports:
- SHA-256
- MD5

### Functions
- Generate secure hashes for input text
- Load text from files
- Save generated hash output

---

## Digital Signature
Supports:
- RSA-based Digital Signatures

### Functions
- Generate RSA private/public keys
- Sign messages digitally
- Display generated signatures
- Load and save files

---

## Blind Signature
Supports:
- Simulated RSA Blind Signature

### Functions
- Blind and sign messages
- Demonstrate blind signature concepts
- Load and save files

---

# Technologies Used

- Python
- CustomTkinter
- Tkinter
- PyCryptodome

---

# Required Libraries

Install the required dependencies using:

```bash
pip install customtkinter pycryptodome
```

---

# How to Run

Run the application using:

```bash
python filename.py
```

Replace `filename.py` with the name of your Python file.

---

# User Interface

The application contains a modern tab-based interface built with `CustomTkinter`:

- Input and output text areas
- Encryption/decryption controls
- File loading and saving options
- Algorithm selection menus

---

# Project Structure

| Component | Description |
|---|---|
| Symmetric Tab | AES and DES encryption/decryption |
| Asymmetric Tab | RSA encryption/decryption |
| Hash Tab | SHA-256 and MD5 hashing |
| Signature Tab | RSA digital signatures |
| Blind Signature Tab | Blind signature simulation |

---

# Educational Purpose

This project is designed for:

- Learning cryptographic concepts
- Demonstrating encryption algorithms
- Understanding digital signatures
- Exploring hashing techniques
- Practicing GUI development with Python

---

# Notes

- AES and DES use ECB mode in this implementation.
- RSA keys are generated dynamically during execution.
- Blind signature implementation is simplified for demonstration purposes.
- MD5 is included for educational comparison and is not recommended for secure applications.


Developed by **Hager Fathy**
