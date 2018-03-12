
label A1_03:
###############

$ persistent.scene_number = "A1_03" # current scene
$ persistent.scene_name = "St. Dymphna" # current scene name
$ renpy.save_persistent()


# Scene 03 - St. Dymphna
# Scene name: St. Dymphna
# 
# Backgrounds:
# Apartment Interior(day)
# School Entrance (day)
# Office (day)
# Classroom (day)
# 
# Sprites:
# Beatrice, Hilda, Mr. + Mrs. Wilhelm, Ms. Claes, Mr. Bosworth, Ela
# 
# Music: 
# Schooltheme
# 
# Sound Effects:
# door closing
# 
#-# >open with car_interior(inside alleyway) BG
scene CarInteriorAlleyWay at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
#--#

n "The car ride lasts hours - or at least it feels like it."

n "It seems like the closer I get to the school, the more apprehensive I feel."

n "I {i}could{/i} say I've changed my mind, but I think the point where I could have turned back passed weeks ago."

n "Besides, I've already troubled my family enough; changing my mind now would just cause more problems."

mum "\"Erik, how are you feeling? You haven't said a thing since we left.\""

erik "\"I'm alright. Just...\""

mum "\"Nervous?\""

erik "\"A little.\""

n "Mum nods in understanding."

mum "\"Just tell me if you don't feel good, and we'll go somewhere so you can take a break.\""

erik "\"Sure.\""

n "Before long, we arrive and file out of the car."

n "It's nice to stretch my legs after being squished into the back of Mom's eco-car with Hilda and Beatrice."

#-# >the main gate
scene mainGate at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
#--#
#-# >Be Green begins (NOTE: NOT BE GREEN AFTERNOON)
play music "music/Be Green (Afternoon).mp3" loop
#--#

n "After consulting a map of the campus from my welcome pack, we set out towards our destination."

n "The main building is the easiest to recognize; it's three stories - the tallest building on campus -  and definitely very old. A mass of ivy coats the entrance, adding a natural, green layer of patina to the stonework."

#-# >Dad_frown
show dad P1_E4:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.25 alpha 1.0
#--#
#-# >Mum_neutral
show mum P1_E1:
  alpha 0.0 xalign 0.9 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.75 alpha 1.0
#--#

mom "\"Isn't this building pretty, Erik? This is where you'll be going for classes.\""

erik "\"It's nice. I like older buildings like this. It's kind of like the old church back home.\""

#-# >Screen Shake
scene mainGate with vpunch
#--#
#-# >All sounds and music cut
stop music
stop music2
stop ambience
stop ambience2
#--#
stop sound

unknownqqq "\"GOOD MORNING!\""

n "Suddenly, a booming voice emerges from the building. Despite the distance, I can hear it very clearly. Is there a loudspeaker nearby?"

n "A large man comes out from behind the entranceway. He's waving at us to come inside."

#-# >Dad_neutral
show dad P1_E1:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.25 alpha 1.0
#--#

dad "\"Ah, that'll be Mr. Bosworth.\""

hilda "\"Is he always so...?\""

n "I tilt my head toward the man in disbelief."

dad "\"... Yes.\""

#-# >Bosworth enter right
show bosworth P1_E2:
  alpha 0.0 xalign 0.9 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
#--#
#-# >The Mind-Boggle begins playing
play music "music/The_Mind-Boggle.mp3" loop
#--#

bosworth "\"Hello again, Mr. and Mrs Wilhelm! So good to see you again, yes, yes...\""

n "The large man - Mr. Bosworth -  vigorously shakes my parent's hands, as if they were old friends seeing each other again."

bosworth "\"And this must be Erik!\""

n "He approaches me. Despite us being almost similar in height, I can't help but feel... diminished by his presence."

#-# >Bosworth smile
show bosworth P1_E4
with Dissolve(0.25)
#--#

bosworth "\"Your parents have already told me so much about you, Erik. Such a gentleman to be joining our halls!\""

n "He steps back and takes a bow."

bosworth "\"On behalf of all the staff here, welcome to Saint Dymphna's Privatgymnasium.\""

erik "\"Uh, thanks...\""

n "He claps his hands together loud enough to scare some of the nearby birds away."

#-# >Bosworth neutral
show bosworth P1_E2
with Dissolve(0.25)
#--#

bosworth "\"Well, then, we have a lot of ground to cover today! There's some paperwork inside for you and your parents to sign, the tour, the ritual...\""

erik "\"Ritual?\""

