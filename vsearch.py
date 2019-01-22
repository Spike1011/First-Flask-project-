def search4vowels(word: str) -> set:
    """Выводит гласные, нйаденные в указанном слове"""
    vowels = set('aeuio')
    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str='aeoui')-> set:
    """Возращает множество букв из Letters, найденных
    в указанной фразе"""
    return set(letters).intersection(set(phrase))
