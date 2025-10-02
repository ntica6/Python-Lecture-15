import re

with open("errors.log", "r") as file:
    lines = file.readlines()

pattern = r"Error \d{3}"

for line in lines:
    match = re.search(pattern, line)
    if match:
        print(line)