__author__ = '<a href="khalasi@gmail.com">Naresh Khalasi</a>'

class Game:
    def __init__(self):
        self._rolls = []
        self._score = 0
        self._current_roll_idx = 0
    def roll(self, pins_knocked):
        self._rolls.append(Roll([self._current_roll_idx], pins_knocked))
        self._current_roll_idx += 1
    @property
    def score(self):
        score = 0
        roll_idx = 0
        for _ in range(10):
            curr_roll = self._rolls[roll_idx]
            if is_strike(curr_roll):
                print('\o/ S t r i k e')
                score += 10 + strike_bonus(self._rolls[roll_idx+1], self._rolls[roll_idx+2])
                roll_idx += 1
            elif is_spare(curr_roll, self._rolls[roll_idx+1]):
                print('\o/ S p a r e')
                score += 10 + spare_bonus(self._rolls[roll_idx+2])
                roll_idx += 2
            else:
                score += curr_roll.score + self._rolls[roll_idx+1].score
                roll_idx += 2
        return score
    def __repr__(self):
        return 'Game[Rolls:{}, Score:{}]'.format(self._rolls, self.score)

class Roll:
    def __init__(self, id, pins_knocked):
        self.id = id
        self._score = pins_knocked
    @property
    def score(self):
        return self._score
    def __repr__(self):
        return 'Roll[id={}, score={}]'.format(self.id, self._score)

def is_strike(roll):
    return roll.score == 10

def is_spare(roll1, roll2):
    return roll1.score + roll2.score == 10

def strike_bonus(roll1, roll2):
    return roll1.score + roll2.score

def spare_bonus(roll):
    return roll.score

