import re

text = "ccccccabbbc"

print(re.search("a(b{3})", text))