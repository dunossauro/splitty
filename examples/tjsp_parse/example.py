from json import dump
from re import search
from splitty import list_by_re_pattern, make_intervals

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
    file = [string.strip() for string in f.readlines() if string.strip()]

vila_prudente_block = make_intervals(
    list_by_re_pattern(file, r'(IX - Vila Prudente|X - Ipiranga)')
)  # [slice(5, 4862, None), slice(4862, None, None)]

vila_prudente = file[vila_prudente_block[0]]

varas_blocks = make_intervals(
    list_by_re_pattern(
        vila_prudente, r'^(Juizado Especial|\dª\sVara)\sCível\n$'
    )
)  # [slice(2, 270, None), slice(270, 921, None), slice(921, 2187, None), slice(2187, 4273, None), slice(4273, None, None)] # NOQA

vara_1 = vila_prudente[varas_blocks[0]]

processo_blocks = make_intervals(list_by_re_pattern(vara_1, regex_process))

processos_1 = {
    get_process_number(vara_1, processo): ' '.join(vara_1[processo])
    for processo in processo_blocks
}

# import ipdb; ipdb.set_trace()

# result = {}

with open('examples/tjsp_parse/caderno3_parsed.json', 'w') as f:
    dump(processos_1, f, indent=2, ensure_ascii=False, sort_keys=True)
