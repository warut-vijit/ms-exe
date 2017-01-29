
label A1_06:
###############

  $ persistent.scene_number = "A1_06" # current scene


# A1_06
# 
# Backgrounds:
# School Grounds, Beautiful Sky(?)
# 
# Sprites:
# Beatrice, Hilda, Ela, Irene, Dr. Faber
# 
# Music:
# TBD
# 
# Sound Effects:
# TBD
# 
#-# <Shot of the beautiful campus of St. Dymphna>

scene entrance1
with Dissolve(2)
#--#

show hilda P2_E5:
  xalign -0.1 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.0 alpha 1.0
  
show beatrice P2_E1 behind hilda:
  xalign 0.15 yalign 1.0 alpha 0.0
  easein 1.0 xalign 0.25 alpha 1.0
  
show ela P1_E3:
  xalign 0.9 yalign -0.4 alpha 0.0
  easein 1.0 xalign 1.0 alpha 1.0

show irene U_P1_E1:
  xalign 0.5 yalign -6.5 alpha 0.0
  easein 1.0 xalign 0.6 alpha 1.0

n "With Irene at the helm, the tour recommences, Ela seemingly resigned to her inclusion. Although calling it a ‘tour’ at this point isn’t exactly accurate."

irene "\"So that building is probably the oldest, at least judging from the brickwork. There’s this one patch where the bricks are newer, but I can’t for the life of me figure out why.\""

erik "\"Maybe they renovated it?\""

irene "\"Nah, too small a section. I was thinking damage, but there’s nothing on record about accidents. I tried getting a look behind it, but it turns out that kind of thing is frowned on here.\""

show ela P1_E4
with Dissolve (0.25)

ela "\"You were chiseling out a section of a building.\""

show ela P1_E7
with Dissolve (0.25)

irene "\"Yeah, for science. This is supposed to be a place of learning, you know.\""

show ela P1_E3
with Dissolve (0.25)

hilda "\"What’s the building used for,  if I might ask?\""

irene "\"Huh? I dunno, like exercise and stuff. They’ve got a gym in there. It’s not very interesting.\""

show ela P1_E8
with Dissolve (0.25)

ela "\"You were talking about brickwork before.\""

show irene U_P1_E4
with Dissolve (0.25)

irene "\"Look, when I find nazi gold hidden in a wall, you’re gonna feel like an idiot, is all I’m saying.\""

n "Our unfortunate guide wrestles with herself before letting the comment go uncontested, but her expression is pretty informative nonetheless. Irene doesn’t seem to notice."

n "As we explore the more mundane aspects of the campus, ironically, I find myself relaxing more. Although Ela seemed concerned I might think badly of them, the truth is that my imagination had far worse ideas."

n "Really, it’s those small touches of personalization, imperfections, that make it feel… normal."

show ela P1_E1
with Dissolve (0.25)

n "Eventually we wander away from the campus, Ela regaining the lead as we head towards the woods. Irene gives a minute shrug, but seems content to follow along. Before I have a chance to ask where we’re heading next, Ela slows to a halt."

scene MainGate
with Dissolve(2)
#--#
show beatrice P2_E2:
  xalign 0.0 yalign 1.0 alpha 0.0
  easein 1.0 xalign 0.1 alpha 1.0
show hilda P3_E4:
  xalign 0.2 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0
  
show ela P1_E1:
  xalign 0.6 yalign -0.4 alpha 0.0
  easein 1.0 xalign 0.7 alpha 1.0
show irene U_P1_E1:
  xalign 0.8 yalign -6.5 alpha 0.0
  easein 1.0 xalign 0.9 alpha 1.0

hilda "\"Anything interesting out here?\""

ela "\"...Not really. I just enjoy the scenery."

n "Beatrice turns to Irene."

beatrice "\"Okay, but is there anything interesting out here?\""

irene "\"No tunnel system that I could find. No murders either, as far as I’m aware. The trees are a nice vantage point for the west side of the building, though.\""

n "Well, it’s a beautiful school, if nothing else."

ela "\"I apologize for the brief delay, but I sometimes just feel the need to stop for moments like this.\""

