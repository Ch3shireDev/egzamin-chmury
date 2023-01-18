import yaml
import random
import os

if __name__ == "__main__":

    with open('data.yml', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()

    random.shuffle(data)

    for question in data:

        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

        print(question['_question'])
        for quiz_answer in question['answers']:
            print(quiz_answer)

        answer = question['answer']
        input()
        print(answer)
        input()