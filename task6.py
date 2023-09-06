import re

text = "ccccccabbbc"

print(re.search("a(b{2,3})", text))