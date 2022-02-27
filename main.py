# import pygame
# import requests
from fetch_questions import QuestionBank
from question_logic import QuestionLogic
# import os

#HIGH LEVEL PROCESS
#1) BUILD QUIZ LOGIC
#a) General logic for going through questions
#b) Pull data from QuizDB - DONE
#c) Create classes for Questions
#d) Create logic for inputting correct/incorrect answers
#e) Build logic for choosing which topic and how many questions
#f) Build Endgame

#2) BUILD QUIZ UI via PYGAME

game_active = True
qb = QuestionBank()
ql = QuestionLogic(qb)

while game_active:
    while ql.current_question < len(ql.qb.question_bank):
        ql.next_question()
    game_active = False
    print('Quiz Complete. Your Score is X')

 