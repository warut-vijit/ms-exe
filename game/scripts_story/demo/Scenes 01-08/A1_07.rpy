
label A1_07:
###############

$ persistent.scene_number = "A1_07" # current scene
$ persistent.scene_name = "A Wilhelm Goodbye" # current scene name
$ renpy.save_persistent()


# A1_07
# Scene name: A Wilhelm Goodbye
# 
# Backgrounds:
# School Entrance (day)
# 
# Sprites:
# Beatrice, Hilda, Mr. + Mrs. Wilhelm, Ela
# 
# Music:
# Schooltheme
# 
# Sound Effects:
# Dull thump/punch
# 
# 
#-# >open to School Entrance (day)
scene mainbuilding
with Dissolve(2)
#--#
#-# >Ela + sisters slide to center, as does the background to signify movement coming to a stop.
show hilda P2_E1:
  xalign 0.12 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.22 alpha 1.0

show beatrice P1_E1 behind hilda:
  xalign 0.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.02 alpha 1.0

show ela P1_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.45 alpha 1.0

show irene U_P1_E1:
  xalign 0.58 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.68 alpha 1.0
show hilda P2_E1 alpha 1.0
show beatrice P1_E1 alpha 1.0
show ela P1_E1 alpha 1.0
show irene U_P1_E1 alpha 1.0
#--#

n "We come to a stop in front of the large building that holds the offices."

#-# >Irene tour over
show irene U_P1_E2
with Dissolve (0.25)
#--#

irene "\"Well, looks like our little tour is over!\""

n "I'd like to be able to say 'This tour has put me at ease', but if anything it's put me more on edge."

n "Sure, I didn't see any padded walls or restraints, but I did see a student fall from a tree before talking about lipreading and Nazi gold. Then there was that run in with Dr. Faber."

n "My palms are sweaty just {i}thinking{/i} about meeting him again."

n "Beatrice still looks like she's off in her own world while Hilda seems to be feeling just as uneasy as I am."

n "Ela breaks the silence with a small cough before speaking."

#-# >Ela back to work
show ela P1_E2
with Dissolve (0.25)

show irene U_P1_E1
with Dissolve (0.25)
#--#

ela "\"I should probably get back to work.\""

ela "\"It was nice meeting you Erik, give me a call if you need to know anything, okay?\""

erik "\"Sure, thanks.\""

#-# >Ela leaves
show ela P1_E1
with Dissolve (0.25)
#--#

n "Ela leaves with a wave and a smile. I offer a half-hearted wave back, but it seems like she's turned around by the time my hand is raised. Ah."

#-# >Ela out
show ela P1_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 1.0 xalign 0.25 alpha 0.0

show irene U_P1_E4
with Dissolve (0.25)
#--#

n "Irene snickers as she notices my half-hearted wave. Before leaving, she leans towards me conspiratorially."

irene "\"Let me know if you {i}actually{/i} need info, she talks a big game but she doesn't know the land like I do.\""

erik "\"Uh, right. Thanks.\""

n "Irene winks and spins on her heels just like Ela did before strutting off towards the forest."

#-# >Irene out
show irene U_P1_E1:
  xalign 0.68 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 1.0 xalign 0.78 alpha 0.0
#--#

n "Beatrice releases a small sigh as her new best friend walks away before turning her eyes to me."

#-# >The sisters move to center
show hilda P2_E1:
  xalign 0.22 yanchor 1.0 ypos 1080+425+85 alpha 1.0
  easein 2.0 xalign 0.6 alpha 1.0

show beatrice P1_E1 behind hilda:
  xalign 0.02 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 2.0 xalign 0.4 alpha 1.0
#--#

beatrice "\"Eeeeerik~\""

erik "\"What?\""

beatrice "\"Oh {i}nooooothing~{/i}\""

erik "\"That means it's definitely something.\""

#-# >beatrice something
show beatrice P2_E4
with Dissolve (0.25)
#--#

