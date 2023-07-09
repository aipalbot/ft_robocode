import sys

from ft_encode import FTEncode
print(sys.maxsize)
a = FTEncode(None)
l_m = a.get_encode_number('hello')
k = int(6704429995583343) + l_m
print(l_m)
print(k)
ft_plus = a.get_ft_value_plus('hello')