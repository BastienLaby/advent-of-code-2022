from collections import defaultdict, deque


class Puzzle(object):
    @classmethod
    def resolve_part_01(cls, data):
        # find number of stacks
        instructions_line_idx = None
        for idx, line in enumerate(data):
            if "1" in line:
                stack_count = int(max(line))
                instructions_line_idx = idx
                break
        # retrieve stacks
        stacks = defaultdict(deque)
        for line in data[:instructions_line_idx]:
            line = line.ljust(stack_count * 3 + stack_count - 1)
            for stack in range(stack_count):
                idx = stack * 3 + stack
                crate = line[idx : idx + 3]
                if crate.split():
                    char = crate.strip("[]")
                    stacks[stack].appendleft(char)
        # apply instructions
        for instruction in data[instructions_line_idx + 2 :]:
            _, count, _, from_stack, _, to_stack = instruction.split()
            count = int(count)
            from_stack = int(from_stack) - 1
            to_stack = int(to_stack) - 1
            for _ in range(count):
                crate = stacks[from_stack].pop()
                stacks[to_stack].append(crate)
        return "".join([stack.pop() for stack in stacks.values()])

    @classmethod
    def resolve_part_02(cls, data):
        # find number of stacks
        instructions_line_idx = None
        for idx, line in enumerate(data):
            if "1" in line:
                stack_count = int(max(line))
                instructions_line_idx = idx
                break
        # retrieve stacks
        stacks = defaultdict(deque)
        for line in data[:instructions_line_idx]:
            line = line.ljust(stack_count * 3 + stack_count - 1)
            for stack in range(stack_count):
                idx = stack * 3 + stack
                crate = line[idx : idx + 3]
                if crate.split():
                    char = crate.strip("[]")
                    stacks[stack].appendleft(char)
        # apply instructions
        for instruction in data[instructions_line_idx + 2 :]:
            _, count, _, from_stack, _, to_stack = instruction.split()
            count = int(count)
            from_stack = int(from_stack) - 1
            to_stack = int(to_stack) - 1
            crates = []
            for _ in range(count):
                crate = stacks[from_stack].pop()
                crates.append(crate)
            for crate in crates[::-1]:
                stacks[to_stack].append(crate)
        return "".join([stack.pop() for stack in stacks.values()])