#-# >Bosworth laugh
show bosworth P1_E4
with Dissolve(0.25)
#--#

bosworth "\"Kidding, kidding!\""

n "He herds us inside with a jolly laugh."

#-# >Fade to interior building
scene classroomhall with Dissolve(1.0)
#--#

#-# >Bosworth neutral 2
show bosworth P1_E2:
  alpha 0.0 xalign 0.4 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
#--#

bosworth "\"If you don't mind, I'd like to begin with a short one-on-one with Erik. Please, make yourselves comfortable in the lobby.\""

mom "\"We'll be right here, then.\""

#-# >Music fadeout
stop music fadeout 1.0
#--#
#-# >Fade in a hero's theme
play music "music/The Hero's Theme.mp3" fadein 1.0
#--#

#-# >Fade to office (day)
#-# >Fade to office (day)
scene BosworthOffice with Dissolve (1.0)
show bosworth P1_E2:
  alpha 0.0 xalign 0.9 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show BosworthOfficeFG
#--#
#-# >Slide across the BG as Erik inspects the room
# not big enough to pan
#--#

n "Bosworth's office is very organized, with bookshelves containing dozens of volumes, paperwork neatly stacked, and a desk polished to a mirror sheen. It's almost intimidatingly perfect."

n "He settles into his massive chair and shuffles a few papers, then gestures to the seat opposite his."

#-# >Return to full BG

#--#

n "..."

n "It's incredibly comfortable. Clearly, this school spares no expense."

bosworth "\"Now, let's get down to business. We like to get a feel for new students by asking them about their comfort levels and what they want out of this school.\""

erik "\"Okay, makes sense.\""

bosworth "\"Glad to hear it!\""

n "He pauses for a moment and thumbs through a file on his desk, presumably mine."

bosworth "\"So you're comfortable with lessons in both English and German?\""

erik "\"That's right.\""

#-# >Bosworth splendid
show bosworth P1_E4
with Dissolve(0.25)
#--#

bosworth "\"Splendid! Ms. Claes is one of our English-speaking instructors; you'll be in her homeroom. I think you'll get along with her just fine!\""

erik "\"Sounds good to me. I take it English classrooms have students from a wider variety of countries?\""

#-# >Bosworth neutral 3
show bosworth P1_E2
with Dissolve(0.25)
#--#

bosworth "\"Ha ha! You're a smart lad. Yes, that's correct! We have a lot of people coming in from all over Europe, so we do our best to accommodate them.\""

bosworth "\"If you had prefered a German classroom, you'd probably see more people who are native to Germany, Switzerland, or Austria.\""

erik "\"Makes sense.\""

n "Bosworth nods in agreement, marking my responses on a sheet of paper."

bosworth "\"Indeed, indeed. Next question: How do you feel about coming here?\""

n "I shift slightly. Obviously, I wasn't expecting such a direct line of questioning."

erik "\"I'm kind of nervous moving here, I guess. It's a new school, after all.\""

n "In truth, I'm kind of freaking out inside. This is all a lot to take in."

n "Even though I was anticipating this."

n "My leg twinges a little bit, as if reacting to my state of mind."

n "Bosworth smiles sympathetically."

bosworth "\"It's not uncommon for our students to feel what you're feeling, Erik. We at St. Dymphna's are always trying our best to listen for when students aren't well or are feeling stressed.\""

n "His words are well-practiced and clearly part of a much longer speech - something he must have had years, maybe decades, of practicing."

n "Nonetheless, I feel a little better."

n "He takes one final glance over the paper in front of him before speaking."

bosworth "\"Is there anything you need before you get started at school? Anything you want me to tell your teachers or supervisors?\""

n "Once again, his words are practiced, yet genuine."

n "Thankfully, I know exactly what I want; It's something that's been on my mind for a while."

erik "\"Where can I go for a good walk?\""

#-# >Bosworth chuckle
show bosworth P1_E4
with Dissolve(0.25)
#--#

n "Bosworth chuckles at my response."

bosworth "\"I'm happy to inform you that the campus has an excellent series of footpaths for you to use at your leisure! When you take the tour, I'm sure your guide will do her best to point that out to you.\""

#-# >Bosworth chuckle 2
show bosworth P1_E4
with Dissolve(0.25)
#--#

bosworth "\"Looks like we're all done, Erik!\""

erik "\"Great.\""

bosworth "\"I'll be out in just a second; please go on ahead.\""

