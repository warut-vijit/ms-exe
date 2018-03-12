
label A1_04:
###############

$ persistent.scene_number = "A1_04" # current scene
$ persistent.scene_name = "An Unabridged Tour" # current scene name
$ renpy.save_persistent()


# Red edits- HarukaNami
# Scene 04 - An Unabridged Tour
# Scene name: An Unabridged Tour
# 
# Backgrounds:
# School Entrance (day)
# Office (day)
# Classroom (day)
# 
# Sprites:
# Ela, Irene
# 
# Music: 
# Schooltheme
# Panic attack noise
# 
# Sound Effects:
# -branch breaking
# -thump sfx
# -walking sfx
# 
#-# <scene fades from CG at the end of scene 03>
scene mainbuildingclose with Dissolve(1.0)
show ela P1_E3:
  alpha 1.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
#--#
#-# >branch breaking
play sound "music/effects/Branch1.mp3"
play sound "music/effects/Branch2.mp3"
#--#
#-# >thump
scene mainbuildingclose with vpunch
show ela P1_E3:
  alpha 1.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
stop music
stop music2
stop ambience
stop ambience2
#--#
#-# >Ela surprised
show ela P1_E4
with Dissolve(0.25)
#--#

n "From above us, a girl crashes through the tree Ela was leaning on."

n "Before I even have time to register this, she rises from the debris, dusting herself off and initiating a conversation as casually as one might wave hello."

#-# >Irene unidentified
show irene U_P1_E1:
  alpha 0.0 xalign 0.75 yanchor 1.0 ypos 1080+425+100
  easein 1.0 xalign 0.75 ypos 1080+425 alpha 1.0
#--#

suspiciousperson "\"Oh hey Ela, didn't see you there; don't mind me. For the record, that tree is a bit iffy! And you must be Erik!\""

#-# >Irene smile
show irene U_P1_E2
with Dissolve(0.25)
#--#

n "She thrusts a hand in my direction, a giant smile plastered on her face."

erik "\"Uh. Yeah. It's nice to meet you...?\""

n "Ela seems to have shorted out, staring at the girl with a mixture of despair and panic."

#-# >Irene intro
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"Irene! Irene Ross, at your service!\""

#-# >In Her Element in
play music "music/In Her Element.mp3"
#--#

#-# >irene U_Post intro
show irene U_P1_E4
with Dissolve(0.25)
#--#

erik "\"Nice to meet you. I'm Erik... Hang on, how do you know my name?\""

#-# >Irene raised eyebrow
show irene U_P1_E4
with Dissolve(0.25)
#--#

irene "\"Huh? Oh. It was kind of a lucky guess? I figured it was either that or Aaron; I mean, lip reading is more art than science-- look, it's not important! And {i}heyyyy{/i} welcome to St. D's!\""

#-# >Irene open mouth smile
show irene U_P1_E2
with Dissolve(0.25)
#--#

n "Irene throws her arms in a wide gesture, at the expansive campus behind her. A thin line of blood seeps from a fresh cut on her cheekbone."

n "Ela's face has completely drained of colour."

erik "\"Uh, thanks?\""

#-# >Irene smile 2
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"No problem! It's always good to see a new face. I'm sure you'll fit right in! Ela, you're giving him the tour, right? I'd be happy to lend a hand. No one knows more about this campus than I do!\""

n "She holds up the case strung loosely around her neck - which I now realize is a pair of well-worn binoculars."

n "Ela finds her voice, maybe an octave higher than when she lost it."

#-# >Ela vs Irene
show irene U_P1_E1
with Dissolve(0.25)
show ela P1_E7
with Dissolve(0.25)
#--#

ela "\"We're fine! {i}It's fine!{/i} You probably have stuff to do, right?\""

#-# >Irene oblivious
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"Nope! Totally open today! Just doing my rounds; nothing really happening around here - except Erik, of course! - so I figured I might as well drop in. Ha! {i}'Drop in!'{/i} I didn't even mean to do that.\""

#-# >Irene yet again
show irene U_P1_E4
with Dissolve(0.25)
#--#

erik "\"So, uh... what were you doing in this tree?\""

irene "\"Oh, just climbing it. Doing some people watching. I would have brought my laser mic today, but it needs fresh batteries.\""

n "Where on Earth did she get a {i}laser microphone{/i}?"

erik "\"I... see.\""

#-# >Ela smile
show ela P1_E2
with Dissolve(0.25)
#--#

ela "\"All right, Irene, you've had your fun. I'm sure you two will run into each other later, so {i}can you please leave us be?{/i}\""

#-# >Irene neutral
show irene U_P1_E1
with Dissolve(0.25)
#--#

irene "\"Well, you just finished up your tour, right? Surely Erik wouldn't mind seeing the more fun parts of campus for a bit?\""

n "Well, I'd be lying if I said that most of Ela's tour was pretty standard..."

