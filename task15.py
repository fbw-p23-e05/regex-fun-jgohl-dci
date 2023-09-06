import re

text = "fgfdfdgfdgfd hgfhgfhgfh"
number = " 0190"

number = re.sub("^.", number, text)

print(number)