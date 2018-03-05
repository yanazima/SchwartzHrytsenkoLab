#!/usr/bin/env python2

import os
import sys
import glob
import subprocess
from subprocess import call
from itertools import izip_longest, izip, product
import math
import pickle
from collections import defaultdict

#ONLY PUT TESTS FOR FUNCTIONS THAT DO MATHEMATICAL CALCULATONS

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
