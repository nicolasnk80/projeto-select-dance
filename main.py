# Projeto de fim de seméstre para o curso: "Dança Urbana" da fábrica de cultura
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from random import choice

Window.size = (400, 600)


class Manager(ScreenManager):
    pass


class Home(MDScreen):
    def on_enter(self, *args):
        Clock.schedule_once(self.screen_dance, 7)
    
    def screen_dance(self, *args):
        MDApp.get_running_app().root.current = "dance"


class Dance(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anterior = ""

    def start_process(self, widget, *args):
        widget.angle = 0

        if self.ids.btn.text == "Start" :
            self.anim = Animation(angle=360 * 2, duration=2)
            self.anim.start(widget)
            self.anim.bind(on_complete=self.random_image)
        elif self.ids.btn.text == "Restart" :
            self.restart_all()
    
    def random_image(self, *args):
        self.anim.cancel(self.ids.img)
        Clock.schedule_once(self.source_img, .5)
    
    def source_img(self, *args):
        imgs = ["img1.jpg", "img2.jpg", "img3.jpg"]
        img = choice(imgs)
        self.ids.myTitle.font_size = 30

        if img == self.anterior :
            self.back_img()
            return

        elif img == "img1.jpg" :
            self.ids.myTitle.text = "KICK OUT"
        
        elif img == "img2.jpg" :
            self.ids.myTitle.text = "FREEZE"
        
        elif img == "img3.jpg" :
            self.ids.myTitle.text = "TOP ROCK"
        
        elif img == "img4.jpg" :
            self.ids.myTitle.text = "FOOT WORK"
        
        self.anterior = img

        self.ids.img.source = "data/breaking/"+img
        self.ids.img.size_hint_x = .7
        self.ids.btn.text = "Restart"

    def back_img(self, *args):
        self.source_img()
    
    def restart_all(self, *args):
        self.ids.btn.text = "Start"
        self.ids.img.size_hint_x = .5
        self.ids.img.source = "data/clock.png"
        self.ids.myTitle.text = "Clique em Start"
        self.ids.myTitle.font_size = 25


class SelectDance(MDApp):
    def build(self):
        return Manager()


SelectDance().run()
