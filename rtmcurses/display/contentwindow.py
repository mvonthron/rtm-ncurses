# Copyright (c) 2010 Manuel Vonthron <manuel.vonthron@acadis.org>
#
# Redistribution of this file is permitted under
# the terms of the BSD license

import curses


class ContentWindow:
  def __init__(self):
    self = curses.newwin(curses.LINES-5, curses.COLS, 1, 0)
    
    self.bkgdset(ord(' '), curses.color_pair(1))
    self.insertln()

    self.refresh()
