
import time
from body import *



# Создание пустого массива
M = []
for i in range(height):
    M.append([])


# Первоначальное заполнение поля и его вывод 
M = Field.field_fill(M)

for i in M:
    print(" ".join(map(str, i)))


    # Вывод матрицы
while True:
    print('   ')
    print('   ')
    print('   ')
    print('   ')
    print('   ')
    M = Field.neighbours_amount(M)
    for i in M:
        print(" ".join(map(str, i)))
    time.sleep(0.1)
    if M == Field.neighbours_amount(M):
        break