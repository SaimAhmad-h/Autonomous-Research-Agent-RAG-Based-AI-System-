class HypothesisEngine:

    def generate(self, context):
        c = context.lower()
        h = []

        if "temperature" in c:
            h.append("High temperature caused failure")

        if "vibration" in c:
            h.append("Vibration caused failure")

        if "pressure" in c:
            h.append("Pressure caused failure")

        if not h:
            h.append("Unknown cause")

        return h