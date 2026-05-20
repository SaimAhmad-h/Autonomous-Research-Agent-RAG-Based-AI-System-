class Verifier:

    def verify(self, hypothesis, context):
        h = hypothesis.lower()
        c = context.lower()

        return any(word in c for word in h.split())