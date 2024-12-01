# Open and read the file
file_path = "New Text Document.txt"  # Replace with the actual path if needed
with open(file_path, "r") as file:
    data = file.readlines()

# Split into two lists
list1, list2 = [], []
for line in data:
    if line.strip():  # Ensure the line is not empty
        col1, col2 = map(int, line.split())  # Convert both columns to integers
        list1.append(col1)
        list2.append(col2)

list1.sort()
list2.sort()

sum = 0
for x, y in zip(list1, list2):
    sum += abs(x - y)


print(sum)
