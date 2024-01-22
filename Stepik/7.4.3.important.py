text=input()
counter=0
while text!='стоп' and text!='хватит' and text!='достаточно':
  counter+=1
  text=input()
print(counter)


word = input()
cnt = 0
while not (word == 'стоп' or word == 'хватит' or word == 'достаточно'):
    cnt += 1
    word = input()
print(cnt)