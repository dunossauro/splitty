from typing import List, Optional, Tuple, Union, Match, Any


def apply_intervals(
    list_: List[Any], intervals: List[slice]
) -> List[List[Any]]:
    ...


def chunks(iterable: List[Any], size: int) -> List[List[Any]]:
    ...


def clear_list_strings(strings: List[str]) -> List[str]:
    ...


def find_elements(
    full_list: List[Any], list_with_values: List[Any]
) -> List[Tuple[int, Any]]:
    ...


def list_by_list(
    list_with_elements: List[Any],
    list_with_intervals: List[Any],
    start: bool = ...,
) -> List[List[Any]]:
    ...


def list_by_re_pattern(
    list_to_be_splited: List[Any], pattern: str, str_convert: bool = ...
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
