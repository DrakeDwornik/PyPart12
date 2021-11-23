from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    returns a list of either even or odd numbers from start (inclusive) to stop (exclusive)

    :param start: integer from which to start the list
    :param stop: the end of the list (exclusive)
    :param parity: an ENUM of either EVEN or ODD to choose the numbers from
    :return: a list of the appropriate range
    """

    result = [n for n in range(start, stop) if n % 2 == (parity.value + 1) % 2]
    return(result)

def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    creates a dict with the keys in range start (inclusive) to stop (exclusive), the strategy is applied to each key
    to produce the value


    :param start: integer for the first key in range
    :param stop: integer for the last key in range (exclusive)
    :param strategy: lambda to apply to the keys
    :return: dictionary of the result
    """
    result = {k: strategy(k) for k in range(start, stop)}
    return result


def gen_set(val_in: str) -> Set:
    """
    returns a set of the lower case letters in val_in converted to uppercase

    :param val_in: a string
    :return: the returned set
    """
    result = {v.upper() for v in val_in if v.islower()}
    return result
