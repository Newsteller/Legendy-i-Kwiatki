import os
import pickle

def setup_root(instance):
    instance.root.geometry("500x500")
    instance.root.title("Legendy i Kwiatki")
    instance.root.iconbitmap("logo.ico")

def save_window_position(window, config_file):
   position = window.winfo_geometry()
   with open(config_file, 'wb') as file:
      pickle.dump(position, file)

def load_window_position(window, config_file):
   if os.path.exists(config_file):
      with open(config_file, 'rb') as file:
         position = pickle.load(file)
         window.geometry(position)