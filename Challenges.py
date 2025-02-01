



def flatten_dict(d, parent_key=''):
    flat_dict ={}
    for key, value in d.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value, new_key))
        else:
            flat_dict[new_key] = value
    return flat_dict

# Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
# For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
# Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.

def isOneToOne(s1, s2):
    if len(s1) != len(s2):
        return False
    dict1 = set(s1)
    dict2 = set(s2)
    return len(dict1) == len(dict2)


def main():

    # var = {
    #     "key": 3,
    #     "foo": {
    #         "a": 5,
    #         "bar": {
    #             "baz": 8
    #         }
    #     }
    # }
    # print(flatten_dict(var))
    print(isOneToOne("foo", "bar"))  # False
    print(isOneToOne("egg", "add"))  # True
    print(isOneToOne("abc", "bcd"))  # True
    print(isOneToOne("ab", "aa"))  # False
    print(isOneToOne("paper", "title"))  # True

if __name__ == '__main__':
    main()