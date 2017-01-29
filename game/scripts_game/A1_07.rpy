
label A1_07:
###############

  $ persistent.scene_number = "A1_07" # current scene


# A1_07

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

scene entrance1
with Dissolve(2)
#--#
#-# >Ela + sisters slide to center, as does the background to signify movement coming to a stop.

show hilda P2_E1:
  xalign -0.1 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.0 alpha 1.0
  
show beatrice P1_E1 behind hilda:
  xalign 0.15 yalign 1.0 alpha 0.0
  easein 1.0 xalign 0.25 alpha 1.0
  
show ela P1_E1:
  xalign 0.9 yalign -0.4 alpha 0.0
  easein 1.0 xalign 1.0 alpha 1.0

show irene U_P1_E1:
  xalign 0.5 yalign -6.5 alpha 0.0
  easein 1.0 xalign 0.6 alpha 1.0

n "We come to a stop in front of the large building that holds the offices."

show irene U_P1_E2
with Dissolve (0.25)

irene "\"Well, looks like our little tour is over!\""

n "I’d like to be able to say ‘This tour has put me at ease’, but if anything it’s put me more on edge."

n "Sure, I didn’t see any padded walls or restraints, but I did see a student fall from a tree before talking about lipreading and nazi gold."

n "My palms are sweaty just thinking about meeting him again."

n "Beatrice still looks like she’s off in her own world while Hilde seems to be feeling just as uneasy as I am."

n "Ela breaks the silence with a small cough before speaking."

show ela P1_E2
with Dissolve (0.25)

show irene U_P1_E1
with Dissolve (0.25)

ela "\"I should probably get back to work.\""

ela "\"It was nice meeting you Erik, give me a call if you need to know anything, Okay?\""

erik "\"Sure, thanks.\""

show ela P1_E1
with Dissolve (0.25)

n "Ela leaves with a wave and a smile. I offer a half-hearted wave back, but it seems like she’s turned around by the time my hand is raised. Ah."

#-# >Ela out

hide ela
with Dissolve(0.5)
#--#

show irene U_P1_E4
with Dissolve (0.25)

n "Irene snickers as she notices my half-hearted wave. Before leaving, she leans towards me conspiratorially."

irene "\"Let me know if you actually need info, she talks a big game but she doesn’t know the land like I do.\""

erik "\"Uh, right. Thanks.\""

n "Irene winks and spins on her heels just like Ela did before strutting off towards the forest."

hide irene
with Dissolve(0.5)

n "Beatrice releases a small sigh as her new best friend walks away before turning her eyes to me."

#-# >Beatrice in close

show hilda P2_E1:
  xalign 0.0 yalign -0.3
  easein 1.0 xalign 0.3
  
show beatrice P2_E3:
  xalign 0.25 yalign 1.0
  easein 1.0 xalign 0.7

beatrice "\"{i}Eeeeerik~{/i}\""

erik "\"What?\""

beatrice "\"Oh {i}nooooothing~{/i}\""

erik "\"That means it’s definitely something.\""

show beatrice P2_E4
with Dissolve (0.25)

beatrice "\"I mean… Ela was cute, riiiight?\""

n "A loaded question aimed right at me. Gulp."

erik "\"...Sure.\""

show beatrice P2_E3
with Dissolve (0.25)

beatrice "\" And what about Ire-!\""

#-# >Beatrice shakes / is bumped over the screen

show hilda P2_E5
with hpunch

show beatrice P1_E5:
  easein 0.5 xalign 0.75
#--#
#-# >Dull thump/punch SFX
todo "{color=#ff8c00}>Dull thump/punch SFX{/color}"
#--#

n "Hilde offers an aggressive elbow into Beatrice’s side, almost knocking her off her feet. Thanks Hilde."

show hilda P3_E4
with Dissolve (0.25)

show beatrice P1_E1
with Dissolve (0.25)
  
hilde "\"Think you’ll get lost much?\""

erik "\"No doubt. I’m pretty sure they gave me a map in my welcome pack though.\""

hilde "\"Good. It looks like a very nice campus.\""

show beatrice P1_E2
with Dissolve (0.25)

beatrice "\"Definitely nicer than mine.\""

show beatrice P1_E5
with Dissolve (0.25)

beatrice "\"And the teachers are nicer too.\""

n "She punctuates her sentence with a drawn out sigh. I don’t think there’s a teacher on this planet that Beatrice could get along with."

hilde "\"Your lecturers are perfectly fine, it’s just that you keep arguing with them.\""

show beatrice P1_E8
with Dissolve (0.25)

beatrice "\"Can you blame me with the amount of work they give out?\""

