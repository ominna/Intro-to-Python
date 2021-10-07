import has_substring
import is_number
import is_case_insensitive_equal

# take input from the user
string_1 = str(input("Enter the first string: "))
string_2 = str(input("Enter the second string: "))

# check if string_2 is a substring of string_1
print(string_2, has_substring.has_substring(string_1, string_2), "of", string_1)

# check if the strings are numbers
print(string_1, is_number.is_number(string_1))
print(string_2, is_number.is_number(string_2))

# check if the two strings are case insensitive equal
print(is_case_insensitive_equal.is_case_insensitive_equal(string_1, string_2))

# check if the two strings are case insensitive equal
is_case_insensitive_equal.is_case_insensitive_equal(string_1, string_2)



