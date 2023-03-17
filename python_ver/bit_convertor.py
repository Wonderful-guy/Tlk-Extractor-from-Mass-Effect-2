# A packed array of booleans.
# @author kiwimoosical
# @link https://www.se7ensins.com/forums/threads/java-c-s-bitconverter-in-java.486271/
def to_int_32(bytes: list, index: int):
    if len(bytes) != 4:
        raise Exception('The length of the byte array must be at least 4 bytes long.')
    return (0xff & bytes[index]) << 24 | \
        (0xff & bytes[index + 1]) << 16 | \
        (0xff & bytes[index + 2]) << 8 | \
        (0xff & bytes[index + 3])


def to_int_64(bytes: list, index: int):
    if len(bytes) != 4:
        raise Exception('The length of the byte array must be at least 8 bytes long.')
    return (0xff & bytes[index]) << 56 | \
        (0xff & bytes[index + 1]) << 48 | \
        (0xff & bytes[index + 2]) << 40 | \
        (0xff & bytes[index + 3]) << 32 | \
        (0xff & bytes[index + 4]) << 24 | \
        (0xff & bytes[index + 5]) << 16 | \
        (0xff & bytes[index + 6]) << 8 | \
        (0xff & bytes[index + 7])


def get_bytes_by_value(value: int) -> list:
    b = format(value, '32b').replace(' ', '0')
    byte_1 = int(b[:8], 2)
    byte_2 = int(b[8:16], 2)
    byte_3 = int(b[16:24], 2)
    byte_4 = int(b[24:], 2)
    return [byte_4, byte_3, byte_2, byte_1]


def to_char_rev(bytes_list: list, index: int):
    if len(bytes_list) < 2:
        raise Exception('The length of the byte array must be at least 2 bytes long.')
    for i in range(len(bytes_list) // 2):
        bytes_list[i], bytes_list[len(bytes_list) - 1 - i] = bytes_list[len(bytes_list) - 1 - i], bytes_list[i]

    buffer = [None] * (len(bytes_list) // 2)
    for i in range(len(buffer)):
        byte_pos = i << 1  # left shift to increase 'i' to power of 2 (multiply by 2)
        byte_1 = bytes_list[byte_pos]
        byte_2 = bytes_list[byte_pos + 1]

        # left shift to paste byte_2 instead of byte_1
        c = (byte_1 << 8) + byte_2
        buffer[i] = chr(c)
    count_of_chars = len(buffer)
    return buffer[count_of_chars - 1 - index]


def get_bytes(x) -> list:
    return [x >> 24, x >> 16, x >> 8, x]
    # if isinstance(x, int):
    #     return [x >> 24, x >> 16, x >> 8, x]
    # elif isinstance(x, long):
    #     return [x >> 56, x >> 48, x >> 40, x >> 32, x >> 24, x >> 16, x >> 8, x]