from itertools import permutations
def solve_cryptarithmetic():
    letters = 'SENDMORY'
    digits = range(10)
    for perm in permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s == 0 or m == 0:
            continue
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        if send + more == money:
            print(f"Solution: S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
            print(f"{send} + {more} = {money}")
            return

    print("No solution found.")
solve_cryptarithmetic()
