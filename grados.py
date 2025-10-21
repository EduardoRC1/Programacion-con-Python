# Determina si un estudiante ha aprobado o reprobado basado en su calificación
grade = 65
# Verifica si la calificación es mayor o igual a 55
if grade >= 55:
  # El estudiante ha aprobado
  print('You passed.')
  # Muestra la calificación obtenida
  print('Your grade is:', grade)
elif grade < 55:
  # El estudiante ha reprobado
  print('You failed.')