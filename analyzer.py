import nltk

class Analyzer():

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        #allocate espace in memory
        self.negatives = set()
        self.positives = set()

        #adding negatives words
        file_neg = open(negatives, "r")
        for line in file_neg:
            if not line.startswith('\n') and not line.startswith(';'):
                self.negatives.add(line.rstrip('\n'))
        file_neg.close()

        #adding positives words
        file_pos = open(positives, "r")
        for line in file_pos:
            if not line.startswith('\n') and not line.startswith(';'):
                self.positives.add(line.rstrip('\n'))
        file_pos.close()

    def analyze(self, text):

        # setting up score to 0
        score = 0
        #getting each word of text
        tokens = nltk.word_tokenize(text)
        for line in tokens:
            if line.lower() in self.positives:
                score += 1
            elif line.lower() in self.negatives:
                score -= 1
            else:
                score += 0

        #retunig score
        return score
