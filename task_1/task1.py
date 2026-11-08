text = input()


def is_valid(txt: str, i=0, exp=[]) -> bool:
    if i == len(txt):
        return not exp

    data = {'(': ')', '[': ']', '{': '}'}
    ch = txt[i]

    if ch in data:
        return is_valid(txt, i + 1, exp + [data[ch]])

    elif ch in data.values():
        if not exp or ch != exp[-1]:
            return False
        return is_valid(txt, i + 1, exp[:-1])

    else:
        return is_valid(txt, i + 1, exp)


print(is_valid(text))