hilda "\"It’s actually kind of nice to get out of city life for a change. You don’t really think of looking up too often when you’re surrounded by walls.\""

beatrice "\"In fairness, you also work more indoors than you should, sis.\""

hilda "\"In fairness, I don’t get much of a say in the matter...\""

n "My two sisters share a short glance and smile, which in turns leads to me finding a smile as well."

n "I turn towards Irene, who seems to be looking every which way BUT the view."

n "I move to mention this, but she beats me to the explanation."

irene "\"Yeah, there's a building there. I’ve seen it before.\""

ela "\"You should probably take time to appreciate it.\""

irene "\"Hey Beatrice, wanna try out the mic?\""

show beatrice P2_E4
with Dissolve (0.25)

beatrice "\"Heck yes.\""

n "Ela and Hilda roll their eyes in perfect unison, and I struggle to suppress a laugh."

show beatrice P2_E2
with Dissolve (0.25)

n "The tour picks up as we make our way to the last legs of the school, though after everything that we had covered I’m not really sure what else there is to show."

n "Familiar locations begin to repeat, and soon I realize we’ve now begun to take a full circle path around the entire campus."

erik "\"So Ela, what do we have left to visit before this tour ends?\""

beatrice "\"Getting bored already, Erik? Even while being led by a pair of attracti-\""

show hilda P3_E3
with hpunch

show beatrice P2_E7:
  easein 0.5 xalign 0.0

n "Beatrice lets out a short yelp as Hilda knocks her in the gut with an elbow."

show beatrice P2_E5
with Dissolve (0.25)

show hilda P3_E2
with Dissolve (0.25)

beatrice "\"-so, through with the tour?\""

n "I didn’t mean to sound as impatient as I did, and in fact I was already quite grateful for what Ela was doing. Even if she was just following orders, she still did a wonderful job helping us."

erik "\"No, I mean... well it just seems like a big school and all. It’s just hard to wrap my head around all of the locations.\""

show ela P1_E2
with Dissolve (0.25)

n "Ela lets out a calm smile, looking as if she was prepared to share some very good news with me."

ela "\"Well, you’re in luck, I have just about one more location to show you guys. In my opinion it’s probably one of the more important locations you’ll be familiarizing yourself with.\""

show ela P1_E1
with Dissolve (0.25)

erik "\"Saving the best for last?\""

show hilda P3_E1
with Dissolve (0.25)

ela "\"It’s the medical facilities, actually.\""

image PitchBlack = Solid("#000")
show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.0
  easein 2.0 alpha 0.1

n "Almost immediately the comment feels like a punch in the gut. Another reminder. Ela continues, seemingly oblivious."

ela "\"Each student has general counseling check ins, though it’s pretty low key depending on how often sessions need to be scheduled.\""

n "‘How often’?"

n "I feel my throat begin to close up on me."

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.1
  easein 2.0 alpha 0.2

n "The thought pounds against my head like a migraine."

erik "\"How… how often would that be?\""

ela "\"Once a week is generally common, but it usually depends on the situation that you and the doctor you’ll be meeting with mutually decide on.\""

hilda "\"Is it normal for these sessions to be scheduled often?\""

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.2
  easein 2.0 alpha 0.3

irene "\"Pretty much. I mean, once a week is the minimum after all.\""

irene "\"I tend to get called in pretty often, actually. It’s kind of like the principle’s office, only with therapists.\""

ela "\"You could serve to take them a little more seriously.\""

irene "\"Yeah, yeah, I get that enough from them, thank you.\""

n "I just…"

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.3
  easein 2.0 alpha 0.4

n "My heartbeat is picking up, and I struggle to focus on my breathing before it becomes noticeable."

erik "\"Could I… pass on this part of the tour?\""

show ela P1_E4
with Dissolve (0.25)

n "The others stop and look in my direction."

erik "\"I think I’ve pretty much gotten an understanding of the campus, is all. I’ll pick up the rest as I go.\""

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.4
  easein 2.0 alpha 0.5

n "I try to cover it with a laugh, but even I can tell it sounds off. My sisters eye me with concern, but Ela doesn’t seem to have picked up on it quite as easily."

ela "\"I mean… you should be able to locate the different facilities your first week. Are you-\""

