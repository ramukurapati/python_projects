import ast
import operator
import re

# ✅ Allowed operators for BODMAS
allowed_ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}

# ✅ Check if input has only allowed characters
def validate_characters(expr):
    if not re.fullmatch(r"[0-9\+\-\*/\(\)\.\s\*]*", expr):
        raise ValueError("Expression contains invalid characters. Use only digits and BODMAS operators: + - * / ** ( )")

# ✅ Check if expression has 2 to 9 numbers
def validate_number_count(expr):
    numbers = re.findall(r'\d+(\.\d+)?', expr)
    count = len(numbers)
    if count < 2:
        raise ValueError("Expression must contain at least 2 values.")
    if count > 9:
        raise ValueError("Expression cannot contain more than 9 values.")

# ✅ AST-based safe evaluation
def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    elif isinstance(node, ast.BinOp):
        if type(node.op) not in allowed_ops:
            raise TypeError("Only BODMAS operators (+, -, *, /, **) are allowed.")
        return allowed_ops[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):
        if type(node.op) not in allowed_ops:
            raise TypeError("Unary operator not supported.")
        return allowed_ops[type(node.op)](safe_eval(node.operand))
    elif isinstance(node, ast.Num):  # For Python <3.8
        return node.n
    elif isinstance(node, ast.Constant):  # For Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        else:
            raise TypeError("Only numbers are allowed.")
    else:
        raise TypeError("Unsupported format in expression.")

# ✅ Main calculator loop
def main():
    print("🧮 Welcome to the BODMAS Rules Calculator!")
    print("Type an expression using only: numbers, +, -, *, /, **, (). Type 'exit' to quit.\n")

    while True:
        expr = input("Enter expression: ").strip()

        if expr.lower() == "exit":
            print("👋 Exiting calculator. Goodbye!")
            break

        try:
            validate_characters(expr)
            validate_number_count(expr)
            parsed = ast.parse(expr, mode='eval')
            result = safe_eval(parsed)
            print(f"✅ Result: {result}\n")

        except ValueError as ve:
            print(f"❌ Error: {ve}\n")
        except SyntaxError:
            print("❌ Error: Invalid format. Please check your parentheses and operator usage.\n")
        except TypeError as te:
            print(f"❌ Error: {te}\n")
        except ZeroDivisionError:
            print("❌ Error: Division by zero is not allowed.\n")
        except Exception as e:
            print(f"❌ Unexpected error: {e}\n")

# ✅ Run program
if __name__ == "__main__":
    main()
