TITLE_TAG = 'TI'
ABSTRACT_TAG = 'AB'


def parse_pubmed_content(raw_content: str):
    lines = raw_content.splitlines()

    # drop empty files
    if len(lines) == 0:
        return None

    TI_sections = []
    AB_sections = []
    for i in range(len(lines)):
        line = lines[i]
        current_section = ""

        if line.startswith("TI"):
            current_section += line[5:]
            i += 1
            while i < len(lines) and lines[i].startswith(' '):
                current_section += lines[i].strip() + " "
                i += 1

            TI_sections.append(current_section)
        elif line.startswith("AB"):
            current_section += line[5:]
            i += 1
            while i < len(lines) and lines[i].startswith(' '):
                current_section += lines[i].strip() + " "
                i += 1

            AB_sections.append(current_section)

    return TI_sections, AB_sections
