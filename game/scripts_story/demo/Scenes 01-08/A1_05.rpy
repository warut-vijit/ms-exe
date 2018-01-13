
label A1_05:
###############

$ persistent.scene_number = "A1_05" # current scene
$ persistent.scene_name = "Surprises in Strange Places" # current scene name
$ renpy.save_persistent()


# Scene 05
# 
# Scene name: Surprises in Strange Places
# 
#-# >open to school hallway
play music "<from 0.0 to 181.0826 loop 10.1653>music/New Beginnings Arise from Old Endings.mp3" loop

scene classroomhall with ImageDissolve("Transitions/clock.png", 1.0)
#--#

#-# >Brunhilde P2_E6
show hilda P2_E6:
  alpha 0.0 xalign 0.6 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.4 alpha 1.0
show hilda P2_E6 alpha 1.0
#--#
#-# >Beatrice smile
show beatrice P2_E1:
  xalign 0.8 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.6 alpha 1.0
show beatrice P2_E1 alpha 1.0
#--#
#-# >Ela smile
show ela P1_E1:
  xalign 0.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.2 alpha 1.0
show ela P1_E1 alpha 1.0
#--#

#-# >The sisters on the right, Ela on the left
#
#--#

#-# >Music: Be Green (Afternoon)
play music "music/Be Green (Afternoon).mp3" loop
#--#

n "The tour is nothing out of the ordinary, even if the school is."

ela "\"... This hallway houses most of the art and music rooms, where elective classes and after-hour clubs are held.\""

n "The buildings themselves are beautiful, but I can't help but notice the additions – light filtering through huge windows with suspiciously thick glass, wide corridors dotted with emergency phone lines."

n "Ela makes no mention of the 'preventative measures' the brochures seemed so eager to promote."

n "If Hilda has caught on, she's kept her mouth shut, mirroring my quiet concern. Beatrice, on the other hand, is in love with the place."

#-# >Beatrice excited
show beatrice P2_E3
with Dissolve (0.25)
#--#

beatrice "\"Oh my God! The ceilings here go on {i}forever!{/i} Erik, check out the {i}rafters!{/i} It's like something out of a movie!\""

ela "\"Privatgymnasium St. Dymphna was established in 1858, and while there's been some modifications to install modern conveniences and the like, for the most part the building itself has been very well preserved.\""

n "Beatrice practically bounces from room to room, alternately running ahead and lagging behind to take in each new sight."

beatrice "\"It's so {i}cool!{/i} It's like a {i}castle!{/i}\""

#-# >Ela happy
show ela P1_E2
with Dissolve (0.25)
#--#

ela "\"It is rather spacious, isn't it? Mr. Bosworth likes to sell the historical significance and 'architectural richness' of the place to some of our visitors, but I'm sure you're not interested in all that canned stuff...\""

#-# >Brunhilde happy
show hilda P2_E2
with Dissolve (0.25)
#--#

n "From her face, I can tell that Hilda actually {i}would{/i} want to hear it, but she doesn't speak up."

ela "\"... so I'll just stick to the basics. The floor above us is reserved for assorted odds and ends, some offices, storage rooms, nothing very impressive. The view is nice, though. Let's just head through to the next building, shall we?\""

#-# >Brunhilde default
show ela P1_E1
with Dissolve (0.25)
#--#
#-# >Beatrice frown
show beatrice P1_E1
with Dissolve (0.25)
#--#

n "Beatrice gives the stairs a longing glance, but reluctantly follows."

#-# >Transition to different building
scene classroomhall2
with Dissolve (1)
#--#

#-# >Beatrice default
show hilda P2_E4:
  xalign 1.0 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.8 alpha 1.0
show beatrice P2_E2:
  xalign 0.7 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show hilda P2_E4 alpha 1.0
show beatrice P2_E2 alpha 1.0
#--#
#-# >Ela default
show ela P1_E1:
  xalign 0.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.2 alpha 1.0
show ela P1_E1 alpha 1.0
#--#

