def upper_case(string):
    return string.upper()

def capitalize_words(string):
    """Делает заглавными первые буквы каждого слова в строке"""
    words = string.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)
