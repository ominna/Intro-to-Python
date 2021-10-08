# take input from the user
string_1 = str(input("Enter the first string: "))
string_2 = str(input("Enter the second string: "))

# check if string_2 is a substring of string_1
def has_substring(s, t):
    if s == t:
        return "String t is a substring of string s"
    else:
        for i in range(len(s) - len(t)+1):
            if s[i:i+len(t)] == t:
                return "is a substring"
    return "is NOT a substring"
print("\"%s\""%string_2, has_substring(string_1, string_2), "of", "\"%s\""%string_1)

# check if the strings are numbers
def is_number(s):
    if s.isdigit():
        return "is a number"
    return "is NOT a number"

print("\"%s\""%string_1, is_number(string_1))
print("\"%s\""%string_2, is_number(string_2))

# check if the two strings are case insensitive equal
def is_case_insensitive_equal(s, t):
    if s.lower() == t.lower():
        return "The two strings are equal (case insensitive)"
    return "The two strings are NOT equal (case insensitive)"

print(is_case_insensitive_equal(string_1, string_2))
