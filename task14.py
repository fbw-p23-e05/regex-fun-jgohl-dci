import re

text = "xelloccccccacccxxxc HHhhhhh_ Hazaaa avvvvvhH1_bhello."

print(re.search("(\w+)+(\d+)+_+", text))