erik "\"I’m fine.\""

n "I shoot my hands up in defense and flash a smile, but I can feel myself breaking into a cold sweat.."

erik "\"I just…\""

n "…can’t do this."

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.5
  easein 2.0 alpha 0.6
  
show beatrice P2_E5
with Dissolve (0.25)

show hilda P2_E1
with Dissolve (0.25)

erik "\"Sorry- Sorry I just need to sit down, I just…need to…\""

n "…leave."

n "I want to say it so badly, just spit it out and head back to my sister’s apartment. Head back to the bedroom and sleep away any inclination of what’s happening."

n "Sleep and go back to the way things were."

n "My heart rate continues to accelerate, exacerbated by the multiple pairs of eyes trained on me."

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.6
  easein 2.0 alpha 0.7

n "It’s hard to keep myself standing at this point, my leg joining the rebellion currently in progress, and I sit on the curb before it gives out entirely."
  
show ela P1_E3:
with Dissolve (0.25)

show irene U_P1_E3
with Dissolve (0.25)

n "Ela quickly finds her way next time me, alongside Hilda and Beatrice who are on me in a flash."

ela "\"Erik, it’s okay. This kind of nervousness is completely normal to a first year St. Dymphna student.\""

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.7
  easein 2.0 alpha 0.8

erik "\"No, I know, it’s just-\""

n "Please stop-"

n "I can’t-"

n "Breathe…"

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.8
  easein 2.0 alpha 0.7

n "Just breathe…"

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.7
  easein 2.0 alpha 0.5

n "In….out…."

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.5
  easein 2.0 alpha 0.3

n "….."

show PitchBlack behind beatrice, hilda, ela, irene:
  alpha 0.3
  easein 2.0 alpha 0.0

n "It takes me a few moments, but soon I can control my thoughts a little better. I’m far from fine, but I can do my best to alleviate some concerned faces."

erik "\"I’m okay, just... feeling a little winded from the tour, is all.\""

ela "\"Well, rest as long as you need to.\""

erik "\"Ela, why are you so…\""

n "{i}Normal.{/i}"

n "The word comes so naturally in my head, by in a place like this it hardly seems appropriate. In fact I’m a little disappointed with myself that the thought had come so so naturally to me."

erik "\"...composed?\""

show ela P1_E1
with Dissolve (0.25)

ela "\"Years of practice, though I guess it’s fair to say it comes with the territory.\""

erik "\"Well I’m sure everyone wouldn’t want to…\""

show irene U_P1_E3:
  easein 1.0 xalign 1.5

Voice "\"Ela?\""

n "An aged voice calls out to our tour guide, who immediately turns over to the man in recognition. Now a bit closer he looks…"

n "Refined. Standing tall the man is not only dressed well but carries himself in an air of intelligence and ability unlike anyone I’ve seen outside my brother."

show faber P1_E1:
  yalign -0.5 xalign 0.9 alpha 0.0
  easein 1.0 xalign 1.0 yalign -0.5 alpha 1.0

ela "\"Dr. Faber!\""

n "The man nods at the title, glancing around at the three of us currently on the ground. Ela stands while Beatrice and Hilda remain crouched by my side."

faber "\"Am I interrupting your tour? I didn’t know Bosworth still had you working on these.\""

ela "\"No, not at all, we were just…\""

show ela P1_E6
with Dissolve (0.25)

n "She shifts her head and makes a knowing glance towards me, one that stung a bit more than I was expecting it to."

ela "\"We just finished actually. I was just leading them back to the administration building.\""

show faber P1_E2
with Dissolve (0.25)

n "Without missing a beat his eyes single me out immediately, a look that seemed to read into me deeply."

n "It looks as if he is beginning to understand something that I can’t."

n "I did my best not to stare too intently back, though in this situation I wasn’t really sure how to present myself. Smile and introduce myself maybe?"

n "It could be a start."

faber "\"And so you’re-\""

erik "\"My name is Erik.\""

n "The interruption comes naturally while my smile doesn’t, giving off an attitude far more rude than I was intending."

n "Still I receive short nod from the doctor, not responding with any ill intent towards my outburst."

