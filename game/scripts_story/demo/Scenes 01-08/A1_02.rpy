
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
n "I crack open my eyes. Daylight streams through the open window."

#-# >Beatrice running
play sound "music/effects/BeatriceRunning.mp3"
#--#

n "Before I can even respond I hear the door open, footsteps rushing in to greet me."

#-# >Beatrice_happy.png, very close, P1_E2, HD sprite
show beatrice HDP1_E2:
  alpha 0.0 xalign 0.0 yanchor 1.0 ypos 1080+425+1650
  easein 1.0 xalign 0.1 alpha 1.0
show beatrice HDP1_E2 alpha 1.0
#--#

#-# >New Beginnings Arise From Old Endings begins
play music "<from 0.0 to 181.0826 loop 10.1653>music/New Beginnings Arise from Old Endings.mp3"
#--#

unknownqqq "\"Hi there!\""

n "A girl is inches away from my face, cheerfully greeting me."

n "It's a face I know all too well."

erik "\"Morning, Beatrice...\""

#-# >Beatrice_happier.png, very close, P1_E3, HD sprite
show beatrice HDP1_E3:
  alpha 1.0 xalign 0.1 yanchor 1.0 ypos 1080+425+1650
#--#

n "A tired mumble escapes me as I greet who most people assume to be my younger sister."

n "Beatrice, however, is my senior by a few years, exuding youth that belies her true age. She's like a little kid, shaking with energy as she tries to pull me out of bed."

n "I'm not ready for this."

#-# >Beatrice_happy.png, normal scaling now, centered
show beatrice P1_E2:
  xalign 0.4 yanchor 1.0 ypos 1080+425
with Dissolve(0.25)
#--#

n "Still drained from last night, I work to pull the covers up as far as my nose."

erik "\"Mind if I sleep some more?\""

#-# >Beatrice pout
show beatrice P1_E5:
  xalign 0.4 yanchor 1.0 ypos 1080+425
with Dissolve(0.25)
#--#

n "Beatrice pouts. A classic expression of hers."

#-# >Beatrice small smile
show beatrice P1_E2
with Dissolve(0.25)
#--#

beatrice "\"But we have breakfast!\""

n "As if on cue my stomach begins to complain loudly to me."

n "... Maybe I can reconsider."

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

n "She whips the covers off my bed in one last-ditch effort for me to finally get up. Instinctively, I pull the covers back; Beatrice just pulls them off playfully again. It's really not as funny as she seems to think it is."

erik "\"Okay, okay, you win. At least let me wash up first.\""

#-# >Beatrice_laugh.png
show beatrice P1_E3
with Dissolve(0.25)
#--#

beatrice "\"Success!\""

#-# >Beatrice out
show beatrice P1_E3:
  easein 2.0 xalign 0.1 alpha 0.0
#--#

n "She cheers and proceeds to jump off my bed, dash out of my room, and run down the hallway announcing my eventual arrival."

n "With my covers at the end of the bed."

n "I guess it was the right choice to wear my pyjamas instead of going for a more 'free' option."

n "Thankfully my morning prep isn't too extensive. With just a rinsing of my face and a quick combing of my hair I'm all set for some breakfast."

#-# >clockwipe
# done next
#--#

