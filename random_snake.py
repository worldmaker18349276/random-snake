import time, random

def main():
    width, length, dt = 5, 5, 0.05

    dots = [[0, 1, 2, 6],
            [3, 4, 5, 7]]
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    snake = [(0,0)]*length
    x, y, d = 0, 0, 0
    while True:
        d_ = (d + random.randint(-1,1)) % 4
        dx, dy = dirs[d_]
        if x+dx not in range(2*width):
            continue
        if y+dy not in range(4):
            continue

        d = d_
        x, y = x+dx, y+dy
        snake.pop(0)
        snake.append((x, y))

        buf = [0x2800]*width
        for x, y in snake:
            buf[x // 2] |= 2**dots[x % 2][y]
        print("".join(map(chr, buf)), end="\r")
        time.sleep(dt)
