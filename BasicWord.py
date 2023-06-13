class BasicWord:
    def __init__(self, word: str, sub_words: list):
        """
        Конструктор
        """
        self.word = word
        self.sub_words_list = sub_words

    def check_sub_word(self, sub_word: str) -> bool:
        """
        Проверка введенного слова в списке допустимых подслов
        """
        return sub_word in self.sub_words_list

    def get_sub_words_count(self) -> int:
        """
        Подсчет количества подслов
        """
        return len(self.sub_words_list)

    def __repr__(self) -> str:
        return f"Исходное слово: {self.word}\nПодслова: {', '.join(self.sub_words_list)}"
