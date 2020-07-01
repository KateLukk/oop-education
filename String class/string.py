class String:
    def __init__(self, list):
        self.list = list

    def length(self): # длина строки
        return len(self.list)

    def concat(self, stroka): # конкатенация
        for i in stroka:
            self.list.append(i)

    def double(self, integer): # многократное дублирование
        d = ''
        for i in range(len(self.list)):
                d += self.list[i]
                d += '.'
        d *= integer
        d = d[:len(d) - 1]
        return d.split('.')

    def f(self, elem): # поиск слева
        for i in range(len(self.list)):
            if self.list[i] == elem:
                return i
        return -1

    def rf(self, elem): # поиск справа
        t = -1
        for i in range(len(self.list)):
            if self.list[i] == elem:
                t = i
        return t

    def is_slovo(self, elem): # есть ли слово в строке
        d = ''
        for i in self.list:
            d += i
        if elem in d:
            return True
        return False

    def big(self): # символ в прописную букву
        ans = []
        for i in self.list:
            if 97 <= ord(i) <= 122:
                ans.append(chr(ord(i) - 32))
            else:
                ans.append(i)
        return ans

    def small(self): # символ в строчную букву
        ans = []
        for i in self.list:
            if 65 <= ord(i) <= 90:
                ans.append(chr(ord(i) + 32))
            else:
                ans.append(i)
        return ans

    def space(self):
        d = []
        for i in self.list:
            if i != ' ' and i != '':
                d.append(i)
        return d

    def is_empty(self):
        if self.length() == 0:
            return True
        d = ''
        for i in self.list:
            d += i
        for i in d:
            if i != ' ':
                return False
        return True


# string_object = String(['d', 'd', 'a', 'c', 's'])
# print(string_object.big())



