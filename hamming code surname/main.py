
from colorama import Fore
import math


def get_text_from_file():
    with open('code_file.txt', 'r',  encoding='utf-8') as file:
        text = file.readline().rstrip()
    return text


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return [int(bit) for bit in bits]


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    bit_string = ''.join(map(str, bits))
    n = int(bit_string, 2)
    byte_array = bytearray()
    while n:
        byte_array.append(n & 0xff)
        n >>= 8
    byte_array.reverse()
    return byte_array.decode(encoding, errors)


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


def remove_check_bits(bits, check_indexes):
    decode = list()
    for index in range(len(bits)):
        if not (index in check_indexes):
            decode.append(bits[index])
    return decode


def main():

    text_surname = get_text_from_file()
    initial_code = text_to_bits(text_surname)
    amount_of_check_bits = calculate_amount_of_check_bits(len(initial_code))
    indexes_of_check_bits = get_indexes_for_check_bits(amount_of_check_bits)
    transfer_code = get_transfer_code(initial_code, indexes_of_check_bits)
    code_with_error = get_code_with_error(transfer_code, 10)
    original_with_error = text_from_bits(remove_check_bits(code_with_error, indexes_of_check_bits))
    binary_code_of_error_bit = get_index_where_error(code_with_error, indexes_of_check_bits)
    decimal_index_of_error_bit = convert_binary_to_decimal(binary_code_of_error_bit)
    corrected_code = get_corrected_code(code_with_error, decimal_index_of_error_bit)
    original_after_error = text_from_bits(remove_check_bits(corrected_code, indexes_of_check_bits))

    print_colorful("Original:                     ", text_surname)
    print_colorful("Initial code:                 ", initial_code)
    print_colorful("Length of initial code:       ", len(initial_code))
    print_colorful("Amount of check bits:         ", amount_of_check_bits)
    print_colorful("Indexes of check bits:        ", indexes_of_check_bits)
    print_colorful("Transfer code:                ", transfer_code)
    print_colorful("Code with error:              ", code_with_error)
    print_colorful("Original with error:          ", original_with_error)
    print_colorful("Binary code of bit with error:", binary_code_of_error_bit)
    print_colorful("Decimal index of error:       ", decimal_index_of_error_bit)
    print_colorful("Corrected code:               ", corrected_code)
    print_colorful("Original after error:         ", original_after_error)


if __name__ == "__main__":
    main()
