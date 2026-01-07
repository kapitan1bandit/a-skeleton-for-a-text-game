class Enemy:
    def __init__(self, health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy):
        self.health_enemy = health_enemy
        self.armor_enemy = armor_enemy
        self.attack_enemy = attack_enemy
        self.danger_enemy = danger_enemy
        self.name_enemy = name_enemy

    def get_stats(self):
        return self.health_enemy, self.armor_enemy, self.attack_enemy, self.danger_enemy, self.name_enemy

rat = Enemy(5,10,2,1,"крыса")

health_enemy, armor_enemy, attack_enemy, danger_enemy, name_enemy = rat.get_stats()
