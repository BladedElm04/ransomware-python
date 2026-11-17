# Python Cryptography Study

Educational project developed to explore file encryption and decryption using Python and the AES (Advanced Encryption Standard) algorithm.

The project uses the `pyaes` library to demonstrate how symmetric encryption works in practice.

> **Disclaimer:** This project is intended strictly for educational purposes and controlled testing. It is not designed for production use or for encrypting files without their owner's explicit permission.

## Technologies

- Python 3
- AES (Advanced Encryption Standard)
- PyAES

## Project Structure

```text
ransomware-python/
├── decrypter.py
├── encrypter.py
├── test.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/BladedElm04/ransomware-python.git

cd ransomware-python
```

### 2. Check Python installation

Make sure Python 3 is installed:

```bash
python3 --version
```

### 3. Create a virtual environment

Creating a virtual environment keeps project dependencies isolated from your system Python installation.

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**Linux / macOS / WSL:**

```bash
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

Update pip:

```bash
python -m pip install --upgrade pip
```

Install PyAES:

```bash
pip install pyaes
```

Alternatively, install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the Project

With the virtual environment activated, run the Python scripts:

```bash
python encrypter.py
```

To run the decryption script:

```bash
python decrypter.py
```

Use only test files created specifically for this project.

## Deactivating the Virtual Environment

When finished, deactivate the environment:

```bash
deactivate
```

## Learning Objectives

- Understand symmetric encryption.
- Explore the AES encryption algorithm.
- Learn how Python libraries implement cryptographic operations.
- Understand the relationship between encryption keys, encryption and decryption.
- Practice Python development and dependency management.

## Disclaimer

This repository is part of a personal learning project. All experiments should be performed exclusively in isolated environments using disposable test files.

Never use this software against systems, files or data without explicit authorization.

## Author

**BladedElm04**

GitHub: [github.com/BladedElm04](https://github.com/BladedElm04)