



def flatten_dict(d, parent_key=''):
    flat_dict ={}
    for key, value in d.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, new_key))
        else:
            flat_dict[new_key] = value
    return flat_dict



def main():

    var = {
        "key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }
    print(flatten_dict(var))

if __name__ == '__main__':
    main()