erik "\"So... Ela. How long have you been here?\""

ela "\"Three years. Transfer students are very common, but St. D's has been my only secondary school.\""

n "{i}But... why are you{/i} here?"

n "I shove the thought out of my mind, but there's nothing there to take its place. My mouth makes a half-hearted attempt to cover for it."

erik "\"It looks nice.\""

#-# >Ela smile 2
show ela P1_E5
with Dissolve (0.25)
#--#

ela "\"It is.\""

#-# >Brunhilde frown
show hilda P2_E5
with Dissolve (0.25)
#--#

n "Hilda shoots me a worried glance, but Ela speaks up before the silence has a chance to entrench itself, gesturing past the hallway windows."

#-# >Brunhilde neutral
show hilda P2_E1:
  xalign 1.0 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.8 alpha 1.0
show hilda P2_E1 alpha 1.0
#--#

ela "\"The lake is a popular spot to relax, although there's no fishing or swimming allowed. There {i}is{/i} a pool though, which is obviously cleaner than the lake in any case.\""

#-# >Transition to outside chapel
scene chapel
with Dissolve (1)

show hilda P2_E4:
  xalign 1.0 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.8 alpha 1.0
show beatrice P2_E2:
  xalign 0.7 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show ela P1_E1:
  xalign 0.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.2 alpha 1.0
show beatrice P2_E2 alpha 1.0
show hilda P2_E4 alpha 1.0
show ela P1_E1 alpha 1.0
#--#

n "As we descend the stairs and emerge from the building into the blinding sunlight, Ela points towards the small structure to the right."

ela "\"The chapel is always open, though not always 'staffed'. Services are held every day, if you're interested.\""

n "She switches to her left."

ela "\"... and the dorms are across the way. We'll head there in a moment, but for now...\""

#-# >Transition to inside main building
scene mainlobby
with Dissolve (1)
#--#
#-# >Beatrice happy
show hilda P2_E1:
  xalign 1.0 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.8 alpha 1.0
show beatrice P1_E2:
  xalign 0.7 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show ela P1_E1:
  xalign 0.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.2 alpha 1.0
show beatrice P1_E2 alpha 1.0
show hilda P2_E1 alpha 1.0
show ela P1_E1 alpha 1.0
#--#

n "Ela leads us straight forward, pushing open larger-than-average double doors into the main building, central to the campus. Beatrice gasps audibly."

ela "\"We call this is the atrium, which is fitting since it's sort of the heart of the building. Most of the classrooms can be accessed from here, as well as the library.\""

ela "\"It can be a little noisy, but if that doesn't bother you, it's a very calming place to study or relax.\""

n "{i}Lots of places to relax, I see. Wouldn't want us getting anxious, after all.{/i}"

n "As impressed as I ought to be, once again, doubt colors my thoughts."

#-# >Ela big smile
show ela P1_E2
with Dissolve (0.25)
#--#

n "Ela takes my silence for awe, and gives me a knowing smile that feels entirely out of place, given my circumstances."

#-# >Ela regular smile
show ela P1_E1
with Dissolve (0.25)
#--#

ela "\"Yeah, it has that effect on people, doesn't it? Well, the classrooms aren't nearly as impressive. They're pretty standard, actually.\""

n "{i}So let's skip those, right?{/i}"

n "After giving us another moment to appreciate the décor, Ela turns to hold the door for us, and I obediently follow my sisters back outside."

#-# >Outside main building with fade
scene mainbuilding
with Dissolve (1)
show hilda P2_E1:
  xalign 1.0 yanchor 1.0 ypos 1080+425+85 alpha 0.0
  easein 1.0 xalign 0.8 alpha 1.0
show beatrice P1_E2:
  xalign 0.7 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show ela P1_E1:
  xalign 0.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.2 alpha 1.0
show beatrice P1_E2 alpha 1.0
show hilda P2_E1 alpha 1.0
show ela P1_E1 alpha 1.0
#--#

n "Ela regains the lead, and begins to direct us to the dorms."

