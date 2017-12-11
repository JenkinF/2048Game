import random
import pyHook
import pythoncom
import sys


class Game(object):
    def __init__(self, xnum=4, ynum=4):
        self.xnum = xnum
        self.ynum = ynum
        # 分数
        self.score = 0
        # 创建棋盘
        self.data = [[0 for j in range(0, xnum)] for i in range(0, ynum)]
        # 回合数
        self.round = 0
        # 每回合出现的随机数字列表
        self.randNumber = [2, 4]
        # 每回合出现的随机数字
        self.thisData = 0
        # 判断棋盘是否还有‘有效移动’
        self.flag = True
        # 是否能移动
        self.ismoved = True

    # 转置棋盘
    def trans(self):
        self.data = [[row[i] for row in self.data] for i in range(self.xnum)]

    # 刷新棋盘
    def refreshboard(self):
        # 判断能否移动
        if self.ismoved == False and self.round > 0:
            return 0
        
        # 生成随机数
        self.thisData = random.choice(self.randNumber)
        # 存放0的坐标
        zero = []

        # 每次棋盘刷新，默认没有有效移动（后面判断）
        self.flag = False

        # 把0的位置存储下来(顺便判断是否赢了)
        for i in range(self.xnum):
            for j in range(self.ynum):
                # 判断是否胜利
                if self.data[i][j] == 2048:
                    print("恭喜你，赢了")
                    sys.exit(0)
                # 判断是否还有‘有效移动’
                if i < self.xnum - 1 and j < self.xnum - 1:
                    if self.data[i][j] == self.data[i][j + 1] or self.data[i][j] == self.data[i + 1][j]:
                        self.flag = True
                # 存储0的坐标
                if self.data[i][j] == 0:
                    zero.append((i, j))

        # 如果没有0并且没有'有效移动'则gameover
        if len(zero) == 0:
            if not self.flag:
                print("很遗憾，你输了")
                sys.exit(0)
        elif len(zero) != 0:
            # 从zero中随机选出一个坐标，该坐标对应的值为thisData
            ranC = random.choice(zero)
            self.data[ranC[0]][ranC[1]] = self.thisData
        # 输出矩阵
        self.round += 1
        print("===========回合数：" + str(self.round) + "============")
        for i in self.data:
            for j in i:
                print(j, end="\t")
            print("\n")
        print("===========分数：" + str(self.score) + "============")

    # 对齐
    def align(self, listdata, dir):
        count = listdata.count(0)
        # 清除所有0节点
        for i in range(count):
            listdata.remove(0)
        if dir == "left":
            # 末尾补0
            for i in range(count):
                listdata.append(0)
        elif dir == "right":
            for i in range(count):
                listdata.insert(0, 0)

    # 向左加
    def addtoleft(self):
        self.ismoved = False
        for list in self.data:
            for j in range(self.ynum - 1):
                for m in range(j + 1, self.ynum):
                    if list[j] == list[m] != 0:
                        list[j] *= 2
                        list[m] = 0
                        self.score += list[j]
                        self.ismoved = True
                        break
                    elif list[j] == 0 and list[m] != 0:
                        self.ismoved = True
                        break
                    elif list[m] != 0 or list[j] == 0:
                        break
            self.align(list, "left")

    # 向右加
    def addtoright(self):
        self.ismoved = False
        for list in self.data:
            for j in range(self.ynum - 1, 0, -1):
                for m in range(j - 1, -1, -1):
                    if list[j] == list[m] != 0:
                        list[j] *= 2
                        list[m] = 0
                        self.score += list[j]
                        self.ismoved = True
                        break
                    elif list[j] == 0 and list[m] != 0:
                        self.ismoved = True
                        break
                    elif list[m] != 0 or list[j] == 0:
                        break
            self.align(list, "right")

    # 按键监听
    def onKeyboardEvent(self, event):

        key = event.Key

        if key == "Up":
            self.trans()
            self.addtoleft()
            self.trans()
            self.refreshboard()

        elif key == "Left":
            self.addtoleft()
            self.refreshboard()

        elif key == "Right":
            self.addtoright()
            self.refreshboard()

        elif key == "Down":
            self.trans()
            self.addtoright()
            self.trans()
            self.refreshboard()

        return True

if __name__ == "__main__":

    g = Game()
    g.refreshboard()

    # 创建一个“钩子”管理对象
    hm = pyHook.HookManager()
    # 监听所有键盘事件
    hm.KeyDown = g.onKeyboardEvent
    # 设置键盘“钩子”
    hm.HookKeyboard()
    # 进入循环
    pythoncom.PumpMessages()
