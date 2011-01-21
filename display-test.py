#!/usr/bin/env python

import threading
import time
import curses.wrapper
import locale
from rtmcurses.display.display import Display
from rtmcurses.parsers import SystemParser


def main(stdscr):
  locale.setlocale(locale.LC_ALL, '')
  code = locale.getpreferredencoding()
  
  display = Display(stdscr)
  display.contentwin.writetask()
  display.contentwin.writetask2()
  
  while not display.inputline.stopflag:
    input = display.inputline.listen()
    if input == "/quit":
      display.inputline.stop()
      
    elif input.startswith("set prefix "):
      display.inputline.set_prefix(input.lstrip("set prefix "))
      
    #~ elif input.startswith('/'):
      #~ SystemParser.parser(input, display)
      
    elif input == "/next":
      display.next()
      
    elif input == "/prev":
      display.prev()
      
    elif input == "/clear":
      display.clear()
    else:
      display.contentwin.println(input)


if __name__ == '__main__':
  curses.wrapper(main)
