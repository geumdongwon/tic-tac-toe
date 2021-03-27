class game:
    def __init__(self):
        self.pA = []
        self.pB = []

    def draw_map(self):
        m = [["*"] *3 for j in range(3)]

        for a_pos in self.pA:
            m[a_pos[0]][a_pos[1]] = "O"

        for b_pos in self.pB:
            m[b_pos[0]][b_pos[1]] = "X"

        for i in range(3):
            for j in range(3):
                print(m[i][j], end=' ')
            print()

    def custom_input(self,str="playerA: "):
        flag =True
        while flag:

            a = list(map(int, input(str).split()))
            if len(a) !=2:
                flag = True
                continue
            if a[0]<0 or a[0]>2:
                flag = True
                continue
            if a[1]<0 or a[1]>2:
                flag =True
                continue

            flag = False

        return a

    def p1(self):
        A = self.custom_input()
        while (A[0], A[1]) in self.pA or (A[0],A[1]) in self.pB:
            A = self.custom_input()
        self.pA.append((A[0], A[1]))


    def p2(self):
        B = self.custom_input(str="playerB: ")
        while (B[0], B[1]) in self.pA or (B[0],B[1]) in self.pB:
            B = self.custom_input(str="playerB: ")
        self.pB.append((B[0], B[1]))

    def win(self):
        for i in range(3):
            if (i,0) in self.pA and (i,1) in self.pA and (i,2) in self.pA:
                print("Player A win!")
                return 0
                break
            elif (0,i) in self.pA and (1,i) in self.pA and (2,i) in self.pA:
                print("Player A win!")
                return 0
                break
        for j in range(3):
            if (j,0) in self.pB and (j,1) in self.pB and (j,2) in self.pB:
                print("Player B win!")
                return 0
                break
            elif (0,j) in self.pB and (1,j) in self.pB and (2,j) in self.pB:
                print("Player B win!")
                return 0
                break
        if (0,0) in self.pA and (1,1) in self.pA and (2,2) in self.pA:
            print("Player A win!")
            return 0
        elif (0,0) in self.pB and (1,1) in self.pB and (2,2) in self.pB:
            print("Player B win!")
            return 0
        elif (2,0) in self.pA and (1,1) in self.pA and (0,2) in self.pA:
            print("Player A win!")
            return 0
        elif (2,0) in self.pB and (1,1) in self.pB and (0,2) in self.pB:
            print("Player B win!")
            return 0
        else:
            return 1
a = game()
m = [["*" for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        print(m[i][j], end=' ')
    print()
flag=1
while flag:
    a.p1()
    a.draw_map()
    flag = a.win()
    if flag==0:
        break
    a.p2()
    a.draw_map()
    flag = a.win()
    if len(a.pA)==4 and len(a.pB)==4:
        print("draw")
        break




