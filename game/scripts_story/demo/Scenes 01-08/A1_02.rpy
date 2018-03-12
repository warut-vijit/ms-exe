
label A1_02:
###############

$ persistent.scene_number = "A1_02" # current scene
$ persistent.scene_name = "A Good Breakfast" # current scene name
$ renpy.save_persistent()


# Scene 02 - A Good Breakfast
# Scene name: A Good Breakfast
# 
# Backgrounds: 
# Apartment Bedroom (day) 
# Wilhelm sisters' flat hallway (day) 
# Wilhelm sisters' flat main room (day) 
# Wilhelm sister's flat exterior (day) 
# 
# Sprites: 
# Marc, Johanna, Beatrice, Hilda 
# 
# Music: 
# Wilhelm theme 
# 
# Sound Effects: 
# ambient city noises (loop) 
# ambient people noises (loop) 
# bedsheets rustling 
# door opening 
# door knocking 
# 
#-# <black screen>
show PitchBlack
#--#
#-# >door knocking (No music)
$ renpy.sound.set_volume(0.75)
play sound "music/effects/Knock Knock.mp3"
#--#

voice "\"Erik? Are you up yet?\""

n "..."

#-# >iris open
scene SisAptMorning at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/eye.png", 1.0)
#--#
#-# <apartment bedroom>
#
#--#
n "I crack my eyes open. Daylight streams in through the open window."

#-# >Beatrice running
$ renpy.sound.set_volume(0.75)
play sound "music/effects/BeatriceRunning.mp3"
#--#

n "Before I can even respond I hear the door open, footsteps rush in to greet me."

#-#>Beatrice_happy.png, very close, P1_E2, HD sprite
show beatrice P1_E2:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425+1100 zoom 2.0
  easein 2.0 xalign 0.4 alpha 1.0
show beatrice P1_E2 alpha 1.0
#--#

#-# >New Beginnings Arise From Old Endings begins
play music "music/New Beginnings Arise From Old Endings.mp3"
#--#

unknown "\"Hi there!\""

n "A girl is inches away from my face, cheerfully greeting me."

n "It's a face I know all too well."

erik "\"Morning, Beatrice...\""

#-#>Beatrice_happier.png, very close, P1_E3, HD sprite
show beatrice HDP1_E3:
  alpha 1.0 xalign 0.5 yanchor 1.0 ypos 1080+425+4500
with Dissolve (0.25)
#--#

n "She's bouncing with energy as she tries to pull me out of bed."

beatrice "\"It's been {i}ages{/i} since I've gotten to wake you up like this. Remember?\""

n "I'm not ready for this."

#-# >Beatrice_happy.png, normal scaling now, centered
show beatrice P1_E4:
  xalign 0.4 yanchor 1.0 ypos 1080+425 zoom 1.0
with Dissolve(0.25)
#--#

n "Still drained from last night, I work to pull the covers up as far as my nose."

erik "\"Mind if I sleep some more?\""

#-# >Beatrice pout
show beatrice P1_E5:
  xalign 0.4 yanchor 1.0 ypos 1080+425
with Dissolve(0.25)
#--#

n "That pout of hers hasn't changed in the slightest."

#-# >Beatrice small smile
show beatrice P1_E2
with Dissolve(0.25)
#--#

beatrice "\"But we have breakfast!\""

n "As if on cue, my stomach begins to complain."

n "...Maybe I can reconsider."

erik "\"What's on the menu?\""

#-# >Beatrice big smile
show beatrice P1_E3
with Dissolve(0.25)
#--#

n "She winks at me."

beatrice "\"You'll have to get your butt out of bed and find out~\""

#-# >Beatrice small smile 2
show beatrice P1_E2
with Dissolve(0.25)
#--#

n "She whips the covers off my bed in a last-ditch effort to finally get me up. Instinctively, I yank the covers back; Beatrice just pulls them off again."

n "It's really not as funny as she seems to think it is."

erik "\"Okay, okay, you win. At least let me wash up first.\""

#-#>Beatrice_laugh.png
show beatrice P1_E3
with Dissolve(0.25)
#--#

beatrice "\"Success!\""

#-#>Beatrice out
show beatrice P1_E3:
  easein 2.0 xalign 0.1 alpha 0.0
#--#

n "She cheers and jumps off my bed, dashes out of my room, and runs down the hallway announcing my eventual arrival."

