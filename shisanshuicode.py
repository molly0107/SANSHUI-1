#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math
import copy
import http
import requests
import json

class CardModel:
    cardList = []
    cardType = 1

    def __init__(self):
        self.cardList = []
        self.cardType = 1


'''一副手牌中的各种情况，用来最后比较哪一种情况得分最多'''
class TypeCard:
    aCardList = []
    headmodul = CardModel()
    midmodul = CardModel()
    lastmodul = CardModel()
    sumscore = 0

    def __init__(self):
        self.aCardList = []
        self.headmodul = CardModel()
        self.midmodul = CardModel()
        self.lastmodul = CardModel()
        self.sumscore = 0

    def getsumsore(self):
        self.sumscore = self.headmodul.cardType + self.midmodul.cardType + self.lastmodul.cardType


'''手牌预处理'''
'''按牌面大小排序！'''


def getcardList2(cardlist):
    cardlist2 = cardlist.copy()
    for i in range(13):
        for j in range(0, 13 - i - 1):
            if (cardlist2[j] % 100) > (cardlist2[j + 1] % 100):
                cardlist2[j], cardlist2[j + 1] = cardlist2[j + 1], cardlist2[j]
            if (cardlist2[j] % 100) == (cardlist2[j + 1] % 100):
                if (cardlist2[j] // 100) > (cardlist2[j + 1] // 100):
                    cardlist2[j], cardlist2[j + 1] = cardlist2[j + 1], cardlist2[j]
    cardlist2.reverse()
    return cardlist2


'''按照牌面从小到大，保存在二维列表里'''


def getcardList3(cardlist):
    cardlist3 = [[0 for item in range(4)] for j in range(13)]
    for item in cardlist:
        y = int((item / 100) - 1)
        x = (item % 100) - 2
        cardlist3[x][y] = item
    return cardlist3


'''按照牌面从大到小，保存在列表'''


def getcardList4(cardlist):
    cardlist4 = [[0 for item in range(4)] for j in range(13)]
    for item in cardlist:
        y = 4 - (item // 100)
        x = 14 - (item % 100)
        cardlist4[x][y] = item
    return cardlist4


'''按牌面花色分类，保存在列表里'''


def getHeitao(cardlist2):
    heitao = []
    for item in cardlist2:
        if item // 100 == 4:
            heitao.append(item)
    return heitao


def getHongtao(cardlist2):
    hongtao = []
    for item in cardlist2:
        if item // 100 == 3:
            hongtao.append(item)
    return hongtao


def getMeihua(cardlist2):
    meihua = []
    for item in cardlist2:
        if item // 100 == 2:
            meihua.append(item)
    return meihua


def getFangkuai(cardlist2):
    fangkuai = []
    for item in cardlist2:
        if item // 100 == 1:
            fangkuai.append(item)
    return fangkuai


def SpecialCard(cardlist, cardlist3, cardlist4, heitao, hongtao, meihua, fangkuai):
    typecard = TypeCard()
    '''至尊青龙 24'''
    zhizunqinglong = []
    zhizunqinglong.append(cardlist[0])
    if heitao.__len__ == 13:
        for ii in cardlist:
            if (ii % 100) + 1 == (zhizunqinglong[-1] % 100):
                zhizunqinglong.append(ii)
        if len(zhizunqinglong) == 13:
            typecard.lastmodul.cardList = zhizunqinglong[0:5]
            typecard.lastmodul.cardType = 24
            typecard.midmodul.cardList = zhizunqinglong[5:10]
            typecard.midmodul.cardType = 24
            typecard.headmodul.cardList = zhizunqinglong[10:13]
            typecard.headmodul.cardType = 24
            return typecard
    if hongtao.__len__ == 13:
        for ii in cardlist:
            if (ii % 100) + 1 == (zhizunqinglong[-1] % 100):
                zhizunqinglong.append(ii)
        if len(zhizunqinglong) == 13:
            typecard.lastmodul.cardList = zhizunqinglong[0:5]
            typecard.lastmodul.cardType = 24
            typecard.midmodul.cardList = zhizunqinglong[5:10]
            typecard.midmodul.cardType = 24
            typecard.headmodul.cardList = zhizunqinglong[10:13]
            typecard.headmodul.cardType = 24
            return typecard
    if meihua.__len__ == 13:
        for ii in cardlist:
            if (ii % 100) + 1 == (zhizunqinglong[-1] % 100):
                zhizunqinglong.append(ii)
        if len(zhizunqinglong) == 13:
            typecard.lastmodul.cardList = zhizunqinglong[0:5]
            typecard.lastmodul.cardType = 24
            typecard.midmodul.cardList = zhizunqinglong[5:10]
            typecard.midmodul.cardType = 24
            typecard.headmodul.cardList = zhizunqinglong[10:13]
            typecard.headmodul.cardType = 24
            return typecard
    if fangkuai.__len__ == 13:
        for ii in cardlist:
            if (ii % 100) + 1 == (zhizunqinglong[-1] % 100):
                zhizunqinglong.append(ii)
        if len(zhizunqinglong) == 13:
            typecard.lastmodul.cardList = zhizunqinglong[0:5]
            typecard.lastmodul.cardType = 24
            typecard.midmodul.cardList = zhizunqinglong[5:10]
            typecard.midmodul.cardType = 24
            typecard.headmodul.cardList = zhizunqinglong[10:13]
            typecard.headmodul.cardType = 24
            return typecard

    '''一条龙 23'''
    yitiaolong = []
    yitiaolong.append(cardlist[0])
    for ii in cardlist:
        if (ii % 100) + 1 == (yitiaolong[-1] % 100):
            yitiaolong.append(ii)
    if len(yitiaolong) == 13:
        typecard.lastmodul.cardList = yitiaolong[0:5]
        typecard.lastmodul.cardType = 23
        typecard.midmodul.cardList = yitiaolong[5:10]
        typecard.midmodul.cardType = 23
        typecard.headmodul.cardList = yitiaolong[10:13]
        typecard.headmodul.cardType = 23
        return typecard

    '''十二皇族 22'''
    shierhuangzu = []
    for ii in cardlist:
        if ((ii % 100) > 10) and ((ii % 100) < 14):
            shierhuangzu.append(ii)
        if len(shierhuangzu) == 12:
            print(shierhuangzu)
            typecard.lastmodul.cardList = shierhuangzu[0:5]
            typecard.lastmodul.cardType = 22
            typecard.midmodul.cardList = shierhuangzu[5:10]
            typecard.midmodul.cardType = 22
            typecard.headmodul.cardList = shierhuangzu[10:13]
            typecard.headmodul.cardType = 22
            return typecard

    '''三同花顺 21'''
    santonghuashun1 = []
    flag = 0
    tempcardlist = cardlist.copy()
    for ii in tempcardlist:  # 查找第一组同花顺
        if not santonghuashun1:
            santonghuashun1.append(ii)
            continue
        print("三同花顺！！", santonghuashun1)
        print((ii % 100))
        print(santonghuashun1[-1] % 100)
        if ((ii % 100) + 1) == (santonghuashun1[-1] % 100) and (ii // 100) == (santonghuashun1[-1] // 100):
            santonghuashun1.append(ii)
            print("lensanshunzi", len(santonghuashun1))
            if len(santonghuashun1) == 5:
                for iii in santonghuashun1:  # 移除以找的第一组同花顺
                    tempcardlist.remove(iii)
                print("tempcardlist", tempcardlist)
                santonghuashun2 = []
                for iii in tempcardlist:  # 查找第二组同花顺
                    if not santonghuashun2:
                        santonghuashun2.append(iii)
                        continue
                    print("iii", iii)
                    print("三同花顺2！！", santonghuashun2)
                    if (iii % 100) + 1 == (santonghuashun2[-1] % 100) and (iii // 100) == (santonghuashun2[-1] // 100):
                        santonghuashun2.append(iii)
                        if len(santonghuashun2) == 5:
                            for iiii in santonghuashun2:
                                tempcardlist.remove(iiii)
                            print("tempcardlist3", tempcardlist)
                            santonghuashun3 = []
                            for iiii in tempcardlist:  # 查找第三组同花顺
                                if not santonghuashun3:
                                    santonghuashun3.append(iiii)
                                    continue
                                print("iiii", iiii)
                                print("三同花顺3！！", santonghuashun3)
                                if (iiii % 100) + 1 == (santonghuashun3[-1] % 100) and (iiii // 100) == (
                                        santonghuashun3[-1] // 100):
                                    santonghuashun3.append(iiii)
                                    if len(santonghuashun3) == 3:
                                        typecard.lastmodul.cardList.extend(santonghuashun1)
                                        typecard.lastmodul.cardType = 21
                                        typecard.midmodul.cardList.extend(santonghuashun2)
                                        typecard.midmodul.cardType = 21
                                        typecard.headmodul.cardList.extend(santonghuashun3)
                                        typecard.headmodul.cardType = 21
                                        return typecard
                    elif (iii % 100) == (santonghuashun2[-1] % 100):
                        continue
                    else:
                        santonghuashun2.clear()
                        santonghuashun2.append(iii)
        elif (ii % 100) == (santonghuashun1[-1] % 100):
            continue
        else:
            santonghuashun1.clear()
            santonghuashun1.append(ii)

    '''三分天下 20'''
    sanfentianxia = []
    for ii in range(len(cardlist4)):
        count = 0
        for jj in range(len(cardlist4[ii])):
            if cardlist4[ii][jj] != 0:
                count = count + 1
        if count == 4:
            sanfentianxia.extend(cardlist4[ii])
    if len(sanfentianxia) == 12:
        typecard.lastmodul.cardList = cardlist[0:5]
        typecard.lastmodul.cardType = 20
        typecard.midmodul.cardList = cardlist[5:10]
        typecard.midmodul.cardType = 20
        typecard.headmodul.cardList = cardlist[10:13]
        typecard.headmodul.cardType = 20
        return typecard

    '''全大 19'''
    quanda = []
    for ii in cardlist:
        if (ii % 100) >= 8:
            quanda.append(ii)
    if len(quanda) == 13:
        typecard.lastmodul.cardList = cardlist[0:5]
        typecard.lastmodul.cardType = 19
        typecard.midmodul.cardList = cardlist[5:10]
        typecard.midmodul.cardType = 19
        typecard.headmodul.cardList = cardlist[10:13]
        typecard.headmodul.cardType = 19
        return typecard

    '''全小 18'''
    quanxiao = []
    for ii in cardlist:
        if (ii % 100) < 8:
            quanxiao.append(ii)
    if len(quanxiao) == 13:
        typecard.lastmodul.cardList = cardlist[0:5]
        typecard.lastmodul.cardType = 18
        typecard.midmodul.cardList = cardlist[5:10]
        typecard.midmodul.cardType = 18
        typecard.headmodul.cardList = cardlist[10:13]
        typecard.headmodul.cardType = 18
        return typecard

    '''凑一色 17'''
    flag = 0
    if len(hongtao) + len(fangkuai) == 13:
        flag = 1
    if len(heitao) + len(meihua) == 13:
        flag = 1
    if flag == 1:
        typecard.lastmodul.cardList = cardlist[0:5]
        typecard.lastmodul.cardType = 17
        typecard.midmodul.cardList = cardlist[5:10]
        typecard.midmodul.cardType = 17
        typecard.headmodul.cardList = cardlist[10:13]
        typecard.headmodul.cardType = 17
        return typecard

    '''双怪冲三（两个葫芦+一个对子+一张杂牌）16'''
    shuangguai = []
    zapai = 0
    flag = 0
    for ii in range(len(cardlist4)):
        count = 0
        for jj in range(len(cardlist4[ii])):
            if cardlist4[ii][jj] != 0:
                count = count + 1
        if count == 1:
            for jj in range(len(cardlist4[ii])):
                if cardlist4[ii][jj] != 0:
                    zapai = cardlist4[ii][jj]
        if count == 3:
            shuangguai.extend(cardlist4[ii])
            n = shuangguai.count(0)
            for iii in range(n):
                shuangguai.remove(0)

    if len(shuangguai) == 6:
        flag = 1
    if flag == 1:
        for ii in range(len(cardlist4)):
            count = 0
            for jj in range(len(cardlist4[ii])):
                if cardlist4[ii][jj] != 0:
                    count = count + 1
            if count == 2:
                shuangguai.extend(cardlist4[ii])
                n = shuangguai.count(0)
                for iii in range(n):
                    shuangguai.remove(0)

    if len(shuangguai) == 12:
        flag = 2
    if flag == 2:
        typecard.lastmodul.cardList.extend(shuangguai[0:3])
        typecard.lastmodul.cardList.extend(shuangguai[6:8])
        typecard.lastmodul.cardType = 16
        typecard.midmodul.cardList.extend(shuangguai[3:6])
        typecard.midmodul.cardList.extend(shuangguai[8:10])
        typecard.midmodul.cardType = 16
        typecard.headmodul.cardList.extend(shuangguai[10:12])
        typecard.headmodul.cardList.append(zapai)
        typecard.headmodul.cardType = 16
        return typecard

    '''四套三条 15'''
    zapai = 0
    sitaosantiao = []
    for ii in range(len(cardlist4)):
        count = 0
        for jj in range(len(cardlist4[ii])):
            if cardlist4[ii][jj] != 0:
                count = count + 1
        if count == 1:
            for jj in range(len(cardlist4[ii])):
                if cardlist4[ii][jj] != 0:
                    zapai = cardlist4[ii][jj]
        if count == 3:
            sitaosantiao.extend(cardlist4[ii])
            n = sitaosantiao.count(0)
            for iii in range(n):
                sitaosantiao.remove(0)
    if len(sitaosantiao) == 12:
        typecard.lastmodul.cardList.extend(sitaosantiao[0:5])
        typecard.lastmodul.cardType = 15
        typecard.midmodul.cardList.extend(sitaosantiao[5:10])
        typecard.midmodul.cardType = 15
        typecard.headmodul.cardList.extend(sitaosantiao[10:12])
        typecard.headmodul.cardType = 15
        typecard.lastmodul.cardList.append(zapai)
        return typecard

    '''五对三条 14'''
    wuduisantiao = []
    for ii in range(len(cardlist4)):
        count = 0
        for jj in range(len(cardlist4[ii])):
            if cardlist4[ii][jj] != 0:
                count = count + 1
        if count == 2:
            wuduisantiao.extend(cardList4[ii])
            n = wuduisantiao.count(0)
            for iii in range(n):
                wuduisantiao.remove(0)
    if len(wuduisantiao) == 10:
        for ii in range(len(cardlist4)):
            count = 0
            for jj in range(len(cardlist4[ii])):
                if cardlist4[ii][jj] != 0:
                    count = count + 1
            if count == 3:
                wuduisantiao.extend(cardList4[ii])
                n = wuduisantiao.count(0)
                for iii in range(n):
                    wuduisantiao.remove(0)
    if len(wuduisantiao) == 13:
        typecard.lastmodul.cardList.extend(wuduisantiao[0:5])
        typecard.lastmodul.cardType = 14
        typecard.midmodul.cardList.extend(wuduisantiao[5:10])
        typecard.midmodul.cardType = 14
        typecard.headmodul.cardList.extend(wuduisantiao[10:13])
        typecard.headmodul.cardType = 14
        return typecard

    '''六对半 13'''
    liuduiban = []
    zapai = 0
    for ii in range(len(cardlist4)):
        count = 0
        for jj in range(len(cardlist4[ii])):
            if cardlist4[ii][jj] != 0:
                count = count + 1
        if count == 2:
            liuduiban.extend(cardList4[ii])
            n = liuduiban.count(0)
            for iii in range(n):
                liuduiban.remove(0)
        if count == 1:
            for jj in range(len(cardlist4[ii])):
                if cardlist4[ii][jj] != 0:
                    zapai = cardlist4[ii][jj]
    if len(liuduiban) == 12:
        typecard.lastmodul.cardList.extend(liuduiban[0:5])
        typecard.lastmodul.cardType = 13
        typecard.midmodul.cardList.extend(liuduiban[5:10])
        typecard.midmodul.cardType = 13
        typecard.headmodul.cardList.extend(liuduiban[10:12])
        typecard.headmodul.cardList.append(zapai)
        typecard.headmodul.cardType = 13
        return typecard

    '''三顺子 12'''
    sanshunzi1 = []
    flag = 0
    tempcardlist = cardlist.copy()
    for ii in tempcardlist:  # 查找第一组同花顺
        if not sanshunzi1:
            sanshunzi1.append(ii)
            continue
        print("三顺子！！", sanshunzi1)
        print((ii % 100))
        print(sanshunzi1[-1] % 100)
        if ((ii % 100) + 1) == (sanshunzi1[-1] % 100):
            sanshunzi1.append(ii)
            print("lensanshunzi", len(sanshunzi1))
            if len(sanshunzi1) == 5:
                for iii in sanshunzi1:  # 移除以找的第一组同花顺
                    tempcardlist.remove(iii)
                print("tempcardlist", tempcardlist)
                sanshunzi2 = []
                for iii in tempcardlist:  # 查找第二组同花顺
                    if not sanshunzi2:
                        sanshunzi2.append(iii)
                        continue
                    print("iii", iii)
                    print("三顺子2！！", sanshunzi2)
                    if (iii % 100) + 1 == (sanshunzi2[-1] % 100):
                        sanshunzi2.append(iii)
                        if len(sanshunzi2) == 5:
                            for iiii in sanshunzi2:
                                tempcardlist.remove(iiii)
                            print("tempcardlist3", tempcardlist)
                            sanshunzi3 = []
                            for iiii in tempcardlist:  # 查找第三组同花顺
                                if not sanshunzi3:
                                    sanshunzi3.append(iiii)
                                    continue
                                print("iiii", iiii)
                                print("三顺子3！！", sanshunzi3)
                                if (iiii % 100) + 1 == (sanshunzi3[-1] % 100):
                                    sanshunzi3.append(iiii)
                                    if len(sanshunzi3) == 3:
                                        typecard.lastmodul.cardList.extend(sanshunzi1)
                                        typecard.lastmodul.cardType = 12
                                        typecard.midmodul.cardList.extend(sanshunzi2)
                                        typecard.midmodul.cardType = 12
                                        typecard.headmodul.cardList.extend(sanshunzi3)
                                        typecard.headmodul.cardType = 12
                                        return typecard
                    elif (iii % 100) == (sanshunzi2[-1] % 100):
                        continue
                    else:
                        sanshunzi2.clear()
                        sanshunzi2.append(iii)
        elif (ii % 100) == (sanshunzi1[-1] % 100):
            continue
        else:
            sanshunzi1.clear()
            sanshunzi1.append(ii)

    '''三同花 11'''
    santonghua = []
    tempcardlist = []
    templist = []
    flag = 0
    tempcardlist.extend(heitao)
    tempcardlist.extend(hongtao)
    tempcardlist.extend(meihua)
    tempcardlist.extend(fangkuai)

    print("三同花", tempcardlist)
    for ii in tempcardlist:
        if not santonghua:
            santonghua.append(ii)
        else:
            print("santonghua", santonghua)
            print("ii", ii)
            if ii // 100 == santonghua[-1] // 100:
                santonghua.append(ii)

                if len(santonghua) == 5:
                    templist.extend(santonghua)
                    santonghua.clear()
            else:
                santonghua.clear()
                santonghua.append(ii)

    if len(templist) == 10:
        for ii in templist:
            tempcardlist.remove(ii)
        flag = 1
        for ii in tempcardlist:
            if ii // 100 != tempcardlist[0] // 100:
                flag = 0
        if flag == 1:
            typecard.lastmodul.cardList.extend(templist[0:5])
            typecard.lastmodul.cardType = 11
            typecard.midmodul.cardList.extend(templist[5:10])
            typecard.midmodul.cardType = 11
            typecard.headmodul.cardList.extend(tempcardlist)
            typecard.headmodul.cardType = 11
            return typecard

    return typecard


'''找到手牌中最大的牌型'''


def findmax(cardlist1, cardlist3, cardlist4, heitao, hongtao, meihua, fangkuai):
    maxlist = []
    cardmodelList = []
    '''同花顺'''
    if heitao.__len__() >= 5:
        templist = heitao
        for i in templist:
            tonghuashun = []

            if i % 100 < 6:
                break
            else:
                tonghuashun.append(i)
                for j in templist:
                    if (j % 100) + 1 == (tonghuashun[-1] % 100):
                        tonghuashun.append(j)
                if tonghuashun.__len__() >= 5:
                    print("tonghuashun!", tonghuashun)
                    num = tonghuashun.__len__() - 4
                    print("黑桃同花顺num", num)
                    for x in range(num):
                        maxlist.extend(tonghuashun[x:x + 5])
                        print(maxlist)
                        cardmodel = CardModel()
                        cardmodel.cardList = maxlist.copy()
                        cardmodel.cardType = 10
                        cardmodelList.append(cardmodel)
                        maxlist.clear()
                    '''找到最大一组连续的同花顺子就不用再找其他同花顺'''
                    break
    if hongtao.__len__() >= 5:
        templist = hongtao
        for i in templist:
            tonghuashun = []
            if i % 100 < 6:
                break
            else:
                tonghuashun.append(i)
                for j in templist:
                    if (j % 100) + 1 == (tonghuashun[-1] % 100):
                        tonghuashun.append(j)
                if tonghuashun.__len__() >= 5:
                    num = tonghuashun.__len__() - 4
                    print("红桃同花顺num", num)
                    for x in range(num):
                        maxlist.extend(tonghuashun[x:x + 5])
                        print(maxlist)
                        cardmodel = CardModel()
                        cardmodel.cardList = maxlist.copy()
                        cardmodel.cardType = 10
                        cardmodelList.append(cardmodel)
                        maxlist.clear()
                    break
            maxlist.clear()
    if meihua.__len__() >= 5:
        templist = meihua
        for i in templist:
            tonghuashun = []
            if i % 100 < 6:
                break
            else:
                tonghuashun.append(i)
                for j in templist:
                    if (j % 100) + 1 == (tonghuashun[-1] % 100):
                        tonghuashun.append(j)
                if tonghuashun.__len__() >= 5:
                    num = tonghuashun.__len__() - 4
                    print("梅花同花顺num", num)
                    for x in range(num):
                        maxlist.extend(tonghuashun[x:x + 5])
                        print(maxlist)
                        cardmodel = CardModel()
                        cardmodel.cardList = maxlist.copy()
                        cardmodel.cardType = 10
                        cardmodelList.append(cardmodel)
                        maxlist.clear()
                    break
            maxlist.clear()
    if fangkuai.__len__() >= 5:
        templist = fangkuai
        for i in templist:
            tonghuashun = []
            if i % 100 < 6:
                break
            else:
                tonghuashun.append(i)
                for j in templist:
                    if (j % 100) + 1 == (tonghuashun[-1] % 100):
                        tonghuashun.append(j)
                if tonghuashun.__len__() >= 5:
                    num = tonghuashun.__len__() - 4
                    print("方块同花顺num", num)
                    for x in range(num):
                        maxlist.extend(tonghuashun[x:x + 5])
                        print(maxlist)
                        cardmodel = CardModel()
                        cardmodel.cardList = maxlist.copy()
                        cardmodel.cardType = 10
                        cardmodelList.append(cardmodel)
                        maxlist.clear()
                    break
            maxlist.clear()

    # if cardmodelList:
    #   return cardmodelList
    maxlist.clear()

    '''炸弹'''
    for i in range(len(cardlist4)):
        count = 0
        for j in range(len(cardlist4[i])):
            if cardlist4[i][j] != 0:
                count = count + 1
        if count == 4:
            maxlist.extend(cardlist4[i])
            print(maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 9
            cardmodelList.append(cardmodel)
        maxlist.clear()
    # if cardmodelList:
    #    return cardmodelList

    '''葫芦（三带二）'''
    '''找三对'''
    for i in range(len(cardlist4)):
        count = 0
        for j in range(len(cardlist4[i])):
            if cardlist4[i][j] != 0:
                count = count + 1
        if count == 3:
            print("hhhhhhhhhhhh")
            '''如果存在一个三对，接着找对子'''
            for ii in range(len(cardlist3)):
                maxlist.extend(cardlist4[i])
                count = 0
                for jj in range(len(cardlist3[i])):
                    if cardlist3[ii][jj] != 0:
                        count = count + 1
                if count == 2:
                    maxlist.extend(cardlist3[ii])
                    '''找到一个葫芦在maxlist里，对手牌进行去0处理'''
                    n = maxlist.count(0)
                    for i in range(n):
                        maxlist.remove(0)

                    if len(maxlist) == 5:
                        print(maxlist)
                        cardmodel = CardModel()
                        cardmodel.cardList = maxlist.copy()
                        cardmodel.cardType = 8
                        cardmodelList.append(cardmodel)
                '''清除已经找到的一个葫芦'''
                maxlist.clear()
        '''清除找到的一个三对'''
        maxlist.clear()

    '''同花，  如果一种花色的牌超过5张，需要多考虑'''
    import itertools as it

    if heitao.__len__() >= 5:
        tonghua = []
        tonghua.extend(heitao)
        for i in it.combinations(tonghua, r=5):
            maxlist = list(i).copy()
            print("***************", maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 7
            cardmodelList.append(cardmodel)
            maxlist.clear()
    if hongtao.__len__() >= 5:
        tonghua = []
        tonghua.extend(hongtao)
        for i in it.combinations(tonghua, r=5):
            maxlist = list(i).copy()
            print("***************", maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 7
            cardmodelList.append(cardmodel)
            maxlist.clear()
    if meihua.__len__() >= 5:
        tonghua = []
        tonghua.extend(meihua)
        for i in it.combinations(tonghua, r=5):
            maxlist = list(i).copy()
            print("***************", maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 7
            cardmodelList.append(cardmodel)
            maxlist.clear()
    if fangkuai.__len__() >= 5:
        tonghua = []
        tonghua.extend(fangkuai)
        for i in it.combinations(tonghua, r=5):
            maxlist = list(i).copy()
            print("***************", maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 7
            cardmodelList.append(cardmodel)
            maxlist.clear()

    maxlist.clear()

    '''顺子'''
    for i in cardlist1:
        shunzi = []
        if i % 100 < 6:
            break
        else:
            shunzi.append(i)
            for j in cardlist1:
                if (j % 100) + 1 == (shunzi[-1] % 100):
                    shunzi.append(j)
            if shunzi.__len__() >= 5:
                num = shunzi.__len__() - 4
                print("顺子", num)
                for x in range(num):
                    maxlist.extend(shunzi[x:x + 5])
                    print(maxlist)
                    cardmodel = CardModel()
                    cardmodel.cardList = maxlist.copy()
                    cardmodel.cardType = 6
                    cardmodelList.append(cardmodel)
                    maxlist.clear()
                break
    maxlist.clear()

    '''三条'''
    for i in range(len(cardlist4)):
        count = 0
        for j in range(len(cardlist4[i])):
            if cardlist4[i][j] != 0:
                count = count + 1
        if count == 3:
            maxlist.extend(cardlist4[i])
        n = maxlist.count(0)
        for i in range(n):
            maxlist.remove(0)
        if len(maxlist) == 3:
            print(maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 5
            cardmodelList.append(cardmodel)
            maxlist.clear()
    maxlist.clear()

    '''两对'''
    for i in range(len(cardlist4)):
        count = 0
        for j in range(len(cardlist4[i])):
            if cardlist4[i][j] != 0:
                count = count + 1
        if count == 2:
            maxlist.extend(cardlist4[i])
            for ii in range(len(cardlist3) - 1 - i):
                count = 0
                for jj in range(len(cardlist3[ii])):
                    if cardlist3[ii][jj] != 0:
                        print("neirong", cardlist3[ii][jj])
                        count = count + 1
                        print("count:", count)
                if count == 2:
                    maxlist.extend(cardlist3[ii])
                    print("两对list", maxlist)
                    break

        if len(maxlist) == 8:
            n = maxlist.count(0)
            print(n)
            for i in range(n):
                maxlist.remove(0)
            print("两对", maxlist)
            cardmodel = CardModel()
            cardmodel.cardList = maxlist.copy()
            cardmodel.cardType = 4
            cardmodelList.append(cardmodel)
            maxlist.clear()
            '''找到一个最大的两对就结束'''
            return cardmodelList
    maxlist.clear()

    '''一对'''
    for i in range(len(cardlist4)):
        count = 0
        for j in range(len(cardlist4[i])):
            if cardlist4[i][j] != 0:
                count = count + 1
        if count == 2:
            maxlist.extend(cardlist4[i])
            break
    n = maxlist.count(0)
    for i in range(n):
        maxlist.remove(0)
    if len(maxlist) == 2:
        print(maxlist)
        cardmodel = CardModel()
        cardmodel.cardList = maxlist.copy()
        cardmodel.cardType = 3
        cardmodelList.append(cardmodel)

    maxlist.clear()

    return cardmodelList


'''主函数部分'''

'''登录'''
url = 'https://api.shisanshui.rtxux.xyz/auth/login'
data = {
  "username": "test",
  "password": "test"
}
r = requests.post(url,json=data)
print(r)
result1 = r.json()
print(result1)
token = result1['data']['token']

'''开启战局'''
headers = {'x-auth-token': token}
url2='https://api.shisanshui.rtxux.xyz/game/open'
r2=requests.post(url2, headers=headers)
result2=r2.json()
print(result2)

'''处理数据得到初始手牌'''
cardstr = result2['data']['card']
cardstr = cardstr.split(" ")

print("cardstr:", cardstr)
CardList = []
hua = 0
shu = 0
for i in cardstr:
  if i[0] == "$":
    hua = 400
    print("花", hua)
  if i[0] == '&':
    hua = 300
    print("花", hua)
  if i[0] == '*':
    hua = 200
    print("花", hua)
  if i[0] == "#":
    hua = 100
    print("花#", hua)

  if i[1:] == '2' or i[1:] == '3' or i[1:] == '4' or i[1:] == '5' or i[1:] == '6' or i[1:] == '7' or i[1:] == '8' or i[1:] == '9' or i[1:] == '10':
    shu = int(i[1:])
    print("数", shu)
    card = hua+shu
    print("牌", card)
    CardList.append(card)

  if i[1:] == 'J':
    shu = 11
    print("数",shu)
    card = hua + shu
    print("牌",card)
    CardList.append(card)
  if i[1:] == 'Q':
    shu = 12
    print("数",shu)
    card = hua + shu
    print("牌",card)
    CardList.append(card)
  if i[1:] == 'K':
    shu = 13
    print("数",shu)
    card = hua + shu
    print("牌",card)
    CardList.append(card)
  if i[1:] == 'A':
    shu = 14
    print("数",shu)
    card = hua + shu
    print("牌",card)
    CardList.append(card)

print("cardlist:", CardList)

TypeCardList1 = []
TypeCardList2 = []
#CardList = [202, 114, 102, 303, 312, 204, 308, 104, 306, 206, 412, 209, 405]

'''调用findmax函数，找到尾墩所有牌型的序列'''
cardList2 = getcardList2(CardList)  # 从大到小的手牌序列
print(cardList2)
cardList3 = getcardList3(cardList2)  # 从小到大的二维序列
print(cardList3)
cardList4 = getcardList4(cardList2)  # 从大到小的二维序列
print(cardList4)
Heitao = getHeitao(cardList2)
print("黑桃", Heitao)
Hongtao = getHongtao(cardList2)
print("红桃", Hongtao)
Meihua = getMeihua(cardList2)
print("梅花", Meihua)
Fangkuai = getFangkuai(cardList2)
print("方块", Fangkuai)

'''判断是否存在特殊手牌'''
flag = 0
finalCard = SpecialCard(cardList2, cardList3, cardList4, Heitao, Hongtao, Meihua, Fangkuai)
if finalCard.lastmodul.cardList:
    print("特殊牌型")
    print(finalCard.lastmodul.cardList)
    print(finalCard.midmodul.cardList)
    print(finalCard.headmodul.cardList)
    flag = 1

if flag == 0:
    print("普通牌型")
    '''普通牌型尾墩的所有情况，一个结构体列表'''
    CardModelList1 = findmax(cardList2, cardList3, cardList4, Heitao, Hongtao, Meihua, Fangkuai)

    for i in CardModelList1:
        typecard = TypeCard()
        typecard.lastmodul = i
        TypeCardList1.append(typecard)

    '''找到每一个后墩对应的多种中墩情况，放入序列'''
    for i in TypeCardList1:  # 第i个情况的手牌
        print("尾墩：", i.lastmodul.cardList)
        i.aCardList = cardList2.copy()
        for item in i.lastmodul.cardList:
            i.aCardList.remove(item)
        print("剩余手牌:", i.aCardList)
        cardList3 = getcardList3(i.aCardList)  # 从小到大的二维序列
        print(cardList3)
        cardList4 = getcardList4(i.aCardList)  # 从大到小的二维序列
        print(cardList4)
        Heitao = getHeitao(i.aCardList)
        print("黑桃", Heitao)
        Hongtao = getHongtao(i.aCardList)
        print("红桃", Hongtao)
        Meihua = getMeihua(i.aCardList)
        print("梅花", Meihua)
        Fangkuai = getFangkuai(i.aCardList)
        print("方块", Fangkuai)
        CardModelList2 = findmax(i.aCardList, cardList3, cardList4, Heitao, Hongtao, Meihua, Fangkuai)
        if CardModelList2:
            for j in CardModelList2:  # 第i种底墩，第j种中墩的情况
                if j.cardType < i.lastmodul.cardType:
                    typecard = TypeCard()
                    typecard.lastmodul = i.lastmodul  # 更改后墩会出bug，只能更改剩余手牌
                    typecard.aCardList = i.aCardList.copy()
                    typecard.midmodul = j
                    print("!!!!!!!!!", j.cardList)
                    print("!!!!!!!!!", typecard.aCardList)
                    for item in j.cardList:
                        typecard.aCardList.remove(item)
                    TypeCardList2.append(typecard)
                elif j.cardType == i.lastmodul.cardType:
                    print("***********", j.cardList[0])
                    print("***********", i.lastmodul.cardList[0])
                    if (j.cardList[0] % 100) < (i.lastmodul.cardList[0] % 100):
                        typecard = TypeCard()
                        typecard.lastmodul = i.lastmodul
                        typecard.aCardList = i.aCardList.copy()
                        typecard.midmodul = j
                        print("***********", j.cardList)
                        print("***********", typecard.aCardList)
                        for item in j.cardList:
                            typecard.aCardList.remove(item)
                        TypeCardList2.append(typecard)
                else:
                    typecard = TypeCard()
                    typecard.lastmodul = i.lastmodul
                    typecard.aCardList = i.aCardList.copy()
                    print("@@@@@@@", typecard.lastmodul.cardList)
                    TypeCardList2.append(typecard)
        else:
            typecard = TypeCard()
            typecard.lastmodul = i.lastmodul
            typecard.aCardList = i.aCardList.copy()
            print("@@@@@@@", typecard.lastmodul.cardList)
            TypeCardList2.append(typecard)
    '''查找前墩是否存在对子的情况，找到不大于中墩的最大牌型'''
    for i in TypeCardList2:
        cardList3 = getcardList3(i.aCardList)  # 从小到大的二维序列
        print(cardList3)
        cardList4 = getcardList4(i.aCardList)  # 从大到小的二维序列
        print(cardList4)
        maxList = []
        CardModelList3 = []
        for ii in range(len(cardList4)):
            count = 0
            for jj in range(len(cardList4[ii])):
                if cardList4[ii][jj] != 0:
                    count = count + 1
            if count == 2:
                maxList.extend(cardList4[ii])
                break
        n = maxList.count(0)
        for ii in range(n):
            maxList.remove(0)
        if len(maxList) == 2:
            print(maxList)
            cardmodel = CardModel()
            cardmodel.cardList = maxList.copy()
            cardmodel.cardType = 3
            CardModelList3.append(cardmodel)

        if CardModelList3:
            if CardModelList3[0].cardType < i.midmodul.cardType:  # 存在前墩牌型比中后墩大的情况，强行让前墩牌型比中墩小
                i.headmodul = CardModelList3[0]
            for item in CardModelList3:
                if item.cardType > i.headmodul.cardType:
                    if item.cardType < i.midmodul.cardType:
                        i.headmodul = item
                if item.cardType == i.headmodul.cardType:
                    if item.cardList[0] > i.headmodul.cardList[0]:
                        if item.cardType < i.midmodul.cardType:
                            i.headmodul = item

    '''给TypeCardList2中的组牌分配散牌'''
    for i in TypeCardList2:
        for item in i.headmodul.cardList:
            i.aCardList.remove(item)
        i.aCardList.reverse()
        print("最终剩余散牌", i.aCardList)
        print("i.lastmodul.cardList", i.lastmodul.cardList)
        print("i.midmodul.cardList", i.midmodul.cardList)
        print("i.headmodul.cardList", i.headmodul.cardList)
        print("i.aCardList", i.aCardList)
        while len(i.headmodul.cardList) < 3:
            temp = i.aCardList.pop()
            i.headmodul.cardList.append(temp)
        print("i.aCardList", i.aCardList)
        # print("i.midmodul.cardList", i.midmodul.cardList)
        while len(i.midmodul.cardList) < 5:
            temp = i.aCardList.pop()
            i.midmodul.cardList.append(temp)
        print("i.aCardList", i.aCardList)
        # print("i.lastmodul.cardList", i.lastmodul.cardList)
        while len(i.lastmodul.cardList) < 5:
            print("i.aCardList", i.aCardList)
            #   print("i.lastmodul.cardList", i.lastmodul.cardList)
            temp = i.aCardList.pop()
            i.lastmodul.cardList.append(temp)

    '''找到最大分数'''
    max_score = 0
    for i in TypeCardList2:
        print("*后墩", i.lastmodul.cardList)
        print("*中墩", i.midmodul.cardList)
        print("*前墩", i.headmodul.cardList)
        i.getsumsore()
        print("分数", i.sumscore)
        if max_score < i.sumscore:
            max_score = i.sumscore

    '''最大分数对应的牌型放入最终选择的牌型中'''
    finalCard = TypeCard()
    for i in TypeCardList2:
        if i.sumscore == max_score:
            if i.sumscore == finalCard.sumscore:
                if i.headmodul.cardType > finalCard.headmodul.cardType:
                    finalCard = i
                if i.headmodul.cardType == finalCard.headmodul.cardType:
                    if i.headmodul.cardList[0] > finalCard.headmodul.cardList[0]:
                        finalCard = i
                    if i.headmodul.cardList[0] == finalCard.headmodul.cardList[0]:
                        if i.midmodul.cardType > finalCard.midmodul.cardType:
                            finalCard = i
                        if i.midmodul.cardType == finalCard.midmodul.cardType:
                            if i.midmodul.cardList[0] > finalCard.midmodul.cardList[0]:
                                finalCard = i
                            if i.midmodul.cardList[0] == finalCard.midmodul.cardList[0]:
                                if i.lastmodul.cardType > finalCard.lastmodul.cardType:
                                    finalCard = i
                                if i.lastmodul.cardType == finalCard.lastmodul.cardType:
                                    if i.lastmodul.cardList[0] > finalCard.lastmodul.cardList[0]:
                                        finalCard = i
            else:
                finalCard = i

print("最终组牌")
print("前墩：", finalCard.headmodul.cardList)
print("中墩：", finalCard.midmodul.cardList)
print("后墩：", finalCard.lastmodul.cardList)
finalCard.getsumsore()
print("前墩牌型分数", finalCard.headmodul.cardType)
print("中墩牌型分数", finalCard.midmodul.cardType)
print("后墩牌型分数", finalCard.lastmodul.cardType)
print("总牌型分数", finalCard.sumscore)

'''处理数据，得到最终手牌'''
#headmodulcardList = [114, 209, 308]
#midmodulcardList = [412, 312, 206, 104, 102]
#lastmodulcardList = [306, 405, 204, 303, 202]
def cardlisttostr(cardList):
  handcard = ''
  hua = ''
  for i in cardList:
    if i//100 == 4:
      hua = '$'
    if i//100 == 3:
      hua = '&'
    if i//100 == 2:
      hua = '*'
    if i//100 == 1:
      hua = '#'
    if (i % 100 >= 2) and (i % 100 <= 10):
      shu = str(i % 100)
      card = hua+shu
      print(card)
      handcard = handcard+card+' '
    if i%100 == 11:
      shu = 'J'
      card = hua + shu
      print(card)
      handcard = handcard + card + ' '
    if i%100 == 12:
      shu = 'Q'
      card = hua + shu
      print(card)
      handcard = handcard + card + ' '
    if i%100 == 13:
      shu = 'K'
      card = hua + shu
      print(card)
      handcard = handcard + card + ' '
    if i%100 == 14:
      shu = 'A'
      card = hua + shu
      print(card)
      handcard = handcard + card + ' '
  handcard = handcard.strip()
  return handcard


Headcard = cardlisttostr(finalCard.headmodul.cardList)
Midcard = cardlisttostr(finalCard.midmodul.cardList)
Lastcard = cardlisttostr(finalCard.lastmodul.cardList)


finalCardstr = []
finalCardstr.append(Headcard)
finalCardstr.append(Midcard)
finalCardstr.append(Lastcard)
print(finalCardstr)
'''出牌'''
id = str(result2["data"]["id"])
print(id)
data = {
  "id": id,
  "card": finalCardstr
}
print(data)
url3='https://api.shisanshui.rtxux.xyz/game/submit'
r3=requests.post(url3, json=data, headers=headers)
result3 = r3.json()
print(result3)
