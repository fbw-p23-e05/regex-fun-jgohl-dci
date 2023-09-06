import re

text = "ccccccacccxxxc HHhhhhh_ avvvvvhb"

print(re.search("a.*(b$)", text))