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


def get_process_number(processo):
    return (
        search(regex_process, processo[0])
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


varas_block = list_by_re_pattern(
    vila_prudente, r'^(Juizado Especial|\dª\sVara)\sCível$'
)

vara_names = [vara[1] for vara in varas_block]


varas = apply_intervals(file, make_intervals(varas_block))

processos = apply_intervals(
    vila_prudente,
    make_intervals(list_by_re_pattern(vila_prudente, regex_process)),
)


processos = {
    vara_name: {
        get_process_number(processo): ''.join(processo)
        for processo in processos
    }
    for vara_name, vara in zip(vara_names, varas)
}

with open('examples/tjsp_parse/caderno3_parsed.json', 'w') as f:
    dump(processos, f, indent=2, ensure_ascii=False, sort_keys=True)
