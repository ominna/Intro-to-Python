
def has_substring(s, t):
    if s == t:
        return "String t is a substring of string s"
    else:
        for i in range(len(s) - len(t)+1):
            if s[i:i+len(t)] == t:
                return "is a substring"
    return "is NOT a substring"
