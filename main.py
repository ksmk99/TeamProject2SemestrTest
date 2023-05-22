"""Modules for create interface, translate text and create sentences"""
from transformers import pipeline, set_seed
from deep_translator import GoogleTranslator
import streamlit as st


def translate_text_to_en(text):
    """Function translate text to English"""
    return GoogleTranslator(source='auto', target='en').translate(text)


def translate_text_to_ru(text):
    """Function translate text to Russian"""
    return GoogleTranslator(source='en', target='ru').translate(text)


def generate_en_text(text, length):
    """Function generate English text"""
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    txt = generator(text, max_length=length,
                    num_return_sequences=1)[0]['generated_text']

    return txt


def generate_ru_text(text, length):
    """Function generate Russian text"""
    en_text = translate_text_to_en(text)
    generated_en_text = generate_en_text(en_text, length)
    generated_ru_text = translate_text_to_ru(generated_en_text)

    return generated_ru_text


if __name__ == '__main__':
    title = st.text_input('Введите свой текст:', 'Life of Brian')
    count = st.slider('Выберите максимальное '
                      'количество слов в предложении', 20, 400, 20)
    if st.button('Начать'):
        result = generate_ru_text(title, count)
        st.write(result)