n "My covers are still at the end of the bed..."

n "I guess it was the right choice to wear my pyjamas instead of going for a more 'freeing' option."

n "Thankfully, my morning prep isn't too extensive. With just a rinsing of my face and a quick combing of my hair, I'm all set for some breakfast."

#-# >clockwipe
# done next
#--#

#-# <Sister's Flat Main Room>
scene SisAptMain at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#

n "I enter the flat's main room, where the rest of my family is squashed into the somewhat small dining space."

erik "\"Morning, everyone.\""

#-#>Mum_smile.png enter right to center
show mum P1_E2:
  alpha 0.0 xalign 0.3 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.45 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

n "Mum immediately comes to my side, patting my shoulders."

mum "\"Erik, good morning! How are you feeling?\""

erik "\"Good. Kind of hungry now that I see what you and Beatrice have been up to.\""

n "There's a delicious-looking spread of eggs, toast, bacon, and fresh pastries almost overcrowding the small table everyone is seated at."

n "My mouth starts to water; I realize that I haven't really eaten since I left home."

unknown "\"Well, I'm glad to see that our baby brother is still easily swayed by some home-cooked food.\""

#-#>Mum_smile.png exit center to right
show mum P1_E2:
  easein 1.0 xalign 0.65 alpha 0.0
#--#

#-#>Hilda enter left to center
show hilda P1_E2 behind mum:
  alpha 0.0 xalign 0.4 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.5 alpha 1.0
show hilda P1_E2 alpha 1.0
#--#

n "Brunhilde rises from the kitchen table to greet me."

erik "\"How can I be a baby if I'm the tallest one here?\""

#-#>Hilda_pout.png
show hilda P2_E6
with Dissolve(0.25)
#--#

hilda "\"Height has nothing to do with maturity.\""

n "It's still so easy to tease her. I guess some things never change."

erik "\"It's the only thing you'll never hold over me. I take pride in that.\""

n "Her eyes narrow. She straightens herself and takes a commanding stance. Stepping close, Hilda purposefully reaches her hand up over my head and proceeds to tousle my hair."

#-# >Hilda_smile.png
show hilda P2_E2
with Dissolve(0.25)
#--#

n "She pulls me in for a quick hug, though it's a bit lighter and stiffer than I remember."

n "A bit more careful, I think?"

n "Still, the feeling's gone in a flash, and her eyes are soon back on mine."

hilda "\"I missed you. It's great to see you up and about, Erik.\""

erik "\"I missed you too.\""

#-# >Hilda_smile.png 2
show hilda P2_E2
with Dissolve(0.25)
#--#

hilda "\"Hey, take a seat. We've got a few things out.\""

n "My sister's reminder that food exists is enough for me. I plop down and am immediately handed a huge plate - a canvas for me to create a picture-perfect breakfast."

#-#>Beatrice enter right to center
show beatrice P1_E2:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.25 alpha 1.0
show beatrice P1_E2 alpha 1.0
#--#

beatrice "\"Just take what you want; I made a bunch for everyone today!\""

n "Beatrice is far more skilled than I am in the culinary arts; I doubt I could have made scrambled eggs in this time - let alone the array of breakfast foods in front of me."

#-# >Mum_smile.png enter offscreenleft to center, between the sisters
show mum P1_E2:
  alpha 0.0 xalign 0.6 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.85 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

n "I take a sampling of scrambled eggs and bacon - and with a gentle nudge from my mum, I take a spoonful of fruit too."

mum "\"Coffee, sweetie?\""

erik "\"Sure. I'm surprised Beatrice didn't drink all of it.\""

#-# >Hilda raised eyebrows
show hilda P2_E4
with Dissolve(0.25)
#--#

hilda "\"I take it that's your version of 'please?'\""

#-# >Beatrice huffy
show beatrice P1_E7
with Dissolve(0.25)
#--#

beatrice "\"I mean, jeez, Erik! I'm not {i}that{/i} obsessed with it, y'know!\""

#-# >Beatrice mock anger
show beatrice P1_E5
with Dissolve(0.25)
#--#

n "Of course, she's already pouring herself another cup as she says this."

#-# >Hilda smug
show hilda P2_E2
with Dissolve(0.25)
#--#

#-# >Beatrice laughing
show beatrice P1_E3
with Dissolve(0.25)
#--#

#-# >beatrice smile
show beatrice P1_E2
with Dissolve(0.25)
#--#

