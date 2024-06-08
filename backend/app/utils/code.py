from enum import Enum


def generate_enum(data_codes):
    enum_dict = {}
    for code in data_codes:
        enum_dict[code.upper()] = code
    return Enum("ColorEnum", enum_dict)
