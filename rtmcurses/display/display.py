# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses

from titleline import TitleLine
from contentwindow import ContentWindow
from statusline import StatusLine
from inputline import InputLine
from errors import *
from rtmcurses import configuration


class View(object):
  def __init__(self, x, y, buffer=""):
    self.x = x
    self.y = y
    self.cursor = self.y
    self.buffer = buffer

"""
Display controller of RTM-ncurses
"""
class Display(object):
  
  def __init__(self, stdscr):
    self._stdscr = stdscr
    self.init_colors()
    
    # views
    self.views       = {
      'default': View(0, 0, ""),
    }
    self.positions   = self.views.keys()
    self.curr_view   = self.positions[0]
    self.nb_views    = len(self.views)
    
    # screen variables
    self.view_h      = curses.LINES-5
    self.view_width  = curses.COLS
    self.pad_height  = configuration.max_view_height
    self.pad_width   = self.nb_views*self.view_width
    
    # curses windows creation
    self.titleline   = TitleLine()
    self.contentwin  = ContentWindow()
    self.statusline  = StatusLine()
    self.inputline   = InputLine()
    
    self.contentwin.fillFromViews(self.views)
    self.statusline.fillFromViewlist(self.positions)
    self.inputline.set_prefix(self.curr_view)
    
  
  def init_colors(self):
    curses.start_color()
    curses.use_default_colors()
    
    curses.init_pair(1, curses.COLOR_WHITE, -1)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)


  #
  # view management methods
  #
  
  def _getView(self, viewid=None):
    """returns name of a view
    if argument 'viewid' is an int, the name of the view at the position is returned
    if argument is None or omitted, the name of current view is returned
    if argument is a string, just check if the view exists and return the name
    """
    
    if viewid is None:
      return self.curr_view
    elif isinstance(viewid, int):
      if viewid < len(self.positions):
        return self.positions[viewid]
      else:
        raise UnknownView()
    elif isinstance(viewid, str):
      if viewid in self.views:
        return viewid
      else:
        raise UnknownView()
    else:
      raise ArgumentError()
  
  
  def addView(self, name, buffer="", pos=None, switch=True):
    """Add a view to the display.
    if pos is none: placed at the end
    """
    if name in self.views:
      raise Exception("Invalid name")
    
    self.views[name] = View(self.nb_views*curses.COLS, 0, buffer)
    self.nb_views = len(self.views)
    self.pad_width += self.view_width
    self.contentwin.resize_pad(self.pad_width, self.pad_height)

    if not pos is None and isinstance(pos, int):
      self.positions.insert(pos, name)
    else:
      self.positions.append(name)

    # something cleaner ?
    self.contentwin.fillFromViews(self.views)
    self.statusline.fillFromViewlist(self.positions)
    
    if(switch):
      self.switchToView(name)


  def removeView(self, viewid=None):
    """remove view"""
    view = self._getView(viewid)

    self.positions.remove(view)
    self.statusline.fillFromViewlist(self.positions)
    
  def swapViews(self, dest_id, origin_id=None):
    """swap views"""
    origin = self.positions.index( self._getView(origin_id) )
    dest   = self.positions.index( self._getView(dest_id) )
    
    self.positions[origin], self.positions[dest] = self.positions[dest], self.positions[origin], 
    self.statusline.fillFromViewlist(self.positions)

  def switchToView(self, viewid):
    """switch requested view"""
    view = self._getView(viewid)
    self.inputline.set_prefix(view)
    self.contentwin.refresh(self.views[view].x, self.views[view].y)
    self.curr_view = view
  
  
  def first(self):
    """Switch to first view"""
    self.switchToView( 0 )
    
  def last(self):
    """Switch to last view"""
    self.switchToView( len(self.positions)-1 )
  
  def next(self):
    """switch to next view: manage contentwin as well as status, etc."""
    current_id = self.positions.index(self.curr_view)
    if current_id != self.nb_views-1:
      self.switchToView( current_id + 1 )
    else:
      # already at last view
      # @todo add conf.circular condition
      self.first()

  def prev(self):
    """switch to previous view"""
    current_id = self.positions.index(self.curr_view)
    
    if current_id > 0:
      self.switchToView( current_id - 1 )
    else:
      # @todo add conf.circular condition
      self.last()
  
  def setName(self, new_name, viewid=None):
    """change name of the current views, affects views list as well as prefix on input bar"""
    view = self._getView(viewid)
    if not isinstance(new_name, str):
      raise ArgumentError()
    
    if viewid is None:
      self.curr_view = new_name
    self.views[new_name] = self.views[view]
    del self.views[view]
    self.positions[ self.positions.index(view) ] = new_name
    self.statusline.fillFromViewlist(self.positions)
    self.inputline.set_prefix(new_name)
    
  #
  # content management methods
  #
  def clear(self, viewid=None):
    """clear content in targeted view, current if arg is omitted"""
    view = self._getView(viewid)
    self.views[view].buffer = ""
    self.views[view].cursor = 0
    self.contentwin.fillFromViews(self.views)
    
  def write(self, content, viewid=None):
    """print content into view, current if arg is omitted"""
    view = self._getView(viewid)
    ''.join([self.views[view].buffer, content, '\n'])
    
    for line in content.split('\n'):
      self.contentwin.write(self.views[view].cursor, self.views[view].x, line, refresh=False)
      self.views[view].cursor += 1
    
    self.contentwin.refresh(self.views[view].x, self.views[view].y)

