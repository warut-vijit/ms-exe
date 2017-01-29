
label A1_05:
###############

  $ persistent.scene_number = "A1_05" # current scene


#-# >open to school hallway
#--#

stop music fadeout 1.0

$ renpy.music.set_volume(0.75)
play music "music/New Beginnings Arise from Old Endings.mp3" fadein 1.0 loop

scene classroomhall
with Dissolve(1)

show hilda P2_E1:
  xalign 0.9 yalign -0.3 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.8 yalign -0.3 alpha 1.0
show beatrice P2_E1:
  xalign 0.6 yalign 1.0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.5 yalign 1.0 alpha 1.0
show ela P1_E1:
  xalign 0.1 yalign -0.4 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.2 yalign -0.4 alpha 1.0

n "The tour is nothing out of the ordinary, even if the school is."

ela "\"...This hallway houses most of the art and music rooms, where elective classes and after-hour clubs are held.\""

n "The buildings themselves are beautiful, but I can’t help but notice the additions - light filtering through huge windows with suspiciously thick glass, wide corridors dotted with emergency phone lines."

n "Ela makes no mention of the ‘preventative measures’ the brochures seemed so eager to promote."

n "If Hilda has caught on, she’s kept her mouth shut, mirroring my quiet concern. Beatrice, on the other hand, is in love with the place."

show beatrice P2_E3
with Dissolve (0.25)

beatrice "\"Oh my God! The ceilings here go on forever! Erik, check out the rafters! It’s like something out of Hogwarts!\""

ela "\"Sondergymnasium St. Dymphna was established in 1858, and while there’s been some modifications to install modern conveniences and the like, for the most part the building itself has been very well preserved.\""

n "Beatrice practically bounces from room to room, alternatively running ahead and lagging behind to take in each new sight."

beatrice "\"It’s so cool! It’s like a castle!\""

show ela P1_E2
with Dissolve (0.25)

ela "\"It is rather spacious, isn’t it? Mr. Bosworth likes to sell the historical significance and ‘architectural richness’ of the place, but I’m sure you’re not interested in all that canned stuff…\""

show hilda P2_E2
with Dissolve (0.25)

n "From her face, I can tell that Hilda actually would want to hear it, but she doesn’t speak up."

show ela P1_E1
with Dissolve (0.25)

ela "\"...so I’ll just stick to the basics. The floor above us is reserved for assorted odds and ends, some offices, storage rooms, nothing very impressive. The view is nice, though. Let’s just head through to the next building, shall we?\""

show hilda P1_E1
with Dissolve (0.25)

n "Hilda gives the stairs a longing glance, but reluctantly follows."

scene hallway3
with Dissolve (1)

show hilda P2_E4:
  xalign 0.9 yalign -0.3 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.8 yalign -0.3 alpha 1.0
show beatrice P2_E2:
  xalign 0.6 yalign 1.0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.5 yalign 1.0 alpha 1.0
show ela P1_E1:
  xalign 0.1 yalign -0.4 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.2 yalign -0.4 alpha 1.0
  
erik "\"So… Ela. How long have you been here?\""

ela "\"Three years. Transfer students are very common, but St. D’s has been my only high school.\""

n "{i}And has there always been something wrong with you?{/i}"

n "I shove the thought out of my mind, but there’s nothing there to take it’s place. My mouth makes a halfhearted attempt to cover for it."

erik "\"It looks nice.\""

show ela P1_E5
with Dissolve (0.25)

ela "\"It is.\""

show hilda P2_E5
with Dissolve (0.25)

n "Hilda shoots me a worried glance, but Ela speaks up before the silence has a chance to entrench itself, gesturing past the hallway windows."

show ela P1_E1
with Dissolve (0.25)

ela "\"The lake is a popular spot to relax, although there’s no fishing or swimming allowed. There is a pool though, which is obviously cleaner than the lake in any case.\""

n "True to her word, there’s a lake, a pair of wooden benches at it’s edge. There doesn’t seem to be anyone there, despite it’s ‘popularity’."

scene entrance4
with Dissolve (1)

show hilda P2_E4:
  xalign 0.9 yalign -0.3 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.8 yalign -0.3 alpha 1.0
