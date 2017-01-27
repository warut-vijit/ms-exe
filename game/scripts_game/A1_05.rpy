
label A1_05:
###############

  $ persistent.scene_number = "A1_05" # current scene


#-# >open to school hallway
todo "{color=#ff8c00}>open to school hallway{/color}"
#--#
scene classroomhall
with Dissolve(2)

#-# >Brunhilde neutral
todo "{color=#ff8c00}>Brunhilde neutral{/color}"
#--#
#-# >Beatrice smile
todo "{color=#ff8c00}>Beatrice smile{/color}"
#--#
#-# >Ela smile
todo "{color=#ff8c00}>Ela smile{/color}"
#--#

#-# >The sisters on the right, Ela on the left
todo "{color=#ff8c00}>The sisters on the right, Ela on the left{/color}"
#--#

show hilda P3_E4:
  xalign 0.0 yalign -0.3 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.4 yalign -0.3 alpha 1.0
show ela P1_E1:
  xalign 0.55 yalign -0.4 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.7 yalign -0.4 alpha 1.0
show beatrice P2_E5:
  xalign 0.15 yalign 0 alpha 0.0 zoom 1.0
  easein 1.0 xalign 0.1 yalign 0 alpha 1.0

n "The tour is nothing out of the ordinary, even if the school is."

ela "\"...This hallway houses most of the art and music rooms, where elective classes and after-hour clubs are held.\""

n "The buildings themselves are beautiful, but I can’t help but notice the additions - light filtering through huge windows with suspiciously thick glass, wide corridors dotted with emergency phone lines."

n "Ela makes no mention of the ‘preventative measures’ the brochures seemed so eager to promote."

n "If Hilda has caught on, she’s kept her mouth shut, mirroring my quiet concern. Beatrice, on the other hand, is in love with the place."

#-# >Beatrice excited
todo "{color=#ff8c00}>Beatrice excited{/color}"
#--#
show beatrice P2_E3

beatrice "\"Oh my God! The ceilings here go on forever! Erik, check out the rafters! It’s like something out of Hogwarts!\""

ela "\"Sondergymnasium St. Dymphna was established in 1858, and while there’s been some modifications to install modern conveniences and the like, for the most part the building itself has been very well preserved.\""

n "Beatrice practically bounces from room to room, alternatively running ahead and lagging behind to take in each new sight."

beatrice "\"It’s so cool! It’s like a castle!\""

#-# >Ela happy
todo "{color=#ff8c00}>Ela happy{/color}"
#--#
show ela P1_E2
ela "\"It is rather spacious, isn’t it? Mr. Bosworth likes to sell the historical significance and ‘architectural richness’ of the place, but I’m sure you’re not interested in all that canned stuff…\""

#-# >Brunhilde happy
todo "{color=#ff8c00}>Brunhilde happy{/color}"
#--#
show hilda P1_E2
n "From her face, I can tell that Hilda actually would want to hear it, but she doesn’t speak up."

ela "\"...so I’ll just stick to the basics. The floor above us is reserved for assorted odds and ends, some offices, storage rooms, nothing very impressive. The view is nice, though. Let’s just head through to the next building, shall we?\""

#-# >Brunhilde default
todo "{color=#ff8c00}>Brunhilde default{/color}"
#--#

show hilda P1_E1
#-# >Beatrice frown
todo "{color=#ff8c00}>Beatrice frown{/color}"
#--#
show beatrice P1_E8
n "Beatrice gives the stairs a longing glance, but reluctantly follows."

#-# >Transition to different building
todo "{color=#ff8c00}>Transition to different building{/color}"
#--#
scene hallway3

#-# >Beatrice default
todo "{color=#ff8c00}>Beatrice default{/color}"
#--#
#-# >Ela default
todo "{color=#ff8c00}>Ela default{/color}"
#--#
show hilda P3_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.4 yalign -0.3 alpha 1.0
show ela P1_E1:
  xalign 0.55 yalign -0.4 alpha 0.0
  easein 1.0 xalign 0.7 yalign -0.4 alpha 1.0
show beatrice P2_E5:
  xalign 0.15 yalign 0 alpha 0.0
  easein 1.0 xalign 0.1 yalign 0 alpha 1.0

  
