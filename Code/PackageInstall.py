print("正在載入套件。")
import os
try:
    import ffmpeg
except:
    print("ffmpeg未安裝，正在下載")
    os.system('pip install ffmpeg')
    import ffmpeg
filename=__file__
filename=filename[:-7]
if (filename+"ffmpeg\\bin") not in os.environ["path"]:
    os.environ["path"]+=(";"+filename+"ffmpeg\\bin"+";")
    #print("path added")#處理path
try:
    import numpy
except:
    print("numpy未安裝，正在下載")
    os.system('pip install numpy')
    import numpy
try:
    import matplotlib.pyplot as plt
except:
    print("matplotlib未安裝，正在下載")
    os.system('pip install matplotlib')
    import matplotlib.pyplot as plt
try:
    import librosa, librosa.display
except:
    print("librosa未安裝，正在下載")
    os.system('pip install librosa')
    import librosa, librosa.display
try:
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
except:
    print("tkinter未安裝，正在下載")
    os.system('pip install tkinter')
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
try:
    from PIL import ImageTk, Image
except:
    print("PIL未安裝，正在下載")
    os.system('pip install pillow')
    from PIL import ImageTk, Image
try:
    import pydub
except:
    print("pydub未安裝，正在下載")
    os.system('pip install pydub')
    import pydub
try:
    import IPython.display as ipd
except:
    print("IPython未安裝，正在下載")
    os.system('pip install IPython')
    import IPython.display as ipd
try:
    import scipy
except:
    print("scipy未安裝，正在下載")
    os.system('pip install scipy')
    import scipy
print("套件皆安裝完成。")