import yt_dlp
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

print(Tcl().eval("info patchlevel"))

ydl_opts = {
    'format': 'bestaudio/best',
    'extractaudio': True,  # Извлекать аудио
    'audioformat': 'MP3',  # Формат аудиофайла
    'outtmpl': '%(title)s.%(ext)s',  # Шаблон имени файла
    'noplaylist': True ,
    'cookies': 'cookies.txt' ,
}
ydl_opts['noplaylist'] = False

window = Tk()
window.title("yt downloader")
window.geometry("400x150")

def puth_select():
    puth = filedialog.askdirectory()
    print(puth)
    label_puth_to['text'] = puth
    
    
def download():
    urls = [entry.get()]
    print(urls)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                print(f"Ошибка при скачивании {url}: {e}. Продолжаем...")
    
    
quality_list = ['1080p','720p','480p','160p']
format_list = ['mp4','mp3','webm']

frame_url = ttk.Frame()
frame_puth = ttk.Frame()
frame_quality = ttk.Frame()
frame_format = ttk.Frame()



combobox_quality = ttk.Combobox(frame_quality,values=quality_list)
combobox_format = ttk.Combobox(frame_format,values=format_list)
button_puth = ttk.Button(frame_puth,text='выбрать путь',command=puth_select)
label_url = Label(frame_url,text='url: ')
label_puth = Label(frame_puth,text='puth: ')
label_puth_to = Label(frame_puth,text='')
label_quality = Label(frame_quality,text='quality: ')
label_format = Label(frame_format,text='format: ')
entry = ttk.Entry(frame_url)
checkbutton = ttk.Checkbutton(frame_url,text='playlist',)
button_download = ttk.Button(text='скачать',command=download)

label_format.pack(side='left',anchor='w')
label_url.pack(side='left',anchor='nw')
label_puth.pack(side='left',anchor='w')
label_quality.pack(side='left',anchor='w')
button_puth.pack(side='left',anchor='w')
label_puth_to.pack(side='left',anchor='w')
entry.pack(side='left',anchor='nw')
checkbutton.pack(side='right',anchor='ne')
combobox_format.pack(side='left',anchor='w')
combobox_quality.pack(side='left',anchor='w')
frame_url.pack(anchor='nw')
frame_puth.pack(anchor='w')
frame_quality.pack(anchor='w')
frame_format.pack(anchor='w')



button_download.pack(anchor="se")



window.mainloop()