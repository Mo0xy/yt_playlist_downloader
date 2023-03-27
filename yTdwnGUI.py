import pytube
import os
import customtkinter
#import time

path = os.path.join(os.path.expanduser('~'), 'Downloads')

def step(current_state, max):
    unit = (1/max)
    print("max value:", max)
    current_state += unit
    print("current state: ", current_state)
    progress_bar.update()
    progress_bar.set(current_state)
    return current_state

def download():
    try:  
        link = entry.get()  
        print(link)
        
        yt = pytube.Playlist(link)  
        pls = yt.video_urls
        vd = pytube.YouTube(link)
        #ytobj = pytube.YouTube(link)
        #ytobj = vd

        max = yt.length

        prg = 0.0
        
        indx = vd.streams.index(vd.streams.first())
        #max = vd.streams.index(vd.streams.last())
        
        """
        for video in yt.videos:
            video.streams.first().download()"""  
        while(indx < max): 
            vd = pytube.YouTube(pls[indx]) #, on_progress_callback=step
            stream = vd.streams.get_highest_resolution()
            stream.download(path)
            #percentage = float(vd.streams.index(vd.streams.last)/100)
            prg = step(prg, max)
            indx += 1
    except:
        print("Error")
    


#setting application appereance
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()
root.geometry("720x480")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=50, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Youtube Playlist Downloader", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry = customtkinter.CTkEntry(master=frame, width=400, height=40, placeholder_text="Insert link")
entry.pack(pady=20, padx=10, expand=True)



button = customtkinter.CTkButton(master=frame, text="Download", command=download)
button.pack(pady=12, padx=10)

progress_bar = customtkinter.CTkProgressBar(master=frame, width=400) 
progress_bar.pack(padx=20, pady=10)
progress_bar.set(0)

root.mainloop()







"""
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
entry2.pack(pady=12, padx=10)




checkbox = customtkinter.CTkCheckBox(master=frame, text="remember me")
checkbox.pack(pady=12, padx=10)

"""

