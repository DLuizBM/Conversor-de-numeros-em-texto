from Repository import hundred, ten_all, ten_half, money
from Repository import unit, millions, thousand_text, cents_text


def base_convert(number):
    number_as_text = []
    if number[0] != "0":
        first_digit = list(filter(lambda hund: hund[0] == int(number[0]), hundred))
        if first_digit[0][0] == 1 and number[1] == "0" and number[2] == "0":
            number_as_text.append(first_digit[0][2])
        else:
            number_as_text.append(first_digit[0][1])
    else:
        number_as_text.append(" ")

    # check ten
    is_there_combined_ten = list(filter(lambda ten: ten[0] == int(number[1] + number[2]), ten_all))
    if is_there_combined_ten:
        number_as_text.append(is_there_combined_ten[0][1])
        number_as_text.append(" ")
    else:
        second_digit = list(filter(lambda ten: ten[0] == int(number[1]), ten_half))
        if second_digit:
            number_as_text.append(second_digit[0][1])
        else:
            number_as_text.append(" ")
        third_digit = list(filter(lambda ten: ten[0] == int(number[2]), unit))
        if third_digit:
            number_as_text.append(third_digit[0][1])
        else:
            number_as_text.append(" ")

    return number_as_text


def base_transform_phrase(number):
    text = ""
    if number[0] != " ":
        text += number[0]
        if number[1] != " " and number[2] != " ":
            text += " e "
        elif number[1] == " " and number[2] != " ":
            text += " e "
        elif number[1] != " " and number[2] == " ":
            text += " e "

    if number[1] != " ":
        text += number[1]
        if number[2] != " ":
            text += " e "

    if number[2] != " ":
        text += number[2]

    return text


def million_phrase(million, thousand, hundreds, text):
    test_million = list(filter(lambda t: t != ' ', million))
    test_thousand = list(filter(lambda th: th != ' ', thousand))
    test_hundred = list(filter(lambda t: t != ' ', hundreds))

    if million[0] == " " and million[1] == " " and million[2] == "um":
        text += " " + millions[0]
    elif len(test_million) > 0:
        text += " " + millions[1]
    else:
        return text

    if len(test_hundred) == 0 and len(test_thousand) == 0:
        text += " de "
    return text


def thousand_phrase(million, thousand, hundreds, text):
    if len(text):
        return text + " " + thousand_text
    return text


def hundred_phrase(million, thousand, hundreds, text):
    test_million = list(filter(lambda t: t != ' ', million))
    test_thousand = list(filter(lambda th: th != ' ', thousand))
    test_hundred = list(filter(lambda t: t != ' ', hundreds))

    if hundreds[0] == ' ' and len(test_hundred) > 0:
        if len(test_thousand):
            return "e " + text
        elif len(test_million):
            return "e " + text
    return text


def cents_phrase(cents, text):
    test_cents = list(filter(lambda c: c != ' ', cents))
    if len(test_cents) == 0:
        #text += " zero centavos"
        return text
    elif cents[1] == " " and cents[2] == "um":
        text += " " + cents_text[0]
        return text
    else:
        text += " " + cents_text[1]
        return text


"""
def convert_million_phrase(million, thousand, hundreds, text):
    test_million = list(filter(lambda t: t != ' ', million))

    if million[0] == " " and million[1] == " " and million[2] == "um":
        text += " " + millions[0]
    elif len(test_million) > 0:
        text += " " + millions[1]
    else:
        return text

    test_thousand = list(filter(lambda th: th != ' ', thousand))
    test_hundred = list(filter(lambda t: t != ' ', hundreds))
    if len(test_hundred) == 0 and len(test_thousand) == 0:
        text += " de"
    return text


def convert_thousand_phrase(thousand, hundreds, text):
    test_thousand = list(filter(lambda th: th != ' ', thousand))
    if len(test_thousand) > 0:
        return text + " " + thousand_text
    elif len(test_thousand) < 0:
        return text + "e"
    else:
        return text


def convert_hundred_phrase(million, thousand, hundreds, text):
    test_thousand = list(filter(lambda th: th != ' ', thousand))
    test_million = list(filter(lambda t: t != ' ', million))
    test_hundred = list(filter(lambda t: t != ' ', hundreds))

    if hundreds[0] == ' ' and hundreds[1] == ' ' and hundreds[2] == 'um':
        if len(test_million) == 0 and len(test_thousand) == 0:
            text += " " + money[0]
        else:
            text += " " + money[1]
    elif hundreds[0] == ' ' and hundreds[1] == ' ' and hundreds[2] == ' ':
        if len(test_million) == 0 and len(test_thousand) == 0:
            text += "zero" + " " + money[1]
        else:
            text += " " + money[1]
    elif len(text) == 0:
        text += money[1]
    else:
        text += " " + money[1]
    return text


def convert_cents_phrase(cents, text):
    test_cents = list(filter(lambda c: c != ' ', cents))
    if len(test_cents) == 0:
        #text += " zero centavos"
        return text
    elif cents[1] == " " and cents[2] == "um":
        text += " " + cents_text[0]
        return text
    else:
        text += " " + cents_text[1]
        return text
"""""