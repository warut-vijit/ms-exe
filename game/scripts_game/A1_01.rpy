
label A1_01:
###############

  $ persistent.scene_number = "A1_01" # current scene


# Scene 01
# 
# Backgrounds:
# Apartment Bedroom (night)
# Wilhelm sisters' flat hallway (night)
# Wilhelm sisters' flat main room (night)
# 
# Sprites:
# Mama Wilhelm
# 
# Music:
# Muted Past
# 
# Sound Effects:
# ambient city noises (loop)
# bedsheets rustling
# window opening
# door opening
# door knocking
# discordant noise (loop)
# 
#-# <scene open>
#
#--#
#-# <apartment bedroom>
image PitchBlack = Solid("#000")
scene PitchBlack
#--#

#-# <pitch black>
#
#--#

n "Welcome to the Missing Stars alpha."

n "This alpha's purpose is to attract new artists."

n "As such, this alpha is non-final and not representative of the final product. Please refrain from uploading it anywhere or sharing it."

n "Please enjoy."

$ renpy.pause (5.0)

#-# >discordant noise
play sound "music/Panic Attack Sounds.mp3" fadein 1.0 loop
$ renpy.sound.set_volume(0.5)
#--#

n "It's here again."

#-# >discordant noise (louder)
$ renpy.sound.set_volume(0.75)
#--#

n "That sound."

n "I can feel it seeping into me, filling my body with a cold chill and crushing pressure."

n "It's chokingly, agonizingly there, and suddenly-"

#-# >pause
$ renpy.pause (1.5)
#--#

n "It hurts to breathe."

#-# >discordant noise (really loud)
$ renpy.sound.set_volume(1.0)
#--#
#-# >bedsheets rustling


play audio "music/effects/heavy cloth.wav"
#--#

#-# <apartment bedroom (night), dark hazy lighting>
image SisAptNight1:
  im.Scale("images/Backgrounds/bedroom.jpg", config.screen_width, config.screen_height)
  alpha 0.2
show SisAptNight1
with Dissolve(2)
#--#

n "I slide over to the edge of the bed, panic still gripping my thoughts as the sheets tangle around my legs."

n "I slump to the ground in a panicked ball, unable to get up."

n "This pressure makes it hard to move and my vision is tunneling as I try and fail to catch my breath."

n "Okay, Erik, try to think back. Remember what the doctors told you. Breathe in..."

n "I inhale, or at least try to. Hyperventilation works just as well, right?"

n "...and breathe out…"

n "I wheeze out as much as my panicked body allows and try to repeat the process."

n "The noise won't let up. My body is being crushed by my own mind as I try to breathe. I'm drenched in sweat now; it's draining out of me like water from a wrung sponge."

n "Time has dragged to a crawl, but my heart only seems to be getting faster."

n "...Breathe in..."

n "...Breathe out..."

#-# >discordant noise (softer)
$ renpy.sound.set_volume(0.666)
#--#
#-# <apartment bedroom (night), dark hazy lighting begins to lighten>
image SisAptNight2:
  im.Scale("images/Backgrounds/bedroom.jpg", config.screen_width, config.screen_height)
  alpha 0.4
show SisAptNight2
with Dissolve(2)
#--#

n "...Breathe in..."

n "...Breathe out..."

#-# >discordant noise (softer, fade over a few seconds)
$ renpy.sound.set_volume(0.5)
stop sound fadeout 3.0
#--#
#-# <apartment bedroom (night), fades into normal cg lighting>
image SisAptNight:
  im.Scale("images/Backgrounds/SistersAppartment_ErikRoom_Night.png", config.screen_width, config.screen_height)
show SisAptNight
with Dissolve(2)
#--#

n "...Breathe in..."

n "...Breathe out..."

n "Eventually, the noise stops, or at least becomes bearable. The pressure lifts, and I can finally pick myself up off of the ground."

n "Decisively, my first pressure free action is to crack open a window."

#-# >window opening
play audio "music/effects/window.mp3"
#--#
#-# >ambient city noises (fade in)

#--#

n "There’s a breeze."

n "It’s cold, but keeping warm is low on my priority list."

n "As the cool night air pushes in to meet my face, I inhale and gulp it down like it's the freshest thing I've tasted in years."

n "Yet this air is something I first encountered only a few hours ago, and the charming back alley view only assists to serve as a reminder of where I am."

n "Vienna, Austria."

n "It’s not the most glamorous view of the city, but the fact that I even have my own room keeps me thankful."

n "My older sisters, Beatrice and Hilda, are hosting me and my parents for the weekend. It’s something we all couldn’t thank them enough for, even if it isn’t the reunion all of us were expecting."

n "I should get back to bed. Maybe the cool air will help."

erik "\"Ah…\""

stop sound fadeout 5.0

n "However, my right leg refuses to cooperate."

erik "\"Come on, you…\""

n "I hammer at it a few times in a frustrated attempt to get it to move, but it just hangs limply from my body."

n "It’s been like this since the accident."

#-# >muted past starts


play music "music/Muted Past.mp3" fadein 2.0 loop
#--#

n "Physically, I am fine, but my right leg still refuses to agree."

n "At best I feel like my leg isn’t even there, and at worst, I can’t even get it to move."

n "I have difficulty sleeping at night, my mind racing, reliving the events over and over. I get more anxious over small things, have more frequent nightmares, and I can't –"

n "I bite my tongue to derail my own train of thought."

n "I shouldn't be like this. This part of me is not what I want to be."

#-# >>door knocking

$ renpy.sound.set_volume(0.75)
play sound "music/effects/Knock Knock.mp3"
#--#