show beatrice P2_E2:
  xalign 0.6 yalign 1.0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.5 yalign 1.0 alpha 1.0
show ela P1_E1:
  xalign 0.1 yalign -0.4 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.2 yalign -0.4 alpha 1.0

n "As we descend the stairs and emerge from the building into the blinding sunlight, Ela points towards the small structure to the right."

ela "\"The chapel is always open, though not always ‘staffed’. Services are held every day, if you’re interested.\""

n "She switches to her left."

ela "\"...and the dorms are across the way. We’ll head there in a moment, but for now…\""

scene mainlobby
with Dissolve (1)

show hilda P2_E1:
  xalign 0.9 yalign -0.3 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.8 yalign -0.3 alpha 1.0
show beatrice P1_E2:
  xalign 0.6 yalign 1.0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.5 yalign 1.0 alpha 1.0
show ela P1_E1:
  xalign 0.1 yalign -0.4 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.2 yalign -0.4 alpha 1.0

n "Ela leads us straight forward, pushing open larger-than-average double doors into the main building, central to the campus. Beatrice gasps audibly."

n "In front of us is a courtyard of awe-inspiring proportions, two matching staircases wrapping around the perimeter, framing a veritable park’s worth of foliage and benches, all contained under a domed glass ceiling several stories above us. Hallways branch from the center on the first and second floors."

ela "\"We call this is the atrium, which is fitting since it’s sort of the heart of the building. Most of the classrooms can be accessed from here, as well as the library.\""

ela "\"It can be a little noisy, but if that doesn’t bother you, it’s a very calming place to study or relax.\""

n "Lots of places to relax, I see. {i}Wouldn’t want us getting anxious, after all.{/i}"

n "As impressed as I ought to be, once again, doubt colors my thoughts."

show ela P1_E2
with Dissolve (0.25)

n "Ela takes my silence for awe, and gives me a knowing smile that feels entirely out of place, given my circumstances."

show ela P1_E1
with Dissolve (0.25)

ela "\"Yeah, it has that effect on people, doesn’t it? Well, the classrooms aren’t nearly as impressive. They’re pretty standard, actually.\""

n "So let’s skip those, right?"

n "After giving us another moment to appreciate the decour, Ela turns to hold the door for us, and I obediently follow my sisters back outside."
scene mainbuilding

show hilda P2_E1:
  xalign 0.9 yalign -0.3 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.8 yalign -0.3 alpha 1.0
show beatrice P1_E2:
  xalign 0.6 yalign 1.0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.5 yalign 1.0 alpha 1.0
show ela P1_E1:
  xalign 0.1 yalign -0.4 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.2 yalign -0.4 alpha 1.0

n "Ela regains the lead, and begins to direct us to the dorms."

ela "\"And that’s pretty much the tour. I’m not the best at this, I know, but hopefully I’ve managed to highlight some of the more interesting spots for you.\""

$ renpy.pause (1.0)

show beatrice P1_E5
with Dissolve (0.25)

show ela P1_E3
with Dissolve (0.25)

n "After a moment, I feel an elbow in my ribs, and glance up to find Beatrice attached to it, an impatient glare on her face. Behind her, Ela’s adopted a slightly worried expression."

erik "\"Er, yeah. It’s fine. It looks good.\""

show beatrice P2_E2
with Dissolve (0.25)

beatrice "\"Good? Lighten up, Erik, this place is amazing!\""

n "{i}Yeah, the parts they’re showing us.{/i}"

erik "\"Yeah, I know. I’m just… kind of shocked, I guess.\""

show ela P1_E6
with Dissolve (0.25)

stop music fadeout 5.0

n "Another moment of uncomfortable tension later, Ela sighs, slowing to a halt, her smile fading into a look of empathy. Her ‘tour guide’ voice drops to something more subdued, but sincere."

$ renpy.music.set_volume(0.75)
play music "music/Reflections.mp3" fadein 1.0 loop

show ela P1_E3
with Dissolve (0.25)

ela "\"...Listen, I know how this all looks. It looks like a prison. New students usually think that way. I thought that way.\""

ela "\"You’re thinking this school is like a warehouse for damaged goods, like no one trusts you to make your own decisions.\""

