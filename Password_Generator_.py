# Password Generator, Developed by Om Jaiswal

print("  Password Generator, By Om Jaiswal")
import secrets
import random

#               ----------Values----------
  
lowchars = "qwertyuiopasdfghjklzxcvbnm"

upchars= "QWERTYUIOPASDFGHJKLZXCVBNM"

digits = "1234567890"
  
symbols = "@#$%&!*-_?^"

letter = lowchars + upchars
 
while True:
  
  password = []
  
  # -----ask for special character-----
  
  choice = input("\n Do you need Special Characters in Your Password? (Yes or No)? \n    ").lower().strip()
  
  #-----Conditions for choice input-----
  
  if choice in["yes","ya","y","ok","ye","ys","ha"]:
    
    password.append(secrets.choice(symbols))
    pool = digits + letter + symbols
    
  elif choice in["no","not","na","n","nhi","nahi"]:
      pool = digits + letter 
      
  elif choice =="":
      print(" You have Entered Nothing, Please try again ")
      continue
      
  else:
     print(choice," Invalid Input, Please Try again in (Yes or No) \n ------Restarting the programme------")
     continue
     
  #-----protect lenght input from crashing tha programme-----
  
  try:
      
      length =int(input("\n Enter Password length:>> "))
      
      if length <= 0:
          print("Not Possible to Generate Password in length equal or less than '0' \n ------Try Again------")
          continue        
          
  except:
      
      print("Invalid Input, Please Enter only Numbers")
      continue
     
# ----- Password Processing-----
  
  password.append(secrets.choice(upchars))
  password.append(secrets.choice(digits))
  
  if length < len(password):
    print("Length too small. Minimum length required:", len(password))
    continue
  
  remaining = length - len(password)

  for i in range(remaining):
      password.append(secrets.choice(pool))
      
  random.shuffle(password)
   
  final_password = "".join(password)
  has_lower = False
  has_upper = False
  has_digit = False
  has_symbol = False
  
  print(f"\n Generated {length} character password: {final_password}")
  #------ Strength testing ------
  
  for ch in final_password:
      
    if ch.islower():
        has_lower = True

    elif ch.isupper():
        has_upper = True

    elif ch.isdigit():
        has_digit = True

    elif ch in symbols:
        has_symbol = True
      
  score= 0
  
  if has_lower:
        score+=1
      
  if has_upper:
        score+=1
      
  if has_digit:
        score+=1
      
  if has_symbol:
        score+=1
      
  if score == 4:
      print("Strength Level: Strong Password")
      
  elif score == 3:
      print("Strength Level: Medium Password")
      
  else:
      print("Strength Level: Weak Password")
      
  
 # -----Ask for Closing Programme -----
 
  close= input("\n -----Do You Want to Generate again?(Yes or No)?>>> ")
  
  if close.lower().strip() =="yes":
    print("-------Restarting the Programme-------")
    
    continue
  
  elif close.strip().lower() =="no":
        print("\n------Closing the Programme------")
        
        break
      
  elif close.strip() == "":
      print("you have Entered Nothing,\n-----Closing Programme-----")
      
      break
      
  else:
      print("You have Entered Invalid Option but,\n------Restarting the Programme------")
      continue