import random
import encipher_crypto
import nltk


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
        f = open("dickens.txt")
        print("Opened dickens")
        x = f.read()
        x = x[0:100]
        print("Split file")
        print(x)
        return nltk.tokenize.sent_tokenize(x)

    def getRandomSentence(self):
        sents = []
        # num_of_sentences = random.randint(1, self.MAX_SENTENCE_LENGTH)
        num_of_sentences = 1
        i = 0
        while i <= num_of_sentences:
            sents.append(random.choice(self.text))
            print(f"Sents is now {sents}")
            i += 1
        return ". ".join(sents)

    def getRandomEncryptedSentence(self):
        print("Getting random sentence")
        sents = self.getRandomSentence()

        sentsEncrypted = self.crypto.randomEncrypt(sents)
        return {"PlainText Sentences": sents, "Encrypted Texts": sentsEncrypted}


obj = encipher()
print(obj.getRandomEncryptedSentence())
