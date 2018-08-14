import itertools


def spiral(n, m):
    _status = itertools.cycle(['right', 'down', 'left', 'up'])  # 用于状态周期性的切换
    _movemap = {
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0),
        'up': (0, -1),
    }
    pos2no = dict.fromkeys([(x, y) for x in range(n) for y in range(m)])
    print(pos2no)
    _pos = (0, 0)
    _st = next(_status)
    for i in range(1, n * m + 1):
        _oldpos = _pos
        _pos = tuple(map(sum, zip(_pos, _movemap[_st])))  # 根据状态进行移动
        if (_pos not in pos2no) or (pos2no[_pos]):  # 当超出范围或遇到障碍时切换方向
            _st = next(_status)
            _pos = tuple(map(sum, zip(_oldpos, _movemap[_st])))
        pos2no[_oldpos] = i
    return pos2no


def display_spiral(n, m):
    pos2no = spiral(n, m)
    for i in range(m):
        for j in range(n):
            print(pos2no[(j,i)],end='')
        print('\n')

display_spiral(5,5)