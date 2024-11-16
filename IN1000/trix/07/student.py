class Student:
    def __init__(self, name, score, quizes):
        self._name = name
        self._score = score
        self._quizes = quizes
    def add_points(self, points):
        self._score += points
        self._quizes += 1
    def average_score(self):
        return self._score / self._quizes
    def info(self):
        print(f"""
        Name: {self._name}
        Score: {self._score}
        Quizes: {self._quizes}
        Average: {self.average_score()}
        """)
