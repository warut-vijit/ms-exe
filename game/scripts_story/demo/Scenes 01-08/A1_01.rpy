
label A1_01:
###############

$ persistent.scene_number = "A1_01" # current scene
$ persistent.scene_name = "Discordance" # current scene name
$ renpy.save_persistent()


# Scene 01 - Discordance
# Scene name: Discordance
# Backgrounds:
# Mountain Range
# Apartment Bedroom (night)
# Wilhelm sisters' flat hallway (night)
# Wilhelm sisters' flat main room (night)
# Sprites:
# Mama Wilhelm (robe)
# Music:
# Muted Past
# Men on the Mountain
# Sound Effects:
# Wind Blowing
# Footsteps over snow/rock
# Ambient city noises (loop)
# Bedsheets rustling
# Window opening
# Door opening
# Door knocking
# Discordant noise (loop)
# 
#-# <scene open>
#
#--#
#-# <mountain range>
show mountainRange
#--#
#-# <pan up slowly>
show mountainRange at Pan((0, 360), (0, 0), 5.0)
#--#
#-# <Men on the Mountain start>
play music "music/Men on the Mountain.mp3"
#--#
#-# <wind sfx blowing for 5 seconds>
play ambience "<from 0 to 5>music/effects/birdsandwind.ogg" 
#--#
n "The mountain looms above us, tall and imposing."

him "\"Hey, see that ledge?\""

n "My gaze follows his finger to an outcrop jutting a few hundred metres out from the mountain's surface."

him "\"Remember the end of our last climb? That's our starting point now. Pretty cool, right?\""

me "\"Wow... We've come a long way, haven't we?\""

him "\"You bet. You've learned the ropes pretty quickly. At the pace we're going now, I'd say we'll be at our goal sometime in the afternoon.\""

me "\"Heh, just enough time to get back for dinner.\""

n "He claps me on the back, his grip firm and reassuring."

him "\"Now {i}that's{/i} what I'm talking about! C'mon, let's go.\""

him "\"Got everything packed?\""

me "\"Double and triple-checked! All weight accounted for.\""

me "\"Well, except breakfast.\""

n "He laughs."

him "\"Well, the more you eat...\""

me "\"...The less you have to carry!\""

n "I finish his sentence and confidently hop off the rock we've been sitting on, enjoying the solid {i}crunch{/i} the ground makes when I land. The shock from the landing helps balance the butterflies in my stomach."

n "Like last night's campfire, I feel a growing heat that radiates to my toes; the sensation eases my nerves."

n "{i}We've got this.{/i}"

n "In a single fluid motion, he finishes the rest of his pitch-black coffee and leaps down to join me."

him "\"All right, let's rumble. Got a long trek ahead of us.\""

me "\"Right behind you!\""

n "I adjust the straps on my backpack and set off down the trail with him."

#-# <replace wind sfx with two sets of booted steps over rock>
play ambience2 "music/effects/WalkingGrass.mp3"
#--#

him "\"Check your straps one last time. Wouldn't want to have to tell Mum that we came all this way, just for you to get a bruise from the gear.\""

me "\"Yup, I know. Double and triple-checked, remember?\""

him "\"{i}Juuuuuuuust{/i} making sure. Worrying's my job here, y'know. Unless you don't need me for this climb?\""

n "We both laugh; the sound bounces off the rocks and echoes in the valley - almost as if the mountain is laughing with us."

me "\"I'd prefer to keep you around, just in case.\""

n "We continue our ascent up the mountain. Gradually, the soil and grass give way to snow and stone."

him "\"Nervous?\""

me "\"A little.\""

him "\"It would be crazy if you weren't, dude. This {i}is{/i} dangerous stuff, you know.\""

him "\"The key thing is to remember that you can make that nervousness work for you, instead of the other way around.\""

him "\"Any-hey, you've got nothing to worry about while I'm here. I've got your back...\""

me "\"...And I've got yours!\""

n "He flashes his trademark grin."

him "\"That's a promise. Just focus on the climb and the goal at the top.\""