ela "\"And that's pretty much the tour. I'm not the best at this, I know, but hopefully I've managed to highlight some of the more interesting spots for you.\""

#-# >Pause
$ renpy.pause (1.0)
#--#

#-# >Beatrice frown 2
show beatrice P1_E5
with Dissolve (0.25)
#--#
#-# >Ela frown
show ela P1_E3
with Dissolve (0.25)
#--#

n "After a moment, I feel an elbow in my ribs, and glance up to find Beatrice attached to it, an impatient glare on her face. Behind her, Ela's adopted a slightly worried expression."

erik "\"Er, yeah. It's fine. It looks good.\""

#-# >Beatrice smile 2
show beatrice P2_E2
with Dissolve (0.25)
#--#

beatrice "\"{i}Good?{/i} Lighten up, Erik, this place is {i}amazing!{/i}\""

n "{i}Yeah, the parts they're showing us.{/i}"

erik "\"Yeah, I know. I'm just... kind of shocked, I guess.\""

#-# >Ela frowns harder
show ela P1_E6
with Dissolve (0.25)

stop music fadeout 5.0
#--#

n "Another moment of uncomfortable tension later, Ela sighs, slowing to a halt, her smile fading into a look of empathy. Her 'tour guide' voice drops to something more subdued."

#-# >Ela natural
play music "music/Reflections.mp3" loop

show CG02
with Dissolve (1.0)
#--#

ela "\"...I realize this is a lot to take in, yes.\""

ela "\"I'm sure you have your own ideas on what to expect here, and I'm not going to say that's unreasonable.\""

#-# >Ela worried
play sound "music/effects/Branch1.mp3"
#--#

ela "\"What I {i}will{/i} say is that this school is probably the best chance you have addressing these issues, rather than ignoring them.\""

n "Ela leans against the trunk of a nearby tree, hands clasped behind her back."

#-# >CG
#
#--#

ela "\"You aren't the first person I've given this tour to, you know.\""

ela "\"Students from all over the world have gone through exactly the same problem, faced the exact same fears.\""

ela "\"You're afraid your condition, whatever it may be, is controlling your life by forcing you to come here.\""

ela "\"...But as long as you're acting on fear, you aren't going to make progress.\""

ela "\"If all you're doing is trying not to get worse, you're not going to get better.\""

ela "\"Of course the school isn't perfect. None of us are. What's important is that you focus on what this school can give you, not what it's taking away.\""

n "A heavy silence settles in, one I'm not sure how to break. I understand what she's saying; I guess it'll just take some time to put it into practice."

erik "\"... thanks, Ela, that's... probably pretty good advice.\""

erik "\"...and for what it's worth, I'm sorry. I guess I'm just worried –\""

#-# >CG END
hide CG02
#--#
#-# >Abrupt music end
stop music fadeout 5.0
#--#
#-# >Crack
play sound "music/effects/Branch2.mp3"
#--#
#-# >Irene sprite tumbles from top of screen to bottom?
show irene U_P1_E1:
  xalign 0.8 yanchor 1.0 ypos 1080+425+300 alpha 0.0
  easein 1.5 xalign 0.8 yanchor 1.0 ypos 1080+425 alpha 1.0
show irene U_P1_E1 alpha 1.0
#--#
#-# >Ela shocked
show ela P1_E4:
  xalign 0.2 yanchor 1.0 ypos 1080+425
  easein 0.75 xalign 0.15
#--#
#-# >Beatrice shocked
show beatrice P2_E5 behind hilda:
  xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 0.75 xalign 0.45
#--#
#-# >Brunhilde shocked
show hilda P2_E3:
  xalign 0.8 yanchor 1.0 ypos 1080+425+85
  easein 0.75 xalign 0.75
#--#

#-# >Beatrice and Brunhilde slide closer to Ela, Beatrice behind Brunhilde
show beatrice P2_E5 behind hilda:
  xalign 0.45 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.4
show hilda P2_E3:
  xalign 0.75 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.57
