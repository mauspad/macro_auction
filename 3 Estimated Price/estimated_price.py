#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on April 07, 2021, at 13:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'estimated_price'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\new_OEA_stuff\\OEA_task_test\\auction\\3 Estimated Price\\estimated_price.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0.522,0.506,0.412], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Pictures of food will appear on the screen.\n\nFor each item, estimate how much the portion in the picture would cost at a grocery store (e.g. Stop & Shop).\n\nClick ONCE to make your rating.\n\nPress enter to begin',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trigger = keyboard.Keyboard()

# Initialize components for Routine "food_item"
food_itemClock = core.Clock()
food = visual.ImageStim(
    win=win,
    name='food', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
estimated_price = visual.TextStim(win=win, name='estimated_price',
    text='Grocery store price:',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
price_slider = visual.Slider(win=win, name='price_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['$0','$2.50','$5'], ticks=[0,500,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname = visual.TextStim(win=win, name='foodname',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruct"-------
# update component parameters for each repeat
trigger.keys = []
trigger.rt = []
# keep track of which components have finished
instructComponents = [instructions, trigger]
for thisComponent in instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *trigger* updates
    waitOnFlip = False
    if trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger.frameNStart = frameN  # exact frame index
        trigger.tStart = t  # local t and not account for scr refresh
        trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger, 'tStartRefresh')  # time at next scr refresh
        trigger.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger.status == STARTED and not waitOnFlip:
        theseKeys = trigger.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
food_items = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageFiles_Cropped.xlsx'),
    seed=None, name='food_items')
thisExp.addLoop(food_items)  # add the loop to the experiment
thisFood_item = food_items.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFood_item.rgb)
if thisFood_item != None:
    for paramName in thisFood_item:
        exec('{} = thisFood_item[paramName]'.format(paramName))

for thisFood_item in food_items:
    currentLoop = food_items
    # abbreviate parameter names if possible (e.g. rgb = thisFood_item.rgb)
    if thisFood_item != None:
        for paramName in thisFood_item:
            exec('{} = thisFood_item[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "food_item"-------
    # update component parameters for each repeat
    food.setImage(ImageFile)
    price_slider.reset()
    #create and hide mouse
    mouse = event.Mouse(visible=False)
    
    #set marker display options
    price_slider.marker.size=(.1,2)
    price_slider.marker.color='Red'
    
    #set mouse and marker positions
    mouse.setPos((0,0))
    price_slider.markerPos=500
    foodname.setText(Name)
    # keep track of which components have finished
    food_itemComponents = [food, estimated_price, price_slider, foodname]
    for thisComponent in food_itemComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    food_itemClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "food_item"-------
    while continueRoutine:
        # get current time
        t = food_itemClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=food_itemClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food* updates
        if food.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food.frameNStart = frameN  # exact frame index
            food.tStart = t  # local t and not account for scr refresh
            food.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food, 'tStartRefresh')  # time at next scr refresh
            food.setAutoDraw(True)
        
        # *estimated_price* updates
        if estimated_price.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            estimated_price.frameNStart = frameN  # exact frame index
            estimated_price.tStart = t  # local t and not account for scr refresh
            estimated_price.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(estimated_price, 'tStartRefresh')  # time at next scr refresh
            estimated_price.setAutoDraw(True)
        
        # *price_slider* updates
        if price_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            price_slider.frameNStart = frameN  # exact frame index
            price_slider.tStart = t  # local t and not account for scr refresh
            price_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(price_slider, 'tStartRefresh')  # time at next scr refresh
            price_slider.setAutoDraw(True)
        #tie mouse to marker position
        x = 500 + mouse.getPos()[0]
        price_slider.markerPos=(x)
        
        #detect and write bid on click
        if mouse.getPressed()[0]:
            food_items.addData('Price', price_slider.markerPos)
            continueRoutine = False
        
        # *foodname* updates
        if foodname.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname.frameNStart = frameN  # exact frame index
            foodname.tStart = t  # local t and not account for scr refresh
            foodname.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname, 'tStartRefresh')  # time at next scr refresh
            foodname.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in food_itemComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "food_item"-------
    for thisComponent in food_itemComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #take a nap
    core.wait(1)
    # the Routine "food_item" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'food_items'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [done]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *done* updates
    if done.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        done.frameNStart = frameN  # exact frame index
        done.tStart = t  # local t and not account for scr refresh
        done.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(done, 'tStartRefresh')  # time at next scr refresh
        done.setAutoDraw(True)
    if done.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > done.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            done.tStop = t  # not accounting for scr refresh
            done.frameNStop = frameN  # exact frame index
            win.timeOnFlip(done, 'tStopRefresh')  # time at next scr refresh
            done.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
