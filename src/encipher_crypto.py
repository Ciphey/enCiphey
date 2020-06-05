import base64
import binascii


class encipher_crypto:

    """Holds the encryption functions
    can randomly select an encryption function to use on text
    returns:
        {"text": t, "plaintext": c, "cipher": p, "suceeds": False}

    where suceeds is whether or not the text is really encrypted or falsely decrypted

    Uses Cyclic3's module to generate psuedo random text"""

    def __init__(self):
        """TODO: to be defined. """

    def toBase64(self, text: str) -> str:
        """Turns text into base64 using Python libray

            args:
                text -> text to convert

            returns:
                text -> as base 64"""
        return base64.b64encode(bytes(text, "utf-8"))

    def caesar_cipher(self, s, k):
        """Iterates through each letter and constructs the cipher text"""
        new_message = ""
        factor = k % 26
        for c in s:
            new_message += self.apply_rotation(c, factor)
        return new_message

    def apply_rotation(self, c, factor):
        """Applies a shift of factor to the letter denoted by c"""
        if c.isalpha():
            lower = ord("A") if c.isupper() else ord("a")
            c = chr(lower + ((ord(c) - lower + factor) % 26))
        return c

    def toBase32(self, text: str) -> str:
        """Turns text into base64 using Python libray

            args:
                text -> text to convert

            returns:
                text -> as base 64"""
        return base64.b32encode(bytes(text, "utf-8"))

    def toBase16(self, text: str) -> str:
        """Turns text into base64 using Python libray

            args:
                text -> text to convert

            returns:
                text -> as base 64"""
        return base64.b16encode(bytes(text, "utf-8"))

    def toBinary(self, text: str) -> str:
        return " ".join(format(ord(x), "b") for x in text)

    def toAscii(self, text: str) -> str:
        res = [ord(c) for c in s]
        return " ".join([str(x) for x in res])

    def toHex(self, text: str) -> str:
        return binascii.hexlify(text.encode()).decode("utf-8")

    def toMorseCode(self, text: str) -> str:
        MORSE_CODE_DICT = {
            "A": ".-",
            "B": "-...",
            "C": "-.-.",
            "D": "-..",
            "E": ".",
            "F": "..-.",
            "G": "--.",
            "H": "....",
            "I": "..",
            "J": ".---",
            "K": "-.-",
            "L": ".-..",
            "M": "--",
            "N": "-.",
            "O": "---",
            "P": ".--.",
            "Q": "--.-",
            "R": ".-.",
            "S": "...",
            "T": "-",
            "U": "..-",
            "V": "...-",
            "W": ".--",
            "X": "-..-",
            "Y": "-.--",
            "Z": "--..",
            "?": "..--..",
            ".": ".-.-.-",
            " ": "/",
            "0": "-----",
            "1": ".----",
            "2": "..---",
            "3": "...--",
            "4": "....-",
            "5": ".....",
            "6": "-....",
            "7": "--...",
            "8": "---..",
            "9": "----.",
            " ": "\n",
        }
        return " ".join(MORSE_CODE_DICT.get(i.upper()) for i in text)
