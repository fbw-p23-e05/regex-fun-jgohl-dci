import re

text = "ccccccabbbc"

print(re.search("ab{2,3}", text))