erik "\"Ela, we still have some time before we go back, right?\""

#-# >Ela neutral
show ela P1_E2
with Dissolve(0.25)
#--#

n "Ela takes a moment to ponder it.."

ela "\"...All right. Irene; why don't you take us to some places you like?\""

#-# >Irene smile 3
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"Great! Follow me!\""

#-# <fade to main campus view>
scene mainbuilding with Dissolve(1.0)
show irene U_P1_E1:
  alpha 0.0 xalign 0.85 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show ela P1_E3:
  alpha 0.0 xalign 0.15 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.25 alpha 1.0
#--#

n "With Irene at the helm, the tour re-commences; Ela is seemingly resigned to her inclusion. Maybe calling it a \"tour\" at this point isn't exactly accurate?"

irene "\"So that building is probably the oldest, at least judging from the brickwork. There's this one patch where the bricks are newer, but I can't {i}for the life of me{/i} figure out why.\""

erik "\"Maybe they renovated it?\""

irene "\"Nah, it's too small a section. I was thinking it could be damaged, but there's nothing on record about accidents. I tried getting a look behind it, but it turns out that kind of thing is frowned upon.\""

#-# >Ela frown
show ela P1_E6
with Dissolve(0.25)
#--#

ela "\"You were chiseling out a section of a building.\""

#-# >Irene neutral 2
show irene U_P1_E1
with Dissolve(0.25)
#--#

irene "\"Yeah, {i}for science.{/i} This is supposed to be a place of learning, you know.\""

#-# >Ela neutral 2
show ela P1_E1
with Dissolve(0.25)
#--#

erik "\"What's the building used for, if I might ask?\""

irene "\"Huh? I dunno; like exercise and stuff. They've got a gym in there. It's not very interesting.\""

ela "\"But {i}brickwork{/i} is?\""

#-# >Irene smile 4
show irene U_P1_E2
with Dissolve(0.25)
#--#

irene "\"No, what's {i}behind{/i} the brickwork might be. Like the Ark of the Covenant. Or Nazi gold.\""

#-# >Ela angry
show ela P1_E7
with Dissolve(0.25)
#--#
#-# >Ela frown 2
show ela P1_E6
with Dissolve(0.25)
#--#
#-# >Ela neutral 3
show ela P1_E1
with Dissolve(0.25)
#--#

n "Ela wrestles with herself before letting the comment go uncontested, but her expression is pretty informative nonetheless. Irene doesn't seem to notice."

n "As we explore the more mundane aspects of the campus, I (ironically) find myself relaxing more. Although Ela seemed concerned I might think badly of them, the truth is that my imagination held far worse ideas."

n "Really, it's those small touches of personalization and little imperfections that make it feel... normal."

#-# >Ela wander
scene schoolground1 with Dissolve(1.0)
show irene U_P1_E1:
  alpha 0.0 xalign 0.85 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show ela P1_E1:
  alpha 0.0 xalign 0.15 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.25 alpha 1.0
#--#

n "Eventually we wander away from the campus, Ela takes the lead again as we head towards the woods. Irene gives a shrug, but seems content to follow along. Before I have a chance to ask where we're heading next, Ela slows to a halt."

erik "\"Anything interesting out here?\""

irene "\"There's a small walking trail just ahead for students who like the outdoors.\""

erik "\"That's me. Mind if we walk down it a bit?\""

ela "\"I don't see why not.\""

irene "\"Boooooo, the woods are {i}boring.{/i} There's rumors of wolves out there, but I've never seen one before.\""

ela "\"Like it or not, this is Erik's tour.\""

n "Irene groans, but leads us down the trail anyway."

#-# <fade to trail BG>
scene schoolground2 with Dissolve(1.0)
show irene U_P1_E1:
  alpha 0.0 xalign 0.85 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show ela P1_E1:
  alpha 0.0 xalign 0.15 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.25 alpha 1.0
#--#
#-# <walking sfx starts>
play sound "music/effects/WalkingGrass.mp3"
#--#

n "The trail is nicely paved, curving through the nearby forest."

ela "\"This trail runs for about a half-mile in a loop, great for jogging, walking, or just stretching your legs.\""

ela "\"There's also a clearing coming up where some of the school clubs frequently meet.\""

erik "\"Which ones?\""

ela "\"The Astronomy Club, mainly, but smaller clubs use the space as well.\""

erik "\"That's pretty neat. Is the Astronomy Club popular?\""

#-# >Ela smile 2
show ela P1_E2
with Dissolve(0.25)
#--#

ela "\"It's got a healthy following - mainly because of the club president's efforts. She's transformed it quite a bit.\""

erik "\"Sounds good to me; I'll check it out if I have the time.\""

ela "\"That's great! Feel free to ask me about any of the clubs here.\""

n "Irene groans."

irene "\"We've been in these woods {i}forever{/i}.\""

