import json

with open("quiz.json", 'r') as  file:
    content=file.read()

data=json.loads(content)

for index, question in enumerate(data):
    print(index+1, "-", question["Question"])
    for index, option in enumerate(question["Options"]):
        print(f"{index+1}) {option}")
    answer=int(input("Enter your answer: "))
    question["User_answer"]=answer

score=0
for index, question in enumerate(data):
    if (question["User_answer"]==question["Correct"]):
        score=score+1
        result="Correct answer"
    else:
        result='Wrong answwer'
    print(f"{index+1} - {result} Your Answer: {question['User_answer']} "
          f"Correct Answer: {question['Correct']}")
print(score, "/", len(data))