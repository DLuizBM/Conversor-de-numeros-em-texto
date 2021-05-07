from collections import deque
import ConvertText as conv
import Input as _in
import Format as format


def treat_data(number):
    
    million, thousand, hundred, cents = _in.treat_input(number)

    # Conversão de array de números para array com as palavras de cada número
    million_base = conv.base_convert(million)
    thousand_base = conv.base_convert(thousand)
    hundred_base = conv.base_convert(hundred)
    cents_base = conv.base_convert(cents)

    # transformando o array de palavras na frase que representa o número
    million_as_phrase = conv.base_transform_phrase(conv.base_convert(million))
    thousand_as_phrase = conv.base_transform_phrase(conv.base_convert(thousand))
    hundred_as_phrase = conv.base_transform_phrase(conv.base_convert(hundred))
    cents_as_phrase = conv.base_transform_phrase(conv.base_convert(cents))

    # inserindo palavras especiais para cada grupo de números 
    million_final_phrase = conv.million_phrase(million_base, thousand_base, hundred_base, million_as_phrase)
    thousand_final_phrase = conv.thousand_phrase(million_base, thousand_base, hundred_base, thousand_as_phrase)
    hundred_final_phrase = conv.hundred_phrase(million_base, thousand_base, hundred_base, hundred_as_phrase)
    cents_final_phrase = conv.cents_phrase(cents_base, cents_as_phrase)

    return format.format_output(million_final_phrase, thousand_final_phrase, hundred_final_phrase, cents_final_phrase)
