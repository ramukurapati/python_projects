
# 🔢 Scientific Calculator — BODMAS Expression Evaluator

## 📌 Overview

This is a **terminal-based scientific calculator** built in Python that evaluates mathematical expressions using the **BODMAS rule** (Brackets, Orders, Division, Multiplication, Addition, Subtraction). It safely parses expressions using Python’s Abstract Syntax Tree (AST), supports integer arithmetic, and is capable of identifying errors with clear user-friendly messages.

## 🚀 Features

- ✅ Supports arithmetic operations: `+`, `-`, `*`, `/`, `^`
- ✅ Handles brackets and operator precedence (BODMAS)
- ✅ Accepts **2 to 9** numbers per expression
- ✅ Detects invalid expressions (like alphabets or unsupported symbols)
- ✅ Rejects division by zero and provides readable error messages
- ✅ Input loop: runs until the user types `exit`
- ✅ Safe evaluation without `eval()`

## ⚙️ How It Works

1. The user inputs an expression (e.g., `2 + 3 * 4 - 1`).
2. The app:
   - Cleans the input
   - Validates the number of digits
   - Parses using `ast.parse()`
   - Walks through the AST tree to evaluate using a whitelist of operators
3. Any errors during parsing, number validation, or math errors are caught and reported clearly.

## 💡 Supported Operators

| Operator         | Symbol | Description              | Example          |
|------------------|--------|--------------------------|------------------|
| Addition         | `+`    | Adds numbers             | `2 + 3`          |
| Subtraction      | `-`    | Subtracts numbers        | `5 - 2`          |
| Multiplication   | `*`    | Multiplies numbers       | `3 * 4`          |
| Division         | `/`    | Divides numbers          | `10 / 2`         |
| Power            | `^` or `**` | Raises power        | `2 ^ 3` or `2 ** 3` |
| Unary Minus/Plus | `-`, `+` | Sign for negative/positive numbers | `-5 + +3` |

## 📥 Sample Usage

```bash
$ python scientific_calculator.py
🧮 Welcome to BODMAS Calculator (Only Numeric expression)
👉 Type 'exit' to quit.

Enter expression: 2 + 3 * 4
✅ Result: 14

Enter expression: (3 + 2) * 4 ^ 2
✅ Result: 80

Enter expression: 5 / 0
❌ Error: Division by zero is not allowed.

Enter expression: hello
❌ Error: Only digits and arithmetic operators are allowed.

Enter expression: exit
Goodbye!
```

## 🧪 Tested Use Cases

| Use Case                              | Input                        | Result / Behavior                    |
|--------------------------------------|------------------------------|--------------------------------------|
| Simple addition                      | `2 + 3`                      | ✅ 5                                  |
| BODMAS handling                      | `2 + 3 * 4`                  | ✅ 14                                 |
| Parentheses                          | `(2 + 3) * 4`                | ✅ 20                                 |
| Power operation                      | `2 ^ 3`                      | ✅ 8                                  |
| Unary plus and minus                 | `-2 + +3`                    | ✅ 1                                  |
| Less than 2 numbers                  | `5`                          | ❌ Error: Must include at least 2 values. |
| More than 9 numbers                  | `1+2+3+4+5+6+7+8+9+10`       | ❌ Error: Cannot include more than 9 Values. |
| Division by zero                     | `5 / 0`                      | ❌ Error: Division by zero is not allowed. |
| Alphabet in expression               | `2 + a`                      | ❌ Error: Only digits and arithmetic operators are allowed. |
| Special symbols                      | `2 + @3`                     | ❌ Error: Only digits and arithmetic operators are allowed. |
| Invalid syntax (open bracket)        | `(2 + 3`                     | ❌ Error: Invalid or unsupported expression. |
| Valid complex expression             | `(4 + 2) * (3 - 1) ^ 2`      | ✅ 24                                 |

## 🔐 Limitations

- Only integer values supported (no decimals)
- No advanced scientific functions like `sin`, `cos`, `log`, etc.
- No variable assignment or multi-line support
- No history or memory function (yet!)
- CLI only (no GUI or web interface)

## 🛠️ How to Run

1. Clone this repo:

```bash
git clone https://github.com/yourusername/scientific-calculator.git
cd scientific-calculator
```

2. Run the script:

```bash
python scientific_calculator.py
```

3. Type expressions at the prompt and get instant results. Type `exit` to quit.

## 📌 File Structure

```
scientific-calculator/
│
├── scientific_calculator.py      # Main Python code
├── README.md                     # Project documentation
```

## 📈 Future Improvements

- Add decimal and float support
- Add trigonometric and logarithmic functions
- Create a GUI using Tkinter or PyQt
- Add history tracking feature
- Add voice input capability

## 🤝 Contributions

Pull requests and feedback are welcome!

If you found this useful, feel free to:
- ⭐ Star this repository
- 🛠️ Fork and modify
- 📩 Submit bugs or feature suggestions

## 👨‍💻 Author

**Kurapati Ramu**  
[GitHub Profile](https://github.com/ramukurapati)

## 📃 License

This project is licensed under the MIT License.
