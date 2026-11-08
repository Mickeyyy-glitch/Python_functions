import re


text = input()
pattern = r'(?=([A-ZА-Ё]{1,6}))'

print(re.findall(pattern, text))
