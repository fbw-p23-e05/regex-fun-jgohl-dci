import re

text = "xelloccccccacccxxxc HHhhhhh_ avvvvvhbhello."

print(re.search("hello\W$", text))