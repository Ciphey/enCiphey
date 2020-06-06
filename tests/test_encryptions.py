import src.encipher_crypto
import base64
import binascii

obj = src.encipher_crypto.encipher_crypto()


def test_base64():
    to_check = obj.Base64("Hello my name is bee")
    res = base64.b64decode(to_check)
    res = res.decode("utf-8")
    assert "Hello my name is bee" == res

def test_base32():
    text = "Since I've got lovely feet"
    res = base64.b32decode(obj.Base32(text))
    res = res.decode("utf-8")
    assert text == res

def test_base16():
    text = "It'd be so nice to have a friend"
    res = base64.b16decode(obj.Base16(text))

