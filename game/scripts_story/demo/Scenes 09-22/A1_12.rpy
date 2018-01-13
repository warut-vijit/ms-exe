
label A1_12:
###############

$ persistent.scene_number = "A1_12" # current scene
$ persistent.scene_name = "Photophobia" # current scene name
$ renpy.save_persistent()


# Photophobia
# Kosherbacon
# Scene name: Photophobia
# 
# BGs:
# Courtyard, Chapel exterior, Newspaper Club Room.
# 
# Sprites:
# Hertha, Lena
# 
# Special Effects:
# 
# lens flare
# 
# Music:
# Be Green (Afternoon)
# 
#-# <Scene opens>
#
#--#

#-# <courtyard(afternoon)>
scene outsidemaledorm
with Dissolve(2)
#--#

n "I'm stewing under my coat after basically running here. Or at least, attempting to. Fanning my lapels doesn't disperse the cloud of sweat. I try taking it off altogether but someone is tugging at my sleeves from behind."

#-# >Lena enter from right to center (P4E1)
show lena U_M_P4_E1:
  xalign 0.7 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show lena U_M_P4_E1 alpha 1.0
#--#
lena "\"You're all wrinkly.\""

erik "\"I don't have an iron.\""

#-# >BIG BAD WOLF IN
play music "music/Big Bad Wolf.mp3" loop
#--#

n "She's still wearing the mask. It would seem to be a permanent fixture on her face, as opposed to something she was using just at the newspaper club."

lena "\"Here's a tip; you can get by without an iron if you put your clothes between your mattress and box spring the night before. Be careful with the collar, though.\""

erik "\"Thanks for the tip. Shall we get started? Where should I go?\""

lena "\"I'm not sure yet.\""

n "I find a stately spot by one of the building's columns and stand by it."

erik "\"How about here?\""

#-# >Lena P4_E2
show lena U_M_P4_E2
with Dissolve(0.25)
#--#
lena "\"You really want to have a picture next to a pile of crumbling bricks and tiles?\""

erik "\"Well, I...\""

#-# >Lena P4_E1
show lena U_M_P4_E1
with Dissolve(0.25)
#--#
lena "\"Just follow me. The lighting isn't that good here.\""

#-# <chapelexterior(afternoon)>
scene chapel
with Dissolve(2)
#--#

n "I feel pretty bad for Lena. She didn't even want to do this, but now she's stuck going up and down campus with me looking for the perfect location for a couple photos."

n "I'm not even that passionate about having a good photo either. I didn't even think I would be in the yearbook at all."

erik "\"So... Lena...? Where are you from?\""

#-# >Lena P4_E4
show lena U_M_P4_E4:
  xalign 0.25 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.45 alpha 1.0
show lena U_M_P4_E4 alpha 1.0
#--#
lena "\"Huh. No.\""

erik "\"Where are you--\""

lena "\"Good idea. Making small talk keeps your brain occupied and less susceptible to electromagnetic mind control.\""

erik "\"Are you serious?\""

lena "\"I figured my idea was better.\""

erik "\"What idea would that be?\""

lena "\"That jokes would work better on an awkward silence than asking me about little things.\""

n "That wasn't funny. Not unfunny in an offensive way, but in a completely-lacking-in-humour way."

erik "\"Oh.\""

#-# >Lena P4_E1 2
show lena U_M_P4_E1
with Dissolve(0.25)
#--#
lena "\"What's your favourite mental disorder?\""

n "What kind of question is that?"
#-# >SCHOOL GROUNDS THEME.MP3 IN
stop music fadeout 5.0
play music "music/Be Green (Afternoon).mp3" loop
#--#

erik "\"Um. I guess, uh, what's that one that makes people swear a lot?\""

lena "\"Tourette's can do that. So can a frontal lobotomy, though.\""

erik "\"Why do you ask?\""

lena "\"I used to ask people what they're in here for but apparently that's 'insensitive', so I ask what their favourite disorder is. They usually pick something interesting like multiple personalities, when their actual thing is like agoraphobia or something generic.\""

n "Mental illnesses aren't like cars or flavours of ice cream. I don't think any well adjusted person would have one readily picked out."

lena "\"For me it's probably amnesia. It's pretty versatile.\""

erik "\"Alright, then. Well, what {i}are{/i} you here for?\""

#-# >Lena P4_E2 2
show lena U_M_P4_E2
with Dissolve(0.25)
#--#
n "Lena snickers."

lena "\"Not amnesia. So, do you have a regular therapist?\""

erik "\"I'm going to see Dr. Faber pretty soon.\""

#-# >Lena P4_E4 2
show lena U_M_P4_E4
with Dissolve(0.25)
#--#
lena "\"Ooh, yikes.\""

erik "\"Hey, what's that supposed to mean?\""

lena "\"Well, only the really messed up kids have Dr. Faber as their therapist, you know.\""

lena "\"He specializes in all sorts of freaky crap - obscure phobias, voyeurism, Ganser Syndrome, et cetera.\""

lena "\"Basically, he's their last hope before they're sent somewhere else.\""

n "I'm not sure if Lena is trying to intentionally freak me out, or if she's always this blunt."

n "I was always under the impression that I'd only be seeing Dr. Faber a couple times before being assigned to someone else, or something like that. But for the whole year?"

erik "\"Maybe it's because I'm new? I mean, don't think I'm really worth his constant atte--\""

#-# >Lena P4_E2 3
show lena U_M_P4_E2
with Dissolve(0.25)
#--#
lena "\"Wait, stop.\""

erik "\"What?\""

lena "\"Right there. Hold still.\""

