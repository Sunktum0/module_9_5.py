class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.pointer >= self.stop) or (self.step < 0 and self.pointer <= self.stop):
            raise StopIteration

        current = self.pointer
        self.pointer += self.step
        return current


# Примеры использования
try:
    iter1 = Iterator(100, 200, 0)  # Изменили шаг на 2
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

print()

iter2 = Iterator(-5, 1)  # Ожидаемый вывод от -5 до 1
for i in iter2:
    print(i, end=' ')
print()

iter3 = Iterator(6, 15, 2)  # Ожидаемый вывод 6, 8, 10, 12, 14
for i in iter3:
    print(i, end=' ')
print()

iter4 = Iterator(5, 1, -1)  # Ожидаемый вывод 5, 4, 3, 2, 1
for i in iter4:
    print(i, end=' ')
print()

iter5 = Iterator(10, 1, -1)  # Ожидаемый вывод 10, 9, 8, 7, 6, 5, 4, 3, 2
for i in iter5:
    print(i, end=' ')
print()