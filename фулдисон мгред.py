#импорт всех библиотек и модулей
import colorama, time, random, sys
from colorama import Fore, Back
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
xp = 100
Strength = 0
Perception = 0
Endurance = 0
Charisma = 0
Intelligence = 0
Agility = 0
Luck = 0
money = 0
#переменные монстров
enemy = ""
xp_enemy = 0
armor_enemy = 0
attack_enemy = 0
danger_enemy = 0
#переменные игры
write_you = "-1"
#функция боёвки
def battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy):
    while xp > 0 and xp_enemy > 0:
        xp -= 10
        #интерфейс
        print(f""" 

                   [ты]                                      [{enemy}]                

                  ❤ {xp}︎                                   ❤ {xp_enemy}      
                  ⛨ {Agility}                                       ⛨ {armor_enemy}                      
                  ⚔ {(Strength + Agility) / 2}                                      ⚔ {attack_enemy}

                  [1] атаковать
                  """)
        #логика боя
        write_you = input()
        if write_you == "1":
            if random.randint(1, 6) * ((Strength + Agility) / 2) >= armor_enemy:
                hit = "попали"
                xp_enemy -= random.randint(1, 6) * ((Strength + Agility) / 2)
            else: hit = "не попали"
            print("вы:" + hit)
        else:
            print("вы ничего не сделали")
        if random.randint(1, 6) * ((attack_enemy) / 2) >= Agility:
            print(f"враг:{enemy} попал по вам")
        else:
            print(f"враг{enemy} не попал по вам")

    #логика выхода из боя
    if xp_enemy <= 0:
        print(f"враг {enemy} погиб")
    else:
        sys.exit("вы проиграли")

    return xp



#функция крысы
def rat():
    enemy = "крыса"
    xp_enemy = 5
    armor_enemy = 10
    attack_enemy = 2
    danger_enemy = 1
    return enemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy


#функция с распределением очков навыков игрока
def points_distribution():
    points = 21
    Strength = 0
    Perception = 0
    Endurance = 0
    Charisma = 0
    Intelligence = 0
    Agility = 0
    Luck = 0
    while points > 0 or points < 0:
         print(f"""
         
            
         
         
         
         
         
    ты имеешь { points} очков персонажа 
    
    СИЛА          [{Strength}]                      
    ВОСПРИЯТИЕ    [{Perception}]        
    ВЫНОСЛИВОСТЬ  [{Endurance}]
    ХАРИЗМА       [{Charisma}]
    ИНТЕЛЛЕКТ     [{Intelligence}]
    ЛОВКОСТЬ      [{Agility}]
    УДАЧА         [{Luck}]
    
    !!!введи ПЕРВЫЕ ДВЕ буквы параметра,[Enter], а потом то, сколько очков ты хочешь прибавить к характеристике, [Enter]!!!
    
           ??? СИ [Enter] 4 [Enter] ???
               ВО [Enter] 5 [Enter]
               ВЫ [Enter] 2 [Enter]
               ... 
               
               
               
               
               
               
               
                        """)
         write_you = input()
         if str(write_you) == "СИ":
             write_you = input()
             Strength += int(write_you)
             points -= int(write_you)
         elif str(write_you) == "ВО":
             write_you = input()
             Perception += int(write_you)
             points -= int(Perception)
         elif str(write_you) == "ВЫ":
             write_you = input()
             Endurance += int(write_you)
             points -= int(Endurance)
         elif str(write_you) == "ХА":
             write_you = input()
             Charisma += int(write_you)
             points -= int(Charisma)
         elif str(write_you) == "ИН":
             write_you = input()
             Intelligence += int(write_you)
             points -= int(Intelligence)
         elif str(write_you) == "ЛО":
             write_you = input()
             Agility += int(write_you)
             points -= int(Agility)
         elif str(write_you) == "УД":
             write_you = input()
             Luck += int(write_you)
             points -= int(Luck)
         else: print("It's okay, try again")

    return Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck



#вызов функции распределения очков игрока
Strength, Perception, Endurance, Charisma, Intelligence, Agility, Luck = points_distribution()



#путешествие
input("\nты начал своё путешествие в подземелье")
if Perception > 4:
    input("\nох, какая удача! на земле валялся не использованный факел. он даст тепе [+ 2 к ВОСПРИЯТИЕ]")
    Perception += 2
if Perception > 5:
    input("\nв далеке ты заметил два приближающихся огонька. КАЖЕТСЯ ЭТО КРЫСА")
else:
     xp -= 10
     input("\n из темноты на тебя набросилось что-то маленькое и укусило за ногу")
input("\n начался бой с крысой")


#бой с крысой
enemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")

#путешествие
input(f"\nвы отправились дальше в темноту ")

print(f"\nАААААААААААААААААААА ДА НУ НАХУЙ ГИГАНТСКАЯ ОРДА КРЫС БЛЯЯЯЯЯЯЯ")

nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
nemy, xp_enemy, armor_enemy, attack_enemy, danger_enemy = rat()
xp = battle(xp,Agility,Strength,xp_enemy,armor_enemy,attack_enemy,enemy)
money = ((danger_enemy + 2) * Luck) // 2
print(f"твоё здоровье: {xp}")
print(f"твои деньги: {money}")
















