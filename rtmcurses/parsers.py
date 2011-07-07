# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses.ascii

class Parser(object):
  def __init__(self, display):
    self._display = display

  def canHandle(input):
    pass
  
  def help(self):
    pass
  
  def handle(self, input):
    pass


class SystemParser(Parser):
  def canHandle(input):
    return input.startswith('/')
   
  def handle(self, input):
    if(input.startswith("/quit") or input.startswith("/exit")):
      self._display.inputline.stop()

    elif(input.startswith("/help")):
      self.help()
      
    if input.startswith("/add "):
      title = input[5:].split()[0]
      if len(input.split()) > 2:
        content = ' '.join(input.split()[2:])
      else:
        content = ''
      
      self._display.addView(title, buffer=content)
      
    elif input.startswith("/rename "):
      self._display.setName(input[8:])

    elif input.startswith("/move "):
      self._display.swapViews(input.split()[1])

    elif input.startswith("/color "):
      self._display.set_color(input.split()[1])
    
    elif input.startswith("/status "):
      self._display.statusline.set_status(input.split()[1])

    elif input == "/refresh":
      pass
      
    elif input == "/remove":
      self._display.removeView()
          
    elif input == "/prev":
      self._display.prev()
      
    elif input == "/next":
      self._display.next()
      
    elif input == "/first":
      self._display.first()

    elif input == "/last":
      self._display.last()
      
    elif input == "/clear":
      self._display.clear()
      
  """
  Should print a detailled list of available commands 
  Output on "system" channel. Creates it and move if necessary
  """
  def help(self):
      
      help_content = """Available system commands
  * /help
    prints this help message
  
  * /quit, /exit
    exits the program
    
*** THIS MESSAGE MUST BE MOVED TO A 'SYSTEM' CHANNEL***
      """
      
      self._display.write(help_content)


"""
Converts keyboard shortcut into real command
"""
class KeyboardShortcutParser(Parser):

  def canHandle(self, input):
    return isinstance(input, int) and curses.ascii.isctrl(input)

  def handle(self, input):
    if not isinstance(input, int):
      return
    
    if input == curses.ascii.DLE:
        return "/prev"

    if input == curses.ascii.SO:
        return "/next"
