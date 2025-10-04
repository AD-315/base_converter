# Manual Numerical Base Converter (Base 2-16)

## Overview
This is a terminal based Python program that converts numbers between different numerical bases (from 2 to 16). Users can input a number, specify its original base, and select the target base to convert to. The program only handles **positive integers** (no negative numbers or floats) and provides clear error messages for invalid inputs.

This program was designed as part of a learning assignment to practice manual base conversions without relying on Python’s built-in base conversion functions.

---

## Features
- Converts numbers between **any base from 2 to 16**.
- Supports **uppercase and lowercase letters** for hexadecimal digits.
- Provides input validation:
  - Rejects negative numbers and floats.
  - Rejects invalid digits for the selected base.
  - Rejects bases outside the range 2–16.
- Repeatable terminal UI: allows multiple conversions without restarting the program.
- Clear error messages for incorrect inputs.

---

## Requirements
- Python 3.x
- No additional libraries required

---

## How to Run
1. Clone the repository:
   ```bash
   git clone <repository-url>
