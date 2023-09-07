import re

text = "ccccccabbbc HHhhhhh_gg"

print(re.search("[a-z]+_[a-z]*", text))     #lower, underline and maybe more lower