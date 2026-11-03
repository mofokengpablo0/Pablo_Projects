
***

# ⚡ FizzBuzz Challenge

A simple Python implementation of the classic FizzBuzz logic test. This project is part of my programming fundamentals journey to practice conditional logic and loop structures.

## 📝 The Challenge
The goal is to write a program that prints numbers from 1 to 100. However, there are specific rules for certain numbers:
- If the number is a **multiple of 3**, print `"Fizz"` instead of the number.
- If the number is a **multiple of 5**, print `"Buzz"` instead of the number.
- If the number is a **multiple of both 3 and 5**, print `"FizzBuzz"`.
- Otherwise, just print the number.

## 🚀 How it Works
The core of this program relies on the **Modulo Operator (`%`)**. 

The modulo operator returns the **remainder** of a division. In this program, we use it to check if a number is perfectly divisible by 3 or 5. If the remainder is `0`, it means the number is a multiple.

**Logic Flow:**
1. **Check for both (3 and 5):** We check if `i % 3 == 0` AND `i % 5 == 0` first. This ensures that numbers like 15 are caught as "FizzBuzz" before they are caught by the individual "Fizz" or "Buzz" rules.
2. **Check for 3:** If not divisible by both, we check if `i % 3 == 0`.
3. **Check for 5:** If not divisible by 3, we check if `i % 5 == 0`.
4. **Default:** If none of the above are true, the number itself is printed.

## 💻 Code Implementation

```python
def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    fizz_buzz()
```

## 🛠️ How to Run
1. Ensure you have [Python](https://www.python.org/) installed on your machine.
2. Copy the code into a file named `FizzBuzz.py`.
3. Open your terminal or command prompt.
4. Run the program using:
   ```bash
   python fizzbuzz.py
   ```

## 📊 Example Output
```text
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
...
14
FizzBuzz
16
```

---
**Objective:** Practice conditional logic and basic loops. ✅