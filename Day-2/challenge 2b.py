def is_safe_report(row):
    # Check if the report is strictly increasing or strictly decreasing
    is_increasing = all(row[i] < row[i + 1] for i in range(len(row) - 1))
    is_decreasing = all(row[i] > row[i + 1] for i in range(len(row) - 1))

    # Check if the difference between adjacent levels is between 1 and 3
    if not (is_increasing or is_decreasing):
        return False

    for i in range(len(row) - 1):
        if not (1 <= abs(row[i] - row[i + 1]) <= 3):
            return False
    return True


def check_reports(data):
    safe_count = 0

    for row in data:
        # Check if the row is safe in its original form
        if is_safe_report(row):
            safe_count += 1
        else:
            # Check if removing one element makes it safe
            for i in range(len(row)):
                modified_row = row[:i] + row[i + 1 :]
                if is_safe_report(modified_row):
                    safe_count += 1
                    break
    return safe_count


# Read the input data
file_path = "Day-2/challenge2.txt"  # Adjust path as needed
with open(file_path, "r") as file:
    data = [list(map(int, line.split())) for line in file.readlines()]

# Get the number of safe reports considering the Problem Dampener
safe_count = check_reports(data)
print(safe_count)