n "I do as he says and lift myself from my seat, before leaving the office and carefully closing the door behind me."

#-# >Music fadeout 2
stop music fadeout 1.0
#--#

#-# >door opening
play sound "music/effects/door open and close.mp3"
#--#

#-# >Fade to interior building 2
scene classroomhall with Dissolve(1.0)
#--#
#-# >Mum enter left
show mum P1_E1:
  alpha 0.0 xalign 0.0 yanchor 1.0 ypos 1080+425+60
  easein 1.0 xalign 0.0 alpha 1.0
#--#
#-# >Beatrice enter left
show beatrice P1_E1:
  alpha 0.0 xalign 0.35 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.35 alpha 1.0
#--#
#-# >Brunhilde enter left
show hilda P1_E1:
  alpha 0.0 xalign 0.65 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.65 alpha 1.0
#--#
#-# >Dad enter left
show dad P1_E1:
  alpha 0.0 xalign 1.1 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 1.1 alpha 1.0
#--#

erik "\"Okay, all done.\""

mum "\"How did it go, Erik?\""

beatrice "\"Is he nice?\""

erik "\"It went well, and yeah, Mr. Bosworth is actually pretty nice.\""

#-# >Bosworth enter right 2
show bosworth P1_E2:
  alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
show beatrice P1_E1:
  alpha 1.0 xalign 0.35 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.2 alpha 1.0
show hilda P1_E1:
  alpha 1.0 xalign 0.65 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.8 alpha 1.0
#--#
#-# >A busier sort of day begins playing
play music "music/A Busier Sort of Day (Based on St. Paul's Suite by Gustav Holst).mp3" loop
#--#

bosworth "\"I'm glad to hear it!\""

n "I turn around, not realizing the man I'm talking about has already finished whatever he was doing."

bosworth "\"I just called Ms. Claes; she's in her classroom at the end of this hallway, Erik. She'll be expecting you in a minute. Now, I'll need to steal you two away, Mr. and Mrs. Wilhelm. Just a few bits and pieces of last-minute paperwork...\""

#-# >Bosworth and mom and dad leave
show bosworth P1_E2:
  alpha 1.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 0.0
show mum P1_E1:
  alpha 1.0 xalign 0.0 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.0 alpha 0.0
show dad P1_E1:
  alpha 1.0 xalign 1.1 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 1.1 alpha 0.0
#--#

n "He guides them into the office and I'm left with Beatrice and Hilda."

#-# >Beatrice and Hilda move to centerleft and center right
show hilda P1_E1:
  easein 1.0 xalign 0.7 alpha 1.0
show beatrice P1_E1:
  easein 1.0 xalign 0.3 alpha 1.0
#--#

erik "\"Well, want to check out my classroom with me?\""

n "My sisters nod in agreement."

n "I lead the way and knock gingerly on the door a few times."

#-# >knock knock
play sound "music/effects/Knock Knock.mp3"
#--#

unknownqqq "\"Come in.\""

#-# >fade to office (day)
scene classroom1 with Dissolve(1.0)
#--#

#-# >Claes enter right
show claes P1_E1:
  alpha 0.0 xalign 1.0 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.9 alpha 1.0
show hilda P2_E2:
  alpha 0.0 xalign 0.0 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.1 alpha 1.0
show beatrice P1_E2:
  alpha 0.0 xalign 0.3 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.4 alpha 1.0
#--#
#-# >Claes_smile.png
show claes P1_E5
with Dissolve(0.25)
#--#

n "A young woman, probably a few years older than Hilda, greets us."

claes "\"Ah, you must be Erik. Welcome.\""

n "Her voice is prim, proper, and polite - very teacher-esque."

erik "\"Thanks. I was told you'll be my teacher?\""

claes "\"That is correct. I teach English, primarily, but I also hold some of the mathematics courses here on campus. Oh, and you two are...?\""

beatrice "\"I'm Erik's older sister, Beatrice Wilhelm.\""

hilda "\"And I'm his other older sister, Brunhilde Wilhelm. Call me Hilda!\""

n "They both shake hands with Ms. Claes, who smiles warmly."

claes "\"It's nice to see family members so interested in this school. Where are you coming from?\""

hilda "\"We actually live in Vienna, but Erik here is from Basel-Stadt.\""

claes "\"Oh! Have you shown him the city? We offer trips into the city on most weekends.\""

hilda "\"Not yet, unfortunately - but we're always open to showing you around, Erik.\""

beatrice "\"Yeah! We know all the best spots.\""

