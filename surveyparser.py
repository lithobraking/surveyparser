import pandas as pd
import tkinter as tk
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw()

print("Please select a .csv file")
# TODO: add file type enforcement
fn = askopenfilename() 

csvFile = pd.read_csv(fn)
print(csvFile)

