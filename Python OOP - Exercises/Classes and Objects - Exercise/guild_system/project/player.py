class Player:
    def __init__(self,name: str, hp: int, mp: int):
        self.mp = mp
        self.hp = hp
        self.name = name
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}"
        for skill_name, mana_cost in self.skills.items():
            result += f"\n==={skill_name} - {mana_cost}"
        return result
