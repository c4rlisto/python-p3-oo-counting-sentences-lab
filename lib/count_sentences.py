class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if not isinstance(val, str):
            print("The value must be a string.")
            return
        self._value = val

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0

        cleaned = (
            self.value.replace("!", ".")
                      .replace("?", ".")
        )

        parts = cleaned.split(".")

        sentences = [p for p in parts if p.strip()]

        return len(sentences)