erik "\"I'd definitely like to explore it at some point; I guess we'll see.\""

claes "\"Sounds like you have some very capable guides.\""

n "She smiles -at least I think it's a smile, as it's such a small change in her expression that it's almost imperceivable."

claes "\"Have you taken a tour of the campus yet?\""

erik "\"Not yet.\""

claes "\"Great, we'll have someone come by and show you around.\""

n "Ms. Claes falters for a second before speaking again."

#-# >Sisters sad
show beatrice P2_E5
with Dissolve(0.25)
show hilda P2_E5
with Dissolve(0.25)
#--#

claes "\"Unfortunately, your sisters won't be able to accompany you.\""

claes "\"I'm afraid it's policy, so I hope you don't mind. \""

n "I cast my eyes over to my sisters."

erik "\"That's fine.\""

n "Beatrice seems downcast, Hilda just looks worried. I guess {i}normal{/i} people aren't allowed any further into the school grounds."

n "There's a knock at the door, distracting Ms. Claes from whatever she was about to say."

#-# >knock knock 2
play sound "music/effects/Knock Knock.mp3"
#--#

claes "\"Ah, perfect timing. Come in.\""

#-# >Ela enters from right
show ela P1_E1:
  alpha 0.0 xalign 1.2 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 1.1 alpha 1.0
#--#
#-# >Claes moves over the left slightly
show claes P1_E1:
  easein 1.0 xalign 0.8 alpha 1.0
show beatrice P1_E1
with Dissolve(0.25)
show hilda P2_E6
with Dissolve(0.25)
#--#

n "A young girl enters from outside."

unknownqqq "\"Is Erik here?\""

erik "\"Uh, yeah, that's me.\""

ela "\"Great! I'm Ela Sahin. I'll be giving you the tour!\""

n "Ela is a dark-skinned, slender girl, about my age. Her uniform is neatly pressed - almost like it's cut out of the glossy pamphlets the school sent me. The rest of her looks just as polished; her hair, her face, and even her beret look to be picture perfect."

erik "\"Nice to meet you, Ela.\""

#-# >ela_smile.png
show ela P1_E2
with Dissolve(0.25)
#--#

ela "\"It's nice to meet you too, Erik.\""

ela "\"Now, let's get started, shall we? Right this way, please!\""

#-# >clock wipe transition
scene mainlobby at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#

#-# >open to school hallway

#--#

#-# >Ela smile
show ela P1_E2:
  alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
#--#

#-# >Music: Be Green (Afternoon)
play music "music/Be Green (Afternoon).mp3"
#--#

n "The tour is nothing out of the ordinary, even if the school is."

ela "\"... This hallway houses most of the art and music rooms, where elective classes and after-hours clubs are held.\""

n "The buildings themselves are beautiful, but I can't help but notice the small additions - like light filtering through huge windows with suspiciously thick glass, or wide corridors dotted with emergency phone lines."

ela "\"Privatgymnasium St. Dymphna was established in 1858, and while there's been some modifications to install modern conveniences and the like, for the most part the building itself has been well preserved.\""

n "Despite my best efforts to hide my limp, Ela notices me lagging behind slightly - and slows down to match my pace."

n "I panic and attempt to say something to cover for myself, even though it's obvious she's already noticed."

erik "\"The, uh, the hallways are really wide here; my old school feels cramped compared to this.\""

n "{i}What was that?{/i}"

ela "\"It is rather spacious, isn't it? Mr. Bosworth likes to sell the historical significance and 'architectural richness' of the place to some of our visitors - but I'm sure you're not interested in all that canned stuff, so I'll just stick to the basics.\""

ela "\"The floor above us is reserved for assorted odds and ends: some offices, storage rooms, nothing very impressive. The view is nice, though. Let's just head through to the next building, shall we?\""

n "Despite my lack of response, Ela continues on, unphased."

n "She must have given a lot of these tours like these - ones with unresponsive, awkward recipients."

#-# >Transition to different building
scene classroomhall with Dissolve(1.0)
#--#

n "Ela does her best to fill the silence with random facts about the school as we move between points of interest, but it seems as though she's starting to run out."

n "Should I try and speak? My last attempt was poor at best."

n "I guess I should present myself as more than a brick wall."

#-# >Ela default
show ela P1_E1:
  alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
#--#

erik "\"So... Ela. How long have you been here?\""

ela "\"Three years. Transfer students are very common, but St. D's has been my only secondary school.\""

n "{i}Why are you here, though?{/i}"

