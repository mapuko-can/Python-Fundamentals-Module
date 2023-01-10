import re
valid = []
text = input()
while text:
    pattern = r"(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
    matches = re.search(pattern, text)
    if matches:
        valid.append(matches.group(0))
    text = input()
print("\n".join(valid))
