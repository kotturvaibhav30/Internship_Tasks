#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    counts = Counter(s)

    for char, count in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, count)