erik "\"So… Ela. How long have you been here?\""

ela "\"Three years. Transfer students are very common, but St. D’s has been my only high school.\""

n "And has there always been something wrong with you?"

n "I shove the thought out of my mind, but there’s nothing there to take it’s place. My mouth makes a halfhearted attempt to cover for it."

erik "\"It looks nice.\""

#-# >Ela smile 2
todo "{color=#ff8c00}>Ela smile 2{/color}"
#--#
show ela P1_E5
ela "\"It is.\""

#-# >Brunhilde frown
todo "{color=#ff8c00}>Brunhilde frown{/color}"
#--#
show hilda P2_E5

n "Hilda shoots me a worried glance, but Ela speaks up before the silence has a chance to entrench itself, gesturing past the hallway windows."

ela "\"The lake is a popular spot to relax, although there’s no fishing or swimming allowed. There is a pool though, which is obviously cleaner than the lake in any case.\""

n "True to her word, there’s a lake, a pair of wooden benches at it’s edge. There doesn’t seem to be anyone there, despite it’s ‘popularity’."

#-# >Transition to outside chapel
todo "{color=#ff8c00}>Transition to outside chapel{/color}"
#--#
scene entrance4

show hilda P3_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.4 yalign -0.3 alpha 1.0
show ela P1_E1:
  xalign 0.55 yalign -0.4 alpha 0.0
  easein 1.0 xalign 0.7 yalign -0.4 alpha 1.0
show beatrice P2_E5:
  xalign 0.15 yalign 0 alpha 0.0
  easein 1.0 xalign 0.1 yalign 0 alpha 1.0

n "As we descend the stairs and emerge from the building into the blinding sunlight, Ela points towards the small structure to the right."

ela "\"The chapel is always open, though not always ‘staffed’. Services are held every day, if you’re interested.\""

n "She switches to her left."

ela "\"...and the dorms are across the way. We’ll head there in a moment, but for now…\""

#-# >Transition to inside main building
todo "{color=#ff8c00}>Transition to inside main building{/color}"
#--#
#-# >Beatrice happy
todo "{color=#ff8c00}>Beatrice happy{/color}"
#--#
scene mainlobby

show hilda P3_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.4 yalign -0.3 alpha 1.0
show ela P1_E1:
  xalign 0.55 yalign -0.4 alpha 0.0
  easein 1.0 xalign 0.7 yalign -0.4 alpha 1.0
show beatrice P2_E5:
  xalign 0.15 yalign 0 alpha 0.0
  easein 1.0 xalign 0.1 yalign 0 alpha 1.0

n "Ela leads us straight forward, pushing open larger-than-average double doors into the main building, central to the campus. Beatrice gasps audibly."

n "In front of us is a courtyard of awe-inspiring proportions, two matching staircases wrapping around the perimeter, framing a veritable park’s worth of foliage and benches, all contained under a domed glass ceiling several stories above us. Hallways branch from the center on the first and second floors."

ela "\"We call this is the atrium, which is fitting since it’s sort of the heart of the building. Most of the classrooms can be accessed from here, as well as the library.\""

ela "\"It can be a little noisy, but if that doesn’t bother you, it’s a very calming place to study or relax.\""

n "Lots of places to relax, I see. Wouldn’t want us getting anxious, after all."

n "As impressed as I ought to be, once again, doubt colors my thoughts."

#-# >Ela big smile
todo "{color=#ff8c00}>Ela big smile{/color}"
#--#
show ela P1_E2
n "Ela takes my silence for awe, and gives me a knowing smile that feels entirely out of place, given my circumstances."

#-# >Ela regular smile
todo "{color=#ff8c00}>Ela regular smile{/color}"
#--#
show ela P1_E1
ela "\"Yeah, it has that effect on people, doesn’t it? Well, the classrooms aren’t nearly as impressive. They’re pretty standard, actually.\""

n "So let’s skip those, right?"

n "After giving us another moment to appreciate the decour, Ela turns to hold the door for us, and I obediently follow my sisters back outside."
scene mainbuilding

