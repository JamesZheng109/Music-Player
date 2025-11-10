#import
from tkinter import *
from tkinter import filedialog
from pygame import mixer
#Init
mixer.init()
#window_info
window=Tk()
class music_player:
    def __init__(self,window):
        #Initialize window
        self.window=window
        self.window.title('Music Player')
        self.window.geometry('300x400')
        self.window.resizable(0,0)
        #Variables
        self.pause=True
        self.music_loaded=False
        self.song=None
        self.pausetext=StringVar(self.window)
        self.pausetext.set('Pause')
        self.nametext=StringVar(self.window)
        self.nametext.set('Nothing')
        #Initialize widget
        self.musicselect=Button(self.window,text='Select Music',width=10,height=5,command=self.load_music)
        self.play_pause_button=Button(self.window,textvariable=self.pausetext,width=10,height=5,command=self.play_pause_music)
        self.play_pause_button['state']='disabled'
        self.restart=Button(self.window,text='Restart',width=10,height=5,command=mixer.music.rewind)
        self.restart['state']='disabled'
        self.songlabel=Label(self.window,text='Now Playing:',width=10,height=1)
        self.songname=Label(self.window,textvariable=self.nametext,width=30,height=1,justify='right')
    def get_filename(self,filename):
        #Loop through filepath
        for char in filename:
            #Check for "/" and remove everything before it
            if '/' in filename:
                filename=filename[1:]
        return filename
    def load_music(self):
        #Get & load song file
        self.song=filedialog.askopenfilename(title='Select Song',filetypes=(('Mp3 files','*.mp3*'),))
        mixer.music.load(self.song)
        #Update states
        self.play_pause_button['state']='active'
        self.restart['state']='active'
        self.pause=False
        self.music_loaded=True
        #Play music
        mixer.music.play()
        #Display song name
        self.nametext.set(self.get_filename(self.song))
        self.play_pause_music()
    def play_pause_music(self):
        #Check if music is loaded
        if self.music_loaded:
            #Check whether song is paused
            if self.pause:
                mixer.music.pause()
                self.pause=False
                self.pausetext.set('Unpause')
            elif not self.pause:
                mixer.music.unpause()
                self.pause=True
                self.pausetext.set('Pause')
    def draw(self):
        #Place Widget
        self.musicselect.place(x=100,y=10)
        self.play_pause_button.place(x=100,y=100)
        self.restart.place(x=100,y=190)
        self.songlabel.place(x=100,y=280)
        self.songname.place(x=140,y=320,anchor='center')
        #Mainloop
        self.window.mainloop()
a=music_player(window)
a.draw()
