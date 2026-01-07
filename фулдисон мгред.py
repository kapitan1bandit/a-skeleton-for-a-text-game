#импорт всех библиотек и модулей
import colorama, time, random, sys
from colorama import Fore
colorama.init()
#постепенный вывод строк с задержкой 2 сек
print(Fore.YELLOW +"\nЛегенды веками шептались о подземелье, что скрывается в разломах Древних Гор.",)
time.sleep(2)
print("\nГоворили, что каждый камень здесь помнит шаги искателей, но лишь единицы возвращались…",)
time.sleep(2)
print("\nА те, что возвращались, несли с собой шёпот о несметных сокровищах, спрятанных в самом сердце бездны.",)
time.sleep(3)
print("\n" * 10)

#переменные игрока
health = 100
money = 0

#функция боёвки
def battle(health, agility, strength, health_enemy, armor_enemy, attack_enemy, name_enemy):
    while health > 0 and health_enemy > 0:

        #интерфейс
        print(f""" 

                   [ты]                                      [{name_enemy}]                

                  ❤ {health}︎                                   ❤ {health_enemy}      
                  ⛨ {agility}                                       ⛨ {armor_enemy}                      
                  ⚔ {(strength + agility) / 2}                                      ⚔ {attack_enemy}

                  [1] атаковать
                  """)
        #логика боя
        write_you = input()
        if write_you == "1":
            if random.randint(1, 6) * ((strength + agility) / 2) >= armor_enemy:
                hit = "попали"
                health_enemy -= random.randint(1, 6) * (strength / 2)
            else: hit = "не попали"
            print("вы:" + hit)
        else:
            print("вы ничего не сделали")
        if random.randint(1, 6) * (attack_enemy / 2) >= agility:
            print(f"враг:{name_enemy} попал по вам")
            health -= random.randint(1, 6) * (attack_enemy / 2)

        else:
            print(f"враг{name_enemy} не попал по вам")

    #логика выхода из боя
    if health_enemy <= 0:
        print(f"враг {name_enemy} погиб")
    else:
        sys.exit("вы проиграли")

    return health



#класс враг
class Enemy:
    def __init__(self, health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy):
        self.health_enemy = health_enemy
        self.armor_enemy = armor_enemy
        self.attack_enemy = attack_enemy
        self.danger_enemy = danger_enemy
        self.name_enemy = name_enemy

    def get_stats(self):
        return self.health_enemy, self.armor_enemy, self.attack_enemy, self.danger_enemy, self.name_enemy
#создание крысы
rat = Enemy(5,10,2,1,"крыса")
#создание гоблина
goblin = Enemy(30, 15, 8, 4, "Гоблин")
#создание крысы
skeleton = Enemy(20, 12, 6, 3, "Скелет")

#функция с распределением очков навыков игрока
def points_distribution():
    points = 21
    strength = 0
    perception = 0
    endurance = 0
    charisma = 0
    intelligence = 0
    agility = 0
    luck = 0
    list_ability_name = ["си", "во", "вы", "ха", "ин", "ло", "уд"]
    list_ability = [strength, perception, endurance, charisma, intelligence, agility, luck]
    while points > 0:
        print(f"""
         
            
         
         
         
         
         
        ты имеешь { points} очков персонажа 
        
        СИЛА          [{list_ability[0]}]                      
        ВОСПРИЯТИЕ    [{list_ability[1]}]        
        ВЫНОСЛИВОСТЬ  [{list_ability[2]}]
        ХАРИЗМА       [{list_ability[3]}]
        ИНТЕЛЛЕКТ     [{list_ability[4]}]
        ЛОВКОСТЬ      [{list_ability[5]}]
        УДАЧА         [{list_ability[6]}]
        
        !!!введи ПЕРВЫЕ ДВЕ буквы параметра,[Enter], а потом то, сколько очков ты хочешь прибавить к характеристике, [Enter]!!!
        
               ??? си [Enter] 4 [Enter] ???
                   во [Enter] 5 [Enter]
                   вы [Enter] 2 [Enter]
                   ... 
                   
                   
               
               
               
               
               
                        """)
        write_you = input().lower()
        if write_you in list_ability_name[:]:
            list_ability[list_ability_name.index(write_you)] += int(input())
            points -= list_ability[list_ability_name.index(write_you)]

    return list_ability



#вызов функции распределения очков игрока
list_ability = points_distribution()



#путешествие
input("\nты начал своё путешествие в подземелье")
if list_ability[1] > 4:
    input("\nох, какая удача! на земле валялся не использованный факел. он даст тепе [+ 2 к ВОСПРИЯТИЕ]")
    list_ability[1] += 2
if list_ability[1] > 5:
    input("\nв далеке ты заметил два приближающихся огонька. КАЖЕТСЯ ЭТО КРЫСА")
else:
     health -= 10
     input("\n из темноты на тебя набросилось что-то маленькое и укусило за ногу")
input("\n начался бой с крысой")


#бой с крысой
health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = rat.get_stats()
health = battle(health, list_ability[5], list_ability[0], health_enemy, armor_enemy, attack_enemy, name_enemy)
money = ((danger_enemy + 2) * list_ability[6]) // 2
print(f"твоё здоровье: {health}")
print(f"твои деньги: {money}")

#путешествие
input(f"\nвы отправились дальше в темноту ")

input(f"\nАААААААААААААААААААА ДА НУ НАХУЙ ГИГАНТСКАЯ ОРДА ГОБЛИНОВ БЛЯЯЯЯЯЯЯ")

input(f"\nХХХХАХАХАХХАХАХАХАХ ТЕБЯ ГОБЛИНЫ ПО КРУГУ ПУСЬТЯТ ЧМОООО")

health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = goblin.get_stats()
health = battle(health, list_ability[5], list_ability[0], health_enemy, armor_enemy, attack_enemy, name_enemy)
money = ((danger_enemy + 2) * list_ability[6]) // 2


health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = goblin.get_stats()
health = battle(health, list_ability[5], list_ability[0], health_enemy, armor_enemy, attack_enemy, name_enemy)
money = ((danger_enemy + 2) * list_ability[6]) // 2


health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = goblin.get_stats()
health = battle(health, list_ability[5], list_ability[0], health_enemy, armor_enemy, attack_enemy, name_enemy)
money = ((danger_enemy + 2) * list_ability[6]) // 2


health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = goblin.get_stats()
health = battle(health, list_ability[5], list_ability[0], health_enemy, armor_enemy, attack_enemy, name_enemy)
money = ((danger_enemy + 2) * list_ability[6]) // 2


health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = goblin.get_stats()
health = battle(health, list_ability[5], list_ability[0], health_enemy, armor_enemy, attack_enemy, name_enemy)
money = ((danger_enemy + 2) * list_ability[6]) // 2