#-# >>Lens Flare~~
#
#--#

n "It takes a moment to register in my mind what she's doing. Lena puts down her bag, holds up what looks like a sheet of cardstock with aluminium foil taped on, and shines a beam of sunlight into my face."

#-# <camera shutter>
show LensFlare1
$ renpy.pause (1.0)
play sound "music/effects/cameraclick.ogg"
$ renpy.pause (0.5)
hide LensFlare1
#--#

lena "\"Okay. Done.\""

erik "\"Can I move now?\""

lena "\"Yeah.\""

erik "\"Maybe a little warning next time?\""

lena "\"People don't look their best when they're too prepared. They're always at least a little phony. I think it looks good.\""

n "Lena crams away her homemade reflector and shoves the screen on the back of her camera into my face. I can barely see the screen since Lena's reflector burned holes into my retinae."

#-# >Lena P3_E2
show lena U_M_P3_E2
with Dissolve(0.25)
#--#
lena "\"There.\""

n "I look somewhat less pained than I do in my school ID photo. Maybe catching me off guard helped me look natural. Anyway, I doubt we could do any better if we try again."

erik "\"It's good enough for me. Thanks.\""

lena "\"Yuh.\""

erik "\"So... are we done here?\""

lena "\"I guess. Are you going to the next meeting?\""

erik "\"I probably will, if my schedule permits. When's that again?\""

lena "\"No clue.\""

erik "\"Right...\""

erik "\"What's it like being in the club, anyway?\""

lena "\"I guess it's alright.\""

erik "\"What are the other members like?\""

lena "\"No stranger than the company {i}you{/i} already keep.\""

n "I assume she means Fran."

erik "\"Do you have some history with Fran? They ditched me at the club room as soon as she could.\""

lena "\"{i}They{/i} know not to mess with me, but aside from that, no. Fran used to date one of the members so they act like they're a full time member even though nothing they do gets published.\""

erik "\"Oh. So if I join, what kind of stuff would I be doing?\""

lena "\"Probably cleaning. It gets messier than you think. Does blood make you squeamish?\""

erik "\"Only if it's mine.\""

lena "\"Great. Are you busy this afternoon?\""

n "The sudden topic change almost knocks me off my feet."

erik "\"I haven't got anything planned, no.\""

lena "\"Perfect. Let's get going.\""

#-# >Timeskip
# next stage direction
#--#
#-# <newspaperclub(afternoon)>
scene clubroom1 with ImageDissolve("Transitions/clock.png", 1.0)
#--#
#-# >LIBRARY THEME IN
stop music fadeout 5.0
play music "music/Library Theme.mp3" loop
#--#

n "As it turns out, Lena would rather have me trained up sooner rather than later. The other students in this club must shirk off their work a lot if she's this eager to recruit."

#-# >Hertha P1_E1
show hertha U_P1_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show hertha U_P1_E1 alpha 1.0
#--#
wieck "\"So, what do you think?\""

n "After looking through a pile of past newspapers, I'd say it looks doable. An activity here, an informal survey there; the school newspaper looks like a good balance between challenge and enjoyability."

n "Most importantly, it looks like a chance to keep active. Meet people. Go into town. Maybe travel when the choir goes on competition or something. Maybe if I go and join the outside world, I'll find a place to belong, even if that place is being nowhere in particular."

erik "\"I think I can do this.\""

#-# >Hertha P1_E1 2
show hertha U_P1_E1
with Dissolve(0.25)
#--#
wieck "\"That's great. Just remember that your health and your studies come first. If you find yourself overwhelmed, nobody will be offended if you lay off club participation.\""

erik "\"Well, thanks, Ms. Wieck.\""

hertha "\"Again, my name is Hertha.\""

erik "\"Right.\""

hertha "\"So, tell me about your hometown. I was thinking of visiting Basel someday.\""

erik "\"It's old for the sake of being old.\""

n "She chuckles."

hertha "\"I can tell you and Lena will get along just fine.\""

erik "\"We'll see about that. Did she bite someone?\""

n "Ms. Wieck laughs heartily enough that it makes her cough."

#-# >Hertha P1_E6
show hertha U_P1_E6
with Dissolve(0.25)
#--#
hertha "\"What? What have you heard?\""

n "Before I can manage to even form a response her lips curl and she breaks into a hearty laugh."
#-# >Hertha P1_E2
show hertha U_P1_E2
with Dissolve(0.25)
#--#

hertha "\"No, she hasn't. She's had a difficult time in the past, but she had a breakthrough over the summer.\""

#-# >Hertha P1_E4
show hertha U_P1_E4
with Dissolve(0.25)
#--#
hertha "\"But if she {i}does{/i} bite, notify security immediately so they can take her out behind the barn to put her down.\""

n "Thinking she had offended me, Ms. Wieck pauses and swallows up whatever else she was going to say. I wonder if her mouth has gotten her in trouble before. It must happen a lot to younger teachers here."

#-# >Hertha P1_E1 3
show hertha U_P1_E1
with Dissolve(0.25)
#--#
hertha "\"Okay, okay, I'll stop wasting your time. I'm sure you've got lots of homework to catch up on. I'll see you soon?\""

erik "\"Maybe if you're lucky.\""

#-# >Hertha P1_E2 2
show hertha U_P1_E2
with Dissolve(0.25)
#--#
hertha "\"See you around, kiddo. And don't let Edna bother you too much! And don't call her Edna. It's \"Ms. Claes\" if she can hear it.\""

#-# <end>
stop music fadeout 5.0
#--#

########

jump A1_13 # jump A?_??