#-# <boot sfx stops>
stop ambience2
#--#

n "We both come to a halt."

n "{i}We're here.{/i}"

me "\"This is the starting point, right?\""

him "\"Yep, this is the place!\""

n "He pulls out a thermos and a small flask."

him "\"Now, I've got a proposition for you: you do everything right, we get to share some of my {i}special{/i} brew at the top. We do this like men. Deal?\""

me "\"Deal.\""

n "He claps me on the back again and sets off."

#-# <Men on the Mountain fades out>
stop music fadeout 2.0
#--#

n "..."


n "..."

n "{i}What's happening?{/i}"

n "{i}Why can't I move?{/i}"

n "I try to call out to him, but there's no sound. I scream, but end up swallowing it. ."

#-# <noise sfx starts softly>
play ambience2 "music/effects/Panic Attack Sounds.ogg" fadein 3.0 loop
$ renpy.music.set_volume(0.5, 0, "ambience2")
#--#

him "\"{i}I've got your back...{/i}\""

me "\"{i}...And I've got yours!{/i}\""

n "I can't hear anything either."

him "\"{i}I've got your back...{/i}\""

me "\"{i}...And I've got yours!{/i}\""

n "No, I checked them."

n "I checked {i}everything{/i}! Why did they--!?"

#-# <fade to black>
scene PitchBlack
with Dissolve(3)
#--#

n "I can only see black."

n "It's here again. That {i}sound.{/i}"

#-# >noise increases in volume
$ renpy.music.set_volume(0.85, 3.0, "ambience2")
#--#

n "It fills my body, choking me."

n "I can't feel my leg."

n "I clench my fists on my thigh, struggling to feel something there."

n "Nothing."

n "I call out for help, but no one will find me here."

n "He's gone."

n "I'm going to die out here."

n "My hands are going numb, gloves soaked through with blood."

n "They slip against the wet fabric of my pants, and--"

#-# >bedsheets rustling
play sound "music/effects/heavy cloth.wav"
#--#
#-# <apartment bedroom (night)>
show SisAptNight:
  alpha 0.1
with Dissolve(2)
sv "A dimly-lit bedroom"
#--#

n "I throw off my covers, damp with sweat. Confusion and panic blur my vision as I struggle to stop the bleeding... but there's no blood."

n "My breathing is shallow and ragged, as though I've just run a hundred miles. Adrenaline is still coursing through my system."

n "I try to slide to the edge of the bed, but my leg tangles in the sheets and I topple gracelessly to the ground."

n "This pressure makes it hard to move, and my vision is tunneling as I try - and fail - to catch my breath."

n "Okay, Erik, try to think back. Remember what the doctors told you. Breathe in..."

n "I inhale - or at least I try to."

n "Breathe out..."

n "I wheeze out as much as my panicked body allows and try to repeat the process."

n "My body is being crushed under its own weight as I breathe. I'm drenched in sweat now; it's draining out of me like water from a wrung sponge."

n "Time has dragged to a crawl, but my heart only seems to be getting faster; its dull, violent thumping fills my ears like tiny explosions."

n "In..."

n "And out..."

#-# <apartment bedroom (night), dark hazy lighting begins to lighten>
show SisAptNight:
  alpha 0.25
with Dissolve(2)
#--#

n "Breathe in..."

n "... Breathe out."

#-# <apartment bedroom (night), fades into normal cg lighting>
show SisAptNight:
  alpha 0.45
with Dissolve(2)
#--#

n "In..."

n "... And out again ..."

n "Eventually, the pressure lifts and I can finally pick myself up off of the ground."

n "I limp my way to the window next to my bed and crack it open."

#-# >window opening
stop ambience2 fadeout 5.0
$ renpy.music.set_volume(0.3, 0, "sound")
play sound "music/effects/window.mp3"
#--#
#-# >ambient city noises (fade in)
play ambience "music/effects/City Night Ambience.mp3" fadein 2.0 loop
#--#
#-# >CG_W1
show CGW1
with Dissolve(2)
#--#

