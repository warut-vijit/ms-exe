
label A1_06:
###############

$ scene_number = "A1_06" # current scene
$ scene_name = "Monologue" # current scene name
$ renpy.save_persistent()


# A1_06
# 
# Scene name: Monologue
# 
# Backgrounds:
# School Grounds, Beautiful Sky(?)
# 
# Sprites:
# None
# 
# Music: 
# TBD
# 
# Sound Effects:
# TBD
# 
#-# >open to mail school grounds.
scene outsidemaledorm with Dissolve(1.0)
#--#

n "Dad's words echo in my head."

n "{i}\"I'm sure you'll make the most of your time here.\"{/i}"

n "How can I be sure that I'll make {i}any{/i} use of my time?"

n "The knot in my stomach coils again and again, holding me in place as I watch my family get smaller and smaller in the distance."

n "They turn a corner - and then, they're gone."

n "Now I'm stranded here."

#-# >New beginnings arise from old endings.mp3
play music "music/New Beginnings Arise from Old Endings.mp3"
#--#

n "Well..."

n "I do know one thing that might be a good use of my time."

n "It might make me feel better, at least."

n "I pick a random direction and begin limping."

n "The tour showed me all the places I'll need to go for classes and daily life, but we only got to see one of the walking paths Mr. Bosworth mentioned."

n "Luckily it seems as though most of the students that were wandering around before have gone elsewhere, so I don't have to try and hide my limp like I had to for that whole tour."

#-# >BG school_generic2
scene school2 with Dissolve(1.0)
#--#

n "Before long, I pass the large academic building and continue onwards."

n "It's liberating to be able to walk by myself, even for just a little while."

n "The freshly cut grass gives off that familiar, calming scent."

n "The school is quiet."

n "It feels a little strange walking around school grounds after classes are done."

n "I'd usually dart off as soon as the bell rang."

#-# >bg school_generic3
scene chapel with Dissolve(1.0)
#--#

n "I wonder if anybody from back home wonders where I went."

n "I guess I was never {i}really{/i} close to anybody there, but I wasn't antisocial."

n "I doubt I'd fit back in anyway..."

n "Now I've got to learn to fit in here."

n "{i}Somehow...{/i}"

#-# >bg school_generic3 2
scene school1 with Dissolve(1.0)
#--#

n "I mean, Ela seemed normal."

n "Surely there must be more just her."

n "Then again, there could be more people like Irene instead."

n "I sigh."

n "This is my punishment, I suppose."

n "If only things had gone differently."

n "I wouldn't be at this school, surrounded by these people."

n "I guess I can't do anything about it now."

n "As Dad said, I've just got to make the most of--"

#-# >Music abruptly stops
stop music
#--#

#-# >Ringtone sound effect
play sound "music/effects/phonering.ogg"
#--#

n "Huh?"

n "Oh, my phone."

n "I pull it from my pocket and look at the screen."

#-# >Traumen.mp3
play music "music/Traumen.mp3"
#--#

n "{i}Gustav.{/i}"

n "Shock runs through me and my arm goes limp.."

n "Why is he..."

n "{i}Why?{/i}"

#-# >Ringtone sound effect 2
play sound "music/effects/phonering.ogg"
#--#

n "I stare at the screen, seemingly unable to move."

n "Incoming call from: Gustav"

n "It doesn't stop."

n "Like it's mocking me."

n "My thumb hovers over the green and red buttons."

n "What would I even say?"

n "Hello? Hi? How are you?"

n "..."

#-# >Ringtone sound effect 3
play sound "music/effects/phonering.ogg"
#--#

n "{i}I get it! Just stop!{/i}"

n "{i}Please...{/i}"

n "As if responding to my pleas, the phone goes dark."

n "I'm left standing in the middle of a path with my phone in hand."

n "Why?"

n "{i}Why?{/i}"

n "..."

n "Ugh. Damn it."

n "I slide the phone back into my pocket and consult my mental map of the campus."

n "I better get back to the dorms before someone sees me like this."

n "I try to take a step and my leg protests. {i}Come on, not now!{/i}"

n "Deep breaths..."

n "Let's just get back to the dorm."

n "With much more effort, I begin limping my way there."

#--#>fade to black
scene PitchBlack
with Dissolve(1)
#--#

########

jump A1_07 # jump A?_??
