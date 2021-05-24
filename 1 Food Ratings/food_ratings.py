#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on May 21, 2021, at 18:23
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
expName = 'food_ratings'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\mauspad\\Desktop\\new_OEA_stuff\\OEA_task_test\\auction\\1 Food Ratings\\food_ratings.py',
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
    text='Please complete the following ratings.\n\nPress enter to start',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trigger = keyboard.Keyboard()

# Initialize components for Routine "liking"
likingClock = core.Clock()
food = visual.ImageStim(
    win=win,
    name='food', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(-7,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
like_q = visual.TextStim(win=win, name='like_q',
    text='How much do you like this or dislike this food?',
    font='Arial',
    pos=(-200, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
like_slider = visual.Slider(win=win, name='like_slider',
    size=(20,800), pos=(700,0), units=None,
    labels=['Most disliked sensation imaginable','Dislike extremely','Dislike very much','Dislike moderately','Dislike slightly','Neutral','Like slightly','Like moderately','Like very much','Like extremely','Most liked sensation imaginable'], ticks=[-100, -62.89, -41.58, -17.59, -5.92, 0, 6.25, 17.82, 44.43, 65.72, 100],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname = visual.TextStim(win=win, name='foodname',
    text='default text',
    font='Arial',
    pos=(-150, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "familiarity"
familiarityClock = core.Clock()
food_2 = visual.ImageStim(
    win=win,
    name='food_2', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
familiar_q = visual.TextStim(win=win, name='familiar_q',
    text='How familiar is this food?',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
familiar_slider = visual.Slider(win=win, name='familiar_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['Not familiar at all','More familiar than anything'], ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname_2 = visual.TextStim(win=win, name='foodname_2',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "filling"
fillingClock = core.Clock()
food_3 = visual.ImageStim(
    win=win,
    name='food_3', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
filling_q = visual.TextStim(win=win, name='filling_q',
    text='How filling do you expect this food to be?',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
filling_slider = visual.Slider(win=win, name='filling_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['Not filling at all','More filling than anything'], ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname_3 = visual.TextStim(win=win, name='foodname_3',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "frequency"
frequencyClock = core.Clock()
food_4 = visual.ImageStim(
    win=win,
    name='food_4', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
frequency_q = visual.TextStim(win=win, name='frequency_q',
    text='How often do you eat this food?',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
frequency_slider = visual.Slider(win=win, name='frequency_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['<1 x/month','2-3 x/month','1-2 x/week','3-4 x/week','5+ x/week'], ticks=[0,250,500,750,1000],
    granularity=250, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname_4 = visual.TextStim(win=win, name='foodname_4',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "healthy"
healthyClock = core.Clock()
food_5 = visual.ImageStim(
    win=win,
    name='food_5', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
healthy_q = visual.TextStim(win=win, name='healthy_q',
    text='How healthy is this food?',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
healthy_slider = visual.Slider(win=win, name='healthy_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['Not healthy at all','More healthy than anything'], ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname_5 = visual.TextStim(win=win, name='foodname_5',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "calories"
caloriesClock = core.Clock()
food_6 = visual.ImageStim(
    win=win,
    name='food_6', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
calorie_q = visual.TextStim(win=win, name='calorie_q',
    text='How many calories are in this portion?',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
calorie_slider = visual.Slider(win=win, name='calorie_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['0','60','120','180','240'], ticks=[0,250,500,750,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname_6 = visual.TextStim(win=win, name='foodname_6',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "dense"
denseClock = core.Clock()
food_7 = visual.ImageStim(
    win=win,
    name='food_7', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0,5), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
dense_q = visual.TextStim(win=win, name='dense_q',
    text='How energy dense is this food?',
    font='Arial',
    pos=(0, -300), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
dense_slider = visual.Slider(win=win, name='dense_slider',
    size=(1000,30), pos=(0, -350), units=None,
    labels=['Not energy dense at all','More energy dense than anything'], ticks=[0,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)
foodname_7 = visual.TextStim(win=win, name='foodname_7',
    text='default text',
    font='Arial',
    pos=(0, -200), height=50, wrapWidth=1000, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "end"
endClock = core.Clock()
bye = visual.TextStim(win=win, name='bye',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=50, wrapWidth=1000, ori=0, 
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
    
    # ------Prepare to start Routine "liking"-------
    # update component parameters for each repeat
    food.setImage(ImageFile)
    like_slider.reset()
    mouse = event.Mouse(visible=False)
    
    like_slider.marker.size=(2,.1);
    like_slider.marker.color='Red';
    
    mouse.setPos((0,0))
    like_slider.markerPos=0
    foodname.setText(Name)
    # keep track of which components have finished
    likingComponents = [food, like_q, like_slider, foodname]
    for thisComponent in likingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    likingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "liking"-------
    while continueRoutine:
        # get current time
        t = likingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=likingClock)
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
        
        # *like_q* updates
        if like_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            like_q.frameNStart = frameN  # exact frame index
            like_q.tStart = t  # local t and not account for scr refresh
            like_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_q, 'tStartRefresh')  # time at next scr refresh
            like_q.setAutoDraw(True)
        
        # *like_slider* updates
        if like_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            like_slider.frameNStart = frameN  # exact frame index
            like_slider.tStart = t  # local t and not account for scr refresh
            like_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(like_slider, 'tStartRefresh')  # time at next scr refresh
            like_slider.setAutoDraw(True)
        x = mouse.getPos()[1]
        like_slider.markerPos=(x // 5)
        
        if mouse.getPressed()[0]:
            food_items.addData('Like', like_slider.markerPos)
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
        for thisComponent in likingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "liking"-------
    for thisComponent in likingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "liking" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "familiarity"-------
    # update component parameters for each repeat
    food_2.setImage(ImageFile)
    familiar_slider.reset()
    mouse = event.Mouse(visible=False)
    
    familiar_slider.marker.size=(.1,2)
    familiar_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    familiar_slider.markerPos=0
    foodname_2.setText(Name)
    # keep track of which components have finished
    familiarityComponents = [food_2, familiar_q, familiar_slider, foodname_2]
    for thisComponent in familiarityComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    familiarityClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "familiarity"-------
    while continueRoutine:
        # get current time
        t = familiarityClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=familiarityClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_2* updates
        if food_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_2.frameNStart = frameN  # exact frame index
            food_2.tStart = t  # local t and not account for scr refresh
            food_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_2, 'tStartRefresh')  # time at next scr refresh
            food_2.setAutoDraw(True)
        
        # *familiar_q* updates
        if familiar_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            familiar_q.frameNStart = frameN  # exact frame index
            familiar_q.tStart = t  # local t and not account for scr refresh
            familiar_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(familiar_q, 'tStartRefresh')  # time at next scr refresh
            familiar_q.setAutoDraw(True)
        
        # *familiar_slider* updates
        if familiar_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            familiar_slider.frameNStart = frameN  # exact frame index
            familiar_slider.tStart = t  # local t and not account for scr refresh
            familiar_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(familiar_slider, 'tStartRefresh')  # time at next scr refresh
            familiar_slider.setAutoDraw(True)
        x = mouse.getPos()[0]
        familiar_slider.markerPos= 500 + (x)
        
        if mouse.getPressed()[0]:
            food_items.addData('Familiar', familiar_slider.markerPos)
            continueRoutine = False
        
        # *foodname_2* updates
        if foodname_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname_2.frameNStart = frameN  # exact frame index
            foodname_2.tStart = t  # local t and not account for scr refresh
            foodname_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname_2, 'tStartRefresh')  # time at next scr refresh
            foodname_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in familiarityComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "familiarity"-------
    for thisComponent in familiarityComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "familiarity" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "filling"-------
    # update component parameters for each repeat
    food_3.setImage(ImageFile)
    filling_slider.reset()
    mouse = event.Mouse(visible=False)
    
    filling_slider.marker.size=(.1,2)
    filling_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    filling_slider.markerPos=0
    foodname_3.setText(Name)
    # keep track of which components have finished
    fillingComponents = [food_3, filling_q, filling_slider, foodname_3]
    for thisComponent in fillingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fillingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "filling"-------
    while continueRoutine:
        # get current time
        t = fillingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fillingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_3* updates
        if food_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_3.frameNStart = frameN  # exact frame index
            food_3.tStart = t  # local t and not account for scr refresh
            food_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_3, 'tStartRefresh')  # time at next scr refresh
            food_3.setAutoDraw(True)
        
        # *filling_q* updates
        if filling_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            filling_q.frameNStart = frameN  # exact frame index
            filling_q.tStart = t  # local t and not account for scr refresh
            filling_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filling_q, 'tStartRefresh')  # time at next scr refresh
            filling_q.setAutoDraw(True)
        
        # *filling_slider* updates
        if filling_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            filling_slider.frameNStart = frameN  # exact frame index
            filling_slider.tStart = t  # local t and not account for scr refresh
            filling_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(filling_slider, 'tStartRefresh')  # time at next scr refresh
            filling_slider.setAutoDraw(True)
        x = mouse.getPos()[0]
        filling_slider.markerPos=500 + (x)
        
        
        if mouse.getPressed()[0]:
            food_items.addData('Filling', filling_slider.markerPos)
            continueRoutine = False
        
        # *foodname_3* updates
        if foodname_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname_3.frameNStart = frameN  # exact frame index
            foodname_3.tStart = t  # local t and not account for scr refresh
            foodname_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname_3, 'tStartRefresh')  # time at next scr refresh
            foodname_3.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fillingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "filling"-------
    for thisComponent in fillingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "filling" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "frequency"-------
    # update component parameters for each repeat
    food_4.setImage(ImageFile)
    frequency_slider.reset()
    mouse = event.Mouse(visible=False)
    
    frequency_slider.marker.size=(.1,2)
    frequency_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    frequency_slider.markerPos=0
    foodname_4.setText(Name)
    # keep track of which components have finished
    frequencyComponents = [food_4, frequency_q, frequency_slider, foodname_4]
    for thisComponent in frequencyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frequencyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "frequency"-------
    while continueRoutine:
        # get current time
        t = frequencyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=frequencyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_4* updates
        if food_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_4.frameNStart = frameN  # exact frame index
            food_4.tStart = t  # local t and not account for scr refresh
            food_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_4, 'tStartRefresh')  # time at next scr refresh
            food_4.setAutoDraw(True)
        
        # *frequency_q* updates
        if frequency_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            frequency_q.frameNStart = frameN  # exact frame index
            frequency_q.tStart = t  # local t and not account for scr refresh
            frequency_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frequency_q, 'tStartRefresh')  # time at next scr refresh
            frequency_q.setAutoDraw(True)
        
        # *frequency_slider* updates
        if frequency_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            frequency_slider.frameNStart = frameN  # exact frame index
            frequency_slider.tStart = t  # local t and not account for scr refresh
            frequency_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(frequency_slider, 'tStartRefresh')  # time at next scr refresh
            frequency_slider.setAutoDraw(True)
        x = mouse.getPos()[0]
        frequency_slider.markerPos=500 + (x)
        
        
        if mouse.getPressed()[0]:
            food_items.addData('Frequency', frequency_slider.markerPos)
            continueRoutine = False
        
        # *foodname_4* updates
        if foodname_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname_4.frameNStart = frameN  # exact frame index
            foodname_4.tStart = t  # local t and not account for scr refresh
            foodname_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname_4, 'tStartRefresh')  # time at next scr refresh
            foodname_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in frequencyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "frequency"-------
    for thisComponent in frequencyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "frequency" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "healthy"-------
    # update component parameters for each repeat
    food_5.setImage(ImageFile)
    healthy_slider.reset()
    mouse = event.Mouse(visible=False)
    
    healthy_slider.marker.size=(.1,2)
    healthy_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    healthy_slider.markerPos=0
    foodname_5.setText(Name)
    # keep track of which components have finished
    healthyComponents = [food_5, healthy_q, healthy_slider, foodname_5]
    for thisComponent in healthyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    healthyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "healthy"-------
    while continueRoutine:
        # get current time
        t = healthyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=healthyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_5* updates
        if food_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_5.frameNStart = frameN  # exact frame index
            food_5.tStart = t  # local t and not account for scr refresh
            food_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_5, 'tStartRefresh')  # time at next scr refresh
            food_5.setAutoDraw(True)
        
        # *healthy_q* updates
        if healthy_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            healthy_q.frameNStart = frameN  # exact frame index
            healthy_q.tStart = t  # local t and not account for scr refresh
            healthy_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(healthy_q, 'tStartRefresh')  # time at next scr refresh
            healthy_q.setAutoDraw(True)
        
        # *healthy_slider* updates
        if healthy_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            healthy_slider.frameNStart = frameN  # exact frame index
            healthy_slider.tStart = t  # local t and not account for scr refresh
            healthy_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(healthy_slider, 'tStartRefresh')  # time at next scr refresh
            healthy_slider.setAutoDraw(True)
        x = mouse.getPos()[0]
        healthy_slider.markerPos=500 + (x)
        
        
        if mouse.getPressed()[0]:
            food_items.addData('Healthy', healthy_slider.markerPos)
            continueRoutine = False
        
        # *foodname_5* updates
        if foodname_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname_5.frameNStart = frameN  # exact frame index
            foodname_5.tStart = t  # local t and not account for scr refresh
            foodname_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname_5, 'tStartRefresh')  # time at next scr refresh
            foodname_5.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in healthyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "healthy"-------
    for thisComponent in healthyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "healthy" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "calories"-------
    # update component parameters for each repeat
    food_6.setImage(ImageFile)
    calorie_slider.reset()
    #make and hide mouse
    mouse = event.Mouse(visible=False)
    
    #marker display options
    calorie_slider.marker.size=(.1,2)
    calorie_slider.marker.color='Red'
    
    #set mouse and marker positions
    mouse.setPos((-500,0))
    calorie_slider.markerPos=0
    foodname_6.setText(Name)
    # keep track of which components have finished
    caloriesComponents = [food_6, calorie_q, calorie_slider, foodname_6]
    for thisComponent in caloriesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    caloriesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "calories"-------
    while continueRoutine:
        # get current time
        t = caloriesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=caloriesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_6* updates
        if food_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_6.frameNStart = frameN  # exact frame index
            food_6.tStart = t  # local t and not account for scr refresh
            food_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_6, 'tStartRefresh')  # time at next scr refresh
            food_6.setAutoDraw(True)
        
        # *calorie_q* updates
        if calorie_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            calorie_q.frameNStart = frameN  # exact frame index
            calorie_q.tStart = t  # local t and not account for scr refresh
            calorie_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calorie_q, 'tStartRefresh')  # time at next scr refresh
            calorie_q.setAutoDraw(True)
        
        # *calorie_slider* updates
        if calorie_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            calorie_slider.frameNStart = frameN  # exact frame index
            calorie_slider.tStart = t  # local t and not account for scr refresh
            calorie_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calorie_slider, 'tStartRefresh')  # time at next scr refresh
            calorie_slider.setAutoDraw(True)
        #tie mouse to marker position
        x = mouse.getPos()[0]
        calorie_slider.markerPos=500 + (x)
        
        #write marker position on click
        if mouse.getPressed()[0]:
            food_items.addData('calorie', calorie_slider.markerPos)
            continueRoutine = False
        
        # *foodname_6* updates
        if foodname_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname_6.frameNStart = frameN  # exact frame index
            foodname_6.tStart = t  # local t and not account for scr refresh
            foodname_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname_6, 'tStartRefresh')  # time at next scr refresh
            foodname_6.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in caloriesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "calories"-------
    for thisComponent in caloriesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #take a nap
    core.wait(0.5)
    # the Routine "calories" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "dense"-------
    # update component parameters for each repeat
    food_7.setImage(ImageFile)
    dense_slider.reset()
    mouse = event.Mouse(visible=False)
    
    dense_slider.marker.size=(.1,2)
    dense_slider.marker.color='Red'
    
    mouse.setPos((-500,0))
    dense_slider.markerPos=0
    foodname_7.setText(Name)
    # keep track of which components have finished
    denseComponents = [food_7, dense_q, dense_slider, foodname_7]
    for thisComponent in denseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    denseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "dense"-------
    while continueRoutine:
        # get current time
        t = denseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=denseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_7* updates
        if food_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_7.frameNStart = frameN  # exact frame index
            food_7.tStart = t  # local t and not account for scr refresh
            food_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_7, 'tStartRefresh')  # time at next scr refresh
            food_7.setAutoDraw(True)
        
        # *dense_q* updates
        if dense_q.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            dense_q.frameNStart = frameN  # exact frame index
            dense_q.tStart = t  # local t and not account for scr refresh
            dense_q.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dense_q, 'tStartRefresh')  # time at next scr refresh
            dense_q.setAutoDraw(True)
        
        # *dense_slider* updates
        if dense_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            dense_slider.frameNStart = frameN  # exact frame index
            dense_slider.tStart = t  # local t and not account for scr refresh
            dense_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dense_slider, 'tStartRefresh')  # time at next scr refresh
            dense_slider.setAutoDraw(True)
        x = mouse.getPos()[0]
        dense_slider.markerPos=500 + (x)
        
        if mouse.getPressed()[0]:
            food_items.addData('Dense', dense_slider.markerPos)
            continueRoutine = False
        
        # *foodname_7* updates
        if foodname_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            foodname_7.frameNStart = frameN  # exact frame index
            foodname_7.tStart = t  # local t and not account for scr refresh
            foodname_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(foodname_7, 'tStartRefresh')  # time at next scr refresh
            foodname_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in denseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "dense"-------
    for thisComponent in denseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    core.wait(0.5)
    # the Routine "dense" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'food_items'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [bye]
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
    
    # *bye* updates
    if bye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bye.frameNStart = frameN  # exact frame index
        bye.tStart = t  # local t and not account for scr refresh
        bye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye, 'tStartRefresh')  # time at next scr refresh
        bye.setAutoDraw(True)
    if bye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bye.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            bye.tStop = t  # not accounting for scr refresh
            bye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bye, 'tStopRefresh')  # time at next scr refresh
            bye.setAutoDraw(False)
    
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