show hilda P3_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.4 yalign -0.3 alpha 1.0
show ela P1_E1:
  xalign 0.55 yalign -0.4 alpha 0.0
  easein 1.0 xalign 0.7 yalign -0.4 alpha 1.0
show beatrice P2_E5:
  xalign 0.15 yalign 0 alpha 0.0
  easein 1.0 xalign 0.1 yalign 0 alpha 1.0

n "Ela regains the lead, and begins to direct us to the dorms."

ela "\"And that’s pretty much the tour. I’m not the best at this, I know, but hopefully I’ve managed to highlight some of the more interesting spots for you.\""

#-# >Pause
todo "{color=#ff8c00}>Pause{/color}"
#--#

#-# >Beatrice frown 2
todo "{color=#ff8c00}>Beatrice frown 2{/color}"
#--#

show beatrice P1_E7

#-# >Ela frown
todo "{color=#ff8c00}>Ela frown{/color}"
#--#

show ela P1_E3

n "After a moment, I feel an elbow in my ribs, and glance up to find Beatrice attached to it, an impatient glare on her face. Behind her, Ela’s adopted a slightly worried expression."

erik "\"Er, yeah. It’s fine. It looks good.\""

#-# >Beatrice smile 2
todo "{color=#ff8c00}>Beatrice smile 2{/color}"
#--#
show beatrice P2_E2
beatrice "\"Good? Lighten up, Erik, this place is amazing!\""

n "Yeah, the parts they’re showing us."

erik "\"Yeah, I know. I’m just… kind of shocked, I guess.\""

#-# >Ela frowns harder
todo "{color=#ff8c00}>Ela frowns harder{/color}"
#--#
show ela P1_E7

n "Another moment of uncomfortable tension later, Ela sighs, slowing to a halt, her smile fading into a look of empathy. Her ‘tour guide’ voice drops to something more subdued, but sincere."

#-# >Ela natural
todo "{color=#ff8c00}>Ela natural{/color}"
#--#
show ela P1_E6

ela "\"...Listen, I know how this all looks. It looks like a prison. New students usually think that way. I thought that way.\""

ela "\"You’re thinking this school is like a warehouse for damaged goods, like no one trusts you to make your own decisions.\""

#-# >Ela worried
todo "{color=#ff8c00}>Ela worried{/color}"
#--#
show ela P1_E7

ela "\"You’re here because there’s something wrong with you, and right now it feels like it’s taking your future away from you.\""

n "That’s… probably a little more dramatic than I would have put it, but she’s not wrong. Ela leans against the trunk of a tree, hands clasped behind her back."

#-# >CG
todo "{color=#ff8c00}>CG{/color}"
#--#
scene MISSINGCG
ela "\"If you’re looking at it that way, that’s all you’re going to see. Perspective is everything.\""

ela "\"So take it from someone who’s been in your shoes: St. D’s is just like us. It’s easy to put a label on it and jump to conclusions about it, but that’s not the whole package.\""

ela "\"Having a condition doesn’t change who you are, catering to those conditions doesn’t change what this is. It’s just a school.\""

n "A heavy silence settles in, one I’m not sure how to break. I understand what she’s saying; I guess it’ll just take some time to put it into practice."

n "Glancing to my side, I see Hilda has a ghost of a smile, and Beatrice looks at me with watery eyes."

erik "\"...thanks, Ela, that’s… actually really good advice.\""

n "I give a nervous laugh, rubbing the back of my head sheepishly."

erik "\"Now I kinda feel like a jerk for treating this place like a loony bin. You’re right. There’s nothing-\""

#-# >CG END
todo "{color=#ff8c00}>CG END{/color}"
#--#
scene mainbuilding

show hilda P3_E4:
  easein 1.0 xalign 0.4 yalign -0.3 alpha 1.0
show ela P1_E1:
  easein 1.0 xalign 0.7 yalign -0.4 alpha 1.0
show beatrice P2_E5:
  easein 1.0 xalign 0.1 yalign 0 alpha 1.0

todo "Crack"
#-# >Irene sprite tumbles from top of screen to bottom?
todo "{color=#ff8c00}>Irene sprite tumbles from top of screen to bottom?{/color}"
#--#
#-# >Ela shocked
todo "{color=#ff8c00}>Ela shocked{/color}"
#--#

