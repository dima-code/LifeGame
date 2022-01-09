
from settings import *
import random

# Основной класс
class Field:

    # Заполнение поля случайными значениями 
    def field_fill(self):

        for i in self:
            for j in range(width):
                if j == 0 or j == width-1:
                    i.append(8)
                else:
                    y = random.randint(0,1)
                    if y == 1:
                        i.append('*')
                    else:
                        i.append(' ')

        for i in range(len(self[0])):
            self[0][i] = 8

        for i in range(width):
            self[height-1][i] = 8
        return self

     
    # Подсчёт количество соседей у каждой клетки и обновление поля
    def neighbours_amount(self):
        N = []
        rez = []
        for i in range(height):
            N.append([])
        for i in range(height):
            for j in range(width):
                n = 0
                if self[i][j] == 8:
                    rez.append(8)
                else: 
                    # Подсчет количества соседей
                    if self[i][j+1] == '*':
                        n += 1
                    if self[i+1][j+1] == '*':
                        n += 1
                    if self[i+1][j] == '*':
                        n += 1
                    if self[i+1][j-1] == '*':
                        n += 1
                    if self[i][j-1] == '*':
                        n += 1
                    if self[i-1][j-1] == '*':
                        n += 1
                    if self[i-1][j] == '*':
                        n += 1
                    if self[i-1][j+1] == '*':
                        n += 1            

                    # Присвоение обновленного значения
                    if self[i][j] == '*' and (n == 3 or n == 2):
                        rez.append('*')

                    if self[i][j] == ' ' and n == 3:
                        rez.append('*')

                    if self[i][j] == '*' and (n < 2 or n > 3):
                        rez.append(' ')

                    if not(self[i][j] == '*' and (n == 3 or n == 2)) and not(self[i][j] == ' ' and n == 3) and not(self[i][j] == '*' and (n < 2 or n > 3)):
                        rez.append(self[i][j])


        for i in range(len(rez)):
            N[i//width].append(rez[i])


        for i in range(width):
            N[0][i] = 8

        for i in range(width):
            N[height-1][i] = 8

        return N