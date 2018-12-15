from json import dump
from re import search
from splitty import (
    list_by_re_pattern,
    make_intervals,
    apply_intervals,
    clear_list_strings,
)

regex_process = (
    r'^Processo \d+-(\d+\.?){5}(/\d{2})?\s?(\(Processo \d+-(\d+\.?){5}\))?'
)


def get_process_number(vara, block):
    return (
        search(regex_process, vara[block][0])
        .group(0)
        .replace('Processo ', '')
        .strip()
    )


with open('examples/tjsp_parse/caderno3_parsed.txt') as f:
    file = clear_list_strings(f.readlines())

vila_prudente = apply_intervals(
    file,
    make_intervals(
        list_by_re_pattern(file, r'(IX - Vila Prudente|X - Ipiranga)')
    ),
)[0]

vara_1 = apply_intervals(
    vila_prudente,
    make_intervals(
        list_by_re_pattern(
            vila_prudente, r'^(Juizado Especial|\dª\sVara)\sCível\n$'
        )
    ),
)[0]

processo_blocks = make_intervals(list_by_re_pattern(vara_1, regex_process))

processos_vara_1 = {
    get_process_number(vara_1, processo): ' '.join(vara_1[processo])
    for processo in processo_blocks
}

with open('examples/tjsp_parse/caderno3_parsed.json', 'w') as f:
    dump(processos_vara_1, f, indent=2, ensure_ascii=False, sort_keys=True)