show ela P1_E4
#-# >Beatrice shocked
todo "{color=#ff8c00}>Beatrice shocked{/color}"
#--#
show beatrice P2_E8
#-# >Brunhilde shocked
todo "{color=#ff8c00}>Brunhilde shocked{/color}"
#--#
show hilda P2_E4
#-# >Beatrice and Brunhilde slide closer to Ela, Beatrice behind Brunhilde
todo "{color=#ff8c00}>Beatrice and Brunhilde slide closer to Ela, Beatrice behind Brunhilde{/color}"
#--#


show beatrice P2_E5 behind hilda:
  easein 1.0 xalign 0.0 yalign 0 alpha 1.0
show hilda P3_E4:
  easein 1.0 xalign 0.1 yalign -0.3 alpha 1.0
show ela P1_E1:
  easein 1.0 xalign 0.4 yalign -0.4 alpha 1.0
n "The sound of splitting wood and rustling leaves interrupts me, causing all of us to instinctively jump closer to Ela, away from the crashing bough."

n "Before I even have time to register the event, a student rises from the debris, dusting herself off and initiating a conversation as casually as one might wave hello."
Voice "\"Oh hey Ela, didn’t see you there, don’t mind me. Pro tip, that tree is a bit iffy! And you must be Erik!\""

show irene U_P1_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.95 yalign -0.3 alpha 1.0
#-# >Irene smile
todo "{color=#ff8c00}>Irene smile{/color}"
#--#

n "She thrusts a hand in my direction, a thousand watt smile on her face."

erik "\"Uh. Yeah. It’s nice to meet you…\""

n "Ela seems to have shorted out, staring at the girl with a mixture of despair and panic."

irene "\"Irene! Irene Ross, at your service!\""

erik "\"Nice to meet you, Irene. I’m… Erik… hang on, where did you hear my name before?\""

#-# >Irene raised eyebrow
todo "{color=#ff8c00}>Irene raised eyebrow{/color}"
#--#

irene "\"Huh? Oh. It was kind of a lucky guess? I figured it was either that or Aaron, I mean, lip reading is more art than science, look it’s not important and heeeey welcome to St. D’s!\""

#-# >Irene open mouth smile
todo "{color=#ff8c00}>Irene open mouth smile{/color}"
#--#
show irene U_P1_E2
n "Irene throws her arms in a wide gesture, the expanse of the campus behind her. A thin line of blood seeps from a fresh cut on her cheekbone."

n "Ela’s face has completely drained of color. Hilda’s jaw hangs slightly agape. At some point Beatrice has taken the opportunity to take cover behind Hilda in case Irene were to spontaneously combust, which doesn’t seem terribly far-fetched. None of them seem eager to join this conversation."

erik "\"...Thanks?\""

#-# >Irene smile 2
todo "{color=#ff8c00}>Irene smile 2{/color}"
#--#

irene "\"No problem! It’s always good to see a new face. I’m sure you’ll fit right in! Ela, you’re giving him the tour, right? I’d be happy to lend a hand. No one knows more about this campus than I do!\""

n "She holds up the case strung loosely around her neck, which I now realize is a pair of well-worn binoculars."

n "Ela finds her voice, maybe an octave higher than when she lost it."

#-# >Ela angry
todo "{color=#ff8c00}>Ela angry{/color}"
#--#

show ela P1_E7
#-# >Irene shocked
todo "{color=#ff8c00}>Irene shocked{/color}"
#--#
show irene U_P1_E1


ela "\"We’re fine! It’s fine! You probably have stuff to do, right? Please?\""

#-# >Irene smile 3
todo "{color=#ff8c00}>Irene smile 3{/color}"
#--#
show irene U_P1_E2
irene "\"Nope! Totally open today! Just doing my rounds, nothing really happening around here -except Erik, of course!- so I figure I might as well drop in. Ha! Drop in! I didn’t even mean to do that.\""

n "Beatrice peeks from around Hilda’s shoulder."

beatrice "\"...Is this real life?\""

irene "\"Hey, how far have you guys gotten, anyway? Has she shown you the old therapy rooms, you know, the ones where they still have all the cool, antique heavy-duty leather restraints and metal dentists chairs an’ stuff?\""

