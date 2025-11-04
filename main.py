import yt_dlp
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

print(Tcl().eval("info patchlevel"))
window = Tk()
window.title("yt downloader")
window.geometry("300x250")

def puth_select():
    puth = filedialog.askdirectory()
    print(puth)
    
button_download = ttk.Button(text='скачать')
button_puth = ttk.Button(text='выбрать путь',command=puth_select)
label_url = Label(text='url: ')
entry = ttk.Entry()
checkbutton = ttk.Checkbutton(text='playelist',)


label_url.pack(side='left',anchor='nw')
entry.pack(side='left',anchor='nw')
checkbutton.pack(side='right',anchor='ne')
button_puth.pack()
button_download.pack(anchor="se")


window.mainloop()









# ydl_opts = {
#     'format': 'bestaudio/best',
#     'extractaudio': True,  # Извлекать аудио
#     'audioformat': 'MP3',  # Формат аудиофайла
#     'outtmpl': '%(title)s.%(ext)s',  # Шаблон имени файла
#     'noplaylist': False ,
# }

# # Список URL для скачивания
# playlist_urls = []  # Замените многоточие на ваши URL

# with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#     for url in playlist_urls:
#         try:
#             ydl.download([url])
#         except Exception as e:
#             print(f"Ошибка при скачивании {url}: {e}. Продолжаем...")