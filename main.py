import re


#Find all bonus codes, a bonus code has to contain 3 letters followed by 3 numbers

bonus_codes = "ABC123, bonus455, bonus22"
pattern = r"\b[A-Za-z]{3}\d{3}\b"
code_patterns = re.findall(pattern, bonus_codes)
print(code_patterns)


#Verify we have the correct username
# a username has to contain a word up to 5 letters followed by minimum 2 numbers
user_name = None
if user_name is None:
    user_name = input("What's your username?: \n")
    username_pattern = r"[A-Za-z]{1,5}\d{2,}"
    username_pattern_check = re.match(username_pattern, user_name)
    if not username_pattern_check:
        print(f"The username '{user_name}' is invalid (has to contain a word up to 5 letters followed by 2 numbers)")
    else:
        print(f"The username '{user_name}' satisfies requirements")
