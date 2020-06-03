class encipher:

    """Generates encrypted text. Used for the NN and test_generator"""

    def __init__(self):
        """Inits the encipher object """
        self.text = self.read_text()
    def read_text(self):
        f = open("text.txt")
        return f.readlines().split(".")
    def 
