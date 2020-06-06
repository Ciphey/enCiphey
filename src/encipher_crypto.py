import random
import base64
import binascii


class encipher_crypto:

    """Holds the encryption functions
    can randomly select an encryption function  use on text
    returns:
        {"text": t, "plaintext": c, "cipher": p, "suceeds": False}

    where suceeds is whether or not the text is really encrypted or falsely decrypted

    Uses Cyclic3's module  generate psuedo random text"""

    def __init__(self):
        """DO:  be defined. """
        self.methods = [
            self.Base64,
            self.Ascii,
            self.Base16,
            self.Base32,
            self.Binary,
            self.Hex,
            self.MorseCode,
            self.Reverse,
        ]

    def randomEncrypt(self, text: str) -> str:
        """Randomly encrypts string with an encryption"""
        func__use = random.choice(self.methods)
        encryptedText = func__use(text)
        name = func__use.__name__

        return {"PlainText": text, "EncryptedText": encryptedText, "CipherUsed": name}

    def Base64(self, text: str) -> str:
        """Turns text in base64 using Python libray

            args:
                text -> text  convert

            returns:
                text -> as base 64"""
        return base64.b64encode(bytes(text, "utf-8"))

    def Caesar(self, s, k):
        """Iterates through each letter and constructs the cipher text"""
        new_message = ""
        facr = k % 26
        for c in s:
            new_message += self.apply_rotation(c, facr)
        return new_message

    def apply_rotation(self, c, facr):
        """Applies a shift of facr  the letter denoted by c"""
        if c.isalpha():
            lower = ord("A") if c.isupper() else ord("a")
            c = chr(lower + ((ord(c) - lower + facr) % 26))
        return c

    def Base32(self, text: str) -> str:
        """Turns text in base64 using Python libray

            args:
                text -> text  convert

            returns:
                text -> as base 64"""
        return base64.b32encode(bytes(text, "utf-8"))

    def Base16(self, text: str) -> str:
        """Turns text in base64 using Python libray

            args:
                text -> text  convert

            returns:
                text -> as base 64"""
        return base64.b16encode(bytes(text, "utf-8"))

    def Binary(self, text: str) -> str:
        return " ".join(format(ord(x), "b") for x in text)

    def Ascii(self, text: str) -> str:
        res = [ord(c) for c in text]
        return " ".join([str(x) for x in res])

    def Hex(self, text: str) -> str:
        return binascii.hexlify(text.encode()).decode("utf-8")

    def MorseCode(self, text: str) -> str:
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
        print(f"*********************8 {text}")
        return " ".join(MORSE_CODE_DICT.get(i.upper()) for i in text)

    def Reverse(self, text: str) -> str:
        return text[::-1]
