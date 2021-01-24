import turtle
import tkinter as tk
import random as rand
from tkinter import ttk

class StartGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Choose a difficulty")
        self.root.geometry("300x200")

        self.frame = ttk.Frame(self.root, padding = "10 10 10 10")
        self.frame.pack(fill=tk.BOTH, expand = True)

        easyButton = ttk.Button(self.frame, text="Easy", command=self.clickEasy)
        lessEasyButton = ttk.Button(self.frame, text="Less Easy", command=self.clickLessEasy)
        hardButton = ttk.Button(self.frame, text="Hard", command=self.clickHard)

        easyButton.pack()
        lessEasyButton.pack()
        hardButton.pack()

        self.root.mainloop()

    def clickEasy(self):
        self.root.destroy()
        Game(1)


    def clickLessEasy(self):
        self.root.destroy()
        Game(2)


    def clickHard(self):
        self.root.destroy()
        Game(3)


class Pen(turtle.Turtle):
    def __init__(self, wallImage):
        turtle.Turtle.__init__(self)
        self.shape(wallImage)
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self, playerImage):
        turtle.Turtle.__init__(self)
        self.shape(playerImage)
        self.penup()
        self.speed(0)

    def go_up (self):
        self.goto(self.xcor(), self.ycor() + 24)

    def go_down (self):
        self.goto(self.xcor(), self.ycor() - 24)

    def go_left (self):
        self.goto(self.xcor() - 24, self.ycor())

    def go_right (self):
        self.goto(self.xcor() + 24, self.ycor())


class Monster(turtle.Turtle):
    def __init__(self, monsterImage):
        turtle.Turtle.__init__(self)
        self.shape(monsterImage)
        self.penup()
        self.speed(0)

    def move(self,moveRandom):
        if moveRandom == 1:
            self.goto(self.xcor(), self.ycor() + 24)
        elif moveRandom == 2:
            self.goto(self.xcor(), self.ycor() - 24)
        elif moveRandom == 3:
            self.goto(self.xcor() - 24, self.ycor())
        elif moveRandom == 4:
            self.goto(self.xcor() + 24, self.ycor())

class door(turtle.Turtle):
    def __init__(self,doorImage):
        turtle.Turtle.__init__(self)
        self.shape(doorImage)
        self.penup()
        self.speed(0)

