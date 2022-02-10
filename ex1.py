def func(list_):
    keys = {}
    for i in list_:
        if isinstance(i, bool):
            keys.update({'boolean': i})
        elif isinstance(i, float):
            keys.update({'float': i})
        elif isinstance(i, str):
            keys.update({'str': i})
        elif isinstance(i, int):
            keys.update({'int': i})
        else:
            keys.update({'None': i})
    return keys


value = [2, 4.7, "hi", False, None]

print(func(value))
