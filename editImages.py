# -*- mode: Python ; coding: utf-8 -*-

# This add on adds a button to the add/editor window that, when clicked, opens up all images in the note in whatever image editor you have set to default in OSx. 
# This is basically a clone of Dimitry Mikheev's "Edit Audio Images" add on (https://ankiweb.net/shared/info/1075177705) with a few work arounds to get it working in Mac OSx.
# There is no shortcut key to open the file, you must click a button in the editor.
# If there is any issues with it, please let me know and I will try my best to fix them. That being said, I have never used python before and I might not be able to fix any bugs!
# https://github.com/carlseverson/anki-edit-images-externally

# • Edit Audio Images
# https://ankiweb.net/shared/info/1040866511
# https://github.com/ankitest/anki-musthave-addons-by-ankitest
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Copyright (c) 2016 Dmitry Mikheev, http://finpapa.ucoz.net/
#
# In card reviewer F10 opens all sounds and images in external editors.
# In Add/Edit window F10 opens sounds and images only from current field.
#
# No support. Use it AS IS on your own risk.


# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import all of the Qt GUI library
from aqt.qt import *

# Chain several iterables
from itertools import chain

#import regular expressions
import re
import os
from anki.hooks import addHook
from anki.hooks import wrap
from aqt.editor import Editor
from aqt.utils import showInfo

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def editPicExternally():

    #counter = len(mw.reviewer.card.note().fields)
    #throw all the fields in string form into an array
    fields = chain(mw.reviewer.card.note().fields)

    #iterate through the array and find all image paths
    for field in fields:
        #put all image paths in an array
        pictures = re.findall(r'\<img src="(.*?)"', field)
        #load the path to the users collection 
        pathToCollection = mw.col.media.dir() +"/"
        #for each picture get the full path and then open it externally
        for picture in pictures: 
            if picture:
                fullPath = os.path.join(pathToCollection,picture)
                #need to escape spaces
                fullPath = re.sub(" ","\ ",fullPath)
                os.system("open " + fullPath)

def buttonPressed(self):
    editPicExternally()

def mySetupButtons(self):
    # - size=False tells Anki not to use a small button
    # - the lambda is necessary to pass the editor instance to the
    #   callback, as we're passing in a function rather than a bound
    #   method
    self._addButton("mybutton", lambda s=self: buttonPressed(self),
                    text="Edit Images", size=False, tip="Edit images in external editor.")

Editor.setupButtons = wrap(Editor.setupButtons, mySetupButtons)
