import random

ADDS = ["n", "r", "s", "f"]
TEST_COUNT = 100

n, m, k = random.randint(1, 50), random.randint(1, 50), random.randint(1, 100)

for i in range(TEST_COUNT):
    f_w = open("test_%s.test" % str(i), "w")
    
    print(n, m, k, file=f_w)
    for _ in range(n):
        for j in range(m):
            print(ADDS[random.randint(0, 3)], end="", file=f_w)
        print(file=f_w)
    f_w.close()
    print("Generated test %s / %s" % (str(i + 1), str(TEST_COUNT)), end="\r")
