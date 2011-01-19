#!/usr/bin/env python

import threading
import time
import curses.wrapper
from rtmcurses.display.display import Display


def main(stdscr):
  display = Display(stdscr)
  
  display.contentwin.writetask()
  
  while not display.inputline.stopflag:
    input = display.inputline.listen()
    if input == "/quit":
      display.inputline.stop()
      
    elif input.startswith("set prefix "):
      display.inputline.set_prefix(input.lstrip("set prefix "))
      
    elif input == "/clear":
      display.contentwin.clear()
    else:
      display.contentwin.println(input)


if __name__ == '__main__':
  curses.wrapper(main)
