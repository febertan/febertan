def char_ki(in_str: str) -> str:
    a = ''

    for elem in in_str:
        if elem != '.':
            a += elem


    return in_str


print(char_ki("alma. korte. citrom."))

# for elem in szavak:
#     if elem != '.':