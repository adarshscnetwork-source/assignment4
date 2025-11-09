try:
    print("Reading file content:")
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
