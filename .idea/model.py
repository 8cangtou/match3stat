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
    while x <= 3: #从左下角矩阵开始检索
        y = 0
        while y <= 3:
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
    #补充检索 四个点
    #(3,3)
    if site[3][3] == site[2][2] == site[1][3] :
        result.cc += 1
    if site[3][3] == site[2][2] == site[3][1] :
        result.cc += 1
    #(2,3)
    if site[2][3] == site[1][2] == site[0][3] :
        result.cc += 1
    if site[2][3] == (site[2][2] or site[3][2]) == site[3][1] :
        result.cc += 1
    #(3,2)
    if site[3][2] == site[2][1] == site[3][0] :
        result.cc += 1
    if site[3][2] == (site[2][2] or site[2][3]) == site[1][3] :
        result.cc += 1
    #(2,2)
    if site[2][2] == site[3][1] == site[3][0] :
        result.cc += 1
    if site[2][2] == site[1][3] == site[0][3] :
        result.cc += 1
    result.site = site
    result.c4 /= 2
    return result


if __name__=="__main__":
    while True :
        num = int(input("计算次数:\n"))
        i = 0
        totalcc = 0
        totalcombo = 0
        onlyccnum = 0
        only2ccnum = 0  # 阻碍2次消除机会后的cc总数
        combonum = 0
        deadnum = 0
        c3 = 0
        c4 = 0
        while i < num:
            i+=1
            print('\n(%d)'%i)
            result = mulsolve(makesite())
            print(result.site)
            print('可消除组合数：%d'%(result.cc))
            print('三消出现数：  %d'%(result.c3))
            print('四消出现数：  %d'%(result.c4))
            c3 +=result.c3
            c4 +=result.c4
            _combo = result.c3 + result.c4
            if _combo >= 1 :
                totalcombo += _combo
                combonum += 1
            elif result.cc >=1 :
                totalcc += result.cc
                onlyccnum += 1
                if result.cc >=3 :
                    only2ccnum += 1
            else :
                deadnum += 1
        if onlyccnum + combonum + deadnum == i :
            print('——'*20)
            normalnum = onlyccnum + deadnum
            print('总局数：%d ; 有效初始版面数：%d (%f)；\n一般局数：%d (%f) ;死局数：%d (%f) ; 动态局数：%d (%f) ; \n被阻碍2个消除机会后的一般局数：%d(%f) ; 三消出现总数：%d(%f) ; 四消出现总数： %d(%f) ;'\
                  %(i,normalnum,(normalnum/i),onlyccnum,(onlyccnum/i),deadnum,(deadnum/i),combonum,(combonum/i),only2ccnum,(only2ccnum/i),c3,(c3/i),c4,(c4/i)))
            #初始版面的场地交换活局概率
            pa = onlyccnum/(i-combonum)
            pa2 = only2ccnum/(i-combonum)
            print('一般局率 Pa = %f'%(pa))
            print('阻碍后一般局率 Pa* = %f'%(pa2))
            #初始版面的活局总概率
            p = 1-(1-pa)*0.75
            print('非死局率 P = %f'%(p))
            #玩家平均每回合消除机会数量（不包括五消以上）
            x = totalcc/onlyccnum
            print('局面平均解数 N = %f'%(x))
            #玩家平均回合净胜牌数
            print('平均回合净胜牌数 X = %f'%((c3*3+c4*4)/totalcombo))
        else :
            print('Error:总数计算不一致')