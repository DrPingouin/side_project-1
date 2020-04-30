from __future__ import annotations
from dataclasses import dataclass, field, InitVar
from RPG.Class.character import Character_ff


@dataclass
class Character:
    '''
    Upgrade : transform attribute variable to dict or array
    '''
    name: str = "Blob"
    is_in_fight: bool = False
    fighting_with: Character = None
    max_life: int = 10
    attk_point: int = 1
    def_point: int = 1
    magick_point: int = 1
    dex_point: int = 1

    def __post_init__(self):
        self.life_point = self.max_life

    def on_attack(self, receiver: Character) -> None:
        """
        if damage is int do damage else print miss
        :param receiver:
        :return: None
        """
        damage = Character_ff.calc_attack(self, receiver)
        if isinstance(damage, int):
            Character_ff.deal_damage(receiver, damage)
        else:
            print(f'attacker : {self.name} {damage}')
        return None

    def on_death(self):
        pass
        '''put del() into monster
        def del(self):
           print('Destructor called, vehicle deleted.')'''
