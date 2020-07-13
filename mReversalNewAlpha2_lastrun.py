#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on July 13, 2020, at 15:30
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
psychopyVersion = '2020.1.3'
expName = 'mReversalNewAlpha2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'taskVer': '1'}
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
    originPath='C:\\Users\\Andrew\\Documents\\Work\\Projects\\mReversalNewAlpha2\\mReversalNewAlpha2_lastrun.py',
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
    size=[1088, 614], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup"
setupClock = core.Clock()
taskVer = int(expInfo['taskVer'])
if taskVer == 1:
    order = [0,1,2]
    
win.mouseVisible = False

# psychoJS.window

targetAngles = [30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60, 30, 60]
#targetAngles = [(t/180)*pi for t in targetAngles]

#mouse = event.Mouse(visible = False)
#mouse = new psychoJS.event.Mouse({"visible": false});


# document.getElementById('hide_id').style.cursor = 'none';
# document.documentElement.style.cursor = 'none';


# Initialize components for Routine "instr"
instrClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
intrResp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
trialMouse = event.Mouse(win=win)
x, y = [None, None]
trialMouse.mouseClock = core.Clock()
trialTarget = visual.Polygon(
    win=win, name='trialTarget',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
trialHome = visual.Polygon(
    win=win, name='trialHome',
    edges=180, size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)
trialCursor = visual.Polygon(
    win=win, name='trialCursor',
    edges=180, size=(0.025, 0.025),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb',
    fillColor=[-1.000,-1.000,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
# Set experiment start values for variable component trialStep
trialStep = 0
trialStepContainer = []
trialCount = visual.TextStim(win=win, name='trialCount',
    text='trialCount',
    font='Arial',
    pos=(-0.4, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
trialSkip = keyboard.Keyboard()

# Initialize components for Routine "end"
endClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='This is the end of the experiment. Thank you for your time. Please remember to return to the questionnaire to carry on with the study. Press ‘space’ to exit.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
endResp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
setupComponents = []
for thisComponent in setupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup"-------
while continueRoutine:
    # get current time
    t = setupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup"-------
for thisComponent in setupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
taskLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('taskConds.xlsx', selection=order),
    seed=None, name='taskLoop')
thisExp.addLoop(taskLoop)  # add the loop to the experiment
thisTaskLoop = taskLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
if thisTaskLoop != None:
    for paramName in thisTaskLoop:
        exec('{} = thisTaskLoop[paramName]'.format(paramName))

for thisTaskLoop in taskLoop:
    currentLoop = taskLoop
    # abbreviate parameter names if possible (e.g. rgb = thisTaskLoop.rgb)
    if thisTaskLoop != None:
        for paramName in thisTaskLoop:
            exec('{} = thisTaskLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    intrResp.keys = []
    intrResp.rt = []
    _intrResp_allKeys = []
    if condsFile == "mReversal1Cond.xlsx":
        instrText.text = "In this task use your mouse to move the cursor (in black) between the middle start position and the outward targets (both in white). Always try to move as straight and smooth as possible. Whenever you make an error, just do better on the next trial and continue as best you can. There will be 20 trials in this first set. Press ‘space’ to start."
    elif condsFile == "mReversal2Cond.xlsx":
        instrText.text = "For the next block of trials, the cursor movement will be mirrored over the Y-axis. Again, use your mouse to move the cursor (in black) between the middle start position and the outward targets (both in white). Always try to move as straight and smooth as possible. Whenever you make an error, just do better on the next trial and continue as best you can. There will be 90 trials in this next set. Press ‘space’ to start."
    elif condsFile == "mReversal3Cond.xlsx":
        instrText.text = "For the next block of trials, the cursor movement will be normal. Again, use your mouse to move the cursor (in black) between the middle start position and the outward targets (both in white). Always try to move as straight and smooth as possible. Whenever you make an error, just do better on the next trial and continue as best you can. There will be 20 trials in this next set. Press ‘space’ to start."
    else:
        instrText.text = "space"
    # keep track of which components have finished
    instrComponents = [instrText, intrResp]
    for thisComponent in instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instr"-------
    while continueRoutine:
        # get current time
        t = instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instrText* updates
        if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instrText.frameNStart = frameN  # exact frame index
            instrText.tStart = t  # local t and not account for scr refresh
            instrText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
            instrText.setAutoDraw(True)
        
        # *intrResp* updates
        waitOnFlip = False
        if intrResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            intrResp.frameNStart = frameN  # exact frame index
            intrResp.tStart = t  # local t and not account for scr refresh
            intrResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(intrResp, 'tStartRefresh')  # time at next scr refresh
            intrResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(intrResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(intrResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if intrResp.status == STARTED and not waitOnFlip:
            theseKeys = intrResp.getKeys(keyList=['space'], waitRelease=False)
            _intrResp_allKeys.extend(theseKeys)
            if len(_intrResp_allKeys):
                intrResp.keys = _intrResp_allKeys[-1].name  # just the last key pressed
                intrResp.rt = _intrResp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr"-------
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    taskLoop.addData('instrText.started', instrText.tStartRefresh)
    taskLoop.addData('instrText.stopped', instrText.tStopRefresh)
    # the Routine "instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trialsLoop = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='trialsLoop')
    thisExp.addLoop(trialsLoop)  # add the loop to the experiment
    thisTrialsLoop = trialsLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
    if thisTrialsLoop != None:
        for paramName in thisTrialsLoop:
            exec('{} = thisTrialsLoop[paramName]'.format(paramName))
    
    for thisTrialsLoop in trialsLoop:
        currentLoop = trialsLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTrialsLoop.rgb)
        if thisTrialsLoop != None:
            for paramName in thisTrialsLoop:
                exec('{} = thisTrialsLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        # setup some python lists for storing info about the trialMouse
        trialMouse.x = []
        trialMouse.y = []
        trialMouse.leftButton = []
        trialMouse.midButton = []
        trialMouse.rightButton = []
        trialMouse.time = []
        gotValidClick = False  # until a click is received
        trialMouse.mouseClock.reset()
        targetangle = targetAngles[trialsLoop.thisN]
        targetangle_rad = pi*(targetangle/180)
        targetPos = (cos(targetangle_rad)*0.4, sin(targetangle_rad)*0.4)
        
        # Math.PI
        # Math.cos()
        # Math.sin()
        
        targetOpacity = 0
        homeOpacity = 0
        
        homeStart = False
        reachOut = False
        
        trialStep = 1
        steps = []
        
        #print('trial: '+str(trials1.thisN)+' ('+str(globalClock.getTime())+')')
        if condsFile == 'mReversal2Cond.xlsx':
            trialCount.text = str(trialsLoop.thisN+1)+" / 90"
        else: 
            trialCount.text = str(trialsLoop.thisN+1)+" / 20"
        
        trialCursor.pos = (1.5,1.5)
        trialMouse.pos = (1.5,1.5)
        trialSkip.keys = []
        trialSkip.rt = []
        _trialSkip_allKeys = []
        # keep track of which components have finished
        trialComponents = [trialMouse, trialTarget, trialHome, trialCursor, trialCount, trialSkip]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *trialMouse* updates
            if trialMouse.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialMouse.frameNStart = frameN  # exact frame index
                trialMouse.tStart = t  # local t and not account for scr refresh
                trialMouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialMouse, 'tStartRefresh')  # time at next scr refresh
                trialMouse.status = STARTED
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if trialMouse.status == STARTED:  # only update if started and not finished!
                x, y = trialMouse.getPos()
                trialMouse.x.append(x)
                trialMouse.y.append(y)
                buttons = trialMouse.getPressed()
                trialMouse.leftButton.append(buttons[0])
                trialMouse.midButton.append(buttons[1])
                trialMouse.rightButton.append(buttons[2])
                trialMouse.time.append(trialMouse.mouseClock.getTime())
            CursorTargetDistance = sqrt((trialCursor.pos[0]-trialTarget.pos[0])**2 + (trialCursor.pos[1]-trialTarget.pos[1])**2)
            CursorHomeDistance = sqrt(trialCursor.pos[0]**2 + trialCursor.pos[1]**2)
            
            steps.append(trialStep)
            # steps.push(step)
            
            if condsFile == 'mReversal2Cond.xlsx':
                mousePosX = -(trialMouse.getPos()[0])
                mousePosY = trialMouse.getPos()[1]
            else:
                mousePosX = trialMouse.getPos()[0]
                mousePosY = trialMouse.getPos()[1]
            
            if not(homeStart):
                homeOpacity = 1
                targetOpacity = 0
                trialStep = 1
                if (CursorHomeDistance < .05):
                    homeStart = True
                    print('end step 1'+' ('+str(globalClock.getTime())+')')
            
            if (not(reachOut) and homeStart):
                homeOpacity = 0
                targetOpacity = 1
                trialStep = 2
                if (CursorTargetDistance < .05):
                    reachOut = True
                    print('end step 2'+' ('+str(globalClock.getTime())+')')
            
            if (reachOut):
                homeOpacity = 1
                targetOpacity = 0
                trialStep = 3
                if (CursorHomeDistance < .05):
                    # maybe this ends the loop prematurely?
                    print('end step 3'+' ('+str(globalClock.getTime())+')')
                    continueRoutine = False
                    
            #steps = steps.append(step)
            
            # *trialTarget* updates
            if trialTarget.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialTarget.frameNStart = frameN  # exact frame index
                trialTarget.tStart = t  # local t and not account for scr refresh
                trialTarget.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialTarget, 'tStartRefresh')  # time at next scr refresh
                trialTarget.setAutoDraw(True)
            if trialTarget.status == STARTED:  # only update if drawing
                trialTarget.setOpacity(targetOpacity, log=False)
                trialTarget.setPos(targetPos, log=False)
            
            # *trialHome* updates
            if trialHome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialHome.frameNStart = frameN  # exact frame index
                trialHome.tStart = t  # local t and not account for scr refresh
                trialHome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialHome, 'tStartRefresh')  # time at next scr refresh
                trialHome.setAutoDraw(True)
            if trialHome.status == STARTED:  # only update if drawing
                trialHome.setOpacity(homeOpacity, log=False)
            
            # *trialCursor* updates
            if trialCursor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCursor.frameNStart = frameN  # exact frame index
                trialCursor.tStart = t  # local t and not account for scr refresh
                trialCursor.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCursor, 'tStartRefresh')  # time at next scr refresh
                trialCursor.setAutoDraw(True)
            if trialCursor.status == STARTED:  # only update if drawing
                trialCursor.setPos((mousePosX, mousePosY), log=False)
            
            # *trialCount* updates
            if trialCount.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialCount.frameNStart = frameN  # exact frame index
                trialCount.tStart = t  # local t and not account for scr refresh
                trialCount.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialCount, 'tStartRefresh')  # time at next scr refresh
                trialCount.setAutoDraw(True)
            
            # *trialSkip* updates
            waitOnFlip = False
            if trialSkip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialSkip.frameNStart = frameN  # exact frame index
                trialSkip.tStart = t  # local t and not account for scr refresh
                trialSkip.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialSkip, 'tStartRefresh')  # time at next scr refresh
                trialSkip.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialSkip.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialSkip.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialSkip.status == STARTED and not waitOnFlip:
                theseKeys = trialSkip.getKeys(keyList=['space'], waitRelease=False)
                _trialSkip_allKeys.extend(theseKeys)
                if len(_trialSkip_allKeys):
                    trialSkip.keys = _trialSkip_allKeys[-1].name  # just the last key pressed
                    trialSkip.rt = _trialSkip_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trialsLoop (TrialHandler)
        trialsLoop.addData('trialMouse.x', trialMouse.x)
        trialsLoop.addData('trialMouse.y', trialMouse.y)
        trialsLoop.addData('trialMouse.leftButton', trialMouse.leftButton)
        trialsLoop.addData('trialMouse.midButton', trialMouse.midButton)
        trialsLoop.addData('trialMouse.rightButton', trialMouse.rightButton)
        trialsLoop.addData('trialMouse.time', trialMouse.time)
        trialsLoop.addData('trialMouse.started', trialMouse.tStartRefresh)
        trialsLoop.addData('trialMouse.stopped', trialMouse.tStopRefresh)
        # thisExp.addData('step', stepvector)
        thisExp.addData('step', steps)
        thisExp.addData('targetangle_deg', targetangle)
        
        # psychoJS.experiment.addData('columnName', variable)
        #psychoJS.experiment.addData('step', steps)
        #psychoJS.experiment.addData('targetangle_deg', targetangle)
        trialsLoop.addData('trialTarget.started', trialTarget.tStartRefresh)
        trialsLoop.addData('trialTarget.stopped', trialTarget.tStopRefresh)
        trialsLoop.addData('trialHome.started', trialHome.tStartRefresh)
        trialsLoop.addData('trialHome.stopped', trialHome.tStopRefresh)
        trialsLoop.addData('trialCursor.started', trialCursor.tStartRefresh)
        trialsLoop.addData('trialCursor.stopped', trialCursor.tStopRefresh)
        trialsLoop.addData('trialCount.started', trialCount.tStartRefresh)
        trialsLoop.addData('trialCount.stopped', trialCount.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialsLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'taskLoop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
endResp.keys = []
endResp.rt = []
_endResp_allKeys = []
# keep track of which components have finished
endComponents = [endText, endResp]
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

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *endText* updates
    if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endText.frameNStart = frameN  # exact frame index
        endText.tStart = t  # local t and not account for scr refresh
        endText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
        endText.setAutoDraw(True)
    
    # *endResp* updates
    waitOnFlip = False
    if endResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endResp.frameNStart = frameN  # exact frame index
        endResp.tStart = t  # local t and not account for scr refresh
        endResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endResp, 'tStartRefresh')  # time at next scr refresh
        endResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endResp.status == STARTED and not waitOnFlip:
        theseKeys = endResp.getKeys(keyList=['space'], waitRelease=False)
        _endResp_allKeys.extend(theseKeys)
        if len(_endResp_allKeys):
            endResp.keys = _endResp_allKeys[-1].name  # just the last key pressed
            endResp.rt = _endResp_allKeys[-1].rt
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
thisExp.addData('endText.started', endText.tStartRefresh)
thisExp.addData('endText.stopped', endText.tStopRefresh)
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
win.mouseVisible = True


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
