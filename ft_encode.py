import math
import re
import struct

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

alphabet = {
    'a': 0.10926049796876,
    'b': 0.16389074695314,
    'c': 0.2731512449219,
    'd': 0.38241174289065,
    'e': 0.06009327388282,
    'f': 0.07101932367969,
    'g': 0.09287142327344,
    'h': 0.10379747307032,
    'i': 0.12564957266407,
    'j': 0.1584277220547,
    'k': 0.16935377185158,
    'l': 0.2021319212422,
    'm': 0.22398402083595,
    'n': 0.23491007063283,
    'o': 0.25676217022658,
    'p': 0.28954031961721,
    'q': 0.32231846900784,
    'r': 0.33324451880471,
    's': 0.36602266819534,
    't': 0.38787476778909,
    'u': 0.39880081758597,
    'v': 0.43157896697659,
    'w': 0.45343106657035,
    'x': 0.48620921596097,
    'y': 0.52991341514848,
    'z': 0.05517655147422,
    ' ': 0.102,
    '\'': 0.103,
    '-': 0.104,
    '0': 0.0573617614336,
    '1': 0.05790806392344,
    '2': 0.05845436641329,
    '3': 0.05900066890313,
    '4': 0.05954697139297,
    '5': 0.06009327388282,
    '6': 0.06063957637266,
    '7': 0.0611858788625,
    '8': 0.06173218135235,
    '9': 0.06227848384219,
}


class FTEncode:

    def __init__(self, your_model):
        if your_model is None:
            self.model = default_model
        else:
            self.model = your_model

    def get_encode_number(self, word):
        original_word = word
        word = self.extract_name_from_text(word)
        word = word.strip().lower()
        sum = 0.0
        bin_ = 0.5
        bin_pow = 1
        c0 = '`'

        for c in word:
            c0 = c
            power = math.pow(bin_, bin_pow)
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

        return round(sum, 14)

    def get_ft_value_plus(self, word):
        word = word.strip().lower()
        word = word.replace(" ", "")
        sum = 0.0
        for i in range(len(word)):
            c = word[i]
            sum += alphabet[c]

        return round(sum, 14)

    def binary_to_double(self, binary):
        bits = int(binary, 2)
        return struct.unpack('!d', struct.pack('!Q', bits))[0]

    def double_to_binary_64bit(self, number):
        bits = struct.unpack('!Q', struct.pack('!d', number))[0]
        binary_builder = bin(bits)[2:].zfill(64)

        # Add the necessary separators for readability
        for i in range(11, 64, 12):
            binary_builder = binary_builder[:i] + " " + binary_builder[i:]

        return binary_builder

    def double_to_binary_32bit(self, number):
        bits = struct.unpack('!I', struct.pack('!f', number))[0]
        binary_builder = bin(bits)[2:].zfill(32)

        # Add the necessary separators for readability
        for i in range(8, 32, 9):
            binary_builder = binary_builder[:i] + " " + binary_builder[i:]

        return binary_builder

    def extract_name_from_text(self, text):
        if text:
            text = re.sub(r'[^A-Za-z0-9]', '', text).lower()

        return text
