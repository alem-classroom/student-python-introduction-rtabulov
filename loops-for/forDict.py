def reverse_dict(dict):
    # swap keys and values within dict and return dict
    newdict = {}
    for k, v in dict.items():
        newdict[v] = k
    return newdict
