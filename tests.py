"""Main module of the program"""
from main import translate_text_to_en, translate_text_to_ru, \
    generate_en_text, generate_ru_text


def test_generate_ru_text():
    """Test checks generation of Russian text"""
    assert generate_ru_text('Привет', 20) == \
           'Здравствуйте, господин президент, ' \
           'если бы вас немного беспокоило, сколько из них'


def test_generate_en_text():
    """Test checks generation of English text"""
    assert generate_en_text('How are you', 22) == \
           "How are you on vacation? " \
           "I'm coming back to the country...to visit my " \
           "family...I'm working"


def test_generate_en_text_len():
    """Test checks length of generation of English text"""
    assert len(generate_en_text('I am go to work', 37).split(' ')) <= 37


def test_translate_text_to_ru():
    """Test checks translation to Russian text"""
    assert translate_text_to_ru('In case someone is still facing this '
                                'issue and none of their code can lead to '
                                'infinite loop, try deleting '
                                'pycache directories that could help.') == \
           'Если кто-то ' \
           'все еще ' \
           'сталкивается ' \
           'с этой ' \
           'проблемой, ' \
           'и ни один из ' \
           'их кодов не ' \
           'может ' \
           'привести к ' \
           'бесконечному ' \
           'циклу, ' \
           'попробуйте ' \
           'удалить ' \
           'каталоги ' \
           'pycache, ' \
           'которые могут ' \
           'помочь.'


def test_translate_text_to_en():
    """Test checks translation to English text"""
    assert translate_text_to_en('Значительная часть этого '
                                'сообщения красного цвета, '
                                'что делает его действительно '
                                'выделяющимся (если у вас '
                                'есть цветной терминал).') == \
           'A lot of this message is in ' \
           'red, which makes it really ' \
           'stand out (if you have a ' \
           'color terminal).'


def test_china_text():
    """Test checks generation of China text"""
    assert generate_ru_text('嗨。', 20) == 'Привет. Я надеюсь, ' \
                                         'у вас это хорошо получается, ' \
                                         'и если да, то мы ' \
                                         'приготовим еще одно.'
