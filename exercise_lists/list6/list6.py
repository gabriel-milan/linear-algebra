print ("#"*30)
print ("# Lista 6 - COC473")
print ("# Gabriel Gazola Milan")
print ("# 2020/PLE")
print ("#"*30)
print ()

for exercise in ['1', '2', '3']:
  print ("#" * 20)
  print ("# Exercício {}".format(exercise.upper()))
  exec ("import exercise{}".format(exercise))
print ("#" * 20)