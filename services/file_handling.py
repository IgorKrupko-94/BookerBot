import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end_symbol = ['.', ',', '!', ':', ';', '?']
    end = start + size
    while text[end:][:1] in end_symbol:
        end -= 1
    text = text[start:end]
    text = text[:max(map(text.rfind, end_symbol)) + 1]
    return text, len(text)


def prepare_book(path: str) -> None:
    total = 0
    page = 1
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        while total < len(content):
            text_for_page = _get_part_text(content, total, PAGE_SIZE)
            book[page] = text_for_page[0].lstrip()
            page += 1
            total += text_for_page[1]


prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