n "He reaches his hand out, and despite how slow it takes me to get up and meet it he patiently keeps it extended until it meets mine."

n "Pulling me up, the two of us end up in a handshake."

show faber P1_E1
with Dissolve (0.25)

faber "\"It is a pleasure then, Erik. All things considered I might expect to see more of you in the future.\""

n "Ela looks like she’s attempting to add something, but the man’s presence is large and overwhelming."

n "It’s not a frightening presence, but one that looks like it holds a lot of power. If Irene was with us I could only guess that this would be her definition of a spy."

faber "\"So what do you make of St. Dymphna so far. See it as a home?\""

n "I answer truthfully."

erik "\"I don’t know.\""

n "He gives another short nod, as if that was the answer he was expecting all along."

n "Giving one final look at everyone he then rests his eyes on Ela."

show ela P1_E1
with Dissolve (0.25)

faber "\"It’s good to see that you and Irene are well.\""

irene "\"Wha-?!\""

n "Irene’s voice bursts from a nearby bush, though Ela gives an unfazed smile and returns the farewell."

faber "\"Well I shouldn’t keep myself. I have quite a bit of paperwork brought to my attention.\""

faber "\"Good luck with learning your direction, Erik.\""

n "The last look he gives me is one that I can’t seem to decipher."

n "His face is intense but his eyes are warm and inviting. I shouldn’t feel nervous around this man, but I also feel as if he’s some kind of person I wouldn’t want on my bad side."

n "Just what kind of doctor is he?"

erik "\"Er…thanks.\""

show faber P1_E1:
  yalign -0.5 xalign 1.0 alpha 1.0
  easein 2.0 xalign 1.1 yalign -0.5 alpha 0.0

n "Giving one last nod Dr. Faber turns and walks opposite of the administration building, towards what I can assume are the medical facilities on campus."

irene "\"I dislike him.\""

show irene U_P1_E1:
  xalign 1.0 yalign -6.5 alpha 0.0
  easein 1.0 xalign 0.9 alpha 1.0

n "In moments Irene is next to us once again, though still has her eyes solely fixed on the back of Faber’s head."

hilda "\"That was…\""

show beatrice P2_E2
with Dissolve (0.25)

beatrice "\"…kinda cool actually.\""

n "In a way it kind of was, and already my mind is already far from the small panic attack just moments ago. Hopefully it was off everyone else’s mind too."

ela "\"Well then, if you’re not-\""

n "I can hear Ela begin to say something, though it cuts off as she begins to work her way back towards where we started our tour."

ela "\"Well we’ve covered everything then. Any other confusion and… there’s always someone you can ask around if you get lost.\""

n "Ela gives a knowing smile towards me, though at this point it doesn’t feel so bad to accept it."

hilda "\"From your ability as a tour guide I think he’s in pretty good shape, right Erik?\""

n "I nod towards my sister, proceeding to turn back towards Ela for a very well deserved thank you."

ela "\"Don’t mention it, I was happy to help out.\""

erik "\"So I guess…we head back now right?\""

show ela P1_E2
with Dissolve (0.25)

ela "\"You sound like this is a goodbye or something. As student council president this year I expect that you’ll be seeing a lot more of me after all.\""

show beatrice P1_E3
with Dissolve (0.25)

show hilda P2_E3
with Dissolve (0.25)

beatrice "\"I’m sure he’s looking forward to it.\""

n "My sister smiles slyly despite the sharp look given off by Hilda, but all in all it seems like everyone’s previous look of concern has faded."

n "Everyone is back to welcoming the sights of St. Dymphna."

hilda "\"So you going to join us on the way back, Irene?\""

irene "\"Well I wasn’t planning not to. Someone has to keep Erik on the lookout for campus dangers.\""

show ela P1_E1
with Dissolve (0.25)

ela "\"As if he couldn’t do that himself.\""

n "For the most part it seemed, but I find myself smiling at the end of our very odd our group."

n "Whether I liked it or not this was a place I was going to be seeing as a home. Ela, Dr. Faber, Irene, these were only a few of the people I would be getting to know."

n "Who I will meet and how I will act at that this point is all up to me."



########

jump A1_07 # jump A?_??
