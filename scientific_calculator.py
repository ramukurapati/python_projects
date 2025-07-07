import ast
import operator
import re

# Step 1: Allowed math operators
allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}


# Step 2: Validate the number of numeric values (2 to 9)
def validate_numbers(expression):
    numbers = re.findall(r'\b\d+\b', expression)
    if len(numbers) < 2:
        raise ValueError("Must include at least 2 numbers.")
    if len(numbers) > 9:
        raise ValueError("Cannot include more than 9 numbers.")

# Step 3: Safe evaluation using AST (no eval())
def safe_eval(node):
    if isinstance(node, ast.Expression):
        return safe_eval(node.body)
    elif isinstance(node, ast.BinOp):
        return allowed_operators[type(node.op)](
            safe_eval(node.left), safe_eval(node.right)
        )
    elif isinstance(node, ast.UnaryOp):
        return allowed_operators[type(node.op)](safe_eval(node.operand))
    elif isinstance(node, ast.Num):        # For Python < 3.8
        return node.n
    elif isinstance(node, ast.Constant):   # For Python ≥ 3.8
        return node.value
    else:
        raise TypeError("Unsupported expression.")

# Step 4: Main function to run the calculator
def main():
    print("Simple BODMAS Calculator (2 to 9 numbers)")
    try:
        expr = input("Enter expression: ").replace(" ", "")
        validate_numbers(expr)
        tree = ast.parse(expr, mode='eval')
        result = safe_eval(tree)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

# Step 5: Run the program
if __name__ == "__main__":
    main()
