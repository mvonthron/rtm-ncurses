#!/usr/bin/env python

import threading
import time
import curses.wrapper
import curses.ascii
import locale
import logging

from rtmcurses.display.display import Display
from rtmcurses.parsers import *


def main(stdscr):
  logging.basicConfig(level=logging.DEBUG)
  
  locale.setlocale(locale.LC_ALL, '')
  code = locale.getpreferredencoding()
  
  display = Display(stdscr)
  
  systemParser = SystemParser(display)
  keyParser    = KeyboardShortcutParser(display)
  
  #display.contentwin.writetask()
  #display.contentwin.writetask2()

  while not display.inputline.stopflag:
    input = display.inputline.listen()
    

    if keyParser.canHandle(input):
        input = keyParser.handle(input)
    
    if input.startswith("/"):
      systemParser.handle(input)

    else:
      display.write(input)


if __name__ == '__main__':
  curses.wrapper(main)