n "There's a breeze."
n "It's cold, but keeping warm is low on my list of priorities."

n "As the cool night air pushes in to meet my face, I inhale and gulp it down like it's the freshest thing I've tasted in years."

n "Yet this air is something I first encountered only a few hours ago, and the charming back-alley view only serves as a reminder of where I am."

n "Vienna, Austria."

n "It's not the most glamorous view of the city, but the fact that I  have my own room keeps me thankful."

n "My older sisters are hosting my parents and I for the weekend. It's something we all couldn't thank them enough for - even if it isn't the reunion any of us were expecting."

n "I should get back to bed. Maybe the cool air will help."

erik "\"Ah...\""

n "However, my right leg refuses to cooperate."

erik "\"Come on, you...!\""

n "I hammer at it a few times in frustration, but it just hangs limply from my body."

n "It's been like this for over half a year now."

#-# >muted past starts
play music "music/Muted Past.mp3" loop
$ renpy.music.set_volume(0.8, 0.0, "music")
$ renpy.music.set_volume(0.1, 2.0, "ambience")
#--#

n "Physically, my leg is fine, but it still refuses to agree with that assessment."

n "At best, I feel like my leg isn't there -  and at its worst, I can't even get it to move."

n "I'm more nervous about small things, I can't think straight sometimes, and those {i}nightmares{/i}..."

n "I bite my tongue in an attempt to derail that train of thought."

n "I shouldn't be like this. This is {i}not{/i} who I want to be."

n "Still struggling between sleep and waking, with cold air blowing against my face, tears well up in my eyes - but it takes me a moment to register them."

n "I'm not going to cry. I'm not going to cry. I won't cry. I'm not that fragile. I won't–"

n "I won't let myself!"

n "What a vicious cycle. Wanting to cry makes me want to cry."

n "Deep breaths. Deep breaths."

n "What kind of man am I being right now? Who cries in the middle of the night because of a nightmare?"

n "It's so pathetic."

n "{i} \"It could've happened to an adult. It happens to soldiers and policemen and firemen all the time. Would you say those people aren't brave?\" {/i}"

n "One of the doctors said that to me. Maybe it's true."

n "I don't know, and I don't want to research it."

n "But if so, what does it matter? They never talk about it. They never show that to you."

#-# >>door knocking
$ renpy.sound.set_volume(0.75)
play sound "music/effects/Knock Knock.mp3"
#--#

n "{i} Oh, Lord. {/i}"

#-# >>door knocking 2
$ renpy.sound.set_volume(0.75)
play sound "music/effects/Knock Knock.mp3"
#--#

n "Another knock on the door. Steps on the wooden floor outside the room."

n "Please, please don't be Mum."

voice "\"Erik? Sweetie?\""

n "Well, I've gone and done it now."

n "Her voice is gentle and concerned. My muscles tense up involuntarily."

mum "\"Erik, is everything alright?\""

n "My throat tightens."

erik "\"Y-Yeah. It's nothing.\""

mum "\"Are you sure? I heard banging from down the hall...\""

erik "\"I'm okay... just had a bad dream.\""

n "I'm so awful."

#-# >>door open
play sound "music/effects/door open and close.mp3"
#--#

#-# >CG_W2
show CGW2
with Dissolve(2)
hide CGW1
#--#

n "Mum quietly opens the door and makes her way to the end of my bed. It's hard to see her in the dim moonlight, but I can practically feel the concern radiating off of her."

#-# >CG_W3
show CGW3
with Dissolve(2)
hide CGW2
#--#

mum "\"Is that why you opened the window?\""

erik "\"I just needed some fresh air; the room felt a little...\""

n "My mind goes blank. I actually don't know if I can say anything else without admitting to my episode."

n "There's never a reason for them, so there's no easy explanation for me to give her."

erik "\"It's just hard to fall back asleep.\""

#-# >CG_01 with mum start
show CG01
with Dissolve(2)
hide CGW3
#--#

