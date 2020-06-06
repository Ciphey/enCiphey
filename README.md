# enCipher
Literally does the opposite of Ciphey. Encrypts text with a random (crackable) encryption, hash or encoding.

Currently used to build datasets of encrypted text, but can be used in CTFs which require random components. 

# How to use
```python3
>>> import encipher_crypto
>>> obj = encipher_crypto.encipher_crypto
>>> print(obj.randomEncrypt("Text you want to encrypt here")
```

# Currently supported encryption methods
* Base64
* Caesar
* Base32
* Base16
* Binary
* Ascii
* Morse Code
* Reverse (reverse the text)

## How to delete ciphers you don't like

To get rid of a cipher you don't like, delete it from the list and it won't be used.

The list is found in `encipher_crypto.py`
```python
self.methods = [
    self.Base64,
    self.Ascii,
    self.Base16,
    self.Base32,
    self.Binary,
    self.Hex,
    self.MorseCode,
    self.Reverse,
]```
