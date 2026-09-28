def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b


print(" Simple Calculator + 2x2 Matrix Calculator")

while True:
    print("Options:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Multiply two numbers")
    print("4. Divide two numbers")
    print("5. 2x2 Matrix Addition")
    print("6. 2x2 Matrix Subtraction")
    print("7. 2x2 Matrix Multiplication")
    print("8. Exit")

    ch = input("Choose (1-8): ")

    if ch == "1":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Result:", add(a, b))

    elif ch == "2":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Result:", subtract(a, b))

    elif ch == "3":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print("Result:", multiply(a, b))

    elif ch == "4":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        res = divide(a, b)
        if res is None:
            print("Error: cannot divide by zero")
        else:
            print("Result:", res)

    elif ch == "5":  
        print("2x2 Matrix Addition (A + B) ---")
        print("Enter matrix A:")
        A = []
        for i in range(2):
            row = []
            for j in range(2):
                val = float(input(f"A[{i+1}][{j+1}] = "))
                row.append(val)
            A.append(row)

        print("Enter matrix B:")
        B = []
        for i in range(2):
            row = []
            for j in range(2):
                val = float(input(f"B[{i+1}][{j+1}] = "))
                row.append(val)
            B.append(row)

        R = [[0.0, 0.0], [0.0, 0.0]]
        for i in range(2):
            for j in range(2):
                R[i][j] = A[i][j] + B[i][j]
        print("Result Matrix (A + B):")
        for i in range(2):
            print(f"{R[i][0]:8.3f} {R[i][1]:8.3f}")

    elif ch == "6":  # Matrix Subtraction
        print("2x2 Matrix Subtraction (A - B) ---")
        print("Enter matrix A:")
        A = []
        for i in range(2):
            row = []
            for j in range(2):
                val = float(input(f"A[{i+1}][{j+1}] = "))
                row.append(val)
            A.append(row)

        print("Enter matrix B:")
        B = []
        for i in range(2):
            row = []
            for j in range(2):
                val = float(input(f"B[{i+1}][{j+1}] = "))
                row.append(val)
            B.append(row)

        R = [[0.0, 0.0], [0.0, 0.0]]
        for i in range(2):
            for j in range(2):
                R[i][j] = A[i][j] - B[i][j]

        print("Result Matrix (A - B):")
        for i in range(2):
            print(f"{R[i][0]:8.3f} {R[i][1]:8.3f}")

    elif ch == "7":  # Matrix Multiplication
        print("2x2 Matrix Multiplication (A * B) ---")
        print("Enter matrix A:")
        A = []
        for i in range(2):
            row = []
            for j in range(2):
                val = float(input(f"A[{i+1}][{j+1}] = "))
                row.append(val)
            A.append(row)

        print("Enter matrix B:")
        B = []
        for i in range(2):
            row = []
            for j in range(2):
                val = float(input(f"B[{i+1}][{j+1}] = "))
                row.append(val)
            B.append(row)

        R = [[0.0, 0.0], [0.0, 0.0]]
        for i in range(2):
            for j in range(2):
                s = 0.0
                for k in range(2):
                    s += A[i][k] * B[k][j]
                R[i][j] = s

        print("Result Matrix (A * B):")
        for i in range(2):
            print(f"{R[i][0]:8.3f} {R[i][1]:8.3f}")

    elif ch == "8":
        print("Bye!")
        break

    else:
        print("Invalid choice. Enter 1-8.")