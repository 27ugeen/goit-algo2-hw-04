from trie import Trie

class Homework(Trie):
    
    def count_words_with_suffix(self, pattern) -> int:
        
        if not isinstance(pattern, str):
            raise ValueError("Помилка: pattern має бути рядком")

        count = 0
        for word in self.keys():  # Отримуємо всі слова у Trie
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix) -> bool:
        
        if not isinstance(prefix, str):
            raise ValueError("Помилка: prefix має бути рядком")

        return len(self.keys_with_prefix(prefix)) > 0  # Використовуємо keys_with_prefix() з Trie

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    
    for i, word in enumerate(words):
        trie.put(word, i)

    # Тест: підрахунок суфіксів
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat
    assert trie.count_words_with_suffix("xyz") == 0  # немає такого суфікса

    # Тест: перевірка префіксів
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False  # немає такого префікса
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat
    assert trie.has_prefix("dog") == False  # немає такого слова

    print("✅ Усі тести пройдено успішно!")