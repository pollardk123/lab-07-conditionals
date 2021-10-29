myVar = input("Does it move? (yes/no) ")
if myVar == "yes":
  myNextVar = input("Should it move? (yes/no) ")
  if myNextVar == "yes":
      print("no problem")
  elif myNextVar == "no":
      print("Duct tape")
  else:
      print("Answer my question! You didn't type yes or no.")
elif myVar == "no":
    myNextVar = input("Should it move? (yes/no) ")
    if myNextVar == "yes":
        print("WD40")
    elif myNextVar == "no":
        print("no problem")
else :
     print("Answer my question! You didn't type yes or no.")
