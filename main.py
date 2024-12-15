import tkinter as tk
from tkinter import ttk, masegebox
class RestaruantOrderManegment:
 def __init__(self,root):
  self.root= root
  self.root.title("Restaurant Manegement App")
  self.menu_items= {"FRIES MEAL":2,"LUNCH MEAL":2,"CHIKEN BURGUR MEAL":3,"HAKA NODELS":3.6}