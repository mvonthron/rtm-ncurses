#!/usr/bin/env python

import threading
import time
import curses.wrapper
from rtmcurses.display.display import Display


def main(stdscr):
  display = Display(stdscr)


if __name__ == '__main__':
  curses.wrapper(main)
