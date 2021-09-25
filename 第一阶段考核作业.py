'''
作业需求：
1、生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示 ）

2、3个玩家(玩家也可以自己定义)
user_list = ["alex","武沛齐","李路飞"]

3、发牌规则
默认先给用户发一张牌，其中 J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
用户根据自己的情况判断是否继续要牌。
    要，则再给他发一张。（可以一直要牌，但是如果自己手中的牌总和超过11点，你的牌就爆掉了(牌面变成0)）
    不要，则开始给下个玩家发牌。（没有牌则则牌面默认是0）
如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌。

4、最终计算并获得每个玩家的分值，例如：
result = {
    "alex":8,
    "武沛齐":9,
    "李路飞":0
}
'''

import random

# 新建一个扑克花色表
poke_color = ["红桃", "黑桃", "方块", "梅花"]

# 新建一个扑克数值列表
num_list = []
for i in range(1, 14):
    num_list.append(i)

# 创建一副新的扑克牌及各牌对应代表分数的列表，如[('红桃', 7 , 7),('黑桃', 12 , 0.5)...]
total_poke_list = []
for color in range(len(poke_color)):
    for num in range(1, 14):
        if num < 11:
            data = (poke_color[color], num_list[num - 1], num_list[num - 1])
            total_poke_list.append(data)
        else:
            data = (poke_color[color], num_list[num - 1], 0.5)
            total_poke_list.append(data)
special_poke = [('小王', 14, 0.5), ('大王', 15, 0.5)]
total_poke_list.extend(special_poke)

print('游戏开始'.center(50, '-'))

# 自定义录入三名玩家姓名
user_list = []
for i in range(3):
    user_input = input(f"请输入玩家{i + 1}号的姓名({i + 1}/3):").strip()
    user_list.append(user_input)

# 首先为三位玩家先随机各发一张牌
poke_first = []
poke_score = []
for i in range(len(user_list)):
    index = random.randint(0, len(total_poke_list) - 1)
    poke = total_poke_list.pop(index)
    poke_first.append(poke)
    poke_score.append(poke[2])

print("各玩家首次发牌完毕，下面是加牌环节".center(50, '-'))

# 依次询问用户是否需要选择要牌，最后统计出各玩家最后得分（牌值爆了则为0分）
result = {}
for i in range(len(user_list)):
    print(f"{user_list[i]}玩家，你的第一张牌是:{poke_first[i][0]}{poke_first[i][1]}")
    while True:
        choice = input("请选择是否需要继续要牌（y/n）：").strip()
        choice = choice.upper()

        # 首先判断用户输入是否符合规则
        if choice not in {'Y', 'N'}:
            print("输入格式错误，请重新正确的输入！")
            continue

        # 输入N，则选择不要牌了
        if choice == 'N':
            result[user_list[i]] = poke_score[i]
            print(f"{user_list[i]}玩家选择不要牌了")
            break

        # 输入Y,继续要牌，将牌得分进行累加，判断是否爆了
        if choice == 'Y':
            index = random.randint(0, len(total_poke_list) - 1)
            poke = total_poke_list.pop(index)
            print(f"{user_list[i]}玩家要的牌为:{poke[0]}{poke[1]}")
            poke_score[i] += poke[2]

            # 判断牌值得分是否爆了
            while poke_score[i] <= 11:
                result[user_list[i]] = poke_score[i]
                break
            else:
                print(f"很遗憾{user_list[i]}玩家,您手中的牌已爆！")
                result[user_list[i]] = 0
                break

print("游戏结束，玩家的得分情况如下：".center(50, '-'))
for i in result:
    print(f"玩家{i}得分：", result[i])
