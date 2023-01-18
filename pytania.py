import re
import lib
import yaml

with open('pytania.md', encoding='utf-8') as f:
    pytania = f.read()
    f.close()



rozdzialy = lib.get_rozdzialy(pytania)

assert len(rozdzialy) == 7, f"Expected 7 rozdzialy, got {len(rozdzialy)}"

data = []

for rozdzial in rozdzialy:
    # print(rozdzial.splitlines()[0])
    title = lib.get_title(rozdzial)
    # print(title) 
    questions = []
    sections = lib.get_sections(rozdzial)
    for section in sections:
        question = lib.get_question(section)
        number = lib.get_number(section)
        # print(question)
        print(question)
        answers = lib.get_answers(section)
        questions.append({
            "_question": question,
            "_number": number,
            "answers": answers,
        })
    data.append({'_title': title, 'questions': questions})

with open('questions.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    f.close()
