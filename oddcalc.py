firstnumber =  float(input("Give me a number,any number..."))
secondnumber = float(input("Wonderful,and give me another number..."))
operation = input("And what operation do you want? (mul, div, or mod)")
if (operation == "mul"):
  print (firstnumber * secondnumber)
elif (operation == "div") :
  print (firstnumber/secondnumber)
elif (operation == "mod"):
  print(firstnumber % secondnumber)
else:
  print("**** INVALID OPERATION!!!!****")
