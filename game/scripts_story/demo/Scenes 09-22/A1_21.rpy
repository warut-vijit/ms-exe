label A1_21:
###############

$ scene_number = "A1_21" # current scene
$ scene_name = "Mulling About"
$ renpy.save_persistent()

# Scene 21
# Mulling About
# 
# BGs:
#     school hallway, outside school, outside dorm (male)
# 
# Music:
#     Be Green
#     Irene’s theme

#-# >School hallway (afternoon) bg
scene classroomhall with Dissolve(2.0)
#--#

#-# >School Grounds Theme.mp3 In
play music "music/Be Green (Afternoon).mp3" loop fadein 5.0
#--#

n "The rest of my afternoon is spent idly walking through the halls. My homework's mostly done, but I can hold off until after dinner."

n "As I wander, my thoughts turn to the recent encounter I had with Isolda."

#-# <If Erik asked Isolda to help him up>
if (persistent.A1_20_bad):

    n "I still have a lot to learn about interacting with people, it seems. If I see her again, I should probably apologize."

#-# <If Erik got up on his own>
else:
    n "I've made another friend. Sort of. At least, I think that's what happened. It was hard to tell with her."

#-# <end variants>

n "Regardless, it's a valuable experience. I just hope that I can get more of them as I continue to go here."

#-# <outside school>
scene school2
with Dissolve(2)
#--#

n "The hallways were mostly empty, but the grounds outdoors tells a different story. Groups of students gather near the entranceways, walk together on the paths, and talk on their phones."

n "It's a surprisingly social place, a common area for students to unwind after a day of stuffy classrooms."

n "Come to think of it, if any of these students were like me for a time, I bet they'd crave a few minutes of the outdoors."

n "Not being allowed to leave your room just to get some fresh air felt like a part of you was stripped away."

n "When I was able to get out of the hospital, fresh air felt like a luxury. I'm sure other students would feel the same way."

#-# <outside male dorms>
scene outsidemaledorm 
with Dissolve(2)
#--#

n "My wanderings eventually take me back to the men's dorms."

n "I realise that I have a bit of homework I can start on before dinner, so I head up to my room and get started."

#-# <Erik's room (day)>
scene erikdorm
with Dissolve(2)
#--#

n "Today's coursework isn't too strenuous; just maths and a French essay I have to write. I can probably knock out the French essay first and start maths after dinner."

n "Let's see..."

n "\"Write about the causes of the French Revolution.\""

n "Okay, simple enough."

n "\"Use the new verb conjugations we learned this week to write your essay.\""

n "Well, that could take a bit longer than I thought it would. Sighing, I open up my laptop and start typing."

#-#timeskip
scene PitchBlack with Clockwipe
scene erikdormnight with Clockwipe
#--#

n "Okay, I can call this a good amount of progress now."

n "Just in time, seeing that all the students outside appear to be heading out for dinner."

n "Sighing, I extract myself from my chair and head over to get some food."

# TODO: presumably this means cafeteria line not cafeteria seats
#-# <cafeteria (evening)>
scene cafeterianight
with Dissolve(2)
#--#

n "More of the usual crowds here, with everyone gathered in a haphazard line for tonight's meal."

irene "\"Erik! Hi!\""

#-# >show Irene happy at center
show irene U_P1_E2:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show irene U_P1_E2 alpha 1.0

erik "\"Oh, hey Irene.\""

irene "\"Doing all right?\""

erik "\"More or less. You?\""

#-# >Irene (Neutral P1E1)
show irene U_P1_E1
with Dissolve(0.25)
#--#

n "She thinks for a bit, almost as if she's analyzing my question."

irene "\"Hmm...\""

n "No, scratch that. She {i}is{/i} analyzing my question."

irene "\"If I'd have to guess...\""

#-# >Irene (Happy P1E2)
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"I'm doing okay!\""

erik "\"You... guess?\""