voice "\"Erik? Sweetie?\""

n "I can hear the voice of my mother from outside the room, taking me a little off guard. I don’t know why I’m beginning to tense up."

erik "\"Y-yeah?\""

mum "\"Are you okay? I heard banging from downstairs...\""

erik "\"I'm okay... just had a bad dream.\""

n "It’s not exactly the truth, but it’s close enough, I suppose."

#-# >>door open


play sound "music/effects/door open and close.mp3"


n "Mum quietly opens the door and makes her way to the end of my bed. It’s hard to see her with only dim moonlight, but I can practically feel the concern radiating off her."

mum "\"Is that why you’re out of bed?\""

erik "\"I just needed some fresh air, the room felt a little...\""

n "My mind blanks. I actually don’t know where to take the train of thought without admitting to my episode."

n "There’s never a reason for these episodes, no easy explanation that I can give her."

erik "\"It’s just hard to fall back asleep.\""

mum "\"Come here. It's going to be fine.\""

#-# >CG1

show CG01
with Dissolve(2)


#--#

n "She sits on the edge of the bed, beckoning me over with open arms. Helpless, I sidle up next to her as she gently puts her arm around my shoulder."

mum "\"Erik, you’re covered in sweat, are you feeling ill?\""

erik "\"No, no. It was just the dream.\""

mum "\"Is your leg giving you much trouble? Could you get up ok?\""

erik "\"Mum, I’m fine. My leg’s fine. I just have a lot on my mind is all.\""

n "I try my best to dispel any of the concern my mum has. Traveling all the way to Vienna is already giving her enough to deal with without me adding ‘unpredictable panic attacks’ to the list."

mum "\"Is it about the school?\""

n "Ah."

n "That."

n "A colleague of my father suggested that I attend a specialty school for treatment. Apparently he had a relative that graduated from there with high honors."

n "St. Dymphna’s Privatgymnasium."

n "A school for… people like me."

erik "\"A little bit, I think... I really don't know.\""

n "Whether or not I was ready for this change didn’t matter much anyways."

n "After my diagnosis, my parents spent a lot of their time trying new ways to help me, from specialized therapists to medication."

n "Promising leads turned out to be duds or outdated therapies. Even the medication I've been taking isn't helping much, especially since it doesn't treat the underlying problem."

n "At this point I’ll reluctantly accept any additional help I can get."

mum "\"It’ll be a good change for you, sweetheart. Your father and I made sure of it.\""

n "My parents did some research and found a promising therapist who worked at St. Dymphna’s."

n "Before long we were all on our way to my final year of secondary school."

erik "\"Yeah, I know.\""

n "I know they have the best intentions, at least. As for where that road leads, well, that isn’t as certain."

n "What I do know is that I'm incredibly exhausted and feeling more on edge than I have since the accident."

n "It feels like I’m being introduced to new sights, new smells, new everything."

n "I want to be excited, but all I can think of is how easily it can all go wrong. Everything is a potential threat."

mum "\"I know it's been a rough few days, but you know we're here for you Erik. Always.\""

n "She hugs me tighter. By instinct, I hug back in response. Something about mothers is that they’re naturally able to figure you out, even without you saying much."

n "After my panic attack, I really needed this."

stop music fadeout 10.0

play sound "music/effects/City Night Ambience.mp3" fadein 2.0 loop
$ renpy.sound.set_volume(0.1)

erik "\"Mum… thanks.\""

mum "\"Anytime.\""

n "She pulls away, and her expression shifts to a warm smile."

#-#

hide CG01
##Not sure why I had to hide this but the next BG refuses to show if I don't.

image SisAptNight:
  im.Scale("images/Backgrounds/SistersAppartment_ErikRoom_Night.png", config.screen_width, config.screen_height)
show SisAptNight
with Dissolve(2)

#-#

mum "\"Now, your sisters have been dying to show you the city tomorrow. Are you okay to get some rest, or do you need anything?\""

n "I’m tempted to ask for water, but at this point I doubt it would do much to steady my nerves."

erik "\"I’m…okay. I really appreciate the checkup.\""

mum "\"It’s my job as a mother. Come on.\""

n "I feel like a kid as she gently pulls me up, tucks me in and kisses me goodnight."

erik "\"Mum, really?\""

n "She grins."

mum "\"All part of my job, sweetie. You want your window closed?\""

n "I shake my head, the air and faint urban sounds now becoming a little more comforting to me."

mum "\"Well, if you need anything, I’m just a call away.\""

erik "\"I know. Goodnight mum.\""

n "She lingers a little, giving me one last smile as she brushes the top of my head."

mum "\"Goodnight Erik.\""

#--#
#-# >door closing
play audio "music/effects/door open and close.mp3"
play sound "music/effects/City Night Ambience.mp3" fadein 5.0 loop
$ renpy.sound.set_volume(0.5)
#--#

n "She leaves my bedroom, and I'm alone once again."

n "As before, my mind drifts to my condition but…"

n "But I guess I’m luckier than most. I’m lucky that my condition isn’t worse. I’m lucky that I have a family just a shout down the hall. I’m lucky to still have a leg, really."

n "It’s these thoughts that brings my mind to what kind of home I’ll find at St. Dymphna’s."

n "Against the noise of Vienna's city life my mind finally drifts away, fading from the lingering thoughts of an uncertain future."

#-# <fade to black>
image PitchBlack2 = Solid("#000")
show PitchBlack2
with Dissolve(2.0)
stop sound fadeout 2.0



pause 3.0
#--#
#-# <end>
#
#--#

########

jump A1_02 # jump A?_??