beatrice "\"I mean... Ela was cute, {i}riiiight?{/i}\""

n "A loaded question aimed right at me. Gulp."

erik "\"... Sure.\""

#-# >beatrice what about
show beatrice P2_E3
with Dissolve (0.25)
#--#

beatrice "\" And what about Ire–!\""

#-# >Beatrice is bumped
show beatrice P2_E3:
  linear 0.090 xoffset -5
  linear 0.090 xoffset 5
  linear 0.090 xoffset -5
  linear 0.090 xoffset 5
  linear 0.090 xoffset 0
#--#
#-# >Dull thump/punch SFX
play sound "music/effects/Punch.mp3"
#--#
#-# >Beatrice P1_E6
show beatrice P1_E6
with Dissolve (0.25)
#--#

n "Hilde offers an aggressive elbow into Beatrice's side, almost knocking her off her feet. Thanks Hilde."

#-# >hilda elbow
show hilda P3_E4
with Dissolve (0.25)

show beatrice P1_E1
with Dissolve (0.25)
#--#

hilde "\"Think you'll get lost much?\""

erik "\"No doubt. I'm pretty sure they gave me a map in my welcome pack though.\""

hilde "\"Good. It looks like a very nice campus.\""

#-# >hilda nice campus
show beatrice P1_E2
with Dissolve (0.25)
#--#

beatrice "\"Definitely nicer than mine.\""

#-# >beatrice nicer
show beatrice P1_E5
with Dissolve (0.25)
#--#

beatrice "\"And the teachers are nicer too.\""

n "She punctuates her sentence with a drawn out sigh. I don't think there's a teacher on this planet that Beatrice could get along with."

hilde "\"Your lecturers are perfectly fine, it's just that you keep arguing with them.\""

#-# >beatrice fine
show beatrice P1_E8
with Dissolve (0.25)
#--#

beatrice "\"Can you blame me with the amount of work they give out?\""

#-# >beatrice work
show hilda P3_E2
with Dissolve (0.25)
#--#

hilde "\"You're a university student, what did you expect?\""

erik "\"Less homework, clearly.\""

#-# >beatrice homework
show beatrice P1_E3
with Dissolve (0.25)
#--#

beatrice "\"Yes! He understands!\""

n "This casual conversation is calming after the whirlwind that my tour turned out to be. I expected today to turn out {i}very{/i} differently."

#-# >Mom + Dad in center
scene mainGate
with Dissolve(2)

show mum P1_E2:
  xalign 0.65 yanchor 1.0 ypos 1080+425+60 alpha 0.0
  easein 1.0 alpha 1.0
show dad P2_E1:
  xalign 0.9 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 alpha 1.0
show mum P1_E2 alpha 1.0
show dad P2_E1 alpha 1.0
#--#
#-# >Sisters slide over to the left
show hilda P1_E2:
  xalign 0.5 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0

show beatrice P1_E1:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.1 alpha 1.0
show hilda P1_E2 alpha 1.0
show beatrice P1_E1 alpha 1.0
#--#

n "Mom and Dad finally exit the large building and make their way over to us, a small folder of papers resting in Dad's hands."

mom "\"Ah, we escaped!\""

dad "\"He certainly had a lot to say about the school.\""

#-# >dad say
show mum P1_E4
with Dissolve (0.25)
#--#

mom "\"That's good! He's passionate!\""

#-# >mom passionate
show mum P1_E2
with Dissolve (0.25)
#--#

mom "\"And he's going to make sure you get the best care possible, Erik.\""

erik "\"Right.\""

erik "\"Once I'm settled in I'll feel a lot better.\""

mom "\"That's great! How was your tour?\""

erik "\"It was... good. There's a lot of places to see, I think I might go for a walk a little later on.\""

#-# >dad careful
show dad P2_E2
with Dissolve (0.25)
#--#

dad "\"Just be sure to be careful, It looks like the weather is going to get worse later on.\""

#-# >music out
stop music fadeout 5.0
#--#

