#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import randint, shuffle
#basic set up
app = QApplication([])
window = QWidget()
window.score = 0
window.total = 0
window.setWindowTitle('Memo Card')
#pertanyaan dan tombol jawaban
btn_OK = QPushButton('Answer')
lb_Question = QLabel('In what year was New York founded?')

RadioGroupBox = QGroupBox('Answer options')
rbtn_1 = QRadioButton('1624')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, alignment=Qt.AlignHCenter)
layout_ans3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
#panel jawaban
AnsGroupBox = QGroupBox('Test result')
lb_Result = QLabel('Are you correct or not?')
lb_Correct = QLabel('the answer will be here!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

RadioGroupBox.hide()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q = Question('In what year was New York founded?', '1624', '1242', '1861', '1943')

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Pertanyaan berikutnya')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Jawab')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if btn_OK.text() == 'Jawab':
        check_answer()
    else:
        show_question()  

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    # answers[0].setText(right_answer)
    # answers[1].setText(wrong1)  
    # answers[2].setText(wrong2)  
    # answers[3].setText(wrong3)  
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Benar!')
        window.score += 1
        print('Statistic\n-Total questions:', window.total, '\n-Correct answers:', window.score)
    else:
        if (answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked()):
            show_correct('Salah')
            print('Rating:', window.score / window.total * 100, '%')
window = QWidget()
window.cur_question = -1
def next_question():
    # window.cur_question = window.cur_question + 1
    # if window.cur_question >= len(question_list):
    #     window.cur_question = 0
    # q = question_list[window.cur_question]
    # ask(q)
    window.total += 1
    print('Statistic\n-Total questions:', window.total, '\n-Correct answers:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Jawab':
        check_answer()
    else:
        next_question()

question_list = []
question_list.append(Question('The State langusage of Brazil is?', 'Portuguese', 'Spanish', 'English', 'French'))
question_list.append(Question('The capital of Indonesia is?', 'Jakarta', 'Bandung', 'Surabaya', 'Medan'))
question_list.append(Question('The largest country in the world is?', 'Russia', 'China', 'USA', 'India'))
question_list.append(Question('The currency of Japan is?', 'Yen', 'Dollar', 'Euro', 'Rupiah'))
question_list.append(Question('The highest mountain in the world is?', 'Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse'))
question_list.append(Question('The longest river in the world is?', 'Nile', 'Amazon', 'Yangtze', 'Mississippi'))
#window.cur_question = -1
btn_OK.clicked.connect(click_OK)
#ask(q)
next_question()
#window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.show()
app.exec()
