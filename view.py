# -*- coding: utf-8 -*-

# from django.http import HttpResponse

import random
from django.shortcuts import render

question = []
answer = []
# model = input("select model:")
output = []

# 两位数加法


def Xxandxx():

	global question
	global answer
	question = []
	answer = []

	i = 0
	limit = 100
# r = range(i,limit)

    # 1
    # for t in r :
	while i < limit:
		num1 = random.randint(10, 99)
		num2 = random.randint(10, 99)
		result = num1 + num2
		question.append(str(num1) + ' + ' + str(num2) + ' = ' + "   ")
		answer.append(str(num1) + ' + ' + str(num2) + ' = ' + str(result))
		i += 1


# 2 问题列表
def Questions():
    global question
    global output
    output = []
    Xxandxx()
    j = 0
    for q in question:
        if j % 2 == 0:
            output.append(q + "\t\t\t")
        else:
            output.append(q + "\n")
        j += 1
    return output


# 3 答案列表


def Answers():
    global answer
    k = 0
    for q in answer:
        if k % 2 == 0:
            print(q, end="\t\t\t")
        else:
            print(q + "\n")
        k += 1


'''
Xxandxx()
if model == '1':
    print("questions are: \n")
    Questions()
else:
    Answers()
'''


def addition(request):
    context = {}
    context['addition'] = Questions()
    return render(request, 'addition.html', context)