irene "\"Sure! You can't {i}really{/i} tell other people how you're feeling, after all. Haven't you read Tolstoy?\""

erik "\"Can't say that I have.\""

irene "\"Could have sworn you had at some point.\""

erik "\"Pretty sure I'd remember.\""

#-# >Irene (Neutral P1E1 to Happy P1E2)
show irene U_P1_E1 with Dissolve(0.25)
$ renpy.pause (1.0)
show irene U_P1_E2 with Dissolve(0.25)
#--#

irene "\"Well anyway, want to eat dinner together?\""

n "That was a quick segue."

erik "\"I... don't see why not.\""

irene "\"Great! Let's grub up and find a place to sit!\""

n "The long line in front of us sort of makes that task a bit longer than Irene's expecting."

#-# <cafeteria seats (evening)>
scene cafeterianight
with Dissolve(2)
#--#

#-# >Irene (Neutral P1E1)
show irene U_P1_E1:
  xalign 0.8 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show irene U_P1_E1 alpha 1.0
#--#

n "Finding our seats, thankfully, was a lot less difficult. "

erik "\"This cafeteria is a lot bigger than I thought.\""

irene "\"Funny, that's what everyone says when they come here.\""

erik "\"Really?\""

irene "\"I mean, I certainly thought so. Then Ela confirmed the same story with me and some other students, and I've figured that at large percentage of the student body thinks this place is smaller than it is.\""

erik "\"Fascinating.\""

n "My food's getting cold, so I shovel a bite into my mouth while she continues."

irene "\"So I decided to take things into my own hands and investigated the cafeteria's dimensions, its {i}feng shui{/i}, everything.\""

irene "\"And you know what I found out?\""

n "I swallow, half-curious about whatever secret this girl is about to reveal to me."

erik "\"What?\""

#-# >Irene (Happy P1E2)
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"It's the tables! They're two inches taller than other, similar tables I could find online.\""

erik "\"Tables. Really?\""

n "Irene nods."

irene "\"Turns out if you feel shorter, everything's bigger. It's subtle, but the effects are huge!\""

n "I'm somewhat impressed that she did all that work, though I wonder just how much time that all took."

irene "\"Then I got to wondering: just why were these tables so tall? What does the school gain from raising all of the tables?\""

erik "\"I have absolutely no idea.\""

n "Irene continues to think for a moment."

irene "\"Me neither, but I’m sure there’s some interesting reason.\""

erik "\"Maybe they’re just cheaper?\""

irene "\"Cheaper for more table? That doesn’t make any sense, Erik.\""

erik "\"I guess.\""

#-# Dialogue based on responses to Ela in A1_18
if (persistent.A1_18 == 1):
    jump A1_21a
elif (persistent.A1_18 == 2):
    jump A1_21b
elif (persistent.A1_18 == 3):
    jump A1_21c
else:
    jump A1_21d
#--#

#-# >If “I’m fine” in A1_18
label A1_21a:

show irene U_P1_E2
with Dissolve(0.25)

irene "\"So how are you settling in?\""

erik "\"Fine, I guess. What makes you ask?\""

irene "\"Oh, Ela asked me to keep an eye on you. I was, anyway, but she asked as well.\""

erik "\"That’s kind of ominous.\""

irene "\"I keep an eye on the whole school, so by default I’m keeping an eye on you.\""

erik "\"And every student?\""

n "She nods."

irene "\"Someone has to!\""

n "I kind of doubt that, but I keep it to myself. I’m glad Ela is trying to make sure I settle in well, but I think Irene might not have been the best choice for that."

n "Her obligation fulfilled, she digs into her dinner. Seeing no opportunity for conversation, I do the same."

jump A1_21end

#-# >If “I’d like to meet people” in A1_18
label A1_21b:

show irene U_P1_E2
with Dissolve(0.25)

irene "\"So I see you’ve settled in quite well.\""

