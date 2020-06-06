from src import encipher_crypto
import base64
import binascii

obj = encipher_crypto.encipher_crypto()


def test_base64():
    to_check = obj.Base64("Hello my name is bee")
    res = base64.b64decode(to_check)
    assert to_check == res
