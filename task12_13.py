import re

text = "xelloccccccacccxxxc HHhhhhh_ Hazaaa avvvvvhbhello."

print(re.search("\w+(z+)\w+", text))