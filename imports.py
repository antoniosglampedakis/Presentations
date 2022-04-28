import tkinter as tk
from tkinter import ttk
import pyodbc
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import re
import datetime
import copy
from tkinter import filedialog

from functions import *

pd.set_option('display.max_columns', None)

listofNetworkNames = ['OGILVY', 'DDB WORLDWIDE', 'BBDO WORLDWIDE', 'McCann Worldgroup', 'TBWA WORLDWIDE',
          'VMLY&R', 'PUBLICIS WORLDWIDE', 'LEO BURNETT', 'WUNDERMAN THOMPSON', 'GREY', 'FCB','DENTSU',
          'MULLENLOWE GROUP', 'havas creative', 'DAS', 'FCB HEALTH', 'AKQA', 'R/GA', 'SAATCHI & SAATCHI','BETC'
]