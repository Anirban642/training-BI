# Flatten Nested Dictionary

dict1 = {
    "a": 10,
    "b": {
        "c": {
            "d": 20
        }
    },
    "e": 100
}


def flatten_dict(d):
    result = {}
    for key, value in d.items():
        if isinstance(value, dict):
            n = flatten_dict(value)
            for n_key, n_value in n.items():
                result[f"{key}.{n_key}"] = n_value
        else:
            result[key] = value
    return result

output = flatten_dict(dict1)
print(output)