erik "\"How so?\""

irene "\"You seem pretty sociable.\""

erik "\"Do I? I don’t feel like it.\""

irene "\"Trust me, I’m pretty sure.\""

erik "\"More sure about what I’ve been doing than me?\""

show irene U_P1_E4
with Dissolve(0.25)

irene "\"I’m like ninety percent confident.\""

erik "\"Well, I guess I’ll take your word for it.\""

show irene U_P1_E2
with Dissolve(0.25)

irene "\"It’s good though! Most transfers just do their own thing and never make any friends. It’s pretty sad, to be honest.\""

erik "\"Wow.\""

irene "\"Like there was this one girl who... uh, nevermind.\""

show irene U_P1_E1
with Dissolve(0.25)

erik "\"Now I’m curious.\""

n "But Irene refuses to elaborate, and simply digs into her dinner, which must be cold at this point. Seeing no opportunity for conversation, I do the same."

jump A1_21end

#-# >If “My classes are tough” in A1_18
label A1_21c:

show irene U_P1_E4
with Dissolve(0.25)

irene "\"How’s class?\""

erik "\"You guys are a little ahead, but I think I should be able to handle it.\""

irene "\"Ah, been out of school?\""

erik "\"Just for a few months, but yeah.\""

n "I briefly consider if giving this information to Irene is a good idea."

show irene U_P1_E1
with Dissolve(0.25)

irene "\"You seem like a smart guy, you even helped Natalya with her homework.\""

erik "\"How do you know about that?\""

show irene U_P1_E4
with Dissolve(0.25)

irene "\"I know about a lot of things, Erik.\""

show irene U_P1_E1
with Dissolve(0.25)

n "I decide to leave that strange remark be and move on with the conversation."

erik "\"That was her geography homework, something I’m pretty good at. When it comes to everything else... I dunno.\""

irene "\"There are study groups in the school, Ela might be able to help you set that up.\""

erik "\"I don’t think I’m that far gone yet. Thanks, though.\""

irene "\"Anytime.\""

n "With conversation dried up, Irene digs into her dinner. With nothing to add, I do the same."

jump A1_21end

#-# >If “It’s overwhelming” in A1_18
label A1_21d:

show irene U_P1_E1
with Dissolve(0.25)

irene "\"So... are you okay?\""

erik "\"Okay?\""

# This should be a more subtle frowning expression instead of "cringe"
show irene U_P1_E3
with Dissolve(0.25)

irene "\"Yeah. You seem... I dunno. Stressed.\""

erik "\"Isn’t that normal for transfer students?\""

irene "\"Sure...\""

show irene U_P1_E1
with Dissolve(0.25)

n "Irene looks like she has more to say, but doesn’t speak it aloud."

n "With conversation dried up, Irene digs into her dinner. With nothing to add, I do the same."

jump A1_21end

#-# >Return
label A1_21end:

#-#timeskip
scene PitchBlack with Clockwipe
scene schoolnight2 with Clockwipe
#--#

#-# >Irene (Neutral P1E1)
show irene U_P1_E1:
  xalign 0.4 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.4 alpha 1.0
show irene U_P1_E1 alpha 1.0
#--#

n "With our dinners complete and our trays returned, we begin to wander from the cafeteria."

irene "\"Are you going back to the dorms?\""

erik "\"Yeah, I’ve got an assignment to work on. How about you?\""

show irene U_P1_E2
with Dissolve(0.25)

irene "\"I have an assignment too. I’ll see ya’ around, Erik!\""

#-# Irene out
show irene U_P1_E1:
  easein 1.0 xalign 0.8 alpha 0.0

n "With that, Irene takes a hard left and starts walking along a patch of grass that I’m pretty sure you’re not meant to walk on."

n "I’m pretty sure that’s not the way to the girl’s dorms, either."

#-# <END>
stop music fadeout 5.0
jump A1_22 # jump A?_??