#--#

n "The sound of splitting wood and rustling leaves interrupts me, causing all of us to instinctively jump closer to Ela, away from the crashing bough."

n "Before I even have time to register the event, a student rises from the debris, dusting herself off and initiating a conversation as casually as one might wave hello."

#-# >Irene unidentified
show irene U_P1_E1:
  xalign 0.8 yanchor 1.0 ypos 1080+425
  easein 1.5 xalign 0.85 yanchor 1.0 ypos 1080+425
#--#

unknownqqq "\"Oh hey Ela, didn't see you there, don't mind me. For the record, that tree is a bit iffy! And you must be Erik!\""

#-# >Irene smile
show irene U_P1_E4
with Dissolve (0.25)
#--#

n "She thrusts a hand in my direction, a thousand watt smile on her face."

erik "\"Uh. Yeah. It's nice to meet you...\""

n "Ela seems to have shorted out, staring at the girl with a mixture of despair and panic."

#-# >Irene intro
show irene U_P1_E2
with Dissolve (0.25)
#--#

irene "\"Irene! Irene Ross, at your service!\""

#-# >In Her Element in
play music "music/In Her Element.mp3" loop
#--#

#-# >Irene post intro
show irene U_P1_E1
with Dissolve (0.25)
#--#

erik "\"Nice to meet you, Irene. I'm... Erik... hang on, where did you hear my name before?\""

#-# >Irene raised eyebrow
show irene U_P1_E4
with Dissolve (0.25)
#--#

irene "\"Huh? Oh. It was kind of a lucky guess? I figured it was either that or Aaron, I mean, lip reading is more art than science, look it's not important and {i}heeey{/i} welcome to St. D's!\""

#-# >Irene open mouth smile
show irene U_P1_E2
with Dissolve (0.25)
#--#

n "Irene throws her arms in a wide gesture, the expanse of the campus behind her. A thin line of blood seeps from a fresh cut on her cheekbone."

n "Ela's face has completely drained of color. Hilda's jaw hangs slightly agape. At some point Beatrice has taken the opportunity to take cover behind Hilda in case Irene were to spontaneously combust, which doesn't seem terribly far-fetched. None of them seem eager to join this conversation."

erik "\"... Thanks?\""

#-# >Irene smile 2
show irene U_P1_E1
with Dissolve (0.25)
#--#

irene "\"No problem! It's always good to see a new face. I'm sure you'll fit right in! Ela, you're giving him the tour, right? I'd be happy to lend a hand. No one knows more about this campus than I do!\""

n "She holds up the case strung loosely around her neck, which I now realize is a pair of well-worn binoculars."

n "Ela finds her voice, maybe an octave higher than when she lost it."

#-# >Ela vs Irene
show ela P1_E7
with hpunch

show irene U_P1_E1
with Dissolve (0.25)
#--#

ela "\"We're fine! It's fine! You probably have stuff to do, right?\""

#-# >Irene oblivious
show irene U_P1_E2
with Dissolve (0.25)
#--#

irene "\"Nope! Totally open today! Just doing my rounds, nothing really happening around here – except Erik, of course! – so I figure I might as well drop in. Ha! Drop in! I didn't even mean to do that.\""

#-# >Irene yet again
show irene U_P1_E4
with Dissolve (0.25)
#--#

irene "\"Hey, how much have you gotten to, anyway? Has she shown you the old therapy rooms, you know, the ones where they still have all the cool, antique heavy-duty leather restraints and metal dentists chairs an' stuff?\""

#-# >Ela exasperated
show ela P1_E7
with hpunch
#--#

ela "\"{i}Irene!{/i}\""

#-# >Irene confused
show irene U_P1_E1
with Dissolve (0.25)
#--#

irene "\"Huh? What?\""

n "Irene follows Ela's line of sight to me, and understanding lights up her face."

#-# >Irene shocked
show irene U_P1_E3
with Dissolve (0.25)
#--#

