import re


def find_abb(txt: str) -> list:
    abbreviations = re.findall(r"\b[A-ZА-ЯЁ]{1,6}\b", text)
    return abbreviations


text = input()

print(find_abb(text))