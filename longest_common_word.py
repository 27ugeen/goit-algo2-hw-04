from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Помилка: вхідні дані повинні бути списком рядків")

        if not strings:
            return ""

        if len(strings) == 1:
            return strings[0]

        # Додаємо всі слова у Trie
        for word in strings:
            self.put(word, None)

        # Шукаємо найдовший спільний префікс
        return self._find_longest_prefix()

    def _find_longest_prefix(self) -> str:
        
        current = self.root
        common_prefix = []

        while len(current.children) == 1 and current.value is None:  
            char = next(iter(current.children))  # Беремо єдиного нащадка
            common_prefix.append(char)
            current = current.children[char]  

        return "".join(common_prefix)
    

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["single"]
    assert trie.find_longest_common_word(strings) == "single"

    print("✅ Усі тести пройдено успішно!")