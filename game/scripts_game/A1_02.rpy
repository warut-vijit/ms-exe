
label A1_02:
###############

  $ persistent.scene_number = "A1_02" # current scene


# Scene 02
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
#-# >door knocking
todo "{color=#ff8c00}>door knocking{/color}"
#--#

voice "\"Erik? Are you up yet?\""

n "…"

#-# >iris open
image SisAptMorning:
  im.Scale("images/Backgrounds/SistersAppartment_ErikRoom_Morning.png", config.screen_width, config.screen_height)
scene SisAptMorning
with irisout
#--#
#-# <apartment bedroom>
#
#--#
n "I crack open my eyes. Daylight streams through the open window."

n "Before I can even respond I hear the door open, footsteps rushing in to greet me."

#-# >Beatrice_happy.png, very close
image Beatrice Happy VClose = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E2.png", 0.8)
show Beatrice Happy VClose:
  offscreenleft
  alpha 0.0 xalign 0.05 yalign 0.05
  easein 1.0 xalign 0.1 alpha 1.0
#--#

Voice "\"Hi there!\""

n "A girl is inches away from my face, cheerfully greeting me."

n "It's a face I know all too well."

erik "\"Morning Beatrice…\""

n "A tired mumble escapes me as I greet who most people assume to be my younger sister."

n "Beatrice, however, is my senior by a few years, exuding youth that belies her true age. She’s like a little kid, literally shaking with energy as she tries to pull me out of bed."

n "I'm not ready for this."

n "Still drained from last night, I work to pull the covers up as far as my nose."

erik "\"Mind if I sleep some more?\""

#-# >Beatrice_pout.png
image Beatrice Pout Close = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E5.png", 0.666)
show Beatrice Pout Close
with Dissolve(0.25)
#--#
n "Beatrice pouts. A classic expression of hers."

beatrice "\"But we have breakfast!\""

n "As if on cue my stomach begins to complain loudly to me."

n "...Maybe I can reconsider."

erik "\"What's on the menu?\""

n "She winks at me."

beatrice "\"You'll have to get your butt out of bed and find out~\""

n "She whips the covers off my bed in one last-ditch effort for me to finally get up. Instinctively, I pull the covers back; Beatrice just pulls them off playfully again. It’s really not as funny as she seems to think it is."

erik "\"Okay, okay, you win. At least let me wash up first.\""

