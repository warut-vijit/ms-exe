
label A1_01:
###############

$ persistent.scene_number = "A1_01" # current scene
$ persistent.scene_name = "Discordance" # current scene name
$ renpy.save_persistent()


# Scene 01 - Discordance
# Scene name: Discordance
# Backgrounds:
# Apartment Bedroom (night)
# Wilhelm sisters' flat hallway (night)
# Wilhelm sisters' flat main room (night)
# Sprites:
# Mama Wilhelm (robe)
# Music:
# Muted Past
# Sound Effects:
# ambient city noises (loop)
# bedsheets rustling
# window opening
# door opening
# door knocking
# discordant noise (loop)
#-# <scene open>
#
#--#
#-# <apartment bedroom>
scene PitchBlack
show CGui
with Dissolve(4)
window show
hide CGui
#--#

n "I can only see black."

#-# >noise starts
play ambience2 "music/effects/Panic Attack Sounds.ogg" fadein 3.0 loop
$ renpy.music.set_volume(0.5, 0, "ambience2")
#--#

n "It's here again. That {i}sound.{/i}"

#-# >noise increases in volume
$ renpy.music.set_volume(0.85, 3.0, "ambience2")
#--#

n "The sound fills my body, choking me."

n "I can't feel my leg."

n "I clench my fists on my thigh, struggling to feel something there."

n "Nothing."

n "I call out for help, but there's nothing. No one will find me here."

n "There's nobody out there."

n "No one is coming."

n "I'm going to die out here."

n "My hands are going numb, gloves soaked through with blood."

n "They slip against the wet fabric of my pants –"

#-# >bedsheets rustling
play sound "music/effects/heavy cloth.wav"
#--#
#-# <apartment bedroom (night)>
show SisAptNight:
  alpha 0.1
with Dissolve(2)
#--#

n "I throw off my covers, damp with sweat, confusion and panic blurring my vision as I struggle to stop the bleeding, but there's no blood."

n "My breathing is shallow and ragged, as though I've just run a hundred miles. Adrenaline is still coursing through my system."

n "I try to slide to the edge of the bed, but my leg tangles in the sheets, and I topple gracelessly to the ground."

n "This pressure makes it hard to move and my vision is tunneling as I try and fail to catch my breath."

n "Okay, Erik, try to think back. Remember what the doctors told you. Breathe in..."

n "I inhale, or at least try to."

n "... and breathe out..."

n "I wheeze out as much as my panicked body allows and try to repeat the process."

n "My body is being crushed by my own mind as I try to breathe. I'm drenched in sweat now; it's draining out of me like water from a wrung sponge."

n "Time has dragged to a crawl, but my heart only seems to be getting faster, its dull, violent thumping filling my ears like tiny explosions."

n "... Breathe in..."

n "... Breathe out..."

#-# <apartment bedroom (night), dark hazy lighting begins to lighten>
show SisAptNight:
  alpha 0.25
with Dissolve(2)
#--#

n "... Breathe in..."

n "... Breathe out..."

#-# <apartment bedroom (night), fades into normal cg lighting>
show SisAptNight:
  alpha 0.45
with Dissolve(2)
#--#

n "... Breathe in..."

n "... Breathe out..."

n "Eventually, the pressure lifts, and I can finally pick myself up off of the ground."

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
n "It's cold, but keeping warm is low on my priority list."

n "As the cool night air pushes in to meet my face, I inhale and gulp it down like it's the freshest thing I've tasted in years."

n "Yet this air is something I first encountered only a few hours ago, and the charming back alley view only assists to serve as a reminder of where I am."

n "Vienna, Austria."

n "It's not the most glamorous view of the city, but the fact that I even have my own room keeps me thankful."

n "My older sisters are hosting me and my parents for the weekend. It's something we all couldn't thank them enough for, even if it isn't the reunion all of us were expecting."

n "I should get back to bed. Maybe the cool air will help."

erik "\"Ah...\""

n "However, my right leg refuses to cooperate."

erik "\"Come on, you...\""

n "I hammer at it a few times in a frustrated attempt to get it to move, but it just hangs limply from my body."

n "It's been like this for over half a year now."

#-# >muted past starts
play music "music/Muted Past.mp3" loop
$ renpy.music.set_volume(0.1, 2.0, "ambience")
#--#

n "Physically, my leg is fine, but it still refuses to agree with that assessment."

n "At best I feel like my leg isn't there, and at its worst, I can't even get it to move."

n "I have difficulty sleeping at night, my mind racing, reliving the events of that day over and over. I get more anxious over small things, I have more frequent nightmares, and I can't –"

n "I bite my tongue to derail my own train of thought."

n "I shouldn't be like this. This part of me is {i}not{/i} what I want to be."

n "Still struggling between sleep and waking, cold air blowing against my face, the tears welling up in my eyes take a moment to register."

n "I'm not going to cry. I'm not going to cry. I won't cry. I'm not that fragile. I won't –"

n "I won't let myself –"

n "What a vicious cycle. Wanting to cry makes me want to cry."

n "Deep breaths. Deep breaths."

n "What kind of man am I being right now? Who cries in the middle of the night because of a nightmare?"

n "It's so pathetic."

n "{i} \"It could've happened to an adult. It happens to soldiers and policemen and firemen all the time. Would you say these people aren't brave?\" {/i}"

n "One of the doctors said that to me. Maybe it's true."
n "I don't know, and I don't want to research it."

