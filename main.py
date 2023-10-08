#!/usr/bin/env python3

import tkinter as tk


class App:
  def __init__(self):
    self.root = tk.Tk()

  def run(self, width, height, title, bg="white"):
    self.w, self.h = width, height
    self.title = title
    self.root.geometry(f"{self.w}x{self.h}")
    self.root.configure(bg=bg)
    self.root.title(f"{self.title}")
    self.root.mainloop()


if __name__ == "__main__":
  app = App()
  app.run(width=1920, height=1080, title="Main", bg="black")
