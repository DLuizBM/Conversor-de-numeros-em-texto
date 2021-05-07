import TreatData as td


def open_write_file(open_path, write_path):
    try:
        with open(open_path, 'r') as f:
            number = f.readline()
            while number:
                write_file(number, write_path)
                number = f.readline()
    except FileNotFoundError as erra:
        print(f'Ops! O arquivo para leitura não foi encontrado: {erra}')


def write_file(number, write_path):
    with open(write_path, 'a') as f:
        phrase = td.treat_data(number)
        num = list(number)
        num.pop()
        phrase_final = "".join(num) + " => " + phrase + "\n"
        f.write(phrase_final)

