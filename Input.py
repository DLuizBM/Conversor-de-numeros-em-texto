from collections import deque
import sys


def treat_input(number_input):
    separate = number_input.split(',')
    before_comma = deque(separate[0])
    after_comma = deque(separate[1])
    after_comma.appendleft("0")

    try:
        if 0 < len(before_comma) < 11:
            i = 1
        else:
            i = 'a'
        test = int(i)
    except ValueError as err:
        print('O tamanho do número anterior a vírgula está incorreto. O programa será interrompido.')
        sys.exit(1)

    try:
        if len(after_comma) == 4:
            i = 1
        else:
            i = 'a'
        test = int(i)
    except ValueError as err:
        print('O tamanho do número após a vírgula está incorreto. O programa será interrompido.')
        sys.exit(1)

    for _ in range(len(before_comma), 9):
        before_comma.appendleft("0")

    million = [before_comma[i] for i in range(0, 3)]
    thousand = [before_comma[i] for i in range(3, 6)]
    hundred = [before_comma[i] for i in range(6, 9)]
    cents = [after_comma[i] for i in range(0, 3)]
    return million, thousand, hundred, cents
