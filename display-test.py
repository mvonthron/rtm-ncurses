#!/usr/bin/env python

import threading
import time
import curses.wrapper
import locale
import logging

from rtmcurses.display.display import Display
from rtmcurses.parsers import SystemParser


def main(stdscr):
  logging.basicConfig(level=logging.DEBUG)
  
  locale.setlocale(locale.LC_ALL, '')
  code = locale.getpreferredencoding()
  
  display = Display(stdscr)
  
  #display.contentwin.writetask()
  #display.contentwin.writetask2()
  
  while not display.inputline.stopflag:
    input = display.inputline.listen()
    
    if input == "/quit":
      display.inputline.stop()
      
    elif input.startswith("/rename "):
      display.setName(input[8:])
    
    #elif input.startswith("/move "):
      #display.swapViews(input.split()[1])
    
    #~ elif input.startswith('/'):
      #~ SystemParser.parser(input, display)
      
    elif input == "/next":
      display.next()
  
    elif input.startswith("/add "):
      title = input[5:].split()[0]
      if len(input.split()) > 2:
        content = ' '.join(input.split()[2:])
      else:
        content = ''
      
      display.addView(title, buffer=content)

    elif input == "/refresh":
      pass

    elif input == "/remove":
      display.removeView()

    elif input == "/prev":
      display.prev()

    elif input == "/first":
      display.first()

    elif input == "/last":
      display.last()
      
    elif input == "/clear":
      display.clear()
    
    else:
      display.write(input)


if __name__ == '__main__':
  curses.wrapper(main)
