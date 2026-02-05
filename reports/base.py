class BaseReport:
    name = None

    def generate(self, rows):
        raise NotImplementedError
