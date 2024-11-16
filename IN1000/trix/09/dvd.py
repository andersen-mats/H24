class Dvd:

    def __init__(self, tittel, produsent, utgavenummer):
        self._temp = [tittel,produsent,utgavenummer]
        for foo in self._temp:
            assert isinstance(foo, str)
            self._foo = foo
    def __str__(self):
        return self._tittel
    def __eq__(self, other):
        if isinstance(other, Dvd):
            for foo in self._temp:
                if not self._foo == other._foo:
                    return False
            return True


dvd1 = Dvd("asd", "qwe", "123")
dvd2 = Dvd("asd", "qwe", "1243")

print(dvd1 == dvd2)