erik "\"There's no such thing as bad weather, just inappropriate clothing.\""

n "..."

#-# >Beatrice P1_E6 2
show beatrice P1_E6
with Dissolve (0.25)
#--#

beatrice "\"Doesn't Gustav say that all the time?\""

#-# >Hilda P1_E1
show hilda P1_E1
with Dissolve (0.25)
#--#
#-# >mom and dad
show mum P1_E7
with Dissolve (0.25)

show dad P2_E5
with Dissolve (0.25)
#--#
#-# >Music: Unknown Past (NB: NOT Muted Past)
play music "music/Unknown Past.mp3" loop
#--#

n "Mom and dad practically freeze at the mention of his name. Silence lingers in the air."

mom "\"...\""

dad "\"...\""

#-# >mom ...
show mum P1_E8
with Dissolve (0.25)
#--#

mom "\"Well I'm sure it will be a nice walk, Erik.\""

#-# >bea and hilda
show beatrice P1_E5
with Dissolve (0.25)

show hilda P1_E4
with Dissolve (0.25)
#--#

n "This time Hilda freezes, a sour look on her face."

#-# >hilda freeze
show hilda P1_E5
with Dissolve (0.25)
#--#

hilda "\"Mum, If we keep ignoring it then you're just wasting his time here!\""

n "That calming feeling is torn from my body almost as quick as it arrived. The last thing I wanted was for my family to fight about this."

mom "\"Oh, don't worry about that now, Erik. It's going to be fantastic here, right?\""

n "Dad nods along with his usual deadpan expression."

n "My family hasn't mentioned Gustav's name directly for a long time, probably for my sake."
n "I try to find the words that I really want to say, but they don't come."

#-# >mom check
show mum P1_E1
with Dissolve (0.25)
#--#

n "Mom quickly checks her watch and launches into her goodbyes as thoroughly as possible."

#-# >and dad
show dad P2_E2
with Dissolve (0.25)
#--#

n "She pulls me into a hug and almost breaks my ribs as she squeezes. Dad follows shortly after, though with a much more relaxed handshake."

mom "\"Well, we better be off. Make sure to relax a little, okay?\""

#-# >music stops
stop music fadeout 6.0
#--#

mom "\"You've got {i}nothing{/i} to worry about here. We're just a phone call away if you need anything. All right?\""

erik "\"... Okay.\""

n "Aside from the fact I'm in a school for the mentally impaired, who knows who could be waiting around the next corner."

dad "\"There's a train you can take that'll get you home in a few hours. You should come around for the holidays at least, son.\""

n "I can't help but grin at him."

erik "\"Wouldn't want to miss Mum's Christmas ham, after all.\""

#-# >dad_smile.png
show dad P1_E2
with Dissolve (0.25)
#--#

n "Dad smiles and nods in agreement."

mum "\"Alright, come on girls, let's go and get some dinner before the restraunts close!\""

n "Her usual peppiness returns as the 'Gustav' issue is sidestepped completely."

#-# >peppy
show hilda P1_E4
with Dissolve (0.25)

show beatrice P1_E4
with Dissolve (0.25)
#--#

beatrice "\"Oh, where do you wanna go?\""

n "In a matter of seconds Beatrice forgets what we were talking about. Hilde looks sour for a second, but folds to Mum's authority with a sigh."

#-# >hilda take care
show hilda P1_E1
with Dissolve (0.25)
#--#

hilde "\"Well then... Take care, Erik.\""

beatrice "\"We love you lots! I'll text you!\""

n "Both sisters move in for a hug, and then are quickly herded towards the car while Mom fusses over them."

#-# >group hug
hide hilda
with Dissolve (1.0)
hide beatrice
with Dissolve (1.0)
hide dad
with Dissolve (1.0)
hide mum
with Dissolve (1.0)
#--#

n "And now I'm alone."

#-# >END
#
#--#



########

jump A1_08 # jump A?_??
