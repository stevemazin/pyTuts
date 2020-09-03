import sys
print('WELCOME 2 the ULTIMATE MAD LIBS game!!')
placeholders = ['NOUN', 'ADJECTIVE', 'VERB_ING', 'VERB']


def process_line(line):
    processed_line = ''
    words = line.split()
    for word in words:
        stripped_word = word.strip('.,;?!')
        if stripped_word in placeholders:
            user_input = input(f'Enter a {stripped_word}: ')
            processed_line = processed_line + user_input
            if word[-1] in '.,;?!':
                processed_line = processed_line + word[-1] + ' '
            else:
                processed_line = processed_line + ' '
        else:
            processed_line = processed_line + word + ' '

    return processed_line + '\n'


def make_mad_lib(filename):
    try:
        my_file = open(filename, 'r')
        processed_text = ''
        for line in my_file:
            processed_text = processed_text + process_line(line)

        my_file.close()
        return processed_text

    except FileNotFoundError:
        print('error! no such file...')
    except IsADirectoryError:
        print(f'error! {filename} is a directory...')
    except Exception:
        print('oops! something went wrong!')


def save_file(filename, text_to_save):
    try:
        my_file = open(filename, 'w')
        my_file.write(text_to_save)
        my_file.close()
    except Exception:
        print('error writing file!')


def main_funk():
    if len(sys.argv) < 2:
        print("crazy.py <filename>")
    else:
        filename = sys.argv[1]
        new_mad_lib = make_mad_lib(filename)

        if new_mad_lib is not None:
            save_file('Ouch.txt', new_mad_lib)
            print('\n...file written successfully!')
        print(f'\n{new_mad_lib}')


if __name__ == '__main__':
    main_funk()
