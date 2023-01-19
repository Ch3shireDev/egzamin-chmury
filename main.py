import yaml
import random
import os

if __name__ == "__main__":

    with open('data.yml', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()

    random.shuffle(data)

    # enumerate with index
    for index, question in enumerate(data):

        # clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Pytanie {index+1}/{len(data)}")
        print()

        print(question['_question'])
        for quiz_answer in question['answers']:
            print(f" - {quiz_answer}")

        answer = question['answer']
        print()
        input("Naciśnij [ENTER] aby zobaczyć odpowiedź.")
        print("\r                                        ")
        print(f"Odpowiedź: {answer}")
        print()
        input("Naciśnij [ENTER] aby przejść do następnego pytania.\n")
        