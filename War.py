
# class Group:
#     def __init__(self, id, my_or_enemy, lvl, count, damage, xp, speed):
#         self.id = id
#         self.type = type
#         self.lvl = lvl
#         self.count = count
#         self.damage = damage
#         self.xp = xp
#         self.speed = speed



# my_Foot = My_Group(1, "Foot", 3, 1400, damage_t3_Foot, 20, 5)
# my_Cava = My_Group(2, "Cava", 3, 1000, damage_t3_Cava, 30, 10)
# my_Luk = My_Group(3, "Luk", 3, 1000, damage_t3_Luk, 10, 5)
# my_Catapult = My_Group(4, "Catapult", 3, 1000, damage_t3_Catapult, 100, 1)


# enemy_Foot = Enemy_Group(1, "Foot", 3, 1350, damage_t3_Foot, 20, 5)
# enemy_Cava = Enemy_Group(2, "Cava", 3, 1000, damage_t3_Cava, 30, 10)
# enemy_Luk = Enemy_Group(3, "Luk", 3, 1000, damage_t3_Luk, 10, 5)
# enemy_Catapult = Enemy_Group(4, "Catapult", 3, 1000, damage_t3_Catapult, 100, 1)



# # Вывод содержимого списка
# for index, data in enumerate(my_group, start=1):
#     print(f"Мой солдат {index}: XP = {data[0]}, Damage = {data[1]}")

# print(f"\n\n")
# # Вывод содержимого списка
# for index, data in enumerate(enemy_group, start=1):
#     print(f"Противник {index}: XP = {data[0]}, Damage = {data[1]}")


# print( Fore.RED + f"\n------------------------------------- \n" +Style.RESET_ALL )
import random
from colorama import *
import time
from itertools import zip_longest

from BD import *



damage_t3_Foot = random.randint(10, 25)
damage_t3_Cava = random.randint(15, 35)
damage_t3_Luk = random.randint(15, 25)
damage_t3_Catapult = random.randint(1, 6) * 10


class My_Group:
    def __init__(self, id, type, lvl, count, damage, xp, speed):
        self.id = id
        self.type = type
        self.lvl = lvl
        self.count = count
        self.damage = damage
        self.xp = xp
        self.speed = speed

class Enemy_Group:
    def __init__(self, id, type, lvl, count, damage, xp, speed):
        self.id = id
        self.type = type
        self.lvl = lvl
        self.count = count
        self.damage = damage
        self.xp = xp
        self.speed = speed




damage_t3_Foot = random.randint(10, 25)
damage_t2_Foot = random.randint(3, 8)

my_Foot = My_Group(1, "t3_foot", 3, 1100, damage_t3_Foot, 70, 5)
enemy_Foot = Enemy_Group(1, "t2_foot", 2, 12000, damage_t2_Foot, 15, 5)


my_group = []
enemy_group = []

print( Fore.RED + f"\n-----     Начало Программы     ----- \n" + Style.RESET_ALL )

for i in range(1, my_Foot.count + 1):
    damage = random.randint(10, 25)
    id = i
    my_group.append((id, my_Foot.xp, damage))

for i in range(1, enemy_Foot.count + 1):
    damage = random.randint(3, 8)
    id = i
    enemy_group.append((id, enemy_Foot.xp, damage))



def New_damage(type):
    if type == "t1_foot":
        return random.randint(1, 4)
    elif type == "t2_foot":
        return random.randint(3, 8)
    elif type == "t3_foot":
        return random.randint(10, 25)

global start_count_attacker_group
global start_count_defender_group

# start_count_attacker_group = 0
# start_count_defender_group = 0

