import base64
class encipher_crypto():

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
        return base64.b64encode(bytes(text, 'utf-8'))
     def caesar_cipher(s, k):
        """Iterates through each letter and constructs the cipher text"""
        new_message = ""
        factor = k % 26
        for c in s:
            new_message += apply_rotation(c, factor)
        return new_message

       def sha1hash(s):
            temp = str.encode(s)
            temp = hashlib.sha1(temp)
            return temp.hexdigest()

        def md5hash(s):
            temp = str.encode(s)
            temp = hashlib.md5(temp)
            return temp.hexdigest()

        def sha256hash(s):
            temp = str.encode(s)
            temp = hashlib.sha256(temp)
            return temp.hexdigest()

        def sha512hash(s):
            temp = str.encode(s)
            temp = hashlib.sha512(temp)
            return temp.hexdigest()

        def apply_rotation(c, factor):
            """Applies a shift of factor to the letter denoted by c"""
            if c.isalpha():
                lower = ord("A") if c.isupper() else ord("a")
                c = chr(lower + ((ord(c) - lower + factor) % 26))
            return c


