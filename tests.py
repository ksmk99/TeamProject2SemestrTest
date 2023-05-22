from main import generate_ru_text, generate_en_text, translate_text_to_ru, translate_text_to_en


def test_generate_ru_text():
    assert generate_ru_text('Привет',
                            20) == 'Здравствуйте, господин президент, если бы вас немного беспокоило, сколько из них'


def test_generate_en_text():
    assert generate_en_text('How are you',
                            22) == "How are you on vacation? I'm coming back to the country...to visit my " \
                                   "family...I'm working "


def test_generate_en_text_len():
    assert len(generate_en_text('I am go to work', 37).split(' ')) <= 37


def test_translate_text_to_ru():
    assert translate_text_to_ru('In case someone is still facing this issue and none of their code can lead to '
                                'infinite loop, try deleting pycache directories that could help.') == 'Если кто-то ' \
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
                                                                                                       'помочь. '


def test_translate_text_to_en():
    assert translate_text_to_en('Значительная часть этого сообщения красного цвета, что делает его действительно '
                                'выделяющимся (если у вас есть цветной терминал).') == 'A lot of this message is in ' \
                                                                                       'red, which makes it really ' \
                                                                                       'stand out (if you have a ' \
                                                                                       'color terminal). '


def test_china_text():
    assert generate_ru_text('嗨。', 20) == 'Привет. Я надеюсь, у вас это хорошо получается, и если да, то мы приготовим ' \
                                         'еще одно. '
