import re

text = "xelloccccccacccxxxc zHHhzhhhh_ Hazzaaaz avvvvvhbhello."

print(re.search("\w*z\w*", text))
print(re.search("[a-yA-Y]+z+[a-yA-Y]+", text))