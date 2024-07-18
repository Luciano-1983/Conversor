from parser import parser

from lexer import lexer


def main(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    lexer.input(data)

    tokens = []
    for tok in lexer:
        tokens.append(tok)
        print(tok)

    result = parser.parse(data)

    if not result:
        print("Parsing failed.")
        return

    with open(output_file, 'w') as file:
        file.write(result)

    print(f'Translation complete. Output written to {output_file}')


if __name__ == '__main__':
    input_file = 'codigo_python.py'
    output_file = 'codigo_javascript.js'

    main(input_file, output_file)
