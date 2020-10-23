from collections.abc import Iterable as Iter
from enum import Enum
from builtins import NotImplementedError
from random import SystemRandom


class Generator:
    def __init__(self, charsets):
        self.charsets = []
        for charset in charsets:
            if isinstance(charset, CharSet):
               self.charsets.append(charset)
            else:
                self.charsets.append(CharSet(charset)) 

    def get_chars(self):
        chars = set()
        return tuple(chars.union(*self.charsets))

    def get_password(self, length=16):
        if not self.charsets:
            return ''
        if not length:
            length = 0
        password = []
        chars = self.get_chars()
        for i in range(length):
            random = self.get_random(0, len(chars))
            password.append(chars[random])
        return ''.join(password)

    @staticmethod
    def get_random(min, max):
        """ min and max are exclusive """
        try:
            rnd = SystemRandom()
        except NotImplementedError as err:
            print("random.SystemRandom not implemented by os.")
        random_number = int((rnd.random()) * (max-min)) + min
        return random_number

    def __str__(self):
        return str(self.get_chars())


class CharSet(Enum):

    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASE = LOWERCASE.upper()
    SYMBOLS = '@!"§$%&/()=?`*+~"'''
    NUMBERS = '0123456789'
    AMBIGUOUS = '{}[]()/\'"`~,;:.<>'
    ALL = ''.join((LOWERCASE, LOWERCASE, SYMBOLS))

    def __init__(self, chars, typ_='whitelist'):
        self.chars = chars
        self.typ_ = typ_

    def get_chars(self):
        return self.chars

    @classmethod
    def by_name(cls, name, *names, length=16):
        names = [name] + list(names)
        for name in names:
            if hasattr(cls, name.upper()):
                yield(cls(getattr(cls, name.upper())))

    def __iter__(self):
        return iter(self.chars)

    def __str__(self):
        return '{}'.format(''.join(self.chars))


if __name__ == '__main__':
    generator = Generator((CharSet.ALL, CharSet.UPPER))
    print(generator.get_password())
