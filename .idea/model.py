# -*- coding: utf-8 -*-
__auther__ = 'Tillfore'

import random
class solve:
    def __init__(self):
        self.c2 = 0     #二连（直接二连或间隔一格）
        self.cc = 0     # 能够被消除的结构（二连且附近有同色）
        self.c3 = 0     # 三连
        self.c4 = 0     # 四连
        self.site = [[]]     # 矩阵

def gettype(i):
    if i < 13:
        return 1
    elif i < 26:
        return 2
    elif i < 39:
        return 3
    elif i < 52:
        return 4
    else:
        return 0

def makesite():
    mycards = random.sample(range(51), 16)
    print(mycards)
    i = 0
    x = 0
    site = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    while x <= 3:
        y = 0
        while y <= 3:
            site[x][y] = gettype(mycards[i])
            i += 1
            y += 1
        x += 1
    return site


def mulsolve(site):
    x = 0
    result = solve()
    while x <= 2: #从左下角2x2矩阵开始检索
        y = 0
        while y <= 2:
            # 根据2x3的六格矩阵判断cc和c3、c4
            if x + 2 > 3 :
                x += 0
            elif site[x][y] == (site[x + 1][y] or site[x + 1][y + 1]) \
                    and site[x][y] == (site[x + 2][y] or site[x + 2][y + 1]):
                result.cc += 1
                if site[x][y] == site[x + 1][y] == site[x + 2][y]:
                    result.cc -= 1
                    result.c3 += 1
                    if site[0][y] == site[1][y] == site[2][y] == site[3][y]:
                        result.c3 -= 1
                        result.c4 += 1
            # 判断1x4矩阵
            elif x == 0 and site[x][y] == site[x+3][y] and (site[x][y] == site[x+1][y] or site[x+2][y]):
                result.cc += 1
            # 根据3x2的六格矩阵判断
            if y + 2 > 3 :
                y += 0
            elif site[x][y] == (site[x][y + 1] or site[x + 1][y + 1]) \
                    and site[x][y] == (site[x][y + 2] or site[x + 1][y + 2]):
                result.cc += 1
                if site[x][y] == site[x][y + 1] == site[x][y + 2]:
                    result.cc -= 1
                    result.c3 += 1
                    if site[x][0] == site[x][1] == site[x][2] == site[x][3]:
                        result.c3 -= 1
                        result.c4 += 1
            # 判断4x1矩阵
            elif y == 0 and site[x][y] == site[x][y+3] and (site[x][y] == site[x][y+1] or site[x][y+2]):
                result.cc += 1
            y += 1
        x += 1
    while x >= 2: #从右上角2x2矩阵开始检索
        y = 3
        while y >= 2:
            # 根据2x3的六格矩阵判断cc和c3、c4
            if x - 3 < 0 :
                x += 0
            elif site[x][y] == (site[x - 1][y] or site[x - 1][y - 1]) \
                    and site[x][y] == (site[x - 2][y] or site[x - 2][y - 1]):
                result.cc += 1
                if site[x][y] == site[x - 1][y] == site[x - 2][y]:
                    result.cc -= 1
                    result.c3 += 1
                    if site[0][y] == site[1][y] == site[2][y] == site[3][y]:
                        result.c3 -= 1
                        result.c4 += 1
            # 判断1x4矩阵
            elif x == 3 and site[x][y] == site[x-3][y] and (site[x][y] == site[x-1][y] or site[x-2][y]):
                result.cc += 1
            # 根据3x2的六格矩阵判断
            if y - 2 < 0 :
                y += 0
            elif site[x][y] == (site[x][y - 1] or site[x - 1][y - 1]) \
                    and site[x][y] == (site[x][y - 2] or site[x - 1][y - 2]):
                result.cc += 1
                if site[x][y] == site[x][y - 1] == site[x][y - 2]:
                    result.cc -= 1
                    result.c3 += 1
                    if site[x][0] == site[x][1] == site[x][2] == site[x][3]:
                        result.c3 -= 1
                        result.c4 += 1
            # 判断4x1矩阵
            elif y == 3 and site[x][y] == site[x][y-3] and (site[x][y] == site[x][y-1] or site[x][y-2]):
                result.cc +=1
            y -= 1
        x -= 1
    result.site = site
    return result


if __name__=="__main__":
    while True :
        num = int(input("计算次数:\n"))
        i = 0
        totalcc = 0
        totalcombo = 0
        onlyccnum = 0
        combonum = 0
        deadnum = 0
        while i < num:
            i+=1
            print('\n(%d)'%i)
            result = mulsolve(makesite())
            print(result.site)
            print('可消除组合数：%d'%(result.cc))
            print('三连组合数：  %d'%(result.c3))
            print('四连组合数：  %d'%(result.c4))
            _combo = result.c3 + result.c4
            if _combo >= 1 :
                totalcombo += _combo
                combonum += 1
            elif result.cc >=1 :
                totalcc += result.cc
                onlyccnum += 1
            else :
                deadnum += 1
        if onlyccnum + combonum + deadnum == i :
            print('——'*20)
            normalnum = onlyccnum + deadnum
            pa = onlyccnum/i
            print('总局数：%d ; 有效初始版面数：%d (%f)；\n一般局数：%d (%f) ;死局数：%d (%f) ;动态局数：%d (%f);'\
                  %(i,normalnum,(normalnum/i),onlyccnum,pa,deadnum,(deadnum/i),combonum,(combonum/i)))
            #初始版面的场地交换活局概率
            print('Pa = %f'%(pa))
            #初始版面的活局总概率
            p = 1-(1-pa)*0.75
            print('P = %f'%(p))
            #玩家平均每回合消除机会数量（不包括五消以上）
            x = totalcc/onlyccnum
            print('X = %f'%(x))
        else :
            print('Error:总数计算不一致')