from collections import deque


class Puzzle(object):
    @classmethod
    def resolve_part_01(cls, data):
        data = data[0]
        buffer = deque()
        buffer_size = 4
        for idx, c in enumerate(data):
            buffer.append(c)
            if len(buffer) < buffer_size:
                continue
            elif len(buffer) == buffer_size:
                if len(set(buffer)) == buffer_size:
                    return idx + 1
                else:
                    buffer.popleft()

    @classmethod
    def resolve_part_02(cls, data):
        data = data[0]
        buffer = deque()
        buffer_size = 14
        for idx, c in enumerate(data):
            buffer.append(c)
            if len(buffer) < buffer_size:
                continue
            elif len(buffer) == buffer_size:
                if len(set(buffer)) == buffer_size:
                    return idx + 1
                else:
                    buffer.popleft()
