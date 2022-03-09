#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on March 09, 2022, at 13:49
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
expName = 'macro_auction'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Silver\\Downloads\\macro_auction-master\\macro_auction-master\\2 Auction Task and winlose\\auction_task_BEHAVIORAL.py',
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

# Initialize components for Routine "choose_prot"
choose_protClock = core.Clock()
choose_text = visual.TextStim(win=win, name='choose_text',
    text='Experimenter: Select protocol 1, 2, or 3 using keyboard',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
prot_selection = keyboard.Keyboard()
#create and hide mouse
mouse = event.Mouse(visible=False)

#create image lists
carb_images = ['ImageFiles_Cropped/Bagel_120_cropped.jpg', 
'ImageFiles_Cropped/BakedBeans_120_cropped.jpg', 
'ImageFiles_Cropped/DriedApricots_120_cropped.jpg',
'ImageFiles_Cropped/FrootLoops_120_cropped.jpg',
'ImageFiles_Cropped/FrostedFlakes_120_cropped.jpg',
'ImageFiles_Cropped/FruitSnacks_120_cropped.jpg',
'ImageFiles_Cropped/GummyBears_120_cropped.jpg',
'ImageFiles_Cropped/JellyBeans_120_cropped.jpg',
'ImageFiles_Cropped/LuckyCharms_120_cropped.jpg',
'ImageFiles_Cropped/PineappleRings_120_cropped.jpg',
'ImageFiles_Cropped/Pretzels_120_cropped.jpg',
'ImageFiles_Cropped/Sorbet_120_cropped.jpg']

fat_images = ['ImageFiles_Cropped/AmericanCheese_120_cropped.jpg',
'ImageFiles_Cropped/BabybelCheeseWheels_120_cropped.jpg',
'ImageFiles_Cropped/BlueCheese_120_cropped.jpg',
'ImageFiles_Cropped/BreakfastSausage_120_cropped.jpg',
'ImageFiles_Cropped/BrieCheese_120_cropped.jpg',
'ImageFiles_Cropped/ColbyJackCheese_120_cropped.jpg',
'ImageFiles_Cropped/DeviledEggs_120_cropped.jpg',
'ImageFiles_Cropped/HardboiledEggs_120_cropped.jpg',
'ImageFiles_Cropped/Pepperoni_120_cropped.jpg',
'ImageFiles_Cropped/StringCheese_120_cropped.jpg',
'ImageFiles_Cropped/SummerSausage_120_cropped.jpg',
'ImageFiles_Cropped/SwissCheese_120_cropped.jpg']

combo_images = ['ImageFiles_Cropped/BananaNutBread_120_cropped.jpg',
'ImageFiles_Cropped/CheeseAndCrackers_120_cropped.jpg',
'ImageFiles_Cropped/ChocolateCoveredPretzels_120_cropped.jpg',
'ImageFiles_Cropped/ChocolateRaisins_120_cropped.jpg',
'ImageFiles_Cropped/Doritos_120_cropped.jpg',
'ImageFiles_Cropped/Guacamole_120_cropped.jpg',
'ImageFiles_Cropped/MiniChocolateChipCookies_120_cropped.jpg',
'ImageFiles_Cropped/MiniNutterButters_120_cropped.jpg',
'ImageFiles_Cropped/PeanutbutterAndCrackers_120_cropped.jpg',
'ImageFiles_Cropped/PizzaRolls_120_cropped.jpg',
'ImageFiles_Cropped/Pringles_120_cropped.jpg',
'ImageFiles_Cropped/RoastedRedPepperHummus_120_cropped.jpg']

#randomize their oder
shuffle(carb_images)
shuffle(fat_images)
shuffle(combo_images)

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='Pictures of food will appear on the screen.\nMake your bid for the food portion shown in the picture.\nYou have 5 seconds to make your bid.\nBe quick, but accurate!\n\n\n\nExperimenter: Press Enter to begin',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
trigger = keyboard.Keyboard()

# Initialize components for Routine "food"
foodClock = core.Clock()
food_item = visual.ImageStim(
    win=win,
    name='food_item', units='cm', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(28,18.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "auction"
auctionClock = core.Clock()
auction_slider = visual.Slider(win=win, name='auction_slider',
    size=(1000,30), pos=(0, 0), units=None,
    labels=['$0','$2.50','$5'], ticks=[0,500,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)

# Initialize components for Routine "auction_sham"
auction_shamClock = core.Clock()
auction_slider_sham = visual.Slider(win=win, name='auction_slider_sham',
    size=(1000,30), pos=(0, 0), units=None,
    labels=['$0','$2.50','$5'], ticks=[0,500,1000],
    granularity=0, style=['slider'],
    color='Black', font='HelveticaBold',
    flip=False)

# Initialize components for Routine "end"
endClock = core.Clock()
done = visual.TextStim(win=win, name='done',
    text='You have completed the task :)\n\nExperimenter: Press Enter to quit',
    font='Arial',
    pos=(0, 0), height=30, wrapWidth=1000, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_task = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "choose_prot"-------
# update component parameters for each repeat
prot_selection.keys = []
prot_selection.rt = []
# keep track of which components have finished
choose_protComponents = [choose_text, prot_selection]
for thisComponent in choose_protComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
choose_protClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "choose_prot"-------
while continueRoutine:
    # get current time
    t = choose_protClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=choose_protClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *choose_text* updates
    if choose_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        choose_text.frameNStart = frameN  # exact frame index
        choose_text.tStart = t  # local t and not account for scr refresh
        choose_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(choose_text, 'tStartRefresh')  # time at next scr refresh
        choose_text.setAutoDraw(True)
    
    # *prot_selection* updates
    waitOnFlip = False
    if prot_selection.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prot_selection.frameNStart = frameN  # exact frame index
        prot_selection.tStart = t  # local t and not account for scr refresh
        prot_selection.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prot_selection, 'tStartRefresh')  # time at next scr refresh
        prot_selection.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prot_selection.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(prot_selection.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prot_selection.status == STARTED and not waitOnFlip:
        theseKeys = prot_selection.getKeys(keyList=['1', '2', '3'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            prot_selection.keys = theseKeys.name  # just the last key pressed
            prot_selection.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    if prot_selection.keys == '1':
        conditionsFile = 'condition_files/prot1.xlsx'
    elif prot_selection.keys == '2':
        conditionsFile = 'condition_files/prot2.xlsx'
    elif prot_selection.keys == '3':
        conditionsFile = 'condition_files/prot3.xlsx'
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in choose_protComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "choose_prot"-------
for thisComponent in choose_protComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if prot_selection.keys in ['', [], None]:  # No response was made
    prot_selection.keys = None
thisExp.addData('prot_selection.keys',prot_selection.keys)
if prot_selection.keys != None:  # we had a response
    thisExp.addData('prot_selection.rt', prot_selection.rt)
thisExp.nextEntry()
# the Routine "choose_prot" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
        waitOnFlip = True
        win.callOnFlip(trigger.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger.status == STARTED and not waitOnFlip:
        theseKeys = trigger.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            trigger.keys = theseKeys.name  # just the last key pressed
            trigger.rt = theseKeys.rt
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
# check responses
if trigger.keys in ['', [], None]:  # No response was made
    trigger.keys = None
thisExp.addData('trigger.keys',trigger.keys)
if trigger.keys != None:  # we had a response
    thisExp.addData('trigger.rt', trigger.rt)
thisExp.addData('trigger.started', trigger.tStartRefresh)
thisExp.addData('trigger.stopped', trigger.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
bid_items = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(conditionsFile),
    seed=None, name='bid_items')
thisExp.addLoop(bid_items)  # add the loop to the experiment
thisBid_item = bid_items.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBid_item.rgb)
if thisBid_item != None:
    for paramName in thisBid_item:
        exec('{} = thisBid_item[paramName]'.format(paramName))

for thisBid_item in bid_items:
    currentLoop = bid_items
    # abbreviate parameter names if possible (e.g. rgb = thisBid_item.rgb)
    if thisBid_item != None:
        for paramName in thisBid_item:
            exec('{} = thisBid_item[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "food"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    if foodtype == 'fat':
        image_file = fat_images.pop()
    elif foodtype == 'carb':
        image_file = carb_images.pop()
    elif foodtype == 'combo':
        image_file = combo_images.pop()
    
    thisExp.addData('image_file', image_file)
    food_item.setImage(image_file)
    # keep track of which components have finished
    foodComponents = [food_item]
    for thisComponent in foodComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    foodClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "food"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = foodClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=foodClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *food_item* updates
        if food_item.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            food_item.frameNStart = frameN  # exact frame index
            food_item.tStart = t  # local t and not account for scr refresh
            food_item.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(food_item, 'tStartRefresh')  # time at next scr refresh
            food_item.setAutoDraw(True)
        if food_item.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > food_item.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                food_item.tStop = t  # not accounting for scr refresh
                food_item.frameNStop = frameN  # exact frame index
                win.timeOnFlip(food_item, 'tStopRefresh')  # time at next scr refresh
                food_item.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in foodComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "food"-------
    for thisComponent in foodComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    bid_items.addData('food_item.started', food_item.tStartRefresh)
    bid_items.addData('food_item.stopped', food_item.tStopRefresh)
    
    # ------Prepare to start Routine "auction"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    auction_slider.reset()
    #create and hide mouse
    mouse = event.Mouse(visible=False)
    
    #start timer
    timer = core.Clock()
    
    #marker display options
    auction_slider.marker.size=(.1,2)
    auction_slider.marker.color='Red'
    
    #set mouse and marker positions
    mouse.setPos((0,0))
    auction_slider.markerPos=500
    
    #start click detector
    didclick = 0
    # keep track of which components have finished
    auctionComponents = [auction_slider]
    for thisComponent in auctionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    auctionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "auction"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = auctionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=auctionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *auction_slider* updates
        if auction_slider.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            auction_slider.frameNStart = frameN  # exact frame index
            auction_slider.tStart = t  # local t and not account for scr refresh
            auction_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(auction_slider, 'tStartRefresh')  # time at next scr refresh
            auction_slider.setAutoDraw(True)
        if auction_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > auction_slider.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                auction_slider.tStop = t  # not accounting for scr refresh
                auction_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(auction_slider, 'tStopRefresh')  # time at next scr refresh
                auction_slider.setAutoDraw(False)
        #tie mouse to marker position
        x = 500 + mouse.getPos()[0]
        auction_slider.markerPos=(x)
        
        #write marker position and RT on click and count it
        if mouse.getPressed()[0]:
            bid_items.addData('Bid', auction_slider.markerPos)
            bid_items.addData('Bid_RT', timer.getTime())
            didclick = 1
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in auctionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "auction"-------
    for thisComponent in auctionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #check for null response and timestamp end of routine
    elapsedtime = timer.getTime()
    if didclick == 0:
        bid_items.addData('Bid', 9999)
        bid_items.addData('Bid_RT', 9999)
    
    # ------Prepare to start Routine "auction_sham"-------
    # update component parameters for each repeat
    #hide mouse
    mouse = event.Mouse(visible=False)
    auction_slider_sham.reset()
    # keep track of which components have finished
    auction_shamComponents = [auction_slider_sham]
    for thisComponent in auction_shamComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    auction_shamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "auction_sham"-------
    while continueRoutine:
        # get current time
        t = auction_shamClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=auction_shamClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *auction_slider_sham* updates
        if auction_slider_sham.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            auction_slider_sham.frameNStart = frameN  # exact frame index
            auction_slider_sham.tStart = t  # local t and not account for scr refresh
            auction_slider_sham.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(auction_slider_sham, 'tStartRefresh')  # time at next scr refresh
            auction_slider_sham.setAutoDraw(True)
        if auction_slider_sham.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > auction_slider_sham.tStartRefresh + 5 - elapsedtime-frameTolerance:
                # keep track of stop time/frame for later
                auction_slider_sham.tStop = t  # not accounting for scr refresh
                auction_slider_sham.frameNStop = frameN  # exact frame index
                win.timeOnFlip(auction_slider_sham, 'tStopRefresh')  # time at next scr refresh
                auction_slider_sham.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in auction_shamComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "auction_sham"-------
    for thisComponent in auction_shamComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "auction_sham" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'bid_items'


# ------Prepare to start Routine "end"-------
# update component parameters for each repeat
end_task.keys = []
end_task.rt = []
# keep track of which components have finished
endComponents = [done, end_task]
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
while continueRoutine:
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
    
    # *end_task* updates
    waitOnFlip = False
    if end_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_task.frameNStart = frameN  # exact frame index
        end_task.tStart = t  # local t and not account for scr refresh
        end_task.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_task, 'tStartRefresh')  # time at next scr refresh
        end_task.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_task.status == STARTED and not waitOnFlip:
        theseKeys = end_task.getKeys(keyList=['return'], waitRelease=False)
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
thisExp.addData('done.started', done.tStartRefresh)
thisExp.addData('done.stopped', done.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