n "I shove the thought out of my mind, but there's nothing to take its place. My mouth makes a half-hearted attempt to cover for it."

erik "\"It looks nice.\""

#-# >Ela smile 2
show ela P1_E2
with Dissolve(0.25)
#--#

ela "\"It is.\""

#-# >pause
$ renpy.pause (1.0)
#--#

n "Ugh, that was awkward. Come on brain, you've done this a million times before! Why can't you think of anything to say now?"

ela "\"The lake is a popular spot to relax, although there's no fishing or swimming allowed. There {i}is{/i} a pool though - which is obviously cleaner than the lake, in any case.\""

#-# >Transition to outside chapel
scene chapel with Dissolve(1.0)
show ela P1_E1:
  alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
#--#

n "We descend the stairs and emerge from the building into the blinding sunlight; Ela points towards the small structure to the right."

ela "\"The chapel is always open, though not always 'staffed.' Services are held every day, if you're interested.\""

n "She switches to her left."

ela "\"... And the dorms are across the way. We'll head there in a moment, but for now...\""

#-# >Transition to main school grounds
scene mainbuildingclose with Dissolve(1.0)
show ela P1_E1:
  alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
#--#

n "Ela leads us straight and comes to a stop in the middle of a walking path between two buildings."

ela "\"This is the main school grounds. I'm sure you saw it in your way in, but I like to stop the tours here.\""

ela "\"It can be a little busy sometimes - but if that doesn't bother you, it's a nice place to relax.\""

n "{i}Lots of places to relax, I see. Wouldn't want us getting anxious, after all.{/i}"

n "As impressed as I ought to be, doubt colors my thoughts once again."

#-# >Ela big smile
show ela P1_E2
with Dissolve(0.25)
#--#

n "Ela takes my silence for awe, and gives me a knowing smile that feels entirely out of place given the circumstances."

#-# >Ela regular smile
show ela P1_E2
with Dissolve(0.25)
#--#

ela "\"Yeah, it has that effect on people, doesn't it? Well, the classrooms aren't nearly as impressive. They're pretty standard, actually.\""

n "{i}So let's skip those, right?{/i}"

n "After giving us another moment to appreciate the freshly-mowed grass, Ela speaks again."

ela "\"And that's pretty much the tour. I'm not the best at this, I know, but hopefully I've managed to highlight some of the more interesting spots for you.\""

#-# >Pause
$ renpy.pause (1.0)
#--#

#-# >Ela frown
show ela P1_E6
with Dissolve(0.25)
#--#

n "After a moment, I realise that I should have responded just now. Ela's adopted a slightly worried expression."

erik "\"Er, yeah. It's fine. It looks good.\""

n "{i}Yeah, the parts they're showing us.{/i}"

erik "\"I'm just... kind of shocked, I guess.\""

n "Another uncomfortably tense moment later, Ela sighs, slowing to a halt; her smile fades into an empathetic look. Her 'tour guide' voice drops to something more subdued."

#-# >Ela natural
show ela P1_E1
with Dissolve(0.25)
#--#

ela "\"...I realize this is a lot to take in.\""

ela "\"I'm sure you have your own ideas on what to expect here, and I'm not going to say that's unreasonable.\""

#-# >Ela worried
show ela P1_E3
with Dissolve(0.25)
#--#

ela "\"What I {i}will{/i} say is that this school is probably the best chance you have at addressing these issues, rather than ignoring them.\""

n "Ela leans against the trunk of a nearby tree, hands clasped behind her back."

#-# >CG
show CG02
with Dissolve(2)
#--#

ela "\"You aren't the first person I've given this tour to, you know.\""

ela "\"Students from all over the world have gone through exactly the same problem - faced the exact same fears.\""

ela "\"You're afraid your condition, whatever it may be, is controlling your life by forcing you to come here.\""

ela "\"...But as long as you're acting on fear, you aren't going to make progress.\""

ela "\"If all you're doing is trying not to get worse, you're not going to get better.\""

ela "\"Of course the school isn't perfect -  none of us are. What's important is that you focus on what we can give you, not what's taken away.\""

n "A heavy silence settles in - one I'm not sure how to break. I understand what she's saying; so I guess it'll just take some time to put it into practice."

erik "\"... Thanks, Ela, that's... probably pretty good advice.\""

erik "\"...And for what it's worth, I'm sorry. I guess I'm just worried--\""

#-# >scene end
#
#--#

########

jump A1_04 # jump A?_??
