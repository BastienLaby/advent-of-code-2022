def mult_list(l):
    result = 1
    for x in l:
        result = result * x
    return result


class Puzzle(object):
    @classmethod
    def resolve_part_01(cls, data):
        width = len(data[0])
        height = len(data)
        visible_trees = 0
        for i, row in enumerate(data):
            for j, tree in enumerate(row):
                trees_to_left = row[0:j]
                trees_to_right = row[j + 1 : width]
                trees_to_top = [data[r][j] for r in range(i)]
                trees_to_bottom = [data[r][j] for r in range(i + 1, height)]
                # visible from left
                if not trees_to_left or max(trees_to_left) < tree:
                    visible_trees += 1
                    continue
                # visible from right
                if not trees_to_right or max(trees_to_right) < tree:
                    visible_trees += 1
                    continue
                # visible from top
                if not trees_to_top or max(trees_to_top) < tree:
                    visible_trees += 1
                    continue
                # visible from bottom
                if not trees_to_bottom or max(trees_to_bottom) < tree:
                    visible_trees += 1
                    continue
        return visible_trees

    @classmethod
    def resolve_part_02(cls, data):
        width = len(data[0])
        height = len(data)
        visible_trees = 0
        scenic_scores = (
            {}
        )  # key = (i, j), value = visible trees left/right/top/bottom [l, r, t b]
        for i, row in enumerate(data):
            for j, tree in enumerate(row):
                scenic_scores[(i, j)] = [0, 0, 0, 0]
                score = scenic_scores[(i, j)]
                # left trees
                left_trees = row[0:j][::-1]
                for other_tree in left_trees:
                    score[0] += 1
                    if other_tree >= tree:
                        break
                # right trees
                right_trees = row[j + 1 : width]
                for other_tree in right_trees:
                    score[1] += 1
                    if other_tree >= tree:
                        break
                # top trees
                top_trees = [data[r][j] for r in range(i)][::-1]
                for other_tree in top_trees:
                    score[2] += 1
                    if other_tree >= tree:
                        break
                # bottom trees
                bottom_trees = [data[r][j] for r in range(i + 1, height)]
                for other_tree in bottom_trees:
                    score[3] += 1
                    if other_tree >= tree:
                        break
        return max([a * b * c * d for (a, b, c, d) in scenic_scores.values()])
