from advent.io import read


class Puzzle(object):

    @classmethod
    def resolve_part_01(cls, data):
        max_cals = 0
        current_cals = 0
        for cal in data:
            if cal:
                current_cals += int(cal)
            else:
                max_cals = max(max_cals, current_cals)
                current_cals = 0
        return max_cals

    @classmethod
    def resolve_part_02(cls, data):
        summed_cals = []
        current_cals = 0
        for cal in data:
            if cal:
                current_cals += int(cal)
            else:
                summed_cals.append(current_cals)
                current_cals = 0
        else:
            summed_cals.append(current_cals)
            current_cals = 0
        return sum(sorted(summed_cals)[::-1][:3])