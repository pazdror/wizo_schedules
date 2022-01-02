__author__ = 'Dror Paz'

from pathlib import Path

from csv_parser import is_valid_file, parse_csv
from tables_generators import generate_by_instructor, generate_by_group


def _exit():
    print('BYE!')
    exit(1)


GROUP_BY = {
    1: ('1. Get schedule by group', generate_by_group),
    2: ('2. Get schedules by instructor', generate_by_instructor),
    3: ('3. Exit', _exit)
}


def _get_input_file() -> str:
    file_is_valid = False
    while not file_is_valid:
        input_csv = input('Please enter location of input csv file (type "exit" to quit):')
        if input_csv == 'exit':
            _exit()
        file_is_valid = is_valid_file(input_csv)
    return input_csv


def _get_output_location() -> Path:
    output_location = None
    while not output_location or not output_location.exists():
        output_location = Path(input('Please enter output location (type "exit" to quit):'))
        if output_location == 'exit':
            _exit()
    output_location = output_location.absolute()
    print(f'Output files will be written to {output_location}')
    return Path(output_location).absolute()


def _get_grouping() -> int:
    number = 0
    valid_options = list(GROUP_BY.keys())
    options_string = '\n'.join([option[0] for option in GROUP_BY.values()])
    while not number:
        print('\nSchedule Options:\n------------------\n')
        print(options_string)
        selection = input("Select your preferred grouping method (type only the number and press ENTER):")

        try:
            if not selection:
                print('No option was selected')
                continue
            number = int(selection)
            assert number, 'No number was selected'
            assert number in valid_options, 'Selected number is not in the list'
            return number
        except AssertionError as exc:
            print(exc)
        except ValueError:
            print('Invalid option. Please enter only the number of your selection')


def wizo_schedules_generator():
    input_csv = _get_input_file()
    output_location = _get_output_location()
    grouping_num = _get_grouping()
    print(f'Creating schedule and saving to {output_location}')
    dataframe = parse_csv(input_csv)
    GROUP_BY[grouping_num][1](dataframe=dataframe, output_location=output_location)


if __name__ == '__main__':
    wizo_schedules_generator()