show ela P1_E6
with Dissolve (0.25)

ela "\"You’re here because there’s something wrong with you, and right now it feels like it’s taking your future away from you.\""

$ renpy.sound.set_volume(0.1)
play sound "music/effects/Branch1.mp3"

n "That’s… probably a little more dramatic than I would have put it, but she’s not wrong. Ela leans against the trunk of a tree, hands clasped behind her back."

scene MISSINGCG
with Dissolve (1.0)

ela "\"If you’re looking at it that way, that’s all you’re going to see. Perspective is everything.\""

ela "\"So take it from someone who’s been in your shoes: St. D’s is just like us. It’s easy to put a label on it and jump to conclusions about it, but that’s not the whole package.\""

ela "\"Having a condition doesn’t change who you are, catering to those conditions doesn’t change what this is. It’s just a school.\""

n "A heavy silence settles in, one I’m not sure how to break. I understand what she’s saying; I guess it’ll just take some time to put it into practice."

n "Glancing to my side, I see Hilda has a ghost of a smile, and Beatrice looks at me with watery eyes."

erik "\"...thanks, Ela, that’s… actually really good advice.\""

n "I give a nervous laugh, rubbing the back of my head sheepishly."

erik "\"Now I kinda feel like a jerk for treating this place like a loony bin. You’re right. There’s nothing-\""

stop music fadeout 1.0

$ renpy.sound.set_volume(1.0)
play sound "music/effects/Branch2.mp3"

scene mainbuilding
with hpunch

show hilda P2_E3:
  xalign 0.8 yalign -0.3
  easein 0.75 xalign 0.9
  
show beatrice P2_E5 behind hilda:
  xalign 0.5 yalign 1.0
  easein 0.75 xalign 1.0
  
show ela P1_E4:
  xalign 0.1 yalign -0.4
  easein 0.75 xalign 0.0 

show irene U_FALLING:
  xalign 0.4 yalign -2.0
  easein 0.75 yalign 2.0
  
n "The sound of splitting wood and rustling leaves interrupts me, causing all of us to instinctively jump closer to Ela, away from the crashing bough."

n "Before I even have time to register the event, a student rises from the debris, dusting herself off and initiating a conversation as casually as one might wave hello."

$ renpy.music.set_volume(0.5)
play music "music/Library Themeloopable.mp3" fadein 1.0 loop

show irene U_P1_E1:
  xalign 0.5 yalign -25.0
  easein 1.5 xalign 0.5 yalign -6.5

Voice "\"Oh hey Ela, didn’t see you there, don’t mind me. Pro tip, that tree is a bit iffy! And you must be Erik!\""

show irene U_P1_E4
with Dissolve (0.25)

n "She thrusts a hand in my direction, a thousand watt smile on her face."

erik "\"Uh. Yeah. It’s nice to meet you…\""

n "Ela seems to have shorted out, staring at the girl with a mixture of despair and panic."

show irene U_P1_E2
with Dissolve (0.25)

irene "\"Irene! Irene Ross, at your service!\""

show irene U_P1_E1
with Dissolve (0.25)

erik "\"Nice to meet you, Irene. I’m… Erik… hang on, where did you hear my name before?\""

show irene U_P1_E4
with Dissolve (0.25)

irene "\"Huh? Oh. It was kind of a lucky guess? I figured it was either that or Aaron, I mean, lip reading is more art than science, look it’s not important and {i}heeeey welcome to St. D’s!{/i}\""

show irene U_P1_E2
with Dissolve (0.25)

n "Irene throws her arms in a wide gesture, the expanse of the campus behind her. A thin line of blood seeps from a fresh cut on her cheekbone."

n "Ela’s face has completely drained of color. Hilda’s jaw hangs slightly agape. At some point Beatrice has taken the opportunity to take cover behind Hilda in case Irene were to spontaneously combust, which doesn’t seem terribly far-fetched. None of them seem eager to join this conversation."

erik "\"...Thanks?\""

show irene U_P1_E1
with Dissolve (0.25)

irene "\"No problem! It’s always good to see a new face. I’m sure you’ll fit right in! Ela, you’re giving him the tour, right? I’d be happy to lend a hand. No one knows more about this campus than I do!\""

