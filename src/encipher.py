import random
import encipher_crypto


class encipher:

    """Generates encrypted text. Used for the NN and test_generator"""

    def __init__(self):
        """Inits the encipher object """
        self.text = self.read_text()
        self.MAX_SENTENCE_LENGTH = 20

    def read_text(self):
        f = open("text.txt")
        return f.readlines().split(".")

    def getRandomSentence(self):
        sents = []
        num_of_sentences = random.randint(1, self.MAX_SENTENCE_LENGTH)
        i = 0
        while i <= num_of_sentences:
            sents.append(random.choice(self.text))
        return ". ".join(sents)

    def getRandomEncryptedSentence(self):
        sents = self.getRandomSentence()
        sentsEncrypted = encipher_crypto.randomEncrypt(sents)
        return {"PlainText Sentences": sents, "Encrypted Texts": sentsEncrypted}
