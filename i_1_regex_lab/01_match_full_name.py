import re

text = input()

matches = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)

print(" ".join(matches))

# matches = re.search(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
# print(matches.group())