mum "\"Enough, girls, cut your brother some slack - at least for today. Help me clean things up, all right?\""

n "We're in their house and already my mother has taken control of the situation. In a way, this treatment does feel kind of... {i}wrong{/i}."

#-# >Mum beatrice and hilda exit
show beatrice P1_E2:
  easein 1.0 xalign 0.0 alpha 0.0
show mum P1_E2:
  easein 3.0 xalign 0.3 alpha 0.0
show hilda P2_E2:
  easein 3.0 xalign 0.0 alpha 0.0
#--#

n "I take a bite of the eggs. They're warm and fluffy; Beatrice has definitely mastered my mum's techniques."

n "I take another bite."

n "..."

n "Suddenly, I realise that I'm not as hungry as I thought I was. My brain says these should be delicious, but my tongue doesn't quite agree."

n "It tastes like something's {i}off{/i}, even though it's perfectly fine."

n "The orange juice is slightly sour, and the bacon feels more like a salty lump of fat."

n "..."

n "I try to hide my lack of appetite by chewing as slowly as possible.."

#-# >mum enters from left to center
show mum P1_E2:
  alpha 0.0 xalign 0.3 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.4 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

mum "\"Erik, eat up; your food's getting cold.\""

erik "\"...\""

n "Mum knows what happened last night, but I can tell she's just trying to get me to \"sweep it under the rug,\" so to speak. Maybe she's trying to ignore it herself."

n "I feel like I should say something here."

label A1_02_menu:
label MENu1:
#-# [Menu choice:] 
menu:
    "\"Sorry, just not hungry after last night.\"":
        jump choice_1
    "\"...Sure.\"":
        jump choice_2
#--#

#-# <if menu choice 1>
label choice_1:
#--#

erik "\"Sorry, I uh...\""

erik "\"I just can't work up much of an appetite after...\""

#-# >mum frown
show mum P1_E7
with Dissolve(0.25)
#--#

n "She realizes her little faux-pas and pats me on the shoulder."

mum "\"Oh, I'm sorry, sweetie. Do you want something else?\""

erik "\"Can I have some water?\""

#-# >mum smile
show mum P1_E2
with Dissolve(0.25)
#--#

mum "\"Of course.\""

#-# >mum exits center to left
show mum P1_E2:
  easein 1.0 xalign 0.0 alpha 0.0
jump resume
#--#

#-# <if menu choice 2>
label choice_2:
#--#

erik "\"...Okay. I'll get a little more in the tank.\""

#-# >mum smile 2
show mum P1_E2
with Dissolve(0.25)
#--#

#-# >mum exits center to left 2
show mum P1_E2:
  easein 1.0 xalign 0.0 alpha 0.0
jump resume
#--#

n "I dutifully continue eating - at least enough to clear off most of my plate; I'd rather not worry her."

#-# <resume here>
label resume:
#--#

dad "\"Okay, we'll be there soon. Thank you, Doctor.\""

#-# >>Dad_neutral enter left to center
show dad P1_E1:
  alpha 0.0 xalign 0.65 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.45 alpha 1.0
show dad P1_E1 alpha 1.0
#--#

#-# >Dad_smile.png
show dad P1_E2
with Dissolve(0.25)
#--#

dad "\"Ah, Erik. Glad to see you're awake. Sleep well?\""

erik "\"I managed. Who were you talking to?\""

#-#>Dad_neutral.png
show dad P1_E1
with Dissolve(0.25)
#--#

dad "\"Ah, I was chatting with Dr. Bosworth, your new principal.\""

#-#>Dad smile
show dad P1_E2
with Dissolve(0.25)
#--#

dad "\"He's... quite the talker.\""

#-# >Mum_smile.png enter offscreenright to rightcenter
show mum P1_E2:
  alpha 0.0 xalign 0.8 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.7 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

mum "\"Dear, would you like something to eat before we go? Some eggs managed to survive.\""

dad "\"Of course I'll take a plate. Coffee too, if you can spare a cup.\""

erik "\"If Beatrice left any, that is.\""

#-# >>scene shifts left
#show SisAptMain at Position(xpos = -1.0, xanchor=-1.0, ypos=0.5, yanchor=0.5):
#  easein 1.0 xalign 0.0
#show dad P1_E2:
#  easein 1.0 xalign 0.75
#show mum P1_E4 behind Dad:
#  easein 1.0 xalign 0.95
#--#