mum "\"Come here. It's going to be fine.\""

mum "\"Erik, you're covered in sweat... are you feeling ill?\""

erik "\"No, no. It was just a dream.\""

mum "\"Is your leg giving you trouble? Could you get up okay?\""

erik "\"Mum, I'm fine. My leg's fine. I just have a lot on my mind is all.\""

n "I try my best to dispel any of the concern my mum has. Traveling all the way to Vienna is already giving her enough to deal with without me adding 'unpredictable panic attacks' to the list."

mum "\"Is it about the school?\""

n "I pause."

n "{i}That.{/i}"

erik "\"A little bit, I think... I really don't know.\""

n "Whether or not I was ready for this change didn't matter much anyway. At this point, I'll reluctantly accept any help I can get."

mum "\"It'll be a good change for you, sweetheart. Your father and I made sure of it.\""

erik "\"Yeah, I know.\""

n "I know they have the best intentions, at the very least. As for where that road leads... well, that isn't so certain."

n "What I {i}do{/i} know is that I'm incredibly exhausted and feeling more on edge than I have since the accident."

n "It feels like I'm being introduced to new sights, new smells, new {i}everything.{/i}"

n "I want to be excited, but all I can think of is how easily everything can go wrong. To me, anything could be a potential threat."

mum "\"I know it's been a rough few days, but you know we're here for you Erik. Always.\""

n "She hugs me tighter, and  I return it on instinct. Something about mothers is that they're naturally able to figure you out, even without you saying much."

n "After my panic attack, I really needed this."

erik "\"Mum... thanks.\""

#-# >Mum_smile.png
#show Mum P1_E2
#with Dissolve(0.25)
#--#

mum "\"Anytime.\""

n "She pats me on the shoulder, and her expression shifts to a warm smile."

mum "\"Are you okay to get some rest, or do you need anything else?\""

n "I'm tempted to ask for water, but at this point I doubt it would do much to steady my nerves."

erik "\"I'm... okay. I really appreciate the check-up.\""

mum "\"It's my job as a mother. Come on.\""

#-# >Back to CG_W1
show CGW1
with Dissolve(2)
hide CG01
#--#

n "I feel like a kid when she gently pulls me up, tucks me in, and kisses me goodnight."

erik "\"Mum, really?\""

#-# >Mum_smile.png 2
stop music fadeout 10.0
$ renpy.music.set_volume(0.3, 10.0, "ambience")
#show Mum P1_E2
#with Dissolve(0.25)
#--#

mum "\"All part of my job, sweetie. You want your window closed?\""

n "I shake my head, the air and faint urban sounds have become comforting to me."

mum "\"Well, if you need anything, I'm just a call away.\""

erik "\"I know. Goodnight Mum.\""

n "She lingers a little, giving me one last smile as she brushes the top of my head."

mum "\"Goodnight Erik.\""

#-# >Mum_smile.png exit center to left
#show Mum Smile Vclose2:
#  easein 2.0 xalign 0.0 alpha 0.0
#--#
#-# >door closing
play sound "music/effects/door open and close.mp3"
$ renpy.music.set_volume(0.5, 5.0, "ambience")
#--#

n "She leaves my bedroom, and I'm alone once again."

n "As before, my mind drifts to my condition, but..."

n "But I guess I'm luckier than most; I'm lucky that my condition isn't worse, for one. I'm lucky that I have a family just a shout down the hall. I'm lucky to still have a leg, really."

n "It's these thoughts that eventually bring my mind to what awaits me at this new school."

n "Against the noise of Vienna's city life, my mind finally drifts away, fading from the lingering thoughts of an uncertain future."

#-# >fade to black
scene PitchBlack
with Dissolve(3)
#--#
#-# >all sounds fade out
stop music fadeout 2.0
stop music2 fadeout 2.0
stop ambience fadeout 2.0
stop ambience2 fadeout 2.0
stop sound fadeout 2.0
#--#
#-# <end>
#
#--#


########

jump A1_02 # jump A?_??
