def convert_bytes_to_integer(input_bytes: bytes) -> int:
    return int.from_bytes(input_bytes, byteorder='big')


def convert_bytes_to_hex_string(
    input_bytes: bytes,
    with_prefix: bool = False,
    digit: int = -1,
) -> str:
    converted_string = hex(convert_bytes_to_integer(input_bytes))
    converted_string = converted_string[2:]
    if digit > 0 & len(converted_string) < digit:
        converted_string = '0' * (digit -len(converted_string)) + converted_string
    if with_prefix:
        converted_string = '0x' + converted_string
    return converted_string