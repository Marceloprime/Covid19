from pyexcel_ods import get_data
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



aux = json.dumps(get_data("Brasil.ods"))
print(aux)