    # function 
def processing_error():
  while True:
    try:
      num = int(input("Your choice (1-3) - "))
      return num
    except ValueError:
      print("Not valid choice. Try again.")
def get_answer_num():
  num = 10001 
  while num < 1 or num >3 :
    if num != 10001 :  # не выдает предупреждение при первом запросе
      print("Not valid. Attempt more")
    num = processing_error()
  return num  
      
    # main
set_of_choice = list()
f_q = open('questions.txt','r')
str = '#'
while str[0] == '#':
  str = f_q.readline()
  #print('coment')
  if str[0] == '@': 
    param = [int(s) for s in str.split() if s.isdigit()]
    print(param)

print(
  "           Test - Bicycle Specialist",
  "Contain 10 questions",
  "each by 0-1 points",
  "Max points are 10",
  "           Lets go...",
  sep="\n")
q_ques = param[0]  #количество вопросов
q_var = param[1]  #кол-во вариантов
for i in range(0,q_ques):
  for k in range(0,q_var+1):
    print(f_q.readline())
  answer_num = get_answer_num()
  set_of_choice.append(answer_num)
f_q.close()
#n = 1  #счетчик кол-ва ответов
#for el in set_of_choice:
#  print(f"Question {n} choice  - {el}")
#  n = n+1
print(set_of_choice)
    #читаем правильные ответы
f_ans = open('answers.txt', 'r')
answer_str = f_ans.readline()
f_ans.close()
answer_list = [int(c) for c in answer_str if c != ',']
answer_list = answer_list[0:q_ques]
print (answer_list)
    #расчет и вывод результата
result = 0
for i in range(q_ques):
  if set_of_choice[i] == answer_list[i]:
    result = result + 1
print(f'Вы правильно ответили на {result} вопросов из {q_ques}')
print(f'Ваш результат {round(result/q_ques*100,1)} %')