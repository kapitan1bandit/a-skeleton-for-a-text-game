class Enemy:
    def  __init__(self,health_enemy,armor_enemy,attack_enemy,danger_enemy,enemy):
        self.health_enemy = health_enemy
        self.armor_enemy = armor_enemy
        self.attack_enemy = attack_enemy
        self.danger_enemy = danger_enemy
        self.enemy = enemy
    def show_stats(self):
        print(f"=== {self.enemy.upper()} ===")
        print(f"❤ Здоровье: {self.health_enemy}")
        print(f"🛡 Броня: {self.armor_enemy}")
        print(f"⚔ Атака: {self.attack_enemy}")
        print(f"⚠ Опасность: {self.danger_enemy}")

rat = Enemy(10,5,2,1,"крыса",)
skeleton = Enemy(25, 8, 6, 3, "скелет")
goblin = Enemy(30, 10, 8, 4, "гоблин")

rat.show_stats()
#health_enemy armor_enemy attack_enemy danger_enemy enemy