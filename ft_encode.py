import math

default_model = {
    'a': 0.200,
    'b': 0.300,
    'c': 0.50,
    'd': 0.700,
    'e': 0.110,
    'f': 0.130,
    'g': 0.170,
    'h': 0.190,
    'i': 0.230,
    'j': 0.290,
    'k': 0.310,
    'l': 0.370,
    'm': 0.410,
    'n': 0.430,
    'o': 0.470,
    'p': 0.530,
    'q': 0.590,
    'r': 0.610,
    's': 0.670,
    't': 0.710,
    'u': 0.730,
    'v': 0.790,
    'w': 0.830,
    'x': 0.890,
    'y': 0.970,
    'z': 0.101,
    ' ': 0.102,
    '\'': 0.103,
    '-': 0.104,
    '0': 0.105,
    '1': 0.106,
    '2': 0.107,
    '3': 0.108,
    '4': 0.109,
    '5': 0.110,
    '6': 0.111,
    '7': 0.112,
    '8': 0.113,
    '9': 0.114,
    '%': 0.115,
    '$': 0.116,
    '.': 0.117,
    '_': 0.118,
    '[': 0.119,
    ']': 0.121,
    ',': 0.122,
    ':': 0.123,
    '’': 0.124,
    '/': 0.125,
}


class FTEncode:

    def __init__(self, your_model):
        if your_model is None:
            self.model = default_model
        else:
            self.model = your_model

    def get_encode_number(self, word):
        original_word = word
        word = word.strip().lower()
        sum = 0.0
        bin = 0.5
        bin_pow = 1
        c0 = '`'

        for c in word:
            c0 = c
            power = math.pow(bin, bin_pow)
            if bin_pow == 1:
                power = math.tan(power)
            elif bin_pow == len(word):
                power = math.cos(power)

            val = 0.0
            try:
                if c in self.model:
                    val = self.model[c]
                else:
                    val = 0.010101
            except:
                val = 0.010101

            sum = sum + (val * power)

            bin_pow = bin_pow + 1
        return sum
