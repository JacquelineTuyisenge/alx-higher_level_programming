#!/usr/bin/env python3
for i in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(i if (i - ord('a')) % 2 == 0 else i - 32), end="")
print()
