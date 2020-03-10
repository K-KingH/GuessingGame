import random
user = input('Guess a number between 0 and 20. To end game enter "done"')
rand = random.uniform(0, 20)
while True:
  if user == rand:
    print("Correct!")
    cnt += 1
    if cnt >=4:
      print("You're amazing!")
  elif user == 'done':
    break
  else:
    print("Incorrect!")
    cnt = 0
    