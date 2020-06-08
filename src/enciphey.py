import random
import encipher_crypto
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer


class encipher:

    """Generates encrypted text. Used for the NN and test_generator"""

    def __init__(self):
        """Inits the encipher object """
        self.text = self.read_text()
        print(f"Self.text is {self.text}")
        self.MAX_SENTENCE_LENGTH = 1
        # ntlk.download("punkt")
        self.crypto = encipher_crypto.encipher_crypto()

    def read_text(self):
        f = open("hansard.txt", encoding="ISO-8859-1")
        print("Opened dickens")
        x = f.read()[0:200]
        print("Split file")
        splits = nltk.tokenize.sent_tokenize(x)
        print(f"Splits is {splits}")
        return splits

    def getRandomSentence(self):
        return TreebankWordDetokenizer().detokenize(
            random.sample(self.text, random.randint(1, self.MAX_SENTENCE_LENGTH))
        )

    def getRandomEncryptedSentence(self):
        print("Getting random sentence")
        sents = self.getRandomSentence()

        sentsEncrypted = self.crypto.randomEncrypt(sents)
        return {"PlainText Sentences": sents, "Encrypted Texts": sentsEncrypted}


obj = encipher()
print(obj.getRandomEncryptedSentence())
