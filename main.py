from tkinter import *
from time import sleep
import webbrowser


root = Tk()
root.title('Klockcraft 1.20')
root.geometry('800x600')
root.resizable(False, False)


def extract_png_asset(asset_name):
    return PhotoImage(file='assets/' + asset_name + '.png')

klockicon_photo = extract_png_asset('klockicon')




titlescreen_top_photo = extract_png_asset('titlescreen_top')
login_photo = extract_png_asset('login')
download_terrian_photo = extract_png_asset('download_terrain')
original_server_photo = extract_png_asset('original_server')
titlescreen_bg_photo = extract_png_asset('titlescreen_bg')
timed_out_photo = extract_png_asset('timed_out')
back_2_titlescreen_photo = extract_png_asset('buttons/back_2_titlescreen')
cancel_photo = extract_png_asset('buttons/cancel')
done_photo = extract_png_asset('buttons/done')
done_hover_photo = extract_png_asset('buttons/done_hover')
multiplayer_photo = extract_png_asset('buttons/multiplayer')
new_world_photo = extract_png_asset('buttons/new_world')
options_photo = extract_png_asset('buttons/options')
realms_photo = extract_png_asset('buttons/realms')
singleplayer_photo = extract_png_asset('buttons/singleplayer')
entry_bar_photo = extract_png_asset('entry_bar')
dropdown_def_steve_photo = extract_png_asset('dropdown_def_steve')
dropdown_def_alex_photo = extract_png_asset('dropdown_def_alex')
dropdown_herobrine_photo = extract_png_asset('dropdown_herobrine')
dropdown_noob_photo = extract_png_asset('dropdown_noob')
def_steve_photo = extract_png_asset('def_steve')
def_alex_photo = extract_png_asset('def_alex')
noob_photo = extract_png_asset('noob')
herobrine_photo = extract_png_asset('herobrine')
def_steve_option_photo = extract_png_asset('options/def_steve_option')
def_alex_option_photo = extract_png_asset('options/def_alex_option')
herobrine_option_photo = extract_png_asset('options/herobrine_option')
noob_option_photo = extract_png_asset('options/noob_option')
more_skins_option_photo = extract_png_asset('options/more_skins_option')
discord_photo = extract_png_asset('discord')
pets_button_photo = extract_png_asset('buttons/pets')
pets_hover_button_photo = extract_png_asset('buttons/pets_hover')
login2_photo = extract_png_asset('login2')

root.iconphoto(False, klockicon_photo)

shown_klock_options = [False]

login_label = Label(root, image=login_photo)
login_label.place(x=0, y=0)

login_avatar = Label(root, image=def_steve_photo)
login_avatar.place(x=50, y=50)




chosen_character = ['def_steve']


def choose_character(char):
    chosen_character.clear()
    chosen_character.append(char)


class EntryBar:
    def __init__(self, x, y):
        self.entry_sprite = Label(root, image=entry_bar_photo)
        self.entry_sprite.place(x=x, y=y)
        self.x = x
        self.y = y
    def hide(self):
        self.entry_sprite.place_forget()
    def show(self):
        self.entry_sprite.place(x=self.x, y=self.y)

class KlockcraftButton:
    def __init__(self, x=0, y=0, photo=None, hover_photo=None, command_func=None):
        self.photo = photo
        self.hover_photo = hover_photo
        self.x = x
        self.y = y
        if command_func == None: self.button = Button(root, image=self.photo)
        else: self.button = Button(root, image=self.photo, command=command_func)
        self.button.place(x=x, y=y)
        self.button.bind('<Enter>', self.hover)
        self.button.bind('<Leave>', self.no_hover)
    def hover(self, _):
        if self.hover_photo != None: self.button.config(image=self.hover_photo)
    def no_hover(self, _):
        if self.hover_photo != None: self.button.config(image=self.photo)
    def change_photo(self, new_photo):
        self.button.config(image=new_photo)
    def destroy(self):
        self.button.place_forget()
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.button.place(x=new_x, y=new_y)
        self.button.update()
    def hide(self):
        self.button.place(x=1000, y=1000)
    def show(self):
        self.button.place(x=self.x, y=self.y)

