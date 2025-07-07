# 🧮 BODMAS Calculator – Python CLI Project

A beginner-friendly calculator built using **Python** that evaluates arithmetic expressions while strictly following the **BODMAS rule**. It’s designed to ensure **safe evaluation**, accepts only valid input, and provides a great learning opportunity for new programmers.

---

## 📌 What This Project **Does**

✅ **Evaluates arithmetic expressions** that include:
- Brackets: `( )`
- Powers: `**`
- Division: `/`
- Multiplication: `*`
- Addition: `+`
- Subtraction: `-`

✅ **Respects BODMAS rule** to calculate the expression in the correct order

✅ Accepts expressions containing:
- **Minimum of 2 numbers**
- **Maximum of 9 numbers**

✅ Validates input before execution

✅ Parses and evaluates expressions using **Python’s AST (Abstract Syntax Tree)** to ensure safe and secure execution

✅ Works entirely in a **command-line interface (CLI)**

---

## 🚫 What This Project **Does Not Do**

❌ It does **not** support scientific functions (e.g., `sqrt`, `log`, `sin`, etc.)

❌ It does **not** allow more than 9 or fewer than 2 numbers

❌ It does **not** use `eval()` for execution, which can be dangerous

❌ It does **not** handle variables or text input (only pure math expressions are allowed)

❌ It does **not** have a GUI (graphic interface) — CLI only

---

## 🧠 What is BODMAS?

**BODMAS** stands for:

| Letter | Meaning          |
|--------|------------------|
| B      | Brackets         |
| O      | Orders (powers)  |
| D      | Division         |
| M      | Multiplication   |
| A      | Addition         |
| S      | Subtraction      |

This is the **standard order** in which operations are performed in arithmetic.

## 🛠️ How It Works – Step by Step

1. 🔢 **Takes input** from the user (e.g., `(2 + 3) * 4`)
2. 🔍 **Validates** the number of numeric values using regex (`re`)
   - Must have **between 2 and 9** numbers
3. 🧱 **Parses** the expression using `ast.parse()`
   - Turns the input into a safe tree of operations
4. ⚙️ **Evaluates** it recursively using the `safe_eval()` function
   - Supports only allowed arithmetic operators
5. 🖨️ **Displays result** or a clear error if invalid

---
📐 Simple BODMAS Calculator (2 to 9 numbers)
Enter your expression: (2 + 3) * 4
✅ Result: 20
---
Enter your expression: 5
❌ Must include at least 2 numbers.
---
Enter your expression: 1+2+3+4+5+6+7+8+9+10
❌ Cannot include more than 9 numbers.
---
### 📥 Installation & Execution

1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/bodmas-calculator.git
   cd bodmas-calculator
## 🧾 Safe Evaluation — Why No `eval()`?

Python’s built-in `eval()` can be **extremely dangerous**, especially for beginners.


Example:
```python
eval("__import__('os').system('rm -rf /')")  # DANGEROUS!

---