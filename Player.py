class Player:
    def __init__(self, name: str):
        """
        Конструктор
        """
        self.name = name
        self.word_list: list = []

    def get_used_words_count(self):
        """
        Получение количества использованных слов
        """
        return len(self.word_list)

    def add_used_word(self, word: str) -> None:
        """
        Добавление слова в использованные слова
        """
        self.word_list.append(word)

    def check_used_word(self, word: str) -> bool:
        """
        Проверка использования данного слова до этого
        """
        return word in self.word_list

    def __repr__(self) -> str:
        return f"Имя пользователя: {self.name}\nИспользованные слова пользователя: {', '.join(self.word_list)}"
