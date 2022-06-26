#Binary Tree projesi

class Node:
    def __init__(self,veri):
        self.liste = []
        self.maxDeger = 0
        self.minDeger = 100
        self.veri = veri
        self.sag = None
        self.sol = None
    def Ekle(self,veri):
        if self.veri > veri:
            if self.sol is None:
                self.sol = Node(veri)
            else:
                self.sol.Ekle(veri)
            self.liste.append(veri)
        elif veri > self.veri:
            if self.sag is None:
                self.sag = Node(veri)
            else:
                self.sag.Ekle(veri)
            self.liste.append(veri)
    def Goster(self):
        if self.sol:
            self.sol.Goster()
        print( self.veri)
        if self.sag:
            self.sag.Goster()
    def Max_deger(self):
        for i in self.liste:
            if i > self.maxDeger:
                self.maxDeger = i
        print(f'Ağaçtaki Maximum deger: {self.maxDeger}')
    def Min_deger(self):
        for i in self.liste:
            if i < self.minDeger:
                self.minDeger = i
        print(f'Ağactaki Minimum deger: {self.minDeger}')
print('******************')
print('Binary Tree: ')
node = Node(20)
node.Ekle(30)
node.Ekle(5)
node.Ekle(10)
node.Ekle(50)
node.Ekle(20)
node.Ekle(3)
node.Goster()
print('******************')
node.Max_deger()
node.Min_deger()