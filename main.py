#!/usr/bin/env python3

import tkinter as tk

from models import AppParams

class App:
  def __init__(self):
    self.root = tk.Tk()

  def run(self, width, height, title, bg="white"):
    if width & height: self.w, self.h = width, height
    elif width: self.w, self.h = width, 1080
    elif height: self.w, self.h = 1920, height
    else: self.w, self.h = 1920, 1080
    self.title = title
    self.root.geometry(f"{self.w}x{self.h}")
    self.root.configure(bg=bg)
    self.root.title(f"{self.title}")
    self.root.mainloop()


def main():
  app = App()
  params = AppParams(width=1920, height=1080, title="Main", bg="white")
  app.run(**params.model_dump())


if __name__ == "__main__":
  main()