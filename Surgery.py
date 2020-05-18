import random


class Surgeon:
    pass


class Patient:
    def __init__(self, first, last, transplant):
        self.first = first
        self.last = last
        self.transplant = transplant


class Kidney:
    # print random number
    chance = random.randint(0, 9)
    pass


patient_a = Patient('Adam', 'Cole', 'Kidney')
patient_b = Patient('Mary', 'Jones', 'Kidney')