ela "\"Irene!\""

#-# >Irene confused
todo "{color=#ff8c00}>Irene confused{/color}"
#--#

irene "\"Huh? What?\""

n "Irene follows Ela’s line of sight to me, and understanding lights up her face."

#-# >Irene shocked 2
todo "{color=#ff8c00}>Irene shocked 2{/color}"
#--#

irene "\"Oh. Oh! Hey, listen, they don’t use that stuff unless shit’s, like, really hitting the fan, so-\""

#-# >Brundhilde angry
todo "{color=#ff8c00}>Brundhilde angry{/color}"
#--#
show hilda P2_E5

hilda "\"What were you doing in a tree?\""

#-# >Irene smile 4
todo "{color=#ff8c00}>Irene smile 4{/color}"
#--#

irene "\"Oh, you know, basic recon, information gathering, stuff like that. It’s like people watching, only with a laser mic.\""

#-# >Beatrice excited, moves out from behind Brunhilde
todo "{color=#ff8c00}>Beatrice excited, moves out from behind Brunhilde{/color}"
#--#
show beatrice P1_E3
n "Beatrice breaks from her cover, a look of excitement on her face."

beatrice "\"You have a laser microphone?!\""

#-# >Ela’s still displeased
todo "{color=#ff8c00}>Ela’s still displeased{/color}"
#--#

ela "\"Irene here likes to eavesdrop on people, but she usually has the best intentions.\""

n "I’m not sure if she’s trying to convince us or herself, but either way, it doesn’t do much."

#-# >Irene open mouth smile 2
todo "{color=#ff8c00}>Irene open mouth smile 2{/color}"
#--#

irene "\"Oh c’mon! It’s not like Erik’s name is a big secret.\""

n "She turns to me, suddenly intense."

#-# >Irene furrowed brow
todo "{color=#ff8c00}>Irene furrowed brow{/color}"
#--#
show irene U_P1_E4
irene "\"Is your name a big secret, though? Because that would be awesome.\""

erik "\"Er, no. Just Erik.\""

#-# >Irene sad
todo "{color=#ff8c00}>Irene sad{/color}"
#--#

n "Irene’s face falls a little, and she looks over her binoculars for a moment before shrugging a little."

#-# >Irene smile 5
todo "{color=#ff8c00}>Irene smile 5{/color}"
#--#

irene "\"Damn. That’s a shame. I mean, not your name, that’s fine. Secret names are just cool. Not that I have one. That you know about.\""

#-# >Ela angry 2
todo "{color=#ff8c00}>Ela angry 2{/color}"
#--#
show ela P1_E7
ela "\"Nobody has one!\""

irene "\"Well, of course you’d think that, they’re secrets.\""

n "I don’t think this place is going to be good for my mental health."

#-# >Ela neutral
todo "{color=#ff8c00}>Ela neutral{/color}"
#--#
show ela P1_E3
irene "\"Anyway, it’s nice to meet you guys! I guess you need some time to, like, adjust, but don’t worry, everyone here is really cool. And I’d know! So don’t worry about it, ‘kay?\""

erik "\"Um, sure? It’s nice to meet you, too. These are my sisters, Hilda and Beatrice.\""

#-# >Brunhilde neutral 2
todo "{color=#ff8c00}>Brunhilde neutral 2{/color}"
#--#

hilda "\"...I apologize for my earli-\""

#-# >Brunhilde shocked 2
todo "{color=#ff8c00}>Brunhilde shocked 2{/color}"
#--#
show hilda P2_E3
#-# >Beatrice excited 2
todo "{color=#ff8c00}>Beatrice excited 2{/color}"
#--#


beatrice "\"-please tell me you actually have a laser mic.\""

irene "\"Of course! Wanna check it out?\""

beatrice "\"Oh my God please.\""

n "Beatrice glances back at us with an expression of childlike joy."

beatrice "\"This is the best school ever.\""

#-# >transition start
todo "{color=#ff8c00}>transition start{/color}"
#--#
#-# <end>
todo "{color=#ff8c00}<end>{/color}"
#--#


########

jump A1_06 # jump A?_??
