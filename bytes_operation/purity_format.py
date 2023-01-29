from icecream import ic
from typing import List

from bytes_operation.convert_bytes import convert_bytes_to_hex_string


def split_string(input_string: str, unit_length: int) -> List[str]:
    if len(input_string) % unit_length == 0:
        unit_number = int(len(input_string) / unit_length)
    else:
        unit_number = int(len(input_string) / unit_length) + 1
    return [
        input_string[unit_length * i:unit_length * (i + 1)]
        for i in range(unit_number)
    ]


def insert_space_and_new_line(
    splitted_string: List[str],
    unit_number: int,
) -> List[str]:
    result = []
    for i in range(len(splitted_string)):
        result.append(splitted_string[i])
        if i % unit_number == unit_number - 1:
            result.append('\n')
        else:
            result.append(' ')
    result = result[:len(result) - 1]
    return result


def purity_hex_format_bytes(input_bytes: bytes) -> str:
    converted_hex_str = convert_bytes_to_hex_string(input_bytes)
    splitted_byte_str_list = split_string(converted_hex_str, unit_length=2)
    space_inserted_byte_str_list = insert_space_and_new_line(
        splitted_byte_str_list,
        unit_number=16,
    )
    return ''.join(space_inserted_byte_str_list)


if __name__ == '__main__':
    input_bytes = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'
    ic(purity_hex_format_bytes(input_bytes))