#-# >Beatrice angry2 enter offscreen left to left
show beatrice P1_E7:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.2 alpha 1.0
show beatrice P1_E7 alpha 1.0
#--#

beatrice "\"{i}I heard that, Erik{/i}!\""

#-# >>scene shifts back
#show SisAptMain at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5):
#  easein 1.0 xalign 1.0
#show dad P1_E2:
#  easein 1.0 xalign 0.45
#show mum P1_E4 behind Dad
#  easein 1.0 xalign 0.75
#show beatrice angry2:
#    easein 1.0 offscreenleft
#--#
#-# >beatrice out
show beatrice P1_E7:
  easein 1.0 xalign 0.1 alpha 0.0
#--#

#-#>Mum_smile.png exit right
show mum P1_E2:
  easein 1.0 xalign 0.85 alpha 0.0
#--#

n "Mum quickly runs to fetch a cup."

dad "\"So, Erik, are you ready to see the St. Dymphna campus today?\""

erik "\"As ready as I'll ever be.\""

n "St. Dymphna's..."

n "If their website is anything to go by, it's certainly picturesque. The campus was an old Jesuit monastery until they converted it into a school a few decades ago."

n "A school for..."
#-# >pause
$ renpy.pause (1.0)

#-# >pause
$ renpy.pause (1.0)
#--#
n "people with problems like mine."

dad "\"Dr. Bosworth's very eager to meet you, Erik. He said he rarely gets to meet new students in person.\""

erik "\"Why's that?\""

dad "\"I'm not sure myself, but I'd take this as a good sign. He'll be able to personally introduce you to your homeroom teacher before classes start, so if you have any questions, feel free to ask them.\""

n "I {i}guess{/i} that's a good thing? My mind's certainly full of questions..."

#-# >timewipe
scene CarInteriorAlleyWay at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#
#-# >car interior
scene CarInteriorAlleyWay at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
#--#

n "Breakfast finishes up not long after that, and the family is ready to head off into the great unknown."

mum "\"Everyone ready?\""

beatrice "\"Yep!\""

#-# >clockwipe 2
scene CarInteriorAlleyWay at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#
#-# >open with car_interior(inside alleyway) BG
scene CarInteriorAlleyWay at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
#--#

n "We all load into the car - mostly padded with my belongings - leaving me squeezed in the back with my sisters."

#-# >thump (camera shake here)
scene CarInteriorAlleyWay with vpunch
#--#

hilda "\"Beatrice, stop {i}shoving{/i}! You have plenty of room!\""

n "..."

n "Thank God I have the side seat."

mum "\"Okay, everyone, ready to go?\""

n "A chorus of \"Yes\" from the rest of us, and Mum starts up the engine."
#-# >Transition to car_interior(in Vienna) BG
scene CarInteriorVienna at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(1.0)
#--#

n "I didn't get a good look last night, but Vienna is an impressive city. There's lots of classic European architecture packed neatly against more modern storefronts and houses."

beatrice "\"Ooh, ooh, we're passing the main thoroughfare! There's a great café there that we go to a lot after work, Erik!\""

hilda "\"We're also close to where I work - oh, it's that building, right there!\""

n "She points at an office building just a block down the street."

erik "\"Wow, so do you just take a U-Bahn over here?\""

hilda "\"Yup, it's pretty convenient.\""

hilda "\"I read that your new school occasionally takes students down here on Saturdays.  We'd love to show you around once you've settled in.\""

beatrice "\"Yeah! There's a lot of fun places tucked away here.\""

erik "\"Sounds good.\""

n "I just hope that I {i}can{/i} settle in. How long will that take, I wonder?"

#-# >Transition to car_interior(highway) BG
scene CarInteriorHighway at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with Dissolve(1.0)
#--#

n "As we exit onto the highway, the city gradually fades out. We pass through smaller towns, eventually making a turn off the highway some forty minutes later."

mum "\"Almost there, everyone! Erik, this is the main road to the school.\""

erik "\"Seems nice.\""

n "And indeed, the road up to the entrance is pretty nice."

n "I only wish that it could assuage my apprehension about this place."

n "My leg twinges, almost like it's agreeing with me."

#-#>transition_start
stop music fadeout 5.0
show PitchBlack
with Dissolve(3.0)
#--#

#-#<end>
#
#--#



########

jump A1_03 # jump A?_??
