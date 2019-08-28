from copy import deepcopy


class NotEnoughManaError(NotImplementedError):
    pass


class EffectAlreadyAppliedError(NotImplementedError):
    pass


class Mob:
    def __init__(self, hp, dmg=0, armor=0, mana=0):
        self.hp = hp
        self.dmg = dmg
        self.armor = armor
        self.mana = mana
        self.effects = []
        self.casted_spells = []
        self.mana_spend = 0

    def alive(self):
        return self.hp > 0

    def cast(self, spell_name, target):
        if spell_name.cost > self.mana:
            raise NotEnoughManaError
        spell_name.casted(self, target)
        self.mana -= spell_name.cost
        self.mana_spend += spell_name.cost
        self.casted_spells.append(spell_name.__class__.__name__)

    def turn(self):
        for effect in self.effects:
            if effect.duration > 0:
                if effect.__class__ == Recharge:
                    self.mana += effect.manareg
                self.hp = self.hp - effect.dmg + effect.heal
                effect.duration -= 1
            if effect.duration == 0:
                if effect.__class__ == Shield:
                    self.armor = 0
                self.effects.remove(effect)
            elif effect.duration < 0:
                raise NotImplementedError


class Hero(Mob):
    pass


class Boss(Mob):
    pass


class Spell:
    def __init__(self, cost=0, dmg=0, heal=0):
        self.cost = cost
        self.dmg = dmg
        self.heal = heal

    def casted(self, caster, target):
        caster.hp += self.heal
        target.hp -= self.dmg


class Effect(Spell):
    def __init__(self, cost, duration, *, dmg=0, heal=0):
        self.duration = duration
        super().__init__(cost=cost, dmg=dmg, heal=heal)

    def casted(self, caster, target):
        if self.__class__ not in map(lambda x: x.__class__, target.effects):
            target.effects.append(self)
        else:
            raise EffectAlreadyAppliedError


# добавляю заклинания из нашей задачи
class BasicAttack(Spell):
    def casted(self, caster, target):
        target.hp -= max(1, caster.dmg - target.armor)


class MagicMissile(Spell):
    def __init__(self, cost=53, dmg=4, heal=0):
        super().__init__(cost=cost, dmg=dmg, heal=heal)


class Drain(Spell):
    def __init__(self, cost=73, dmg=2, heal=2):
        super().__init__(cost=cost, dmg=dmg, heal=heal)


class Shield(Effect):
    def __init__(self, cost=113, duration=6, armor=7, dmg=0, heal=0):
        self.armor = armor
        super().__init__(cost=cost, dmg=dmg, heal=heal, duration=duration)

    def casted(self, caster, target):
        super().casted(caster, caster)
        caster.armor = self.armor


class Poison(Effect):
    def __init__(self, cost=173, duration=6, dmg=3, heal=0):
        super().__init__(cost=cost, duration=duration, dmg=dmg, heal=heal)


class Recharge(Effect):
    def __init__(self, cost=229, duration=5, dmg=0, heal=0, manareg=101):
        self.manareg = manareg
        super().__init__(cost=cost, duration=duration, dmg=dmg, heal=heal)

    def casted(self, caster, target):
        super().casted(caster, caster)


all_spells = (MagicMissile, Drain, Shield, Poison, Recharge)


def is_viable(caster, target, spell):
    spell = spell()
   # cache_state = deepcopy(state)
    cache_caster = deepcopy(caster)
    cache_target = deepcopy(target)
    if spell.cost > cache_caster.mana:
        return False, [caster, target]
    cache_caster.turn()
    cache_target.turn()
    if (spell.__class__ in map(lambda x: x.__class__, cache_target.effects)
    or  spell.__class__ in map(lambda x: x.__class__, cache_caster.effects)):
        return False, [caster, target]
    cache_caster.cast(spell, cache_target)
    if not cache_target.alive():
        return '{} defeated'.format(cache_target.__class__.__name__), [cache_caster, cache_target]
    return True, [cache_caster, cache_target]


def new_states(states_):
    won_fights = []
    cache_states = []
    for state in states_:
        for spell in all_spells:
            result, cache_state = is_viable(*state, spell)
            if result == 'Boss defeated':
                won_fights.append(cache_state)
            elif result:
                result, cache_state = is_viable(*cache_state[::-1], BasicAttack)
                if result != 'Hero defeated':
                    cache_states.append(cache_state[::-1])
    return cache_states, won_fights


hero = Hero(hp=50, mana=500)
boss = Boss(hp=58, dmg=9)
states = [[hero, boss]]
wins = []
while states:
    states, wins_cache = new_states(states)
    wins.extend(wins_cache)
    print('States:', len(states), 'Boss defeated:', len(wins))
min_mana_spend = 100000
for win in wins:
    print(win[0].hp, win[0].casted_spells, win[0].mana_spend, win[0].mana)
    mana_spend = win[0].mana_spend
    if mana_spend < min_mana_spend:
        min_mana_spend = mana_spend
        spell_queue = win[0].casted_spells
print(spell_queue, min_mana_spend)
