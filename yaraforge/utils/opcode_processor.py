import binascii

from yaraforge.metadata import pathnames
# Assuming yaraforge.metadata.pathnames and yaraforge.utils.logger are valid modules
from yaraforge.utils.logger import get_global_logger

logger = get_global_logger(pathnames['logger_dir'])


def format_hex(data):
    """
    Format the hex data
    :param data:
    :return: Formatted hex data
    """
    return " ".join(data[i:i + 2] for i in range(0, len(data), 2))


def _wildcard_bytes(data, offset, length):
    """
    Wildcard the bytes in the data
    :param data:
    :param offset:
    :param length:
    :return: Wildcarded bytes
    """
    for i in range(offset, offset + length):
        data[i] = "?"
    return data


def _process_instruction(ins):
    """
    Process the instruction
    :param ins:
    :return: Processed instruction
    """
    ins_hex_list = list(binascii.hexlify(ins.bytes).decode("ascii").upper())

    ins_hex_list = _wildcard_bytes(ins_hex_list, ins.disp_offset * 2, ins.disp_size * 2)

    signature = ''.join(ins_hex_list)
    return signature


def format_bytes_with_space(bytes_str):
    """將機器碼字串中每兩個字符之間加入空格"""
    return ' '.join(bytes_str[i:i + 2] for i in range(0, len(bytes_str), 2))
