# 🔐 RAR Brute-Force Scripts

Two Python scripts for performing brute-force attacks on `.rar` archives. Designed for educational purposes, CTFs, or testing secure extraction mechanisms.

---

## Contents

- **`bruteforce_parallel.py`**  
  → Uses Python's `multiprocessing` to run brute-force attempts in parallel (up to 14 workers by default).  
   Great for larger character sets and faster cracking using CPU.

- **`bruteforce_sequential.py`**  
  → A simpler brute-force script using `itertools.permutations`.  
  ❗ Best suited for short passwords due to exponential complexity.

---

## How to Use

1. Install required dependencies:
   ```bash
   pip install rarfile
   ```
3.	Run the script:
```
python rar_bruteforce_parallel.py
```

### Notes
	•	The rar_bruteforce_parallel.py script supports batch processing (100 passwords per task).
	•	The rar_bruteforce_simple.py version is brute-force only with permutations — slower but useful for testing shorter passwords.
	•	Both scripts assume the .rar file is password-protected and uses standard encryption.

### ⚠️ Disclaimer
This project is intended for educational and authorized testing only. Do not use it on systems or files without explicit permission. You are responsible for your actions.
