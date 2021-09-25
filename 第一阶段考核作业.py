"""
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
"""

import random

# 新建一个扑克花色表
poke_color = ["红桃", "黑桃", "方块", "梅花"]

# 创建一副新的扑克牌及各牌对应代表分数的列表，如[('红桃', 7 , 7),('黑桃', 12 , 0.5)...]
total_poke_list = []
for color in poke_color:
    for num in range(1, 14):
        if num < 11:
            score = num
        else:
            score = 0.5
        data = (color, num, score)
        total_poke_list.append(data)
special_poke = [('小王', 14, 0.5), ('大王', 15, 0.5)]
total_poke_list.extend(special_poke)

print('游戏开始'.center(50, '-'))

# 自定义录入三名玩家姓名
user_list = []
while len(user_list) < 3:
    user_order = len(user_list) + 1
    user_input = input(f"请输入玩家{user_order}号的姓名({user_order}/3):").strip()
    if user_input and user_input not in user_list:
        user_list.append(user_input)
    else:
        print("输入错误，请重新输入")

# 首先为三位玩家先随机各发一张牌
poke_first = []
poke_score = []
for name in user_list:
    index = random.randint(0, len(total_poke_list) - 1)
    poke = total_poke_list.pop(index)
    poke_first.append(poke)
    poke_score.append(poke[2])

print("各玩家首次发牌完毕，下面是加牌环节".center(50, '-'))

# 依次询问用户是否需要选择要牌，最后统计出各玩家最后得分（牌值爆了则为0分）
result = {}
for index, name in enumerate(user_list):
    print(f"{name}玩家，你的第一张牌是:{poke_first[index][0]}{poke_first[index][1]}")
    while True:
        choice = input("请选择是否需要继续要牌（y/n）：").strip()
        choice = choice.upper()

        # 首先判断用户输入是否符合规则
        if choice not in {'Y', 'N'}:
            print("输入格式错误，请重新正确的输入！")
            continue

        # 输入N，则选择不要牌了
        if choice == 'N':
            result[user_list[index]] = poke_score[index]
            print(f"{user_list[index]}玩家选择不要牌了")
            break

        # 输入Y,继续要牌，将牌得分进行累加，判断是否爆了
        if choice == 'Y':
            index_random = random.randint(0, len(total_poke_list) - 1)
            poke = total_poke_list.pop(index_random)
            print(f"{user_list[index]}玩家要的牌为:{poke[0]}{poke[1]}")
            poke_score[index] += poke[2]

            # 判断牌值得分是否爆了
            while poke_score[index] <= 11:
                result[user_list[index]] = poke_score[index]
                break
            else:
                print(f"很遗憾{user_list[index]}玩家,您手中的牌已爆！")
                result[user_list[index]] = 0
                break

print("游戏结束，玩家的得分情况如下：".center(50, '-'))
for name in result:
    print(f"玩家{name}得分：", result[name])