irene "\"Oh. {i}Oh!{/i} Hey, listen, they don't use that stuff unless shit's, like, {i}really{/i} hitting the fan, so –\""

#-# >Brunhilde angry
show hilda P2_E5
with Dissolve (0.25)
#--#

hilda "\"W-What were you doing in a {i}tree?{/i}\""

n "Hilda is the first to recover some semblance of control over the situation."

#-# >Irene smile 3
show irene U_P1_E1
with Dissolve (0.25)
#--#

irene "\"Oh, you know, basic recon, information gathering, stuff like that. It's like people watching, only with a laser mic.\""

#-# >Beatrice excited, moves out from behind Brunhilde
show beatrice P1_E2:
  easein 1.0 xalign 0.7

show hilda P2_E5:
  easein 1.0 xalign 0.45

with Dissolve (0.25)
#--#

n "Beatrice breaks from her cover, a look of excitement on her face."

beatrice "\"You have a {i}laser microphone?!{/i}\""

#-# >Ela's still displeased
show ela P1_E7
with Dissolve (0.25)
#--#

ela "\"{i}Irene{/i} here likes to eavesdrop on people, but she {i}usually{/i} has the best intentions.\""

n "I'm not sure if she's trying to convince us or herself, but either way, it doesn't do much."

#-# >Irene open mouth smile 2
show irene U_P1_E2
with Dissolve (0.25)
#--#

irene "\"Oh c'mon! It's not like Erik's name is a big secret.\""

n "She turns to me, suddenly intense."

#-# >Irene furrowed brow
show irene U_P1_E1
with Dissolve (0.25)
#--#

irene "\"Is your name a big secret, though? Because that would be {i}awesome.{/i}\""

erik "\"Er, no. Just Erik.\""

#-# >Irene sad
show irene U_P1_E1
with Dissolve (0.25)
#--#

n "Irene's face falls a little, and she looks over her binoculars for a moment before shrugging a little."

#-# >Irene smile 4
show irene U_P1_E4
with Dissolve (0.25)
#--#

irene "\"Damn. That's a shame. I mean, not your name, that's fine. Secret names are just cool. Not that I have one. That {i}you{/i} know about.\""

#-# >Ela angry
show ela P1_E7
with Dissolve (0.25)
#--#

ela "\"{i}Nobody{/i} has one!\""

irene "\"Well, of course you'd {i}think{/i} that, they're {i}secrets.{/i}\""

#-# >Ela secrets
show ela P1_E8
with Dissolve (0.25)
#--#

n "{i}I don't think this place is going to be good for my mental health.{/i}"

#-# >Ela neutral
show ela P1_E3
with Dissolve (0.25)
#--#

irene "\"Anyway, it's nice to meet you guys! I guess you need some time to, like, adjust, but seriously, everyone here is really cool. And I'd know! So don't worry about it, 'kay?\""

erik "\"Um, sure? It's nice to meet you, too. These are my sisters, Hilda and Beatrice.\""

#-# >Brunhilde neutral 2
show hilda P2_E1:
  xalign 0.45 yanchor 1.0 ypos 1080+425+85 alpha 1.0
  easein 1.0 xalign 0.48 alpha 1.0
show hilda P2_E1 alpha 1.0
#--#

hilda "\"... I apologise for my earli – \""

#-# >Brunhilde shocked 2
show hilda P2_E3
with Dissolve (0.25)
#--#
#-# >Beatrice excited 2
show beatrice P2_E3
with Dissolve (0.25)
#--#

beatrice "\"{i} – please tell me you actually have a laser mic.{/i}\""

irene "\"Of course! Wanna check it out?\""

beatrice "\"{i}Oh my God please.{/i}\""

n "Beatrice glances back at us with an expression of childlike joy."

#-# >Beatrice joy
show beatrice P2_E4
with Dissolve (0.25)
#--#

beatrice "\"This is the {i}best school ever.{/i}\""

#-# >transition start
#
#--#
#-# <end>
stop music fadeout 5.0
#--#

########

jump A1_06 # jump A?_??
