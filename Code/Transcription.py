#載入套件
print("正在載入套件。")
import os
import ffmpeg
filename=__file__
filename=filename[:-16]
if (filename+"ffmpeg\\bin") not in os.environ["path"]:
    os.environ["path"]+=(";"+filename+"ffmpeg\\bin"+";")
    print("path added")#處理path
import numpy
import matplotlib.pyplot as plt
import librosa, librosa.display
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import pydub
import IPython.display as ipd
import scipy
    
#定義按鈕指令
def open_file():
    global x
    global sr
    filename = askopenfilename(
        filetypes = [ ("OGG Files", "*.ogg"),("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")]
    )
    if not filename:
        return
    if filename[-4:]==".mp3":
        audSeg = pydub.AudioSegment.from_mp3(filename)
        audSeg.export(__file__[:-16] + filename.split("/")[-1][:-4] + ".wav", format="wav")
        filename = __file__[:-16] + filename.split("/")[-1][:-4] + ".wav"
        x, sr = librosa.load(filename[:-4] + ".wav")
        reply["text"] = "mp3格式不支援，將其轉換成wav。\n" + filename
    else:
        x, sr = librosa.load(filename)
        reply["text"] = filename
        
def analyze():
    global x
    global sr
    global spec_image
    global cur_img
    cur_img="spec_chromaSTFT.png"
    
    if sr == 0:
        return
        
    plt.rcParams['figure.figsize'] = (22, 10.5)
    bins_per_octave = 36
    
    #onset
    hop_length = 100
    onset_env = librosa.onset.onset_strength(y = x, sr=sr, hop_length = hop_length)
    onset_samples = librosa.onset.onset_detect(y = x,
                                           sr=sr, units='samples', 
                                           hop_length=hop_length, 
                                           backtrack=False,
                                           pre_max=20,
                                           post_max=20,
                                           pre_avg=100,
                                           post_avg=100,
                                           delta=0.2,
                                           wait=0)
    onset_boundaries = numpy.concatenate([[0], onset_samples, [len(x)]])
    onset_times = librosa.samples_to_time(onset_boundaries, sr=sr)
    librosa.display.waveshow(y=x, sr=sr)
    plt.vlines(onset_times, -1, 1, color='r')
    plt.savefig("onset.png")#onset *****************************
    
    plt.clf()
    
    #cqt
    cqt = librosa.cqt(x, sr = sr, n_bins = 300, bins_per_octave = bins_per_octave)
    log_cqt = librosa.amplitude_to_db(numpy.abs(cqt))
    spec = librosa.display.specshow(log_cqt, sr = sr, x_axis = "time", y_axis = "cqt_note",
                                   bins_per_octave = bins_per_octave)
    plt.grid(which = "both",color='g',axis='y',linewidth=0.7)
    plt.savefig("spec_cqt.png")#cqt ****************************
    
    plt.grid(which = "both",color='w',axis='y',linewidth=0.7)
    plt.savefig("spec_cqt_temp.png")#cqt for bm 
    
    image = Image.open("spec_cqt_temp.png")
    gray = image.convert("L")
    threshold = 150
    image_threshold = gray.point(lambda x: 255 if x > threshold else 0)
    image_threshold.save("bm_spec_cqt.png")#cqt with bm ***************************
    
    plt.grid(which = "both",color='g',axis='y',linewidth=0.7)
    for i in onset_times:
        plt.axvline(i, -1, 1, color='w',lw=0.7)
    plt.savefig("spec_cqt_tempo.png")#cqt with tempo ****************************
    
    plt.grid(which = "both",color='w',axis='y',linewidth=0.7)
    plt.savefig("spec_cqt_temp_tempo.png")#cqt with tempo for bm
    image = Image.open("spec_cqt_temp_tempo.png")
    gray = image.convert("L")
    threshold = 150
    image_threshold = gray.point(lambda x: 255 if x > threshold else 0)
    image_threshold.save("bm_spec_cqt_tempo.png")#cqt with tempo,bm ****************************
    
    plt.clf()
    
    #chroma_stft
    S = numpy.abs(librosa.stft(x))
    chroma = librosa.feature.chroma_stft(S=S, sr=sr)
    img = librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
    plt.grid(which = "both",color='g',axis='y',linewidth=0.7)
    plt.savefig("spec_chromaSTFT.png")#chromaSTFT ****************************
    
    image = Image.open("spec_chromaSTFT.png")
    gray = image.convert("L")
    threshold = 150
    image_threshold = gray.point(lambda x: 255 if x > threshold else 0)
    image_threshold.save("bm_spec_chromaSTFT.png")#chromaSTFT with bm ****************************
    
    for i in onset_times:
        plt.axvline(i, -1, 1, color='w',lw=0.7)
    plt.savefig("spec_chromaSTFT_tempo.png")#chromaSTFT with tempo ****************************
    
    plt.clf()
    
    #final
    image = Image.open("spec_chromaSTFT_tempo.png")
    gray = image.convert("L")
    threshold = 150
    image_threshold = gray.point(lambda x: 255 if x > threshold else 0)
    image_threshold.save("bm_spec_chromaSTFT_tempo.png")#chromaSTFT with tempo,bm ****************************
    
    cur_img = "bm_spec_chromaSTFT_tempo.png"
    spec_image = ImageTk.PhotoImage(Image.open("bm_spec_chromaSTFT_tempo.png"))
    panel.configure(image = spec_image)
    panel.image = spec_image
    
    plt.clf()
    
