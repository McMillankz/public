class Player():
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.intel = 0
        self.strenght = 0
        self.endurance = 0

    def role_choose(self):
        choose = False
        while choose is False:
            role = input("Выберите роль (Воин, Маг, Разбойник): ").lower()
            if role == "воин":
                with open(r'C:\Users\mcmil\OneDrive\Documents\1. Game\warrior.py', encoding='utf-8') as f:
                    code = f.read()
                exec(code)
                choose = True
            elif role == "маг":
                with open(r'C:\Users\mcmil\OneDrive\Documents\1. Game\mage.py', encoding='utf-8') as f:
                    code = f.read()
                exec(code)
                choose = True
            elif role == "разбойник": 
                with open(r'C:\Users\mcmil\OneDrive\Documents\1. Game\rogue.py', encoding='utf-8') as f:
                    code = f.read()
                exec(code)
                choose = True
            else:
                print (f"Ты не можешь выбрать роль {role}, он слишко опасен для наших земель. Давай лучше выберем из доступных вариантов.")
        
class PathChoose:
    def __init__(self, player):
        self.player = player
        self.end_story = False

    def player_path(self):
        if self.end_story is True:
            quit (f"Твоя история {player.role}а завершена, {player.name}.")
        else:
            self.path_1()
        if self.end_story is True:
            quit (f"Твоя история {player.role}а завершена, {player.name}.")
        else:
            self.path_2()
        if self.end_story is True:
            quit (f"Твоя история {player.role}а завершена, {player.name}.")
        else:
            self.path_end()

    def path_1(self):
        with open(r"C:\Users\mcmil\OneDrive\Documents\1. Game\path_1.txt", 'r', encoding="utf-8") as file:
            lines = file.readline().split("\\n")
            choose_lines = file.readlines()
            for line in lines:
                print(line)
        path = int(input("Ваш выбор: "))
        if path == 1 and player.endurance < 10:
            self.end_story = True
            print(choose_lines[0])
        elif path == 1 and player.endurance == 10:
             print(choose_lines[1])
        elif path == 2:
             print(choose_lines[2])
        
        
    def path_2(self):
        with open(r"C:\Users\mcmil\OneDrive\Documents\1. Game\path_2.txt", 'r', encoding="utf-8") as file:
            lines = file.readline().split("\\n")
            choose_lines = file.readlines()
            for line in lines:
                print(line)
        path = int(input("Ваш выбор: "))
        if path == 1 and player.strenght < 10:
            self.end_story = True
            print(choose_lines[0])
        elif path == 1 and player.strenght == 10:
             print(choose_lines[1])
        elif path == 2:
             print(choose_lines[2])

    def path_end(self):
        with open(r"C:\Users\mcmil\OneDrive\Documents\1. Game\path_end.txt", 'r', encoding="utf-8") as file:
            lines = file.readline().split('\\n')
            for line in lines:
                print(f"{line}")

name = input("Введите ваше имя: ")
player = Player(name, "")
player.role_choose()

path_choose = PathChoose(player)

path_choose.player_path()