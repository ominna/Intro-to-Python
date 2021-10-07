"""
is_case_insensitive_equal(s, t) - проверяет что строки одинаковы, даже если отличаются регистром букв.
Например, "AAbbAA" одинаковая со строкой "aaBBaA". Эти строки состоят из тех же букв на тех же позициях
просто в разных регистрах.

"""



def is_case_insensitive_equal(s, t):
    if s.lower() == t.lower():
        return "The two strings are equal (case insensitive)"
    return "The two strings are NOT equal"
