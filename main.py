import random, os
def clear(): os.system("clear")
letters = ' abcdefgh'
def colorSquare(letter, number):
  letterNum = letters.index(letter)
  num = number + letterNum
  if num % 2 == 1:
    color = 'Light'
  elif num % 2 == 0:
    color = 'Dark'
  return color
numOfTimes = 0
score = 0
while True:
  number = random.randint(1,8)
  letter = letters[random.randint(1,8)]
  color = colorSquare(letter, number)
  clear()
  print(f'{letter}{number}')
  guess = input('\nColor(w or b): ').lower()
  if guess[0] == 'w':
    if color == 'Light':
      score += 1
      input('Correct!\nEnter To Continue\n')
    else:
      input('Incorrect!\nEnter To Continue\n')
  elif guess[0] == 'b':
    if color == 'Dark':
      score += 1
      input('Correct!\nEnter To Continue\n')
    else:
      input('Incorrect!\nEnter To Continue\n')
  else:
    input('???\nPress Enter To Continue\n')
  print(f'{score}/{numOfTimes}')
clear()
score = 0
while True:
  number = random.randint(1,8)
  letter = letters[random.randint(1,8)]
  color = colorSquare(letter, number)
  clear()
  print(f'{letter}{number}')
  guess = input('\nColor(w or b): ').lower()
  if guess[0] == 'w':
    if color == 'Light':
      score += 1
      input('Correct!\nEnter To Continue\n')
    else:
      input('Incorrect!\nEnter To Continue\n')
  elif guess[0] == 'b':
    if color == 'Dark':
      score += 1
      input('Correct!\nEnter To Continue\n')
    else:
      input('Incorrect!\nEnter To Continue\n')
  else:
    input('???\nPress Enter To Continue\n')
  print(f'{score}/{numOfTimes}')
clear()