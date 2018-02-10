import random
from collections import OrderedDict
import pprint
import csv
import math

users = {}

f = open('event300.csv', 'r')
csvReader = csv.reader(f)
for user, vote in csvReader:
    users[user] = math.log10(float(vote)) + 3

f.close()

total = sum([float(prob) for user, prob in users.items()])

accumulated_prob = 0
usersWithRange = OrderedDict()
for user, prob in users.items():
    users[user] = prob / total
    usersWithRange[user] = [accumulated_prob, accumulated_prob + users[user]]
    accumulated_prob = accumulated_prob + users[user]

pprint.pprint(usersWithRange)


picked_num = 0
winner = []
idx = 1

print("#### 추첨을 시작합니다! ####")

while len(winner) < 6:
    if idx <= 3:
        input("3등 3분 추첨! ({}/3)".format(idx))

    elif idx > 3 and idx <= 5:
        input("2등 2분 추첨! ({}/2)".format(idx-3))

    else:
        input("대망의 1등 추첨!!")

    picked_num = random.random()
    print("컴퓨터가 뽑은 숫자: {}".format(picked_num))
    for user, probRange in usersWithRange.items():
        if probRange[0] <= picked_num and picked_num <= probRange[1] and user not in winner:
            print("당첨자는 {}님!".format(user))

            if idx < 6:
                input("다음 추첨으로..")

            idx += 1
            winner.append(user)
            break

    else:
        print("중복당첨 재추첨!")

print("당첨자: {}".format(winner))