def show_cqt():
    global cur_img
    cur_img = "spec_cqt.png"
    spec_image = ImageTk.PhotoImage(Image.open("spec_cqt.png"))
    panel.configure(image = spec_image)
    panel.image = spec_image
    
def show_onset():
    global cur_img
    cur_img = "onset.png"
    spec_image = ImageTk.PhotoImage(Image.open("onset.png"))
    panel.configure(image = spec_image)
    panel.image = spec_image
    
def show_stft():
    global cur_img
    cur_img = "spec_chromaSTFT.png"
    spec_image = ImageTk.PhotoImage(Image.open("spec_chromaSTFT.png"))
    panel.configure(image = spec_image)
    panel.image = spec_image
    
def binary_mask():
    global cur_img
    if cur_img[:2] != "bm" and cur_img != "onset.png":
        spec_image = ImageTk.PhotoImage(Image.open("bm_"+cur_img))
        panel.configure(image = spec_image)
        panel.image = spec_image
        cur_img = "bm_"+cur_img
    elif cur_img[:2] == "bm" and cur_img != "onset.png":
        spec_image = ImageTk.PhotoImage(Image.open(cur_img[3:]))
        panel.configure(image = spec_image)
        panel.image = spec_image
        cur_img = cur_img[3:]
    else:
        pass
        
def tempo():
    global cur_img
    if cur_img[-9:-4] != "tempo" and cur_img != "onset.png":
        spec_image = ImageTk.PhotoImage(Image.open(cur_img[:-4]+"_tempo.png"))
        panel.configure(image = spec_image)
        panel.image = spec_image
        cur_img = cur_img[:-4]+"_tempo.png"
    elif cur_img[-9:-4] == "tempo" and cur_img != "onset.png":
        spec_image = ImageTk.PhotoImage(Image.open(cur_img[:-10]+".png"))
        panel.configure(image = spec_image)
        panel.image = spec_image
        cur_img = cur_img[:-10] + ".png"
    else:
        pass
        
def quit():
    window.destroy()
    
def resize_image(event):#縮放
    global spec_image
    if spec_image == None:
        return
    else:
        new_width = event.width+100
        new_height = event.height+100
        spec = Image.open(cur_img)
        resize = spec.resize((new_width, new_height))
        spec_image = ImageTk.PhotoImage(resize)
        panel.config(image = spec_image)
        panel.image = spec_image

#初始設定
window = tk.Tk()
window.title("MusicTransription")
window.geometry("1920x1080")
x = []
sr = 0
spec_image = None
window.columnconfigure(0, weight = 1)
window.rowconfigure(2, weight = 1)

#按鈕
frm_buttons = tk.Frame(window, relief = tk.RAISED, bd = 2)
frm_buttons.grid(row = 0, column = 0, sticky = "ew")
btn_open = tk.Button(frm_buttons, text = "Open", command = open_file)
btn_open.grid(row = 0, column = 0, sticky = "ew", pady = 5)
btn_analyze = tk.Button(frm_buttons, text = "Analyze", command = analyze)
btn_analyze.grid(row = 0, column = 1, sticky = "ew", pady = 5, padx = 5)
btn_cqt = tk.Button(frm_buttons, text = "CQT", command = show_cqt)
btn_cqt.grid(row = 0, column = 2, sticky = "ew", pady = 5)
btn_onset = tk.Button(frm_buttons, text = "onset", command = show_onset)
btn_onset.grid(row = 0, column = 3, sticky = "ew", pady = 5)
btn_stft = tk.Button(frm_buttons, text = "Chroma ftst", command = show_stft)
btn_stft.grid(row = 0, column = 4, sticky = "ew", pady = 5)
btn_tempo = tk.Button(frm_buttons, text = "tempo", command = tempo)
btn_tempo.grid(row = 0, column = 5, sticky = "ew", pady = 5, padx = 5)
btn_bm = tk.Button(frm_buttons, text = "binary mask", command = binary_mask)
btn_bm.grid(row = 0, column = 6, sticky = "ew", pady = 5)
btn_close = tk.Button(frm_buttons, text = "Exit", command = quit)
btn_close.grid(row = 0, column = 7, sticky = "ew", pady = 5, padx = 20)

#訊息
reply = tk.Label(window, text = "empty")
reply.grid(row = 1, column = 0, sticky = "ew")

#版面
panel = tk.Label(window)
panel.grid(row = 2, column = 0, sticky = "nsew")
panel.bind('<Configure>', resize_image)

#start!
window.mainloop()

