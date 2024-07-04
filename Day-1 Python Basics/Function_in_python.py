# PROG 3: Define Function
# Write the Assisted Practice Code Here
# Please ensure output as shown below

# def finale_score(score_1, score_2):
#   print(f"The finale score is {score_1 + score_2}")

# score_1 = 15
# score_2 = 15
# finale_score(score_1, score_2)

def add(x,y):
  return x + y

total_sum = 10
bonus_points = 20
finale_score = add(total_sum, bonus_points)

print(f"Finale Score is {finale_score}")


# PROG 4.1 Proper Function Usage
# Write the Assisted Practice Code Here
# Please ensure output as shown below
finale_score1 = 60  # Global variable

def finale_score():
  print(f"The finale score is {finale_score1}")

finale_score()

# PROG 4.2: Function Parameter Type Annotation
# Write the Assisted Practice Code Here
# Please ensure output as shown below
# def sum(a: int , b : int):
#   return a+b

# total : int = sum(5,6)
# print(f"The total is {total}")

def calculate_sum(x:int, y:int):
  """""
  Returns the sum of two numbers.
  """""

  return x + y

total_sum = 10
bonus_points = 20

print(f"Data type of total_sum is {type(total_sum)} and \n" +
      f"bonus_points is {type(bonus_points)}")
finale_score = calculate_sum(total_sum,bonus_points)

print(f"Finale Score is {finale_score}")