def open_discord(): webbrowser.open('')

def choose_def_steve(): 
    choose_character('def_steve')
    login_avatar.config(image=def_steve_photo)
    login_dropdown.change_photo(dropdown_def_steve_photo)

def choose_def_alex(): 
    choose_character('def_alex')
    login_avatar.config(image=def_alex_photo)
    login_dropdown.change_photo(dropdown_def_alex_photo)


def choose_herobrine():
    choose_character('herobrine')
    login_avatar.config(image=herobrine_photo)
    login_dropdown.change_photo(dropdown_herobrine_photo)

def choose_noob():
    choose_character('noob')
    login_avatar.config(image=noob_photo)
    login_dropdown.change_photo(dropdown_noob_photo)

def more_skins():
    def_steve_option.hide()
    def_alex_option.hide()
    herobrine_option.hide()
    noob_option.hide()
    more_skins_option.hide()
    screename_bar.hide()
    pets_button.hide()
    discord_button.hide()
    done_button.hide()
    login_dropdown.hide()
    login_label.place_forget()

    login2_label = Label(root, image=login2_photo)
    login2_label.place(x=0, y=0)

    char = chosen_character[0]
    login_avatar2 = Label(root, image=def_steve_photo)
    login_avatar2.place(x=50, y=50)
    def return_normal_login():
        more_skins_done_button.hide()
        login_avatar2.place_forget()
        login2_label.place_forget()
        def_steve_option.show()
        def_alex_option.show()
        herobrine_option.show()
        noob_option.show()
        more_skins_option.show()
        screename_bar.show()
        pets_button.show()
        discord_button.show()
        done_button.show()
        login_dropdown.show()
        login_label.place(x=0, y=0)
    more_skins_done_button = KlockcraftButton(300, 550, done_photo, done_hover_photo, return_normal_login)
    if char == 'def_steve': login_avatar2.config(image=def_steve_photo)
    elif char == 'def_alex': login_avatar2.config(image=def_alex_photo)
    elif char == 'herobrine': login_avatar2.config(image=herobrine_photo)
    elif char == 'noob': login_avatar2.config(image=noob_photo)
    
    


def_steve_option = KlockcraftButton(350, 340, def_steve_option_photo, None, choose_def_steve)
def_alex_option = KlockcraftButton(350, 370, def_alex_option_photo, None, choose_def_alex)
herobrine_option = KlockcraftButton(350, 400, herobrine_option_photo, None, choose_herobrine)
noob_option = KlockcraftButton(350, 430, noob_option_photo, None, choose_noob)
more_skins_option = KlockcraftButton(350, 460, more_skins_option_photo, None, more_skins)

def_steve_option.hide()
def_alex_option.hide()
herobrine_option.hide()
noob_option.hide()
more_skins_option.hide()

def klock_options(): 
    if shown_klock_options == [False]:
        def_steve_option.show()
        def_alex_option.show()
        herobrine_option.show()
        noob_option.show()
        more_skins_option.show()
        shown_klock_options.remove(False); shown_klock_options.append(True)
    else:
        def_steve_option.hide()
        def_alex_option.hide()
        herobrine_option.hide()
        noob_option.hide()
        more_skins_option.hide()
        shown_klock_options.remove(True); shown_klock_options.append(False)

global login_dropdown
login_dropdown = KlockcraftButton(350, 290, dropdown_def_steve_photo, None, klock_options)



screename_bar = EntryBar(350, 160)
done_button = KlockcraftButton(50, 550, done_photo, done_hover_photo)
discord_button = KlockcraftButton(700, 520, discord_photo, None, open_discord)
pets_button = KlockcraftButton(400, 540, pets_button_photo, pets_hover_button_photo, None)


root.mainloop()
