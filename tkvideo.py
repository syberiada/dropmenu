import tkinter as tk
from tkVideoPlayer import TkinterVideo

root = tk.Tk()
root.geometry("800x600")
lf = tk.LabelFrame(root, text="preview")
videoplayer = TkinterVideo(lf, scaled=True)
videoplayer.load(r"sample.mp4")
print(videoplayer.video_info())
videoplayer.pack(expand=True, fill="both")
lf.pack(fill="both", expand="yes")

videoplayer.play() # play the video
print(videoplayer.video_info())

root.mainloop()