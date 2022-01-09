
import tkinter as tk
from psutil import net_io_counters

# Variablat per manipulim me Bytes
KB = float(1024)
MB = float(KB ** 2) # 1,048,576
GB = float(KB ** 3) # 1,073,741,824
TB = float(KB ** 4) # 1,099,511,627,776
def size(B):
	
	B = float(B)
	if B < KB: return f"{B} Bytes"
	elif KB <= B < MB: return f"{B/KB:.2f} KB"
	elif MB <= B < GB: return f"{B/MB:.2f} MB"
	elif GB <= B < TB: return f"{B/GB:.2f} GB"
	elif TB <= B: return f"{B/TB:.2f} TB"

## Konstantet
WINDOW_SIZE = (400, 400)  # Width x Height
WINDOW_RESIZEABLE = False  # If the window is resizeable or not.
REFRESH_DELAY = 1500 # Window update delay in ms.

## Variablat dalese
last_upload, last_download, upload_speed, down_speed = 0, 0, 0, 0