n "But if so, what? They never talk about it. They never show that to you."

#-# >>door knocking
$ renpy.music.set_volume(0.75, 0, "sound")
play sound "music/effects/Knock Knock.mp3"
#--#

n "{i} Oh, Lord. {/i}"

#-# >>door knocking 2
play sound "music/effects/Knock Knock.mp3"
#--#

n "Another knock on the door. Steps on the wooden floor outside the room."

n "Please, please don't be Mum."

voice "\"Erik? Sweetie?\""

n "Well, I've gone and done it now."

n "Mum's voice is gentle and concerned. My muscles tense up involuntarily."

mum "\"Erik, is everything alright?\""

n "My throat tightens."

erik "\"Y-yeah. It's nothing.\""

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

n "Mum quietly opens the door and makes her way to the end of my bed. It's hard to see her with only dim moonlight, but I can practically feel the concern radiating off her."

#-# >CG_W3
show CGW3
with Dissolve(2)
hide CGW2
#--#

mum "\"Is that why you opened the window?\""

erik "\"I just needed some fresh air, the room felt a little...\""

n "My mind blanks. I actually don't know where to take the train of thought without admitting to my episode."

n "There's never a reason for these episodes, no easy explanation that I can give her."

erik "\"It's just hard to fall back asleep.\""

#-# >CG_01 with mum start
show CG01
with Dissolve(2)
hide CGW3
#--#

mum "\"Come here. It's going to be fine.\""

mum "\"Erik, you're covered in sweat, are you feeling ill?\""

erik "\"No, no. It was just the dream.\""

mum "\"Is your leg giving you much trouble? Could you get up okay?\""

erik "\"Mum, I'm fine. My leg's fine. I just have a lot on my mind, is all.\""

n "I try my best to dispel any of the concern my mum has. Traveling all the way to Vienna is already giving her enough to deal with without me adding 'unpredictable panic attacks' to the list."

mum "\"Is it about the school?\""

n "I pause."

n "{i}That.{/i}"

n "A colleague of my father suggested that I attend a specialty school for treatment. Apparently they had a relative that graduated from there with high honors."

n "St. Dymphna's Privatgymnasium."

n "A school for... people like me."

erik "\"A little bit, I think... I really don't know.\""

n "Whether or not I was ready for this change didn't matter much anyways."

n "After my diagnosis, my parents spent a lot of their time trying new ways to help me, from specialized therapists to medication."

n "Promising leads turned out to be duds or outdated therapies. Even the medication I've been taking isn't helping much, especially since it doesn't treat the underlying problem."

n "At this point I'll reluctantly accept any additional help I can get."

mum "\"It'll be a good change for you, sweetheart. Your father and I made sure of it.\""

n "My parents did some research and found a promising therapist who worked at St. Dymphna's."

n "Before long we were all on our way to my final year of secondary school."

erik "\"Yeah, I know.\""

n "I know they have the best intentions, at least. As for where that road leads, well, that isn't as certain."

n "What I do know is that I'm incredibly exhausted and feeling more on edge than I have since the accident."

n "It feels like I'm being introduced to new sights, new smells, new {i}everything.{/i}"

n "I want to be excited, but all I can think of is how easily it can all go wrong. Everything is a potential threat."

mum "\"I know it's been a rough few days, but you know we're here for you Erik. Always.\""

n "She hugs me tighter. By instinct, I hug back in response. Something about mothers is that they're naturally able to figure you out, even without you saying much."

n "After my panic attack, I really needed this."

erik "\"Mum... thanks.\""
#-# >Mum_smile.png
#show Mum P1_E2
#with Dissolve(0.25)
#--#
mum "\"Anytime.\""

n "She pats me on the shoulder, and her expression shifts to a warm smile."

mum "\"Now, your sisters have been dying to show you the city tomorrow. Are you okay to get some rest, or do you need anything else?\""

n "I'm tempted to ask for water, but at this point I doubt it would do much to steady my nerves."

erik "\"I'm... okay. I really appreciate the checkup.\""

mum "\"It's my job as a mother. Come on.\""

#-# >Back to CG_W1
show CGW1
with Dissolve(2)
hide CG01
#--#

n "I feel like a kid as she gently pulls me up, tucks me in and kisses me goodnight."

erik "\"Mum, really?\""

n "She grins."
#-# >Mum_smile.png 2
stop music fadeout 10.0
$ renpy.music.set_volume(0.3, 10.0, "ambience")
#show Mum P1_E2
#with Dissolve(0.25)
#--#

mum "\"All part of my job, sweetie. You want your window closed?\""

n "I shake my head, the air and faint urban sounds now becoming a little more comfortable to me."

mum "\"Well, if you need anything, I'm just a call away.\""

erik "\"I know. Goodnight mum.\""

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

n "As before, my mind drifts to my condition but..."

n "But I guess I'm luckier than most. I'm lucky that my condition isn't worse. I'm lucky that I have a family just a shout down the hall. I'm lucky to still have a leg, really."

n "It's these thoughts that brings my mind to what kind of home I'll find at St. Dymphna's."

n "Against the noise of Vienna's city life my mind finally drifts away, fading from the lingering thoughts of an uncertain future."

#-# >fade to black
scene PitchBlack
with Dissolve(3)
#--#
#-# >all sounds fade out
stop ambience fadeout 3.0
stop ambience2 fadeout 3.0
#--#
#-# <end>
#
#--#





########

jump A1_02 # jump A?_??
