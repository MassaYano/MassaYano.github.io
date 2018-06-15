#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on Fri Jun 15 12:23:59 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'rating'  # from the Builder filename that created this script
expInfo = {u'gender': u'', u'participant': u'', u'L1': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/masayano/Downloads/Rating_Mac/rating.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1000, 600], fullscr=False, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "practice_introduction"
practice_introductionClock = core.Clock()
instruction1 = visual.TextStim(win=win, name='instruction1',
    text='Welcome.\n\nListen carefully to the sounds that you will hear \nand then rate on a scale from 1 to 7.\n\nTry to respond as quickly and as accurately as possible.\n\nPress spacebar to begin.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
word1 = visual.TextStim(win=win, name='word1',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
trial_number1 = visual.TextStim(win=win, name='trial_number1',
    text='default text',
    font='Arial',
    pos=(0.5, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)
scale_msg1 = visual.TextStim(win=win, name='scale_msg1',
    text='least accurate(1)            most accurate(7)',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
rating1 = visual.RatingScale(win=win, name='rating1', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Initialize components for Routine "main_instruction"
main_instructionClock = core.Clock()
instruction2 = visual.TextStim(win=win, name='instruction2',
    text='OK, ready to start the main experiment?\n\nListen and rate on a scale from 1 to 7.\nTry to respond as quickly and as accurately as possible.\n\nPress spacebar to continue.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial2"
trial2Clock = core.Clock()
word2 = visual.TextStim(win=win, name='word2',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.3, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
trial_number2 = visual.TextStim(win=win, name='trial_number2',
    text='default text',
    font='Arial',
    pos=(0.5, -0.8), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
sound_2 = sound.Sound('A', secs=-1)
sound_2.setVolume(1)
scale_msg2 = visual.TextStim(win=win, name='scale_msg2',
    text='least accurate(1)            most accurate(7)',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
rating2 = visual.RatingScale(win=win, name='rating2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')

# Initialize components for Routine "the_end"
the_endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Thank you for participating in this experiment.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "practice_introduction"-------
t = 0
practice_introductionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_1 = event.BuilderKeyResponse()
# keep track of which components have finished
practice_introductionComponents = [instruction1, key_resp_1]
for thisComponent in practice_introductionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practice_introduction"-------
while continueRoutine:
    # get current time
    t = practice_introductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction1* updates
    if t >= 0.0 and instruction1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction1.tStart = t
        instruction1.frameNStart = frameN  # exact frame index
        instruction1.setAutoDraw(True)
    
    # *key_resp_1* updates
    if t >= 0.0 and key_resp_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_1.tStart = t
        key_resp_1.frameNStart = frameN  # exact frame index
        key_resp_1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_1.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_introduction"-------
for thisComponent in practice_introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pract_trial = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_stimuli.xlsx'),
    seed=None, name='pract_trial')
thisExp.addLoop(pract_trial)  # add the loop to the experiment
thisPract_trial = pract_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPract_trial.rgb)
if thisPract_trial != None:
    for paramName in thisPract_trial:
        exec('{} = thisPract_trial[paramName]'.format(paramName))

for thisPract_trial in pract_trial:
    currentLoop = pract_trial
    # abbreviate parameter names if possible (e.g. rgb = thisPract_trial.rgb)
    if thisPract_trial != None:
        for paramName in thisPract_trial:
            exec('{} = thisPract_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    word1.setText(word)
    trial_number1.setText(str(pract_trial.thisN+1) + " / " + str(pract_trial.nTotal) )
    sound_1.setSound(sound, secs=-1)
    rating1.reset()
    # keep track of which components have finished
    trial1Components = [word1, trial_number1, sound_1, scale_msg1, rating1]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word1* updates
        if t >= 0.0 and word1.status == NOT_STARTED:
            # keep track of start time/frame for later
            word1.tStart = t
            word1.frameNStart = frameN  # exact frame index
            word1.setAutoDraw(True)
        
        # *trial_number1* updates
        if t >= 0 and trial_number1.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_number1.tStart = t
            trial_number1.frameNStart = frameN  # exact frame index
            trial_number1.setAutoDraw(True)
        # start/stop sound_1
        if t >= 1 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        
        # *scale_msg1* updates
        if t >= 2 and scale_msg1.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg1.tStart = t
            scale_msg1.frameNStart = frameN  # exact frame index
            scale_msg1.setAutoDraw(True)
        # *rating1* updates
        if t >= 2 and rating1.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating1.tStart = t
            rating1.frameNStart = frameN  # exact frame index
            rating1.setAutoDraw(True)
        continueRoutine &= rating1.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop()  # ensure sound has stopped at end of routine
    # store data for pract_trial (TrialHandler)
    pract_trial.addData('rating1.response', rating1.getRating())
    pract_trial.addData('rating1.rt', rating1.getRT())
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pract_trial'


# ------Prepare to start Routine "main_instruction"-------
t = 0
main_instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
main_instructionComponents = [instruction2, key_resp_2]
for thisComponent in main_instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "main_instruction"-------
while continueRoutine:
    # get current time
    t = main_instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction2* updates
    if t >= 0.0 and instruction2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction2.tStart = t
        instruction2.frameNStart = frameN  # exact frame index
        instruction2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in main_instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "main_instruction"-------
for thisComponent in main_instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "main_instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_trial = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_stimuli.xlsx'),
    seed=None, name='main_trial')
thisExp.addLoop(main_trial)  # add the loop to the experiment
thisMain_trial = main_trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
if thisMain_trial != None:
    for paramName in thisMain_trial:
        exec('{} = thisMain_trial[paramName]'.format(paramName))

for thisMain_trial in main_trial:
    currentLoop = main_trial
    # abbreviate parameter names if possible (e.g. rgb = thisMain_trial.rgb)
    if thisMain_trial != None:
        for paramName in thisMain_trial:
            exec('{} = thisMain_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial2"-------
    t = 0
    trial2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    word2.setText(word)
    trial_number2.setText(str(main_trial.thisN+1) + " / " + str(main_trial.nTotal) )
    sound_2.setSound(sound, secs=-1)
    rating2.reset()
    # keep track of which components have finished
    trial2Components = [word2, trial_number2, sound_2, scale_msg2, rating2]
    for thisComponent in trial2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial2"-------
    while continueRoutine:
        # get current time
        t = trial2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *word2* updates
        if t >= 0.0 and word2.status == NOT_STARTED:
            # keep track of start time/frame for later
            word2.tStart = t
            word2.frameNStart = frameN  # exact frame index
            word2.setAutoDraw(True)
        
        # *trial_number2* updates
        if t >= 0.0 and trial_number2.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_number2.tStart = t
            trial_number2.frameNStart = frameN  # exact frame index
            trial_number2.setAutoDraw(True)
        # start/stop sound_2
        if t >= 1 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        
        # *scale_msg2* updates
        if t >= 2 and scale_msg2.status == NOT_STARTED:
            # keep track of start time/frame for later
            scale_msg2.tStart = t
            scale_msg2.frameNStart = frameN  # exact frame index
            scale_msg2.setAutoDraw(True)
        # *rating2* updates
        if t >= 2 and rating2.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating2.tStart = t
            rating2.frameNStart = frameN  # exact frame index
            rating2.setAutoDraw(True)
        continueRoutine &= rating2.noResponse  # a response ends the trial
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial2"-------
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop()  # ensure sound has stopped at end of routine
    # store data for main_trial (TrialHandler)
    main_trial.addData('rating2.response', rating2.getRating())
    main_trial.addData('rating2.rt', rating2.getRT())
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'main_trial'


# ------Prepare to start Routine "the_end"-------
t = 0
the_endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
the_endComponents = [text]
for thisComponent in the_endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "the_end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = the_endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in the_endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "the_end"-------
for thisComponent in the_endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
