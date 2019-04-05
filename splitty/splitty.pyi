from typing import List, Optional, Tuple, Union, Match


def apply_intervals(
    list_: List[Union[str, int]], intervals: List[slice]
) -> List[List[Union[str, int]]]:
    ...


def chunks(iterable: List[str], size: int) -> List[List[str]]:
    ...


def clear_list_strings(strings: List[str]) -> List[str]:
    ...


def find_elements(
    full_list: Union[List[str], List[Union[str, int]]],
    list_with_values: List[str],
) -> List[Tuple[int, str]]:
    ...


def list_by_list(
    list_with_elements: List[Union[str, int]],
    list_with_intervals: List[str],
    start: bool = ...,
) -> List[List[Union[str, int]]]:
    ...


def list_by_re_pattern(
    list_to_be_splited: Union[List[str], List[Union[str, int]]],
    pattern: str,
    str_convert: bool = ...,
) -> List[Tuple[int, str]]:
    ...


def make_intervals(
    blocks: Union[List[int], List[Tuple[int, str]]], start: bool = ...
) -> List[slice]:
    ...


def number_eq(matcher: int, element: int) -> bool:
    ...


def str_eq(matcher: str, element: Union[str, int]) -> Optional[Match]:
    ...
