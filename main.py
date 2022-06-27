import puzzle
from tkinter import *

def Init():
    def work(b, path):
        if len(path) == (b.st + 1):
            dex["state"] = DISABLED
            dex["text"] = "DONE"
            fex["state"] = DISABLED
            fex["text"] = "DONE"
        if path[b.st] == 1:
            b.state[b.x * 3 + b.y], b.state[(b.x - 1) * 3 + b.y] = b.state[(b.x - 1) * 3 + b.y], b.state[b.x * 3 + b.y]
            b.x -= 1
        if path[b.st] == 2:
            b.state[b.x * 3 + b.y], b.state[(b.x + 1) * 3 + b.y] = b.state[(b.x + 1) * 3 + b.y], b.state[b.x * 3 + b.y]
            b.x += 1
        if path[b.st] == 3:
            b.state[b.x * 3 + b.y], b.state[b.x * 3 + b.y - 1] = b.state[b.x * 3 + b.y - 1], b.state[b.x * 3 + b.y]
            b.y -= 1
        if path[b.st] == 4:
            b.state[b.x * 3 + b.y], b.state[b.x * 3 + b.y + 1] = b.state[b.x * 3 + b.y + 1], b.state[b.x * 3 + b.y]
            b.y += 1
        puzzle1.config(text=bd.state[0])
        puzzle2.config(text=bd.state[1])
        puzzle3.config(text=bd.state[2])
        puzzle4.config(text=bd.state[3])
        puzzle5.config(text=bd.state[4])
        puzzle6.config(text=bd.state[5])
        puzzle7.config(text=bd.state[6])
        puzzle8.config(text=bd.state[7])
        puzzle9.config(text=bd.state[8])
        b.st += 1

    def work_f(b, path):
        while True:
            if len(path) < (b.st + 1):
                dex["state"] = DISABLED
                dex["text"] = "DONE"
                fex["state"] = DISABLED
                fex["text"] = "DONE"
                break
            if path[b.st] == 1:
                b.state[b.x * 3 + b.y], b.state[(b.x - 1) * 3 + b.y] = b.state[(b.x - 1) * 3 + b.y], b.state[b.x * 3 + b.y]
                b.x -= 1
            if path[b.st] == 2:
                b.state[b.x * 3 + b.y], b.state[(b.x + 1) * 3 + b.y] = b.state[(b.x + 1) * 3 + b.y], b.state[b.x * 3 + b.y]
                b.x += 1
            if path[b.st] == 3:
                b.state[b.x * 3 + b.y], b.state[b.x * 3 + b.y - 1] = b.state[b.x * 3 + b.y - 1], b.state[b.x * 3 + b.y]
                b.y -= 1
            if path[b.st] == 4:
                b.state[b.x * 3 + b.y], b.state[b.x * 3 + b.y + 1] = b.state[b.x * 3 + b.y + 1], b.state[b.x * 3 + b.y]
                b.y += 1
            puzzle1.config(text=bd.state[0])
            puzzle2.config(text=bd.state[1])
            puzzle3.config(text=bd.state[2])
            puzzle4.config(text=bd.state[3])
            puzzle5.config(text=bd.state[4])
            puzzle6.config(text=bd.state[5])
            puzzle7.config(text=bd.state[6])
            puzzle8.config(text=bd.state[7])
            puzzle9.config(text=bd.state[8])
            b.st += 1
            window.after(200)
            window.update()

    def dest():
        window.destroy()
        Init()

    window = Tk()
    window.title("8-Puzzle-Game")
    window.geometry("720x360+0+0")
    window.resizable(False,False)
    window.configure(background="RoyalBlue4")
    title = Label(window, text="8-Puzzle-Game", font=("Tahoma", 20), pady=18, bg="RoyalBlue4", fg="deep sky blue")
    title.pack()
    frm = Frame(window)
    frm.pack()
    board = puzzle.Board()
    board.set()
    pt = Path(board)
    bd = puzzle.Board(board)
    dex = Button(window, width=12, height=2, text="Run One-Step", command=lambda: work(bd, pt))
    dex.place(x=260, y=300)
    fex = Button(window, width=12, height=2, text="Run ALL", command=lambda: work_f(bd, pt))
    fex.place(x=370, y=300)
    rex = Button(window, width=14, height=2, text="RESET", command=lambda: dest())
    rex.place(x=550, y=240)
    puzzle1 = Label(frm, text=board.state[0], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle2 = Label(frm, text=board.state[1], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle3 = Label(frm, text=board.state[2], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle4 = Label(frm, text=board.state[3], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle5 = Label(frm, text=board.state[4], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle6 = Label(frm, text=board.state[5], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle7 = Label(frm, text=board.state[6], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle8 = Label(frm, text=board.state[7], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle9 = Label(frm, text=board.state[8], width=4, height=2, fg="RoyalBlue2", relief="solid", bd=1, font=("Tahoma", 20))
    puzzle1.grid(row=0, column=0)
    puzzle2.grid(row=0, column=1)
    puzzle3.grid(row=0, column=2)
    puzzle4.grid(row=1, column=0)
    puzzle5.grid(row=1, column=1)
    puzzle6.grid(row=1, column=2)
    puzzle7.grid(row=2, column=0)
    puzzle8.grid(row=2, column=1)
    puzzle9.grid(row=2, column=2)
    window.mainloop()


def Path(board):
    resultList = []
    closedList = []
    openList = puzzle.Storage()
    openList.push(board)
    while True:
        temp = openList.list.pop()
        temp.check()
        if temp.heuristic - temp.moveCount == 0:
            resultList = temp.path[:]
            break
        check = 0
        for i in range(len(closedList)):
            if closedList[i] == temp.state:
                check = 1
                break
        if check == 1:
            continue
        if temp.x > 0:
            c = puzzle.Board(temp)
            c.state[c.x * 3 + c.y], c.state[(c.x - 1) * 3 + c.y] = c.state[(c.x - 1) * 3 + c.y], c.state[c.x * 3 + c.y]
            c.x -= 1
            c.check()
            c.moveCount += 1
            c.path.append(1)
            openList.push(c)
        if temp.x < 2:
            c = puzzle.Board(temp)
            c.state[c.x * 3 + c.y], c.state[(c.x + 1) * 3 + c.y] = c.state[(c.x + 1) * 3 + c.y], c.state[c.x * 3 + c.y]
            c.x += 1
            c.check()
            c.moveCount += 1
            c.path.append(2)
            openList.push(c)
        if temp.y > 0:
            c = puzzle.Board(temp)
            c.state[c.x * 3 + c.y], c.state[c.x * 3 + c.y - 1] = c.state[c.x * 3 + c.y - 1], c.state[c.x * 3 + c.y]
            c.y -= 1
            c.check()
            c.moveCount += 1
            c.path.append(3)
            openList.push(c)
        if temp.y < 2:
            c = puzzle.Board(temp)
            c.state[c.x * 3 + c.y], c.state[c.x * 3 + c.y + 1] = c.state[c.x * 3 + c.y + 1], c.state[c.x * 3 + c.y]
            c.y += 1
            c.check()
            c.moveCount += 1
            c.path.append(4)
            openList.push(c)
        closedList.append(temp.state)
    return resultList


if __name__ == '__main__':
    Init()