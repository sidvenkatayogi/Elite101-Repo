import random


yesList = ["yes", "yeah", "yea", "sure", "of course", "y"]
responses = ["Of course!","Not really.","I dont know.","How could you!?!?!?!?!?","Yes.", "No.","Yes.", "Maybe.", "It's possible.", "No way.", "Soon."] #list from a prework example

#greeting
name = input("What's your name? ")
print(f"Hello {name}, I'm Chatbot. Nice to meet you!")

#mood
def moodAns(mood):
  goodMood = ["happy","delighted" , "great" , "okay" ,"good" , "well" , "nice"] #list from a prework example
  badMood = ["sad","down","depressed", "unwell","unhappy" ,"bad"] #list from a prework example
  if mood in goodMood:
    print("Great!")
  elif mood in badMood:
    print("I'm sorry to hear that.")
  else:
    print("Alright.")
    
    
myMood = input("\nHow are you feeling? ").lower()
moodAns(myMood)

#hobby
myHobby = input("\nWhat do like to do in your free time? ")
print("Cool! I'm really into competitive duck herding.") 

#place
place = input("\nWhere are you from? ").capitalize()
print(f"I think I have a friend from {place}!")
print("Just kidding, I'm a computer program.")

#age
def ageAns(age):
  if age < 3:
    print("How are you typing this!?")
  elif age < 14:
    print("Wow, you're really young.")
  elif age < 20:
    print("A teenager! Interesting...")
  elif age < 55:
    #job
    employed = input("Do you have a job?")
    if employed in  yesList:
      job = input ("Well, what do you work as? ")
      print("Interesting!")
  elif age < 120:
    print(f"I don't have camera access, but you probably don't look a day over {age-10}!")
  else:
    print("I doubt that...")

ageInt = False
while ageInt != True:
  try:
    myAge = int(input("\nHow old are you? "))
    ageAns(myAge)
    ageInt = True
  except:
    print("Just type in a integer...")

print("\nNow it's time for you to ask the questions!")
question = input("Fire Away! (enter q to end) ")
print(random.choice(responses))
while question != "q":
  question = input("Question? ")
  print("\n"+random.choice(responses))

print("\nBye!")