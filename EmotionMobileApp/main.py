#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
business logic
Created on Tue Jun 23 23:46:35 2020

@author: tianlu
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from datetime import datetime
import json
import glob
from pathlib import Path
import random

Builder.load_file('design.kv')

#the class name should be exactly the same as the widget name in kv file
class LoginScreen(Screen):
    def login(self,uname,pword):
        with open("users.json") as userFile:
            users = json.load(userFile)
            if uname in users and pword==users[uname]['password']:
                self.manager.current = 'login_success_screen'
            else:
                self.ids.login_error.text = "Wrong username or password"
        
    
    def sign_up(self):
        self.manager.current = "sign_up_screen"
        
class SignUpScreen(Screen):
    def add_user(self,uname,pword):
        with open("users.json") as userFile:
            users = json.load(userFile)
            users[uname] = {'username':uname,'password':pword,'created':datetime.now().strftime('%Y-%m-%d %H-%M-%S')}
        
            #overwrite users in the json file
            with open("users.json",'w') as userFile:
                json.dump(users,userFile)
            self.manager.current = "sign_up_screen_success"

class SignUpScreenSuccess(Screen):
    def back_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginSuccessScreen(Screen):
    def log_out(self):
        self.manager.current = "login_screen"
    def get_quote(self,feeling):
        feeling = feeling.lower()
        feeling_quotes = glob.glob("quotes/*txt")
        feeling_quotes = [Path(filename).stem for filename in feeling_quotes]
        
        if feeling in feeling_quotes:
            with open(f"quotes/{feeling}.txt") as quotesFile:
                quotes = quotesFile.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"
    
    
class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

