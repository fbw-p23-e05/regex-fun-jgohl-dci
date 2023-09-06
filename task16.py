import re

text = "000f0fgfdfdgfdgfd hgfhgfhgfh"

number = re.sub("^0+", "", text)

print(number)