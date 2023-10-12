from Data import Data
from random import shuffle

while True:
    try:
        numberOfQuestions = int(input("How many Questions do you want?\n"))
        if numberOfQuestions <= 0:
            raise Exception()
        break
    except KeyboardInterrupt:
        exit(1)
    except:
        print("Please Enter Positive Numbers Only.")

while True:
    try:
        difficulty = input("What Difficulty do you want? [Easy/Medium/Hard ]\n").lower()
        if not (difficulty == "easy" or difficulty == "medium" or difficulty == "hard"):
            raise Exception()
        break
    except KeyboardInterrupt:
        exit(1)
    except:
        print("Please Enter The Correct Value.")

data = Data(numberOfQuestions, difficulty)

score = 0

i = 0

try:
    while i < numberOfQuestions:
        print(
            f"\n{i + 1}: ",
            data[i]["question"]
            .replace("&quot;", '"')
            .replace("&#039;", "'")
            .replace("&eacute;", "é")
            .replace("&amp;", "&"),
            "\n",
        )
        answerList = data[i]["incorrect_answers"]
        answerList.append(data[i]["correct_answer"])
        shuffle(answerList)

        for index, value in enumerate(answerList):
            print(
                f"{index + 1}: ",
                value.replace("&quot;", '"')
                .replace("&#039;", "'")
                .replace("&eacute;", "é")
                .replace("&amp;", "&"),
            )

        while True:
            try:
                answer = int(input("Type The Answer Number: \n"))
                if answer <= 0 or answer > 4:
                    raise Exception()
                break
            except KeyboardInterrupt:
                exit(1)
            except:
                print("Please Enter The Correct Option Number.")

        if answerList[answer - 1] == data[i]["correct_answer"]:
            score += 1

        i += 1
except KeyboardInterrupt:
    exit(1)

print(f"Your score is {int((score / numberOfQuestions) * 100)}%")
