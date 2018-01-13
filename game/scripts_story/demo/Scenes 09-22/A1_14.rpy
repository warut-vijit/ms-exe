
label A1_14:
###############

$ persistent.scene_number = "A1_14" # current scene
$ persistent.scene_name = "House Call" # current scene name
$ renpy.save_persistent()


# Scene 14
# Scene name: House Call
# BGs:
# Erik's room (night)
# men's dorm hallway (night)
# 
# Music:
# Be Green (Afternoon)
# Traumen
# 
#-# <Erik's room (evening)>
scene erikdormcloudy
with Dissolve(2)
#--#

#-# >start Be Blue
play music "music/Be_Blue.mp3" loop
#--#

#-# <CG of Erik's laptop>
#
#--#

n "\"Mr Wilhelm,\""

n "\"I understand that you are joining our community a touch late in the semester. Please let me extend a warm welcome and an open invitation to drop by the counseling offices at any time.\""

n "\"Under normal circumstances, we would have had an opportunity to meet for a more formal welcome before classes had begun. This meeting allows me to get to know new students and address any concerns they may have. I apologize for missing this opportunity in your case, but I would like to make it up to you as soon as possible. Please stop by my office Wednesday at 15:45 if you are able.\""

n "\"I look forward to seeing you."
n "– Dr Faber\""

n "Dr Siegfried Schultz Faber, MB BCh"
n "Chief Counselor"
n "Privatgymnasium St. Dymphna...\""

n "Etc. etc. – I get the idea."

n "You know you're an important person when your signature goes on for six lines."

n "I sit back and wonder whether I'm supposed to click the reply button. I'm sure he'll expect me unless I outright tell him not to, and I get the distinct impression that turning down this little 'offer' of his will be more trouble than the alternative."

n "The last thing I need is to add 'antisocial' or 'problems with authority' to my extensive dossier."

n "I type out a quick 'Sure thing' back to Faber in response, just in case he needs confirmation from me."

n "After a moment's consideration, I add 'I appreciate your consideration', and hit send."

n "It's always tough figuring out how formal to be with psychiatrics."

n "Closing the laptop, I review the day's events."

n "It wasn't too bad, I have to say."

n "Sure, the students are weird, but they aren't {i}crazy{/i}. Well, most of them aren't crazy. Of the ones I've met so far."

n "And no one is strapping me to a table yet."

n "All things considered, I'd say I'm cautiously optimistic."

#-# >phone ring, possibly phone mini-cg
play sound "music/effects/phonering.ogg"
show EriksPhone
with Dissolve (2.0)
stop music fadeout (5.0)
#--#

n "My thoughts are interrupted by my phone on the desk, the default ringtone I hadn't bothered to change. I look at the number displayed almost as an afterthought as I reach for it, and my hand stops."

n "{i}Gustav.{/i}"

#-# >Traumen starts
play music "music/Traumen.mp3" loop
#--#
#-# >phone ring
play sound "music/effects/phonering.ogg"
#--#

n "A second ring jolts me from my stunned stupor, and I grab the phone, my thumb hovering over the cheerful green 'accept' graphic which now dominates my vision."

n "I haven't talked to him since the accident. My leg pulses in time with my heartbeat, as though I had needed reminding of our last meeting."

n "Why is he calling now? What time zone is he in? I bet he heard about my new accommodations. He's probably trying to be encouraging, great guy that he is."

#-# >phone ring 2
play sound "music/effects/phonering.ogg"
#--#

n "A third ring. My window is narrowing and I'm no closer to a decision than when this started. I'm not ready for this. This is too sudden, damn it. I'm trying to be a better person, sure, but Jesus it's day one and you're going to spring this on me out of nowhere?"

#-# >phone ring 3
play sound "music/effects/phonering.ogg"
#--#

n "A fourth ring, last chance. It's just a stupid phone call, not the Inquisition. I shouldn't be like this. I should just pick up the phone and say... what? 'Hi?' I can't act like everything's fine, {i}look where I am{/i}, damn it!"

#-# >phone cg out
hide EriksPhone
with Dissolve (0.5)
stop music fadeout 5.0
#--#

n "The phone finally goes dark."

n "I release a breath I didn't realize I was holding, dropping the phone like a hot coal while my voicemail lies to Gustav about my availability."

n "Please God, don't leave a message. This is already bad enough without some Schrödinger's Cat of familial guilt taking up residence in my inbox."

n "A few minutes pass in heavy silence, and there's no new notifications."

n "... {i}Starting the year off right, aren't we, Erik?{/i}"




#-# <End scene>
#
#--#

########

jump A1_15 # jump A?_??
