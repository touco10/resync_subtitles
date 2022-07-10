import os 
import subprocess
from natsort import natsorted



directory = r"C:\Users\touco\Desktop\alhayba_s4"



path =[]
def synchro() :
    for root, dirs, files in os.walk(directory):
        try:
            path.append(root+"\\")
        except:
            pass
    d=natsorted(path)
    for i,file in enumerate(d) :
        if i > 0:
            filenum = str(i).zfill(2)
            fichier =f'{file}Al_Hayba_-_S04E{filenum}_-_Episode_{i}_-_WEBDL-1080p_HEVC_x265.fr.srt'
            command = f'astisub sync -i {fichier} -s "-194s" -o {file}video.srt'
            subprocess.Popen(command)
   
synchro()
