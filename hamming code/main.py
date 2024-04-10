
from colorama import Fore
import random
import math


def get_code_from_file():
    code = list()
    with open('code_file.txt', 'r') as file:
        character = file.read(1)
        while character:
            if character != '\n':
                code.append(int(character))
            character = file.read(1)
    return code


def calculate_amount_of_check_bits(length_of_code):
    k = 0
    while k < math.log2(k + length_of_code + 1):
        k += 1
    return k


def get_indexes_for_check_bits(check_bits_amount):
    indexes = list()
    for i in range(check_bits_amount):
        indexes.append(pow(2, i) - 1)
    return indexes


def check_bits_included(number, mask):
    return (number & mask) == mask


def get_transfer_code(code, indexes_check_bits):
    _code = list(code)
    for i in indexes_check_bits:
        _code.insert(i, 0)
    for index_element in range(len(_code)):
        if index_element in indexes_check_bits:
            flag = False
            for index in range(len(_code)):
                if check_bits_included(index+1, index_element+1):
                    if flag:
                        _code[index_element] ^= _code[index]
                    else:
                        flag = True
                        _code[index_element] = _code[index]
    return _code


def get_code_with_error(code, index):
    _code = list(code)
    _code[index-1] = 0 if _code[index-1] else 1
    return _code


def get_index_where_error(code, indexes_check_bits):
    binary_code_error_bit = list()
    for index_element in range(len(code)):
        if index_element in indexes_check_bits:
            flag = False
            for index in range(len(code)):
                if check_bits_included(index+1, index_element+1):
                    if flag:
                        bit ^= code[index]
                    else:
                        flag = True
                        bit = code[index]
            binary_code_error_bit.append(bit)
    binary_code_error_bit.reverse()
    return binary_code_error_bit


def convert_binary_to_decimal(binary_code_error_bit):
    error_bit = 0
    size = len(binary_code_error_bit) - 1
    for element in binary_code_error_bit:
        if element:
            error_bit += pow(2, size)
        size -= 1
    return error_bit


def get_corrected_code(code, decimal_index):
    corrected = list(code)
    corrected[decimal_index-1] = 0 if corrected[decimal_index-1] else 1
    return corrected


def print_colorful(string, var):
    print(Fore.GREEN + string + Fore.BLUE, var)


def main():
    initial_code = get_code_from_file()
    amount_of_check_bits = calculate_amount_of_check_bits(len(initial_code))
    indexes_of_check_bits = get_indexes_for_check_bits(amount_of_check_bits)
    transfer_code = get_transfer_code(initial_code, indexes_of_check_bits)
    random_index = random.randint(1, len(transfer_code))
    # code_with_error = get_code_with_error(transfer_code, 8)
    code_with_error = get_code_with_error(transfer_code, 5)
    # code_with_error = get_code_with_error(transfer_code, random_index)
    binary_code_of_error_bit = get_index_where_error(code_with_error, indexes_of_check_bits)
    decimal_index_of_error_bit = convert_binary_to_decimal(binary_code_of_error_bit)
    corrected_code = get_corrected_code(code_with_error, decimal_index_of_error_bit)

    print_colorful("Initial code:                 ", initial_code)
    print_colorful("Length of initial code:       ", len(initial_code))
    print_colorful("Amount of check bits:         ", amount_of_check_bits)
    print_colorful("Indexes of check bits:        ", indexes_of_check_bits)
    print_colorful("Transfer code:                ", transfer_code)
    print_colorful("Index for error:              ", random_index)
    print_colorful("Code with error:              ", code_with_error)
    print_colorful("Binary code of bit with error:", binary_code_of_error_bit)
    print_colorful("Decimal index of error:       ", decimal_index_of_error_bit)
    print_colorful("Corrected code:               ", corrected_code)


if __name__ == "__main__":
    main()