#-# <Sister's Flat Main Room>
scene SisAptMain at Position(xpos=0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#

n "I enter the main area of the flat, where the rest of my family is squashed into the somewhat small dining space."

erik "\"Morning, everyone.\""

#-# >Mum_smile.png enter right to center
show mum P1_E2:
  alpha 0.0 xalign 0.3 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.45 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

n "Mum immediately comes to my side, patting my shoulders."

mum "\"Erik, good morning! How are you feeling?\""

erik "\"Good. Kind of hungry now that I see what you and Beatrice have been up to.\""

n "There's a delicious-looking spread of eggs, toast, bacon, and fresh pastries almost overflowing from the small table everyone is seated at."

n "My mouth starts to water; I realize that I haven't really eaten since I left home."

unknownqqq "\"Well, I'm glad to see that our baby brother is still easily swayed by some home cooking.\""

#-# >Mum_smile.png exit center to right
show mum P1_E2:
  easein 1.0 xalign 0.65 alpha 0.0
#--#

#-# >Hilda enter left to center
show hilda P1_E2 behind mum:
  alpha 0.0 xalign 0.3 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.4 alpha 1.0
show hilda P1_E2 alpha 1.0
#--#

n "My other older sister, Brunhilde, rises from the kitchen table to greet me. Beatrice's exact opposite; Brunhilde  – though we all just call her Hilda – was always a bit more stern with me and my sister while we were growing up. Cool, collected, and responsible – that's her personality in a nutshell."

erik "\"How can I be a baby if I'm the tallest one here?\""

#-# >Hilda_pout.png
show hilda P2_E6
with Dissolve(0.25)
#--#

hilda "\"Height is no indication of maturity.\""

n "It's so easy to tease her, though."

erik "\"It's the only thing you'll never hold over me. I take pride in that.\""

n "Her eyes narrow, straightening herself and taking a commanding stance. Stepping close, she reaches her hand up purposely over my head – and proceeds to tousle my hair."

#-# >Hilda_smile.png
show hilda P2_E2
with Dissolve(0.25)
#--#

n "Her pout quickly dissipates into a warm and comforting smile. She pulls me in for a quick hug, though it's a bit lighter and stiffer than how I remembered them."

n "A bit more careful."

n "Still, the feeling's gone in a flash, and her eyes are soon back on mine."

#-# >Hilda_smile
show hilda P3_E2
with Dissolve(0.25)
#--#

hilda "\"I missed you. It's great to see you up and about, Erik.\""

erik "\"I missed you too. I hate how every time I see you guys there has to be some reason behind it.\""

#-# >Hilda_smile.png 2
show hilda P2_E2
with Dissolve(0.25)
#--#

hilda "\"It's understandable. Making a trip out to Vienna isn't something you can do on a whim. If anything, it would be more feasible for us to come visit you.\""

erik "\"Well, it's the thought that counts, right? I don't think any of us have as much spare time as we used to...\""

erik "\"Speaking of which, where's Dad?\""

#-# >Hilda E4 (Same P as last)
show hilda P2_E4
with Dissolve(0.25)
#--#

hilda "\"He stepped out to take a phone call.\""

erik "\"Even on a weekend? Geez, work never lets up for him, does it?\""

n "It's not unheard of for Dad to have to take or receive calls at any time during the week. It seems like someone always needs him for something. I'm sure he hates it at this point."

#-# >Hilda smile again, from center to leftcenter
show hilda P1_E2:
  easein 1.0 xalign 0.2 alpha 1.0
#--#

#-# >Beatrice_happy.png enter from offscreenleft to rightcenter
show beatrice P1_E2:
  alpha 0.0 xalign 0.7 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.8 alpha 1.0
show beatrice P1_E2 alpha 1.0
#--#

beatrice "\"Sit down and eat something, Erik! The food's getting cold.\""

n "My sister's reminder that food exists is enough for me. I plop down and am immediately handed a huge plate: a canvas for me to create a picture perfect breakfast."

beatrice "\"Just take what you want – I made a bunch for everyone today!\""

n "Beatrice is apparently far more skilled than I am at the culinary arts; I doubt I could have made scrambled eggs by this time, let alone the array of breakfast foods in front of me."

#-# >Mum_smile.png enter offscreenleft to center, between the sisters
show mum P1_E2:
  alpha 0.0 xalign 0.45 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.55 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

n "I take a generous sampling of eggs and bacon, and with a gentle nudge from my mum, I take a spoonful of fruit too."

mum "\"Coffee, sweetie?\""

erik "\"Sure. I'm surprised Beatrice didn't drink all of it.\""

#-# >Hilda raised eyebrows
show hilda P2_E4
with Dissolve(0.25)
#--#

hilda "\"I take it that's your version of 'please'?\""

#-# >Beatrice huffy
show beatrice P1_E7
with Dissolve(0.25)
#--#

beatrice "\"I mean jeez, Eric! I'm not {i}that{/i} obsessed with coffee, y'know!\""

#-# >Beatrice mock anger
show beatrice P1_E5
with Dissolve(0.25)
#--#

n "Of course she's already holding a cup as she says this, which she seems to realize the moment the words have left her mouth."

#-# >Hilda smug
show hilda P2_E2
with Dissolve(0.25)
#--#

#-# >Beatrice laughing
show beatrice P1_E3
with Dissolve(0.25)
#--#

n "If this wasn't already her third mug into a potential heart attack I'd be thoroughly surprised."

#-# >beatrice smile
show beatrice P1_E2
with Dissolve(0.25)
#--#

mum "\"Enough, girls, cut your brother some slack. At least for today.\""

n "We're in their house and already my mother has taken control of the situation. In a way this treatment does feel kind of... wrong."

#-# >Mum beatrice and hilda exit
show beatrice P1_E2:
  alpha 1.0 xalign 0.8 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.9 alpha 0.0
show hilda P2_E2:
  alpha 1.0 xalign 0.2 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.1 alpha 0.0
show mum P1_E2:
  alpha 1.0 xalign 0.55 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.45 alpha 0.0
#--#

n "...But, I could get used to this treatment. In the back of my head, though, I'm well aware of what Monday will bring. A new school and no more breakfasts as good as this one. At least, not until Christmas."

#-# >Music volume lowers slightly
$ renpy.music.set_volume(0.6, 2.0, "music")
#--#

n "St. Dymphna's..."

n "It's a photogenic school, at least if their website is anything to go by. The campus was an old Jesuit monastery until they converted it into a school a few decades ago."

n "A school for..."

#-# >pause
$ renpy.pause (1.0)
#--#

n "People with problems."

n "I'll be seeing it tomorrow. Today, however, my sisters want to take me around Vienna while Mum and Dad take care of some school paperwork and arrange to meet with the headmaster."

n "I don't know how different this will be from the other therapists and special organizations I've visited in the past few months. All I can think of is the alien sterility of the hospitals."

n "Pastel green to keep patients calm, the smell of antiseptics and bleach, and worst of all, the uncanny appearance of the patients that I would occasionally catch a glimpse of."

#-# >Music back to normal volume
$ renpy.music.set_volume(0.75, 2.0, "music")
#--#

dad "\"Okay, we'll be there soon. Thank you, Doctor.\""

#-# >>Dad_neutral enter left to center
show dad P1_E1:
  alpha 0.0 xalign 0.65 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.45 alpha 1.0
show dad P1_E1 alpha 1.0
#--#

n "My dad finally returns from his phone call."

#-# >Dad_smile.png
show dad P1_E2
with Dissolve(0.25)
#--#

dad "\"Ah, Erik. Glad to see you're awake. Ready for today?\""

erik "\"Pretty much. You and Mum are taking care of the admission paperwork today?\""

#-# >Dad_neutral.png
show dad P1_E1
with Dissolve(0.25)
#--#

dad "\"Most of it, anyway. I was just talking to Dr. Bosworth to confirm that we're meeting him today. But he's...well, quite the talker.\""

#-# >Mum_smile.png enter offscreenright to rightcenter
show mum P1_E2:
  alpha 0.0 xalign 0.8 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.7 alpha 1.0
show mum P1_E2 alpha 1.0
#--#

mum "\"Dear, would you like something to eat before we go? Some eggs managed to survive.\""

#-# >Dad_smile.png 2
show dad P1_E2
with Dissolve(0.25)
#--#

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

#-# >Mum_smile.png exit right
show mum P1_E2:
  easein 1.0 xalign 0.85 alpha 0.0
#--#

n "Mum quickly runs to fetch a cup."

dad "\"So, Erik, are you ready for today? Your sisters are very eager to show you around town for a while.\""

erik "\"Yeah. I guess I haven't seen Vienna ever since we helped them move here.\""

dad "\"It's a beautiful city. Classical architecture, plenty of shops and cafes – you'll have fun, I'm sure.\""

#-# >Hilda enter from left
show hilda P3_E2:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.2 alpha 1.0
show hilda P3_E2 alpha 1.0
#--#

hilda "\"Erik, Beatrice is almost ready. Why don't you wait outside with me?\""

erik "\"Uh, sure. Sounds good.\""

n "I hand over my empty plate and mug to Mum and prepare to head outside."

#-# >transition_start
stop music fadeout 5.0
show PitchBlack
with Dissolve(3.0)
#--#

#-# <end>
#
#--#





########

jump A1_03 # jump A?_??