def battle(attacker_group, attacker_group_type, defender_group, defender_group_type):
    round = 1
    
    # min_len_groups = min(len(attacker_group), len(defender_group)) # Ищу длинну МИНИМАЛЬНОГО отряда
    # n = int(min_len_groups * 0.2)     # беру 20% - это будет фаланга
    start_count_attacker_group = len(attacker_group) # для вывода конечного результата
    start_count_defender_group = len(defender_group)
    falang_1 = min(len(attacker_group), int(len(attacker_group) * 0.2)) # беру 20% - это будет фаланга
    falang_2 = min(len(defender_group), int(len(defender_group) * 0.2))

    if len(attacker_group) < len(defender_group):
        if ((len(attacker_group) * 2) < len(defender_group)) and len(attacker_group) >= falang_2 // 2:
            falang_1 = falang_2 // 2
        elif (len(attacker_group) * 2) < len(defender_group):
            falang_1 = int(len(attacker_group) * 0.4)
    elif len(defender_group) < len(attacker_group):
        if ((len(defender_group) * 2) < len(attacker_group)) and len(defender_group) >= falang_1 // 2:
            falang_2 = falang_1 // 2
        elif (len(defender_group) * 2) < len(attacker_group):
            falang_2 = int(len(defender_group) * 0.4)
        

    # smaller_group = min(len(attacker_group), len(defender_group))
    # bigger_group =  max(len(attacker_group), len(defender_group))

    print(f"Размер группы Атакующих = {len(attacker_group)}\t\t Флалнга: {falang_1}")
    print(f"Размер группы Защитников = {len(defender_group)}\t\t Флалнга: {falang_2}")

    front_line_attack = attacker_group[:falang_1] # закидываю первые falang_1 элементов в фалангу
    front_line_def = defender_group[:falang_2] 

    del attacker_group[:falang_1] # убираю первые n элементов из запасных
    del defender_group[:falang_2]


    alive_group_1 = True 
    alive_group_2 = True 



    while alive_group_1 and alive_group_2:  # 0 - id,  1 - xp,    2 - damage
        # print(f"\t\t\t--- РАУНД: {round}---\n\n")

        # if round > 1:
        #     print("\nСостояние Атакующей Группы:")
        #     for index, data in enumerate(front_line_attack, start=1):
        #         print(f"\t\tМой Солдат {index}: ID = {data[0]} XP = {data[1]}, Damage = {data[2]}")
        #         if data[1] is None:
        #             count_MY_dead += 1
        #     print(f"Мертвых: {count_MY_dead}/{len(front_line_attack)}")

        #     print("\nСостояние Защищающейся группы:")
        #     for index, data in enumerate(front_line_def, start=1):
        #         print(f"\t\tСолдат Противника {index}: ID = {data[0]} XP = {data[1]}, Damage = {data[2]}")
        #         if data[1] is None:
        #             count_Enemy_dead += 1
        #     print(f"Мертвых: {count_Enemy_dead}/{len(front_line_def)}")
        #     print("\n\n")

        # for attacker, defender in zip_longest(front_line_attack, front_line_def, fillvalue=None):
        #     if  attacker is not None and defender is not None and attacker[1] is not None and defender[1] is not None :
        #         print(f"Атакующий солдат ID:{attacker[0]} ХР: {attacker[1]} Урон: {attacker[2]}  --> Защищающийся солдат ID:{defender[0]} ХР: {defender[1]} Урон: {defender[2]}")
        #     elif attacker is not None and attacker[1] is not None:
        #         print(f"Атакующий солдат ID:{attacker[0]} ХР: {attacker[1]} Урон: {attacker[2]}  -->")
        #     elif defender is not None and defender[1] is not None:
        #         print(f"\t\t\t\t\t--> Защищающийся солдат ID:{defender[0]} ХР: {defender[1]} Урон: {defender[2]}")
        #     # else:
        #     #     print("Какая то хреновина")

        # print("\n\n")


        round += 1
        i_def = 0
        defender_group_leave_buffer = front_line_def.copy()
        for i_atack in range(len([attacker for attacker in front_line_attack if attacker[1] is not None])):

            attacker = front_line_attack[i_atack]

            if attacker == (None, None, None):
                # print("Атакующие кончились")
                break

            new_damage = New_damage(attacker_group_type)
            re_atack = True
            itr = 0

            while re_atack is True:
                attacker = (attacker[0], attacker[1], new_damage)
                
                if attacker == (None, None, None):
                    #print("Атакующие кончились")
                    break
                
                if i_def + 1 > len(front_line_def):
                    defender = (None, None, None)
                else:
                    if front_line_def[i_def] is not None and i_def < len(front_line_def):
                        defender = front_line_def[i_def]
                    elif front_line_def[i_def] is None and i_def < len(front_line_def):
                        defender = (None, None, None)
                    # else:
                    #     defender = min((soldier for soldier in front_line_def if soldier[1] is not None), key=lambda x: x[0], default=None)




                if defender[1] is not None : 
                    # print(f"Удар Атакующего Cолдата #{i_atack + 1} (ID: {attacker[0]}, ХР: {attacker[1]}, Урон: {attacker[2]}) на Защитника #{i_def + 1} (ID: {defender[0]} ХР: {defender[1]})")
                    
                    defender_health = defender[1] - attacker[2]
                    front_line_def[i_def] = (defender[0], defender_health, defender[2])

                    # print(f"XP Защитника #{i_def + 1} (ID: {defender[0]}): {defender[1]} --> {defender_health}")
                    if defender_health <= 0:
                        # print(Fore.RED + f"Защитник {i_def + 1} (ID: {defender[0]}) повержен!" + Style.RESET_ALL)
                        front_line_def[i_def] = (defender[0], None, defender[2]) 
                else:
                    stop_iter = True
                    k = max(enumerate(front_line_def), key=lambda x: x[0])[0]
                    while k >= 0:
                        defender = front_line_def[k]
                        if defender[1] is not None :
                            # print(f"Защитника #{k + 1} (ID: {defender[0]} ХР: {defender[1]})" + Fore.RED + " АТАКУЮТ ЕЩЁ РАЗ" + Style.RESET_ALL)
                            # print(f"Удар Атакующего Cолдата #{i_atack + 1} (ID: {attacker[0]}, ХР: {attacker[1]}, Урон: {attacker[2]}) на Защитника #{k + 1} (ID: {defender[0]} ХР: {defender[1]})")
                            defender_health = defender[1] - attacker[2]
                            front_line_def[k] = (defender[0], defender_health, defender[2])
                            # print(f"XP Защитника #{k + 1} (ID: {defender[0]}): {defender[1]} --> {defender_health}")
                            if defender_health <= 0:
                                # print(Fore.RED + f"Защитник {k + 1} (ID: {defender[0]}) повержен!" + Style.RESET_ALL)
                                front_line_def[k] = (defender[0], None, defender[2]) 
                            k = -10
                            stop_iter = False
                        k -= 1
                    if stop_iter == True:
                        # print("Защитников не осталось")
                        break
                if defender_health < 0:
                    re_atack = True
                    new_damage = defender_health * (-1)
                    
                    # print(f"Cолдат #{i_atack + 1} (ID: {attacker[0]}, Урон: {attacker[2]} \t\tАтакует ЕЩЁ РАЗ") 
                else:
                    re_atack = False
                    new_damage = 0
                i_def += 1
                
                itr+=1
                if itr > 200:
                    print("ЗАЦИКЛИЛАСЬ")
                    break
            # i_def += 1
            # last_atacked_defender = front_line_def[i_1]
            # new_damage = random.randint(10, 25)
            # attacker = (attacker[0], attacker[1], new_damage)
            # if defender[1] is not None : 
            #     print(f"Удар Атакующего Cолдата #{i_atack + 1} (ID: {attacker[0]}, ХР: {attacker[1]}, Урон: {attacker[2]}) на Защитника #{i_def + 1} (ID: {defender[0]} ХР: {defender[1]})")
                
            #     defender_health = defender[1] - attacker[2]
            #     front_line_def[i_def] = (defender[0], defender_health, defender[2])

            #     print(f"XP Защитника #{i_def + 1} (ID: {defender[0]}): {defender[1]} --> {defender_health}")
            #     if defender_health <= 0:
            #         print(Fore.RED + f"Защитник {i_def + 1} (ID: {defender[0]}) повержен!" + Style.RESET_ALL)
            #         front_line_def[i_def] = (defender[0], None, defender[2]) 
            # else:
            #     stop_iter = True
            #     k = max(enumerate(front_line_def), key=lambda x: x[0])[0]
            #     while k >= 0:
            #         defender = front_line_def[k]
            #         if defender[1] is not None :
            #             print(f"Защитника #{k + 1} (ID: {defender[0]} ХР: {defender[1]})" + Fore.RED + " АТАКУЮТ ЕЩЁ РАЗ" + Style.RESET_ALL)
            #             print(f"Удар Атакующего Cолдата #{i_atack + 1} (ID: {attacker[0]}, ХР: {attacker[1]}, Урон: {attacker[2]}) на Защитника #{k + 1} (ID: {defender[0]} ХР: {defender[1]})")
            #             defender_health = defender[1] - attacker[2]
            #             front_line_def[k] = (defender[0], defender_health, defender[2])
            #             print(f"XP Защитника #{k + 1} (ID: {defender[0]}): {defender[1]} --> {defender_health}")
            #             if defender_health <= 0:
            #                 print(Fore.RED + f"Защитник {k + 1} (ID: {defender[0]}) повержен!" + Style.RESET_ALL)
            #                 front_line_def[k] = (defender[0], None, defender[2]) 
            #             k = -10
            #             stop_iter = False
            #         k -= 1
            #     if stop_iter == True:
            #         print("Защитников не осталось")
            #         break
            # i_def += 1
            # # last_atacked_defender = front_line_def[i_1]

            
        defender_group_dead_buffer = front_line_def.copy()
        

        # print("\n\n")

        front_line_def = defender_group_leave_buffer.copy()
        i_atack = 0
        # for i_def in range(len(front_line_def)):
        #     # print(f"ID: {i_def[0]}, XP: {i_def[1]}, Damage: {i_def[2]}")
        #     print(f"ID: {front_line_def[i_def][0]}, XP: {front_line_def[i_def][1]}, Damage: {front_line_def[i_def][2]}")
            
        for i_def in range(len([defender for defender in front_line_def if defender[1] is not None])):

            # try:
            #     if front_line_attack[i_atack] is not None and i_atack < len(front_line_attack):
            #         attacker = front_line_attack[i_atack]
            #     elif front_line_attack[i_atack] is None and i_atack < len(front_line_attack):
            #         attacker = (None, None, None)
            # except Exception as e:
            #     print(f"Ошибка в attacker: {e}")

            defender = front_line_def[i_def]
            if defender == (None, None, None):
                # print("Защитники кончились")
                break

            #new_damage = random.randint(3, 8)
            new_damage = New_damage(defender_group_type)
            re_atack = True
            itr = 0

            while re_atack is True:
                defender = (defender[0], defender[1], new_damage)

                if defender == (None, None, None):
                    # print("Защитники кончились")
                    break

                if i_atack + 1 > len(front_line_attack):
                    attacker = (None, None, None)
                else:
                    if front_line_attack[i_atack] is not None and i_atack < len(front_line_attack):
                        attacker = front_line_attack[i_atack]
                    elif front_line_attack[i_atack] is None and i_atack < len(front_line_attack):
                        attacker = (None, None, None)
                    # else:
                    #     attacker = min((soldier for soldier in front_line_attack if soldier[1] is not None), key=lambda x: x[0], default=None)


                if attacker[1] is not None:
                    # print(f"Атака Защищающегося солдата #{i_def + 1} (ID: {defender[0]}, ХР: {defender[1]}, Урон: {defender[2]}) на Атакующего {i_atack + 1} (ID: {attacker[0]} ХР: {attacker[1]}):")

                    attacker_health = attacker[1] - defender[2]
                    front_line_attack[i_atack] = (attacker[0], attacker_health, attacker[2])

                    # print(f"XP Атакующего #{i_atack + 1} ID: {attacker[0]}: {attacker[1]} --> {attacker_health}")
                    if attacker_health <= 0:
                        # print(Fore.RED + f"Атакующий #{i_atack + 1} (ID: {attacker[0]}) повержен!" + Style.RESET_ALL)
                        front_line_attack[i_atack] = (attacker[0], None, attacker[2]) 
                else:
                    stop_iter = True
                    k = max(enumerate(front_line_attack), key=lambda x: x[0])[0]
                    while k >= 0:
                        attacker = front_line_attack[k]
                        if attacker[1] is not None :
                            # print(f"Атакующего #{k + 1} (ID: {attacker[0]} ХР: {attacker[1]})" + Fore.RED + " АТАКУЮТ ЕЩЁ РАЗ" + Style.RESET_ALL)
                            # print(f"Удар Защищающегося Cолдата #{i_def + 1} (ID: {defender[0]}, ХР: {defender[1]}, Урон: {defender[2]}) на Атакующего #{k + 1} (ID: {attacker[0]} ХР: {attacker[1]})")
                            attacker_health = attacker[1] - defender[2]
                            front_line_attack[k] = (attacker[0], attacker_health, attacker[2])
                            # print(f"XP Атакующего #{k + 1} (ID: {attacker[0]}): {attacker[1]} --> {attacker_health}")
                            if attacker_health <= 0:
                                # print(Fore.RED + f"Атакующий {k + 1} (ID: {attacker[0]}) повержен!" + Style.RESET_ALL)
                                front_line_attack[k] = (attacker[0], None, attacker[2]) 
                            k = -10
                            stop_iter = False
                        k -= 1
                    if stop_iter == True:
                        # print("Атакующих не осталось")
                        break
                if attacker_health < 0:
                    re_atack = True
                    new_damage = attacker_health * (-1)
                    
                    # print(f"Cолдат #{i_def + 1} (ID: {defender[0]}, Урон: {defender[2]} \t\tАтакует ЕЩЁ РАЗ") 
                else:
                    re_atack = False
                    new_damage = 0
                i_atack += 1

                itr+=1
                if itr > 200:
                    print("ЗАЦИКЛИЛАСЬ")
                    break

        front_line_def = defender_group_dead_buffer.copy()
        # print("\n\n")

        # count_MY_dead = 0
        # count_Enemy_dead = 0

        # # Вывод состояния групп после раунда
        # print("\nСостояние Атакующей Группы:")
        # for index, data in enumerate(front_line_attack, start=1):
        #     # print(f"\t\tМой Солдат {index}: ID = {data[0]} XP = {data[1]}, Damage = {data[2]}")
        #     if data[1] is None:
        #         count_MY_dead += 1
        # print(f"Мертвых: {count_MY_dead}/{len(front_line_attack)}")

        # print("\nСостояние Защищающейся группы:")
        # for index, data in enumerate(front_line_def, start=1):
        #     # print(f"\t\tСолдат Противника {index}: ID = {data[0]} XP = {data[1]}, Damage = {data[2]}")
        #     if data[1] is None:
        #         count_Enemy_dead += 1
        # print(f"Мертвых: {count_Enemy_dead}/{len(front_line_def)}")
        # print("\n\n")


        # ДЕЛАЕМ ЗАМЕНЫ
        # Замена мертвых атакующих
        new_front_line_attack = []
        for soldier in front_line_attack:
            id, xp, damage = soldier
            if xp is None and attacker_group:
                new_soldier = min(attacker_group, key=lambda x: (x[0] is not None, x[0]))
                #print(f"Замена Атакующего - ID {id} --> {new_soldier}")
                new_front_line_attack.append(tuple(new_soldier))
                attacker_group.remove(new_soldier)
            else:
                new_front_line_attack.append(soldier)
        

        # Замена мертвых защитников
        new_front_line_def = []
        for soldier in front_line_def:
            id, xp, damage = soldier
            if xp is None and defender_group:
                new_soldier = min(defender_group, key=lambda x: (x[0] is not None, x[0]))
                # print(f"Замена Защитника - ID {id} --> {new_soldier}")
                new_front_line_def.append(tuple(new_soldier))
                defender_group.remove(new_soldier)
            else:
                new_front_line_def.append(soldier)

        front_line_attack = new_front_line_attack
        front_line_def = new_front_line_def
        
        # for i, (id, xp, damage) in enumerate(front_line_attack, start=0):
        #     if xp is None:
        #         if attacker_group:
        #             new_soldier = min(attacker_group, key=lambda x: (x[0] is not None, x[0]))   # Находим нового солдата с минимальным ID и XP не равным None
        #             print(f"Замена Атакующего -  ID {front_line_attack[i]} --> {new_soldier}")
        #             front_line_attack[i] = (new_soldier[0], new_soldier[1], new_soldier[2])   # Заменяем мертвого солдата на нового
        #             attacker_group.remove(new_soldier) # Удаляем найденного солдата из attacker_group   
        #         else:
        #             print("У Атакующего Запас закончися!")
        #             print(f"Был удален ID {front_line_attack[i]}")
        #             front_line_attack.remove(front_line_attack[i])
        # print("\n")
        # for i, (id, xp, damage) in enumerate(front_line_def, start=0):
        #     if xp is None:
        #         if defender_group:
        #             new_soldier = min(defender_group, key=lambda x: (x[0] is not None, x[0]))   
        #             print(f"Замена Защитника -  ID {front_line_def[i]} --> {new_soldier}")
        #             front_line_def[i] = (new_soldier[0], new_soldier[1], new_soldier[2])  
        #             defender_group.remove(new_soldier) 
        #         else:
        #             print("У Защитника Запас закончися!")
        #             print(f"Был удален ID {front_line_def[i]}")
        #             front_line_def.remove(front_line_def[i])
        # print("\n-----------------------\n")


        # print(f"\nАтакующие запас:")
        # for index, data in enumerate(attacker_group, start=1):
        #     print(f"\t\tМой Солдат: ID = {data[0]} XP = {data[1]}, Damage = {data[2]}")
        # print(f"\nЗащитники запас:")
        # for index, data in enumerate(defender_group, start=1):
        #     print(f"\t\tСолдат Врага: ID = {data[0]} XP = {data[1]}, Damage = {data[2]}")
        # print("\n-----------------------------------------------------\n")

        alive_group_1 = any(attacker[1] is not None for attacker in front_line_attack)
        alive_group_2 = any(defender[1] is not None for defender in front_line_def)
        # print(f"1 группа живет - {alive_group_1}")
        # print(f"2 группа живет - {alive_group_2}")

        # ПРОВЕРКА
        for i in range(len(front_line_attack)):
            if(len(front_line_attack) <= 0 or len(front_line_def) <= 0 or alive_group_1 == False or alive_group_2 == False):
                The_end_result(front_line_attack, attacker_group, start_count_attacker_group, front_line_def, defender_group, start_count_defender_group)
                if alive_group_1 == False and alive_group_2 == False:
                    print(Fore.BLUE + f"Победителей НЕТ - НИЧЬЯ" + Style.RESET_ALL)
                    return "All dead"
                elif(len(front_line_def) <= 0) or alive_group_2 == False:
                    print(Fore.BLUE + f"Атакующие ВЫЙГРАЛИ!" + Style.RESET_ALL)
                    return "atack"
                else:
                    print(Fore.BLUE + f"Защитники ВЫЙГРАЛИ!" + Style.RESET_ALL)
                    return "def"