ela "\"It can't have been more than five minutes.\""

irene "\"{i}Foreverrrr.{/i} Can we head back now?\""

n "I shrug."

erik "\"Sure, we don't have a whole lot of time left anyway.\""

#-# <timeskip>
scene mainbuilding at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#
#-# <show campus BG>
show irene U_P1_E1:
  alpha 0.0 xalign 0.85 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show ela P1_E1:
  alpha 0.0 xalign 0.15 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.25 alpha 1.0
#--#

#-# <show Ela neutral and Irene neutral>
show ela P1_E1
with Dissolve(0.25)
show irene U_P1_E1
with Dissolve(0.25)
#--#

n "The tour picks up again as we make our way to the last areas of the school - though after everything that we had covered, I'm not really sure what else there is to show."

n "Familiar locations begin to repeat, and I soon realize we've begun to take a circular path around the entire campus."

erik "\"So Irene, what do we have left to visit before this tour ends?\""

irene "\"Well, uh, that's it. I've shown you the places I liked, and I even helpfully pointed out the walking trail.\""

ela "\"Well, you're in luck, Erik. I have just about one more location to show you. In my opinion, it's probably one of the more important ones.\""

erik "\"What's that?\""

ela "\"It's the medical facilities, where our therapists are staffed.\""

#-# >Schooltheme fade out
stop music fadeout 2.0
#--#
#-# >Panic attack noise fade in
$ renpy.sound.set_volume(0.75)
play sound "music/effects/Panic Attack Sounds.mp3" fadein 1.0
#--#

n "A chill trails down my spine. Ela continues, unaware of my growing dread."

ela "\"Each student has general counseling check-ups, though it's pretty relaxed depending on how often sessions need to be scheduled.\""

n "{i}How often?{/i}"

n "I feel my throat begin to close up on me."

irene "\"I usually go a few times a month; it's kind of like the principal's office, except only therapists are there.\""

ela "\"You could take those sessions more seriously.\""

irene "\"Yeah, yeah, I get that enough from {i}them,{/i} thank you.\""

n "My heartbeat is picking up, and I struggle to focus on my breathing before they get suspicious."

erik "\"Could I... pass on this part of the tour?\""

#-# >Ela look
show ela P1_E4
with Dissolve(0.25)
#--#

#-# >Irene look
show irene U_P1_E3
with Dissolve(0.25)
#--#

erik "\"I think I've gotten a good understanding of the campus. I'll pick up the rest as I go.\""

#-# >more black
show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.4
  easein 2.0 alpha 0.5
$ renpy.sound.set_volume(0.5)
#--#
#-# >Panic noise louder
$ renpy.sound.set_volume(1.0)
play sound "music/effects/Panic Attack Sounds.mp3"
#--#

n "I try to cover it with a laugh - but I can tell it sounds off. Ela doesn't seem to have noticed, though."

ela "\"I mean... you should be able to locate the different facilities in your first week. Are you--\""

erik "\"I'm fine.\""

n "I shoot my hands up in defense and flash a smile, but I can feel myself breaking into a cold sweat."

erik "\"I just...\""

n "{i}...Can't do this.{/i}"

#-# >ears ringing
play sound "music/effects/RingingEars.mp3"
#--#

erik "\"Sorry, sorry. I just need to sit down, I just... need to...\""

n "{i}Leave....{/i}"

n "I want to say it so badly - to just spit it out and head back to my sister's apartment so I can sleep away any inclination of what's happening right now."

n "I want to go back to the way things were."

n "I lean up against the wall and try to control my breathing."

ela "\"Erik?\""

n "{i}Breathe in.{/i}"

n "{i}Breathe out.{/i}"

#-# >Panic noise fades out
stop sound fadeout 2.0
show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.4
  easein 2.0 alpha 0.0
#--#
#-# >School theme fades in
play music "music/The_Mind-Boggle.mp3" fadein 1.0
#--#

n "I finally shake off my mini panic attack after a minute."

#-# >Ela surprised 2
show ela P1_E4
with Dissolve(0.25)
#--#

ela "\"Erik, are you okay?\""

#-# >Irene frown
show irene U_P1_E3
with Dissolve(0.25)
#--#

irene "\"You need me to fetch someone, for you?\""

n "Both of them instantly react as if they've seen this before."

erik "\"No, I'm fine. Thanks. I'm just... a little nervous about the new school. Even talking about {i}that{/i} is a little too much for me.\""

erik "\"Sorry.\""

n "Ela nods."

#-# >Ela smile 3
show ela P1_E2
with Dissolve(0.25)
#--#
#-# >Irene smile 5
show irene U_P1_E2
with Dissolve(0.25)
#--#

ela "\"I understand. Well, at least you know where this building is and what it does. Do you want to head back now?\""

erik "\"Yeah, I think I'm done for the day.\""

#-# <end>
#
#--#


########

jump A1_05 # jump A?_??