class Game:
    def __init__(self, difficulty):

        self.levels = [""]

        self.level3 = [
                "xxxxxxxxxxxxxxxxxxxxxxxxx",
                "xxxPxxxx       xxx    D x",
                "xxx xxxx xxx xxxx      xx",
                "xxx xxxxx xxxxxxxx    xxx",
                "xxx xxxxx    M         xx",
                "xx   xxxx xxx     xxxxxxx",
                "xxx xxxxx xxx    xxxxxxxx",
                "xxx xxxxx   M  xxxxxxxxxx",
                "xxx   M           xxxxxxx",
                "xxxxxxxxxxxxxxxxxxxxxxxxx"]

        self.level2 = [
                "xxxxxxxxxxxxxxxxxxxxxxxxx",
                "xxxP xxx       xxxxxx   x",
                "xxx  xxx     xxxxxx    xx",
                "xxx  xxxx xxxxxxxxxxx xxx",
                "xxx  xxxx    M         xx",
                "xx   xxxx xxx     xxxxxxx",
                "xxx xxxxx xxx    xxxxxxxx",
                "xxx xxxxx   M  xxxxxxxxxx",
                "xxx                    xx",
                "xxxx xxxxxx xxxxxxxx    x",
                "xxxx   xxxx xxxxxxxx  xxx",
                "xxxx xxxx       xxxx  xxx",
                "xxxx xxxx       xxx  xxxx",
                "xxx                 xxxxx",
                "xxxx xxxxxx xxx    Dxxxxx",
                "xxxxxxxxxxxxxxxxxxxxxxxxx"
                ]

        self.level1 = [
                "xxxxxxxxxxxxxxxxxxxxxxxxx",
                "xxxP xxx       xxxxxx   x",
                "xxx  xxx     xxxxxx    xx",
                "xxx  xxxx xxxxxxxxxxx xxx",
                "xxx  xxxx    M         xx",
                "xx   xxxx xxx     xxxxxxx",
                "xxx xxxxx xxx    xxxxxxxx",
                "xxx xxxxx   M  xxxxxxxxxx",
                "xxx                    xx",
                "xxxx xxxxxx xxxxxxxx    x",
                "xxxx xxxxxx xxxxxxxx  xxx",
                "xxxx xxxx       xxxx  xxx",
                "xxxx xxxx       xxx  xxxx",
                "xxx    xxxx xxxxxx xxxxxx",
                "xxxx xxxxxx xxxxx  xxxxxx",
                "xxxx        xxxx   xxxxxx",
                "xxxx    xxx       xxxxxxx",
                "xxxx  xxxxx     xxxxxxxxx",
                "xxx    xxxxxxx       xxxx",
                "xxxx xxxxx  xxx    xxxxxx",
                "xxxx    xxx xxxx  xxxxxxx",
                "xxxxx          M   xxxxxx",
                "xxxx      M         xxxxx",
                "xx     xxx    xxxx   D xx",
                "xxxxxxxxxxxxxxxxxxxxxxxxx",
                ]

        self.playerImage = "warrior.gif"
        self.wallImage = "wall.gif"
        self.background = "stonefloor.gif"
        self.monsterImage = "monster.gif"
        self.doorImage = "door.gif"
        self.win = "win.gif"
        self.lose = "lose.gif"

        turtle.register_shape(self.playerImage)
        turtle.register_shape(self.wallImage)
        turtle.register_shape(self.monsterImage)
        turtle.register_shape(self.doorImage)
        turtle.register_shape(self.win)
        turtle.register_shape(self.lose)

        self.levels.append(self.level1)
        self.levels.append(self.level2)
        self.levels.append(self.level3)

        self.pen = Pen(self.wallImage)
        self.player = Player(self.playerImage)
        self.door = door(self.doorImage)
        self.monsters = []
        self.walls = []
        self.difficulty = difficulty

        self.setUpMaze(self.levels, self.difficulty)


        turtle.listen()
        turtle.onkey(self.moveLeft, "Left")
        turtle.onkey(self.moveRight, "Right")
        turtle.onkey(self.moveUp, "Up")
        turtle.onkey(self.moveDown, "Down")


    def testCollision(self, x, y):
        test = False
        if x == self.door.xcor() and y == self.door.ycor():
            turtle.shape(self.win)
            turtle.stamp()
            self.penup()
            self.speed(0)
        elif (x, y) not in self.walls:
            test = True

        for self.monster in self.monsters:
            if x == self.monster.xcor() and y == self.monster.ycor():
                turtle.shape(self.lose)
                turtle.stamp()
                self.penup()
                self.speed(0)
                test = False

        return test

    def moveLeft(self):
        x = self.player.xcor() - 24
        y = self.player.ycor()
        if self.testCollision(x, y):
            self.player.go_left()


        self.moveMonsters()

    def moveRight(self):
        x = self.player.xcor() + 24
        y = self.player.ycor()
        if self.testCollision(x, y):
            self.player.go_right()
        self.moveMonsters()

    def moveUp(self):
        x = self.player.xcor()
        y = self.player.ycor() + 24
        if self.testCollision(x, y):
            self.player.go_up()
        self.moveMonsters()

    def moveDown(self):
        x = self.player.xcor()
        y = self.player.ycor() - 24
        if self.testCollision(x, y):
            self.player.go_down()
        self.moveMonsters()

    def moveMonsters(self):
        for self.monster in self.monsters:
            choiceMove = rand.randint(0,4)
            self.monster.move(choiceMove)


    def setUpMaze(self, levels, difficulty):
        turtle.hideturtle()
        self.monster = 0

        if difficulty == 3:
            self.wn = turtle.Screen()
            self.wn.setup(600,700)
            self.wn.bgpic(self.background)
            self.wn.title("Maze: Hard")

        elif difficulty == 2:
            self.wn = turtle.Screen()
            self.wn.setup(700,700)
            self.wn.bgpic(self.background)
            self.wn.title("Maze: Less Easy")

        else:
            self.wn = turtle.Screen()
            self.wn.setup(700,700)
            self.wn.bgpic(self.background)
            self.wn.title("Maze: Easy")


        level = levels[difficulty]

        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]

                if difficulty == "3":
                    screenX = -288 + (x * 24)
                    screenY = 288 - (y * 24)
                elif difficulty == "2":
                    screenX = -288 + (x * 24)
                    screenY = 288 - (y * 24)
                else:
                    screenX = -288 + (x * 24)
                    screenY = 288 - (y * 24)

                if character == "x":
                    self.pen.goto(screenX, screenY)
                    self.pen.stamp()
                    self.walls.append((screenX,screenY))
                elif character == "P":
                    self.player.goto(screenX,screenY)
                elif character == "M":
                    self.monsters.append(Monster(self.monsterImage))
                    self.monsters[self.monster].goto(screenX,screenY)
                    self.monster += 1
                elif character == "D":
                    self.door.goto(screenX, screenY)



def main():

    StartGUI()

if __name__ == '__main__':
    main()