#-# >Beatrice_laugh.png
image Beatrice Laugh Close2 = im.Flip(im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E3.png", 0.666), horizontal=True)
show Beatrice Laugh Close2:
  easein 1.0 xalign 0.0 alpha 0.0
#--#

beatrice "\"Success!\""

n "She cheers and proceeds to jump off my bed, dash out of my room, and run down the hallway announcing my eventual arrival."

n "With my covers at the end of the bed."

n "I guess it was the right choice to wear my pyjamas instead of going for a more ‘free’ option."

n "Thankfully my morning prep isn't too extensive. With just a rinsing of my face and a quick combing of my hair I’m all set for some breakfast."

#-# <Sister's Flat Main Room>
image SisAptMain:
  im.Scale("images/Backgrounds/SistersAppartmentMain.png", config.screen_width*1.2, config.screen_height*1.2)
scene SisAptMain at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
#--#



n "I enter the main area of the flat, where the rest of my family is squashed into the somewhat small dining space."

erik "\"Morning, everyone.\""

#-# >Mum_smile.png enter right to center
image Mum Smile = im.FactorScale("images/Sprites/Side Characters/Mrs Wilhelm/MamaWilhelm_P1_E2.png", 0.5)
show Mum Smile:
  offscreenright
  alpha 0.0 xalign 0.3 yalign -0.1
  easein 1.0 xalign 0.45 alpha 1.0
#--#

n "Mum immediately comes to my side, patting my shoulders."

mum "\"Erik, good morning! How are you feeling?\""

erik "\"Good. Kind of hungry now that I see what you and Beatrice have been up to.\""

n "There's a delicious-looking spread of eggs, toast, bacon, and fresh pastries almost overflowing from the small table everyone is seated at."

n "My mouth starts to water; I realize that I haven't really eaten since I left home."

Voice "\"Well, I'm glad to see that our baby brother is still easily swayed by some home cooking.\""

#-# >Mum_smile.png  exit center to right
show Mum Smile:
  easein 1.0 xalign 0.8 alpha 0.0
#--#

#-# >Hilda enter left to center
image Hilda Neutral = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P1_E2.png", 0.5)
show Hilda Neutral:
  offscreenleft
  alpha 0.0 xalign 0.0 yalign -0.2
  easein 1.0 xalign 0.1 alpha 1.0
#--#

erik "\"How can I be a baby if I'm the tallest one here?\""

#-# >Hilda_pout.png
image Hilda Pout = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E1.png", 0.5)
show Hilda Pout
with Dissolve(0.25)
#--#

hilda "\"Height is no indication of maturity.\""

erik "\"It’s the only thing you’ll never hold over me. I take pride in that.\""

n "Her eyes narrow, straightening herself and taking a commanding stance. Stepping close, she reaches her hand up purposely over my head - and proceeds to tousle my hair."

#-# >Hilda_smile.png
image Hilda Smile = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E2.png", 0.5)
show Hilda Smile
with Dissolve(0.25)
#--#

n "Her pout quickly dissipates into a warm and comforting smile. She pulls me in for a quick hug, though it’s a bit lighter and stiffer than how I remembered them."

n "Still, the feeling’s gone in a flash, and her eyes are soon back on mine."

hilda "\"I missed you. It’s great to see you up and about, Erik.\""

erik "\"I missed you too. I hate how every time I see you guys there has to be some reason behind it.\""

hilda "\"It’s understandable. Making a trip out to Vienna isn’t something you can do on a whim. If anything, it would be more feasible for us to come visit you.\""

erik "\"Well, it’s the thought that counts, right? I don’t think any of us have as much spare time as we used to…\""

erik "\"Speaking of which, where's Dad?\""

#-# >Hilda_neutral.png
show Hilda Neutral
with Dissolve(0.25)
#--#

hilda "\"He stepped out to take a phone call.\""

erik "\"Even on a Sunday? Geez, work never lets up for him, does it?\""





"It's not unheard of for Dad to have to take or receive calls at any time during the week. During dinner, at breakfast, even when we're in the car – it seems like someone always needs Dad for something. I'm sure he hates it at this point."

#-# >Beatrice_happy.png enter right
image Beatrice Happy2 = im.Flip(im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E2.png", 0.5), horizontal=True)
show Beatrice Happy2:
  offscreenright
  alpha 0.0 xalign 0.8 yalign 0.05
  easein 1.0 xalign 0.7 alpha 1.0
#--#

beatrice "\"Sit down and eat something, Erik! The food’s getting cold.\""

n "My sister's reminder that food exists is enough for me. I plop down and am immediately handed a huge plate: a canvas for me to create a picture perfect breakfast."

beatrice "\"Just take what you want – I made a bunch for everyone today!\""

#-# >Beatrice_happy.png exit right
image Beatrice Happy = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E2.png", 0.5)
show Beatrice Happy:
  easein 1.0 xalign 0.9 alpha 0.0
#--#

n "Beatrice is apparently far more skilled than I am at the culinary arts; I doubt I could have made scrambled eggs by this time, let alone the array of breakfast foods in front of me."

#-# >Mum_smile.png enter left
show Mum Smile:
  offscreenleft
  alpha 0.0 xalign 0.2 yalign -0.1
  easein 1.0 xalign 0.35 alpha 1.0
#--#

n "I take a generous sampling of eggs and bacon, and with a gentle nudge from my mum, I take a spoonful of vegetables too."

mum "\"Coffee, sweetie?\""

erik "\"Sure. I’m surprised Beatrice didn’t drink all of it.\""

hilda "\"I take it that’s your version of ‘please’?\""

beatrice "\"I mean jeez, Eric! I’m not that obsessed with coffee, y’know!\""

n "Of course she’s already holding a cup as she says this, which she seems to realize the moment the words have left her mouth."

n "If this wasn’t already her third mug into a potential heart attack I’d be thoroughly surprised."

mum "\"Enough, girls, cut your brother some slack. At least for today.\""

n "We’re in their house and already my mother has taken control of the situation. In a way this treatment does feel kind of… wrong."

#-# >Beatrice_happy.png exit right 2
show Beatrice Happy:
  easein 1.0 xalign 0.9 alpha 0.0
show Hilda:
  easein 1.0 xalign 0. alpha 0.0
#--#

#-# >Mum_smile.png exit left
image Mum Smile2 = im.Flip(im.FactorScale("images/Sprites/Side Characters/Mrs Wilhelm/MamaWilhelm_P1_E2.png", 0.5), horizontal=True)
show Mum Smile2:
  easein 1.0 xalign 0.1 alpha 0.0
#--#

n "I could get used to this treatment. In the back of my head, though, I'm well aware of what Monday will bring. A new school and no more breakfasts as good as this one. At least not until Christmas."

n "St. Dymphna’s..."

n "It’s a photogenic school, at least if their website is anything to go by. The campus was an old Jesuit monastery until they converted it into a school a few decades ago."

n "A school for..."

#-# >pause
$ renpy.pause (3.0)
#--#

n "well, people like me."

n "I'll be seeing it tomorrow. Today, however, my sisters want to take me around Vienna while Mum and Dad take care of some school paperwork and arrange to meet with the headmaster."

n "I don't know how different this will be from the other therapists and special organizations I've visited in the past few months. All I can think of is the alien sterility of the hospitals."

n "Pastel green to keep patients calm, the smell of antiseptics and bleach, and worst of all, the uncanny appearance of the patients that I would occasionally catch a glimpse of."

dad "\"Okay, we'll be there soon. Thank you, Doctor.\""

#-# >>Dad enter left to center
image Dad Neutral2 = im.Flip(im.FactorScale("images/Sprites/Side Characters/Mr Wilhelm/MrWilhelm_P1_E1.png", 0.5), horizontal=True)
show Dad Neutral2:
  offscreenleft
  alpha 0.0 xalign 0.3 yalign 0.05
  easein 1.0 xalign 0.45 alpha 1.0
with Dissolve(0.25)
#--#

n "My dad finally returns from his phone call."

#-# >Dad_smile.png
image Dad Smile2 = im.Flip(im.FactorScale("images/Sprites/Side Characters/Mr Wilhelm/MrWilhelm_P1_E2.png", 0.5), horizontal=True)
show Dad Smile2
with Dissolve(0.25)
#--#

dad "\"Ah, Erik. Glad to see you're awake. Ready for today?\""

erik "\"Pretty much. You and Mum are taking care of the admission paperwork today?\""

#-# >Dad_neutral.png
show Dad Neutral2
with Dissolve(0.25)
#--#

dad "\"Most of it, anyway. I was just talking to Dr. Bosworth to confirm that we're meeting him today. But he's...well, quite the talker.\""

n "My dad was never one for drawn out conversations. His job as a financial analyst revolves around lots of paperwork, approving new product types and building assessment tools for credit scoring."

n "Not a \"fun\" job by definition, but it pays well, according to him."

#-# >Mum_smile.png enters right
show Mum Smile2 behind Dad:
  offscreenright
  alpha 0.0 xalign 0.87 yalign -0.1
  easein 1.0 xalign 0.75 alpha 1.0
#--#

mum "\"Dear, would you like something to eat before we go? Some eggs managed to survive.\""

#-# >Dad_smile.png 2
show Dad Smile2
with Dissolve(0.25)
#--#

dad "\"Of course I'll take a plate. Coffee too, if you can spare a cup.\""

erik "\"If Beatrice left any, that is.\""

beatrice "\"OH MY GOD, ERIK.\""

#-# >>scene shifts left
show SisAptMain at Position(xpos = 0.0, xanchor=0.0, ypos=0.5, yanchor=0.5)
show Dad Neutral2:
  xalign 0.75
show Mum Smile2 behind Dad:
  xalign 0.95
#--#

"{color=#ff8c00}{/color}"


#-# >>scene shifts back
show SisAptMain at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
show Dad Neutral2:
  xalign 0.45
show Mum Smile2 behind Dad:
  xalign 0.75
#--#

#-# >Mum_smile.png exit right
show Mum Smile:
  easein 1.0 xalign 0.85 alpha 0.0
#--#

n "Mum quickly runs to fetch a cup."

dad "\"So, Erik, are you ready for today? Your sisters are very eager to show you around town for a while.\""

erik "\"Yeah. I guess I haven't seen Vienna ever since we helped them move here.\""

dad "\"It's a beautiful city. Classical architecture, plenty of shops and cafes – you'll have fun, I'm sure.\""

#-# >Hilda enter from right
show Hilda Neutral:
  offscreenright
  alpha 0.0 xalign 0.8 yalign -0.2
  easein 1.0 xalign 0.7 alpha 1.0
#--#

#-# >Hilda_smile.png 2
show Hilda Smile
with Dissolve(0.25)
#--#

hilda "\"Erik, Beatrice is almost ready. Why don't you wait outside with me?\""

erik "\"Uh, sure. Sounds good.\""

n "I hand over my empty plate and mug to Mum and prepare to head outside."

#-# >transition_start
show PitchBlack
with Dissolve(3.0)
#--#

#-# <end>
#
#--#



########

jump A1_03 # jump A?_??
