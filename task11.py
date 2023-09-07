import re

text = "xelloccccccacccxxxc HHhhhhh_ avvvvvhbhello!."

print(re.search("\w+(\W*)$", text))