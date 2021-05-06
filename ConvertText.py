from Repository import hundred, ten_all, ten_half
from Repository import unit, millions, thousand


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


def base_transform_phrase(million):
    text = ""
    if million[0] != " ":
        text += million[0]
        if million[1] != " " and million[2] != " ":
            text += " e "
        elif million[1] == " " and million[2] != " ":
            text += " e "
        elif million[1] != " " and million[2] == " ":
            text += " e "

    if million[1] != " ":
        text += million[1]
        if million[2] != " ":
            text += " e "

    if million[2] != " ":
        text += million[2]

    return text


def convert_million_phrase(million, text):
    if million[0] == " " and million[1] == " " and million[2] == "um":
        text += " " + millions[0]
    else:
        text += " " + millions[1]
    return text


def convert_thousand_phrase(text):
    return text + " " + thousand