def The_end_result(front_line_attack, attacker_group, start_count_attacker_group, front_line_def, defender_group, start_count_defender_group):

    # Подсчет живых солдат 
    count_attack_soldiers = sum(1 for soldier in front_line_attack if soldier[1] is not None) + sum(1 for soldier in attacker_group if soldier[1] is not None)
    count_def_soldiers = sum(1 for soldier in front_line_def if soldier[1] is not None) + sum(1 for soldier in defender_group if soldier[1] is not None)

    # alive_soldiers_front_line_def = sum(1 for soldier in front_line_def if soldier[1] is not None)
    # alive_soldiers_defender_group = sum(1 for soldier in defender_group if soldier[1] is not None)

    # ALL_alive_attacker_soldiers = count_attack_soldiers + count_def_soldiers
    # ALL_alive_defender_soldiers = alive_soldiers_front_line_def + alive_soldiers_defender_group

    print(f"Живых солдат из 1 группы: {count_attack_soldiers} из {start_count_attacker_group}")
    print(f"Живых солдат из 2 группы: {count_def_soldiers} из {start_count_defender_group}")




# Процесс битвы

# print("Мой отряд:")
# for index, data in enumerate(my_group, start=1):
#     print(f"Мой солдат {index}: ID = {data[0]} XP = {data[1]},     Урон = {data[2]}")

# print(f"\n\n")

# print("Отряд противника:")
# for index, data in enumerate(enemy_group, start=1):
#     print(f"Противник {index}: ID = {data[0]} XP = {data[1]},     Урон = {data[2]}")
# print(f"\n\n")

print("Начало:")

# itog = battle(my_group, enemy_group)
itog = battle(enemy_group, enemy_Foot.type, my_group, my_Foot.type)

print(f"\n\n\nИТОГ: побеза за {itog}")



















