import yaml
import random
import os

with open('questions.yml', encoding='utf-8') as f:
    questions = yaml.load(f, Loader=yaml.FullLoader)
    f.close()

with open('answers.yml', encoding='utf-8') as f:
    answers = yaml.load(f, Loader=yaml.FullLoader)
    f.close()

data = []

for section in questions:
    for question in section['questions']:
        # question['_question'] = lib.gen_question(question['_question'])
        answer = [a for a in answers if a['_title'] == section['_title']][0]
        answer = [a for a in answer['answers'] if a['number'] == question['_number']][0]
        question['answer'] = answer['answer']
        data.append(question)

with open('data.yml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    f.close()