class Enemy:
    life = 3

    def attack(self):
        print("OUCH!")
        self.life -= 1


    def check_life(self):
        if self.life <= 0:
            print("Enemy destroyed!!!")
        else:
            print(str(self.life) + " lives left.")


bot1 = Enemy()
bot2 = Enemy()
bot3 = Enemy()

bot1.attack()
bot1.check_life()
