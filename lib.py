import re

def get_rozdzialy(pytania):
    matches = re.split(r'## Rozdział', pytania, flags=re.MULTILINE, maxsplit=0)
    if not pytania.startswith("## Rozdział"):
        matches = matches[1:]
    matches = [m.strip() for m in matches if m.strip()]
    matches = [f"## Rozdział {m}" for m in matches if m]
    return matches

def get_title(rozdzial):
    matches = re.findall(r'## Rozdział \d+. (.*)', rozdzial)
    if not matches:
        return ""
    return matches[0]

def get_sections(rozdzial):
    rozdzial = rozdzial.strip()
    rozdzial = re.sub(r'## Rozdział.*', '', rozdzial)
    matches = re.split(r'\d+\. ', rozdzial, flags=re.MULTILINE, maxsplit=0)
    matches = matches[1:]
    matches = [f"{i+1}. {m}" for i, m in enumerate(matches)]
    return matches

def get_question(section):
    question = re.findall(r'^\d+\. (.*)', section)
    return question[0]

def get_number(section):
    number = re.findall(r'^(\d+)\.', section)
    return number[0]

def get_answers(section):
    answers = section.splitlines()[1:]
    answers = [a.strip() for a in answers if a]
    answers = [re.findall(r'^[a-z]\)\s*(.*)', answer)[0] for answer in answers]
    answers = [a.strip() for a in answers if a]
    return answers

def gen_answer(section):
    lines = section.splitlines()
    lines = [l.strip() for l in lines if l.strip() and l.strip().startswith('Odpowiedź')]
    return lines[0].replace('Odpowiedź: ', '')

def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list