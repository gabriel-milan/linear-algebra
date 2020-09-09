print ("#"*30)
print ("# Lista 1 - COC473")
print ("# Gabriel Gazola Milan")
print ("# 2020/PLE")
print ("#"*30)
print ()

for exercise in ['2a', '2b', '2c', '3', '5', '6']:
  print ("#" * 20)
  print ("# Exercício {}".format(exercise.upper()))
  exec ("import exercise{}".format(exercise))
print ("#" * 20)