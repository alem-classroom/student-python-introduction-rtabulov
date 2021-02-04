def reverse_dict(dict):
    newdict = {}
    for k, v in dict.items():
        newdict[v] = k
    return newdict
