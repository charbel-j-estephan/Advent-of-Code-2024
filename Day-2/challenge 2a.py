file_path = "Day-2/challenge2.txt"  # Replace with the actual path if needed

# Read the file
with open(file_path, "r") as file:
    data = file.readlines()

safe_count = 0  # Counter for safe rows
rows = {}

# Parse rows into a dictionary
for index, line in enumerate(data):
    rows[f"row{index + 1}"] = list(map(int, line.split()))
# Process each row
for name, row in rows.items():
    is_increasing = row == sorted(row)
    is_decreasing = row == sorted(row, reverse=True)

    if not (is_decreasing or is_increasing):
        continue

    valid_row = True
    for i in range(len(row) - 1):
        if not (1 <= abs(row[i] - row[i + 1]) <= 3):
            valid_row = False
            break
    if valid_row:
        safe_count += 1

print(safe_count)
