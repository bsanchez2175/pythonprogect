def begin_story(): 
    user_response = 0
    print('you wake up late what do you do.',
    'What do you do?')
    print('Enter the number that corresponds to your decision')
    user_response = int(input('1. You continue to sleep. \n2. You wake up and go shower. \n3. You try to commit suicide with toilet paper '))
    decision1(user_response)

def decision1(user_response):
	print("you walk downstairs")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.go eat breakfast\n2.feed your dog\n3.you eat your dog just kidding"))
		decision2_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.you do your hair\n2.you pick out an outfit\n3.you go downstairs"))
		decision2_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.you try again\n2.drink bleach\n3.you go cry in your room "))
		decision2_3(user_response)
	
def decision2_1(user_response):
	print("you go eat breakfast and you find your parents dead")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.call the police\n2.pretend you didnt see anything\n3.steal their credit cards"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.go back upstairs\n2.play PS4\n3.cry"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.call your friend\n2.take a walk\n3.you do nothing"))

def decision2_2(user_response):
	print("you start the day")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.start making cereal\n2.wait for your dad\n3.give the dog food"))
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.nice outfit\n2.regular outfit\n3.lazy outfit"))
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.say good morning to you parents\n2.walk to school\n3.sit down on the couch"))

def decision2_3(user_response):
	print("You stay home because you feel sick")
	if user_response == 1:
		print("User selected 1. What do you do next?")
		user_response = int(input("1.you cry\n2.you give up\n3.you sit in silence"))
		decision3_1(user_response)
	elif user_response == 2:
		print("User selected 2. What do you do next?")
		user_response = int(input("1.you dont die\n2.you throw it up\n3.you regret it"))
		decision3_2(user_response)
	elif user_response == 3:
		print("User selected 3. What do you do next?")
		user_response = int(input("1.laugh\n2.stop crying\n3.slam your head on the door"))
		decision3_3(user_response)
		
def decision3_1(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.they get to the house\n2.they dont show up\n3.you runaway"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.walk out\n2.text a frined\n3.dont care"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.go to the mall\n2.waste money on suprene\n3.waste money on bape"))
    decision3_3(user_response)

def decision3_2(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1. frosted flakes\n2.apple jacks\n3.corn flakes"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.you walk the dog\n2.ride booosted board\n3.go to school"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.watch a movie \n2. watch tv\n3.watch youtube"))
    decision3_3(user_response)
    
def decision3_3(user_response):
  print("This would be the story continuing after the user's third response")
  if user_response == 1:
    print("User selected 1. What do you do next?")
    user_response = int(input("1.go wipe your face\n2.continue crying\n3.im tired of the storyry end"))
    decision3_1(user_response)
  elif user_response == 2:
    print("User selected 2. What do you do next?")
    user_response = int(input("1.\n2.option two\n3.end story"))
    decision3_2(user_response)
  elif user_response == 3:
    print("User selected 3. What do you do next?")
    user_response = int(input("1.option one\n2.option two\n3.end story now "))
    decision3_3(user_response)
	
#This runs the game
user_name = input("Enter your name")
begin_story()