show hilda P3_E2
with Dissolve (0.25)

hilde "\"You’re a university student, what did you expect?\""

erik "\"Less homework, clearly.\""

show beatrice P1_E3
with Dissolve (0.25)

beatrice "\"Yes! He understands!\""

n "This casual conversation is calming after the whirlwind that my tour turned out to be. I expected today to turn out very differently."

#-# >mum + Dad in center
scene MainGate
with Dissolve(2)

show hilda P1_E2:
  xalign 0.4 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.2 yalign -0.3 alpha 1.0

show beatrice P1_E1:
  xalign 0.10 yalign 1.0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.0 yalign 1.0 alpha 1.0

show mum P1_E2:
  xalign 0.65 yalign -0.2 alpha 0.0
  easein 1.0 alpha 1.0
show dad P2_E1:
  xalign 1.0 yalign 0.0alpha 0.0
  easein 1.0 alpha 1.0

mum "\"Ah, we escaped!\""

n "Mum and Dad finally exit the large building and make their way over to us, a small folder of papers resting in Dad’s hands."

dad "\"He certainly had a lot to say about the school.\""

show mum P1_E4
with Dissolve (0.25)

mum "\"That’s good! He’s passionate!\""

show mum P1_E2
with Dissolve (0.25)

mum "\"And he’s going to make sure you get the best care possible, Erik.\""

erik "\"Right.\""

erik "\"Once I’m settled in I’ll feel a lot better.\""

mum "\"That’s great! How was your tour?\""

erik "\"It was... good. There’s a lot of places to see, I think I might go for a walk a little later on.\""

show dad P2_E2
with Dissolve (0.25)

dad "\"Just be sure to be careful, It looks like the weather is going to get worse later on.\""

todo "music stops."

erik "\"There’s no such thing as bad weather, just inappropriate clothing.\""

n "…"

show beatrice P1_E2
with Dissolve (0.25)

beatrice "\"Doesn’t Gustav say that all the time?\""

show mum P1_E7
with Dissolve (0.25)

show dad P2_E5
with Dissolve (0.25)

n "Mum and dad practically freeze at the mention of his name. Silence lingers in the air."

mum "\"...\""

dad "\"...\""

show mum P1_E8
with Dissolve (0.25)

mum "\"Well I’m sure it will be a nice walk, Erik.\""

show beatrice P1_E5
with Dissolve (0.25)

show hilda P1_E4
with Dissolve (0.25)

n "This time Hilda freezes, a sour look on her face."

show hilda P1_E5
with Dissolve (0.25)

hilda "\"Mum, If we keep ignoring it then you’re just wasting his time here!\""

n "That calming feeling is torn from my body almost as quick as it arrived. The last thing I wanted was for my family to fight about this."

mum "\"Oh, don’t worry about that, Erik. It’s going to be fantastic here, right?\""

n "Dad nods along with his usual deadpan expression. I guess that’s what being a financial analyst does to you."

show mum P1_E1
with Dissolve (0.25)

n "Mum quickly checks her watch and launches into her goodbyes as thoroughly as possible."

show dad P2_E2
with Dissolve (0.25)

n "She pulls me into a hug and almost breaks my ribs as she squeezes. Dad follows shortly after, though with a much more relaxed handshake."

mum "\"Well, we better be off. Make sure to relax a little, okay?\""

mum "\"You’ve got nothing to worry about here.\""

erik "\"... Okay.\""

n "Aside from the fact I’m in a school for the mentally impaired, who knows who could be waiting around the next corner."

mum "\"Alright, come on girls, let’s go and get some dinner before the restaurants close!\""

n "Her usual peppiness returns as the ‘Gustav’ issue is sidestepped completely."

show hilda P1_E4
with Dissolve (0.25)

hilde "\"Mother, come on.\""

show beatrice P1_E4
with Dissolve (0.25)

beatrice "\"Oh, where do you wanna’ go?\""

n "In a matter of seconds Beatrice forgets what we were talking about. Hilde looks sour for a second, but folds to mum’s overwhelming social power with a sigh."

show hilda P1_E1
with Dissolve (0.25)

hilde "\"Well then… Take care, Erik.\""

beatrice "\"We love you lots!\""

n "Both sisters move in for a hug, and then are quickly herded towards the car while mum fusses over them."

hide hilda
with Dissolve (1.0)
hide beatrice
with Dissolve (1.0)
hide dad
with Dissolve (1.0)
hide mum
with Dissolve (1.0)

n "And now I’m alone."


#-# >END

#
#--#

########

jump A1_08 # jump A?_??