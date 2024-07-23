import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python mutiplyer.py <num1> <num2>")
    return

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    result = num1 + num2
    print(result)

except ValueError:
    print("Please provide wo valid numbers.")

if __name__ == "__main__":
    main()