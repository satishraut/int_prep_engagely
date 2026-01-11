def string_frq(string):
    empt = {}
    for i in string:
        if i in empt:
            empt[i] += 1
        else:
            empt[i] = 1
    return empt

print(string_frq(["hi","hello","make","hello"]))