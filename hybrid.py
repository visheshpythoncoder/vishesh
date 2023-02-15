class A:
    def QofA(self):
        print("A")

class B(A):
    def QofB(self):
        print("B")

class C(A):
    def QofC(self):
        print("C")

class D(A):
    def QofD(self):
        print("D")

class E(B,C):
    def QofE(self):
        print("E")

class F(C,B):
    def QofF(self):
        print("F")

class G(F,D):
    def QofG(self):
        print("G")

class H(G):
    def QofH(self):
        print("H")
    
class I(G):
    def QofI(self):
        print("I")

class J(G):
    def QofJ(self):
        print("J")

raj = H()
raj.QofG()
raj.QofF()
raj.QofD()

