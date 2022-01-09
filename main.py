import random

##### Создание изначального массива с рамкой
width = 80
M = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
V = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
rez = []
# Основной класс
class Field:

    # Заполнение поля случайными значениями 
    def field_fill(self):
        
        for i in self:
            for j in range(width):
                if j == 0 or j == 79:
                    i.append(8)
                else:
                    i.append(random.randint(0,1))

        for i in range(len(self[0])):
            self[0][i] = 8

        for i in range(len(self[24])):
            self[24][i] = 8
        return self

     
    # Подсчёт количество соседей у каждой клетки и обновление поля
    def neighbours_amount(self):

        N = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        rez = []
        for i in range(25):
            for j in range(80):
                n = 0
                if self[i][j] == 8:
                    rez.append(8)
                else: 
                    # Подсчет количества соседей
                    if self[i][j+1] == 1:
                        n += 1
                    if self[i+1][j+1] == 1:
                        n += 1
                    if self[i+1][j] == 1:
                        n += 1
                    if self[i+1][j-1] == 1:
                        n += 1
                    if self[i][j-1] == 1:
                        n += 1
                    if self[i-1][j-1] == 1:
                        n += 1
                    if self[i-1][j] == 1:
                        n += 1
                    if self[i-1][j+1] == 1:
                        n += 1                  
                    
                    # Присвоение обновленной ячейки 
                    if self[i][j] == 1 and (n == 3 or n == 2):
                        rez.append(1)

                    if self[i][j] == 0 and n == 3:
                        rez.append(1)

                    if self[i][j] == 1 and (n < 2 or n > 3):
                        rez.append(0)

                    if not(self[i][j] == 1 and (n == 3 or n == 2)) and not(self[i][j] == 0 and n == 3) and not(self[i][j] == 1 and (n < 2 or n > 3)):
                        rez.append(self[i][j])


        for i in range(len(rez)):
            N[i//80].append(rez[i])


        for i in range(len(N[0])):
            N[0][i] = 8

        for i in range(len(N[24])):
            N[24][i] = 8

        return N



# Первоначальное заполнение поля и его вывод
M = Field.field_fill(M)

for i in M:
    print(" ".join(map(str, i)))



# Вывод матриц
while True:
    M = Field.neighbours_amount(M)
    for i in M:
        print(" ".join(map(str, i)))
    print('   ')
    print('   ')
    print('   ')
    print('   ')
    print('   ')




