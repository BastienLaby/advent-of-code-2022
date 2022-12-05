import string

SCORES = {
    char: index + 1
    for index, char in enumerate(string.ascii_lowercase)
}
SCORES.update({
    char: index + 1 + len(string.ascii_lowercase)
    for index, char in enumerate(string.ascii_uppercase)
})


class Puzzle(object):

    @classmethod
    def resolve_part_01(cls, data):
        score = 0
        for rucksack in data:
            comp_length = len(rucksack) / 2
            comp1 = set(rucksack[:comp_length])
            comp2 = set(rucksack[comp_length:])
            mutual = (comp1 & comp2).pop()
            score += SCORES[mutual]
        return score

    @classmethod
    def resolve_part_02(cls, data):
        score = 0
        for _, rucksack in enumerate(data[::3]):
            idx = data.index(rucksack)
            ruck1 = set(rucksack)
            ruck2 = set(data[idx + 1])
            ruck3 = set(data[idx + 2])
            mutual = (ruck1 & ruck2 & ruck3).pop()
            score += SCORES[mutual]
        return score



