def reverse_string(s):
    rev = ""
    for i in range(-1, -len(s) - 1, -1):
        rev += s[i]
    return rev

# Test
print(reverse_string("cool"))  # Outputs: "looc"