n "She holds up the case strung loosely around her neck, which I now realize is a pair of well-worn binoculars."

n "Ela finds her voice, maybe an octave higher than when she lost it."

show ela P1_E7
with hpunch

show irene U_P1_E1
with Dissolve (0.25)

ela "\"We’re fine! It’s fine! You probably have stuff to do, right? {i}Please?{/i}\""

show irene U_P1_E2
with Dissolve (0.25)

irene "\"Nope! Totally open today! Just doing my rounds, nothing really happening around here -except Erik, of course!- so I figure I might as well drop in. Ha! Drop in! I didn’t even mean to do that.\""

n "Beatrice peeks from around Hilda’s shoulder."

beatrice "\"...Is this real life?\""

show irene U_P1_E4
with Dissolve (0.25)

irene "\"Hey, how far have you guys gotten, anyway? Has she shown you the old therapy rooms, you know, the ones where they still have all the cool, antique heavy-duty leather restraints and metal dentists chairs an’ stuff?\""

show ela P1_E7
with hpunch

ela "\"{i}Irene!{/i}\""

show irene U_P1_E1
with Dissolve (0.25)

irene "\"Huh? What?\""

n "Irene follows Ela’s line of sight to me, and understanding lights up her face."

show irene U_P1_E3
with Dissolve (0.25)

irene "\"Oh. {i}Oh!{/i} Hey, listen, they don’t use that stuff unless shit’s, like, really hitting the fan, so-\""

show hilda P2_E5
with Dissolve (0.25)

hilda "\"What were you doing in a tree?\""

show irene U_P1_E1
with Dissolve (0.25)

irene "\"Oh, you know, basic recon, information gathering, stuff like that. It’s like people watching, only with a laser mic.\""

show beatrice P1_E2:
  easein 1.0 xalign 0.75

show hilda P2_E5:
  easein 1.0 xalign 1.1

with Dissolve (0.25)

n "Beatrice breaks from her cover, a look of excitement on her face."

beatrice "\"You have a laser microphone?!\""

ela "\"Irene here likes to eavesdrop on people, but she {i}usually{/i} has the best intentions.\""

n "I’m not sure if she’s trying to convince us or herself, but either way, it doesn’t do much."

show irene U_P1_E2
with Dissolve (0.25)

irene "\"Oh c’mon! It’s not like Erik’s name is a big secret.\""

n "She turns to me, suddenly intense."

show irene U_P1_E1
with Dissolve (0.25)

irene "\"Is your name a big secret, though? Because that would be awesome.\""

erik "\"Er, no. Just Erik.\""

show irene U_P1_E1
with Dissolve (0.25)

n "Irene’s face falls a little, and she looks over her binoculars for a moment before shrugging a little."

show irene U_P1_E4
with Dissolve (0.25)

irene "\"Damn. That’s a shame. I mean, not your name, that’s fine. Secret names are just cool. Not that I have one. That you know about.\""

show ela P1_E4
with Dissolve (0.25)

ela "\"Nobody has one!\""

irene "\"Well, of course you’d think that, they’re secrets.\""

show ela P1_E8
with Dissolve (0.25)

n "I don’t think this place is going to be good for my mental health."

show ela P1_E3
with Dissolve (0.25)

irene "\"Anyway, it’s nice to meet you guys! I guess you need some time to, like, adjust, but don’t worry, everyone here is really cool. And I’d know! So don’t worry about it, ‘kay?\""

erik "\"Um, sure? It’s nice to meet you, too. These are my sisters, Hilda and Beatrice.\""

show hilda P2_E1
with Dissolve (0.25)

hilda "\"...I apologize for my earli-\""

show hilda P2_E3
with Dissolve (0.25)

beatrice "\"-please tell me you actually have a laser mic.\""

irene "\"Of course! Wanna check it out?\""

show beatrice P2_E3
with Dissolve (0.25)

beatrice "\"Oh my God please.\""

n "Beatrice glances back at us with an expression of childlike joy."

show beatrice P2_E4
with Dissolve (0.25)

beatrice "\"This is the best school ever.\""


########

jump A1_06 # jump A?_??
