class StringUtils:
    @staticmethod
    def is_empty(s: str) -> bool:
        """Проверяет, является ли строка пустой ('' или None)"""
        return s is None or s == ''

    @staticmethod
    def is_not_empty(s: str) -> bool:
        """Проверяет, что строка не пустая"""
        return not StringUtils.is_empty(s)

    @staticmethod
    def is_blank(s: str) -> bool:
        """Проверяет, является ли строка пустой или состоящей только из пробелов"""
        return s is None or s.strip() == ''

    @staticmethod
    def count_words(s: str) -> int:
        """Считает количество слов в строке (разделитель — пробел)"""
        if s is None:
            return 0
        return len(s.strip().split())

    @staticmethod
    def capitalize_first(s: str) -> str:
        """Возвращает строку с первой буквой в верхнем регистре"""
        if not s or not s[0].isalpha():
            return s
        return s[0].upper() + s[1:]