"""
MainScreen:
    the screen that contains all info, eg. last result, overall statistics current scramble
TimerScreen:
    the screen when the cuber is fixing the cube, there is only a timer on the screen
ReadyScreen:
    when the player press the space button but has not released it, a big "READY" on the screen. And the text
    changes color as the time goes

MainScreen => Pressed Space Bar => ReadyScreen
ReadyScreen => Hold Space Bar for over a fixed time and release => TimerScreen
ReadyScreen => Hold Space Bar for less than a fixed time and release => MainScreen
TimerScreen => Space is pressed => Main Screen

Other classes:
Cube:
    do all action relative to cubing, eg. move the cube, generate scramble
    one instance for each solve
SQLManager:
    communicate with SQL database, eg. read and write
    instance only exist at the beginning and the end of the entire program
"""
import pygame

from ProgramManager import ProgramManager

pygame.init()

p = ProgramManager()
p.run()
