import re

text = "000f0fgfdfdgfdgfd hgfhgfhgfh"

number = re.sub("^0+", "", text)

print(number)



# actual solution -> remove leading zeros
ip_address = "024.505.010.80"

new_ip = re.sub('0*(\d*)', r'\1', ip_address)

print(new_ip)