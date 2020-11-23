# -*- coding: UTF-8 -*-

# Import from standard library
import os
import mlproject
import pandas as pd
# Import from our lib
from mlproject.tools import haversine
import pytest


def test():
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 42.7, 3.0167
    haver = haversine(lon1, lat1, lon2, lat2)
    assert haver == 687.2930027036251