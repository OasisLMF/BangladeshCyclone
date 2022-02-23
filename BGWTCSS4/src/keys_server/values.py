


NULL_VALUES = [None, '', 'n/a', 'N/A', 'null', 'Null', 'NULL']


def to_string(val):
    """
    Converts value to string, with possible additional formatting.
    """
    return '' if val is None else str(val)


def to_int(val):
    """
    Parse a string to int
    """
    return None if val in NULL_VALUES else int(val)


def to_float(val):
    """
    Parse a string to float
    """
    return None if val in NULL_VALUES else float(val)
