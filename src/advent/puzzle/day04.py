class Puzzle(object):

    @classmethod
    def resolve_part_01(cls, data):
        score = 0
        for pair in data:
            scope1, scope2 = pair.split(",")
            s1_in, s1_out = [int(s) for s in scope1.split("-")]
            s2_in, s2_out = [int(s) for s in scope2.split("-")]
            scope1 = set(range(s1_in, s1_out + 1))
            scope2 = set(range(s2_in, s2_out + 1))
            intersection = scope1.intersection(scope2)
            if intersection == scope1 or intersection == scope2:
                score += 1
        return score

    @classmethod
    def resolve_part_02(cls, data):
        score = 0
        for pair in data:
            scope1, scope2 = pair.split(",")
            s1_in, s1_out = [int(s) for s in scope1.split("-")]
            s2_in, s2_out = [int(s) for s in scope2.split("-")]
            scope1 = set(range(s1_in, s1_out + 1))
            scope2 = set(range(s2_in, s2_out + 1))
            if scope1 & scope2:
                score += 1
        return score



