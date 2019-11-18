
repeat = True
while repeat:
  dice = 0
  dice = int(input("How many dice do you want to roll? ""\n"))
  print("\nThanks! You picked: ", dice," dice.""\n""\nWhat kind of dice do you want to roll?""\n""\n(04)FOUR SIDED""\n(06)SIX SIDED""\n(08)EIGHT SIDED""\n(10)TEN SIDED""\n(12)TWELVE SIDED""\n(20)TWENTY SIDED""\n")

  diceSides = int(input("Choose which type of dice by typing the number of sides \nand hitting enter.""\n"))

  print("\nYou chose to roll, ", dice,"D", diceSides,"\n""\n!!!ROLLING!!!""\n")

  from random import randint

  diceRolls = 0

  while diceRolls < dice:
    print("YOU ROLLED: ", randint(1,diceSides))
    diceRolls += 1

  print("\nThanks for rolling!")
  print("\nDo you want to roll again?")
  repeat = ("y" or "yes") in input().lower()



  
