import lib
import yaml

with open('odpowiedzi.md', encoding='utf-8') as f:
    answers = f.read()
    f.close()


rozdzialy = lib.get_rozdzialy(answers)

data = []

for rozdzial in rozdzialy:
    title = lib.get_title(rozdzial)
    sections = lib.get_sections(rozdzial)
    answers = []
    for section in sections:
        question = lib.get_question(section)
        number = lib.get_number(section)
        answer = lib.gen_answer(section)
        print(f"{number}. {question}")
        print(answer)
        answers.append({'question': question, 'answer': answer, 'number': number})
    data.append({'_title': title, 'answers': answers})

with open('answers.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    f.close()