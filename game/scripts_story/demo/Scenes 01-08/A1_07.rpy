
label A1_07:
###############

$ persistent.scene_number = "A1_07" # current scene
$ persistent.scene_name = "Icebreaker" # current scene name
$ renpy.save_persistent()


# Scene name: Icebreaker
# 
#-# >fade open to Erik's dorm room, morning
#scene erikdorm at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/eye.png", 1.0)
#--#

#-# >Alarm clock sound effect
play sound "music/effects/Phone alert.mp3"
#--#

#-# "Scene Opens"
#-# >> Wakeup Effect to <School_ErikRoom_NOPAN.png>
scene erikdorm at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/eye.png", 1.0)
#--#

n "A shaft of pale sunlight wakes me up from a shallow, restless sleep before my alarm. Despite the bright morning sun, my room feels chilly and I shiver in my thin pyjamas."

n "I wonder if it actually is chilly or if the endless cycle of negative thoughts in my head is just making me think it is."

n "You'd think the room would retain heat better what with the window being three times thicker than I'm used to, but it might as well be a hole in the wall."

n "Not even a day here, and that window's thickness is already bothering me. It's such a small detail I'm not even sure I'd have noticed it if it hadn't been pointed out, but now I just can't seem to stop thinking about it."
n "I roll out of bed and try opening it."

#-# >>window opening
play sound "music/effects/window.mp3"
#--#
#-# >>change to some sort of outside background if one is available, but otherwise stay in Erik's room (the view will have to be left to the reader's imagination)
#
#--#
#-# >>birds tweeting, wind in trees etc.
play ambience "music/effects/birdsandwind.ogg"
#--#

n "It's heavy, but it does open. Why wouldn't it? They said my room had been fitted for a low-risk student."

n "The air streaming in through the crack smells faintly of freshly cut grass and dew. It's numbingly cold, but I let it linger for a moment."

n "Just as much as having that window here in the first place feels stifling, knowing that it can be opened feels relatively comforting. A small measure of control over my life. Tiny and inconsequential, maybe, but it's something."

n "I take one final deep breath to clear my head and shut the window."

#-# >> Music: New Beginnings Arise from Old Endings
play music "music/New Beginnings Arise from Old Endings.mp3"
#--#
#-# >>window closing
play sound "music/effects/window.mp3"
#--#
#-# >>outside SFX stop
stop ambience
#--#

n "Control's fine and all, but it probably isn't worth coming back to a freezing room."

n "I should get ready for school. No sense in getting all mopey about nothing before I've even started."

n "I put on my glasses and check my phone for the time."

n "6:55."

n "Just too late to get a bit more sleep. Ugh. With an involuntary groan, I grab my clothes bag to hit the shower."

#-# >>passage of time
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene erikdorm with Clockwipe
#--#

n "By the time I've come back clean and dressed, someone's sent me a text message."

#-# >>Some sort of mobile phone graphic if we have it. If not, again, leave it to the imagination.
show EriksPhone
with Dissolve (2.0)
#--#

beatrice "\"Morning bro! Sleep well? Cheer up no matter what!! <3\""

beatrice "\"Hope you have a wonderful day!! I know you'll make a ton of friends!\""

n "The rest is just a bunch of emoji that, if nothing else, represent her perfectly."

n "I stare at the screen until it turns off by itself, wondering what I should send in return. It did feel good to read – it's nice to know that she cares."

n "It's just, no matter how much I try to force on a smile and absorb some of Beatrice's enthusiasm through her text, I just can't bring myself to feel that kind of cheer."

n "It's not even like I'm really sad. More like emotionally neutral. Numb."

n "I turn the screen back on and tap out a quick reply."

erik "\"Slept okay. Thanks. Talk to you later :)\""

#-# >>phone out
hide EriksPhone
with Dissolve (0.5)
#--#

n "There. I even add a little smiley face at the end so she doesn't worry too much. Now I'm feeling illiterate as well as disingenuous. Good start to the day if ever there was one."

n "Giving the rest of the room one final look-over to make sure I haven't forgotten anything, I grab my bag and the map from my bedside table and set out to my first class."

#-# >Music fade out
stop music fadeout 3.0
#--#

#-# <Crossfade to School_MaleDormsOut.png>
scene PitchBlack
with Dissolve(1)
scene outsidemaledormcloudy
with Dissolve(2)
#--#
#-# >>Music: The Mind-Boggle Fade in
play music "music/The_Mind-Boggle.mp3" fadein 3.0 loop
#--#
#-# >>Quiet crowd sound effects
play ambience "music/effects/muffledchatter.ogg" loop fadein 1.0
#--#


n "Despite it already being after seven, the male dorm courtyard is almost as empty right now as it was last night."

n "I thought there'd be a crowd of students moving in the general direction of the school, but far as I can see the few that are out seem content to sit on benches and chat. A few are even jogging around in tracksuits. Don't these guys have class in a little bit?"

n "I shuffle slowly through the courtyard, throwing the occasional glance this way and that to see if anyone looks like they're in any kind of hurry."

n "More and more students are leaving the dorms and they're all moving about here and there, but there's no prevailing direction to their movement. A few even acknowledge my presence, waving or smiling at me when I pass. I smile back and nod, but nothing much more than that."

n "Either I'm missing something about campus culture, or being late for first period is standard around here."

n "Actually, scratch that. It's probably just first day nerves on my part. The anxiety over getting to my first class on time is overbearing. Either way, I think I'd be better get moving. Wouldn't have anything to say to them anyway."

#-# <Clock wipe to School_MainHall.png>
stop ambience
scene classroomhall2 with Clockwipe
#--#

n "After deciding against eating in the crowded cafeteria and taking breakfast in the form of a vending machine cereal bar, I drift back into the lobby to see if I can remember the way to my form room."

n "As I enter, I feel a surge of relief as I see a familiar face for the first time that morning – a tutor, Ms. Claes. It looks as though she's waiting for someone, standing amidst a gaggle of other students and looking around."

n "Apparently she was waiting for me as when our eyes make contact she walks briskly in my direction, a stern expression on her face. The students instinctively part before her and merge back together in her wake. Surely I'm not already in trouble."

#-# >Edna_P1_E2.png enters from left to middle left
show claes P1_E2:
  xalign 0.1 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0
show claes P1_E2 alpha 1.0
#--#

claes "\"Erik! I'm glad you found your way here. I wasn't sure if you'd have been shown the way, so I thought it best to wait for you here.\""

n "It seems I'm not in trouble as I'd feared, despite her almost frightening expression and short, clipped manner of speech."

erik "\"Oh, thank you, but you didn't have to. Ela showed me where it was yesterday.\""

erik "\"Plus, I have a map.\""

#-# >Edna_P1_E1.png
show claes P1_E1
with Dissolve(0.25)
#--#

n "She gives a curt nod and chimes her approval with a small 'hmm'."

claes "\"Good, good. Glad to hear Ela did a good job of introducing you to the building. Shall we be off then?\""

#-# >Claes exits to left
show claes P1_E1:
  easein 1.0 xalign 0.1 alpha 0.0
#--#

n "With only the most cursory pause for me to confirm, she's turned on her heel and started walking away as briskly as she approached. Apparently she still wants to walk me to my form room."

#-# <Crossfade to School_Corridor1.png>
scene PitchBlack
with Dissolve(1)
scene classroomhall
with Dissolve(2)
#--#

n "I hurry along, but her pace is faster than mine, forcing me to half-hop awkwardly to match her."

#-# >Edna_P1_E2.png enters from left
show claes P1_E2:
  xalign 0.2 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.4 alpha 1.0
show claes P1_E2 alpha 1.0
#--#

n "Within a few seconds she glances around at me and seems to notice my struggling, her expression shifting to become more apologetic."

#-# >Edna_P1_E1.png 2
show claes P1_E1
with Dissolve(0.25)
#--#

n "She slows to a much more comfortable pace and I'm able to catch up and walk next to her instead of trailing behind."

n "As we walk up a set of stairs I feel my palms start to sweat a little. I hadn't realised how nervous I was, but I honestly have no idea what to expect from this place."

n "I don't know what's going to be expected of me when we reach the form room. Will I have to introduce myself? The sharp clack-clack of Ms. Claes' heels echo against the stone walls, for some reason bringing the ticking of a time bomb to my mind."

#-# <Crossfade to School_Corridor2.png>

#--#

#-# >Edna_P1_E1.png enters from left

#--#

n "As we reach the top of the stairs and enter another corridor, rather more clinical than the last, she seems to pick up on my nerves, cocking her head as she looks at me. Her expression softens somewhat."

claes "\"Nervous?\""

n "Despite her apparent concern, her voice remains quite harsh. I suppose I can forgive her; I wouldn't know how to behave in her shoes."

erik "\"Honestly, yeah.\""

claes "\"That's perfectly understandable. It's completely natural to feel nervous in new situations.\""

n "I can tell Ms. Claes is genuinely trying to reassure me but she isn't very good at it; it comes off feeling sort of forced and awkward."

claes "\"Especially in circumstances like these.\""

n "Yeah. No kidding."

claes "\"But I assure you, you really have nothing to worry about. Our introductions are quite relaxed.\""

#-# >Edna_P1_E5.png
show claes P1_E5
with Dissolve(0.25)
#--#

n "Ms. Claes stops in front of a door and turns to me. She glances at the door, then at me. To my surprise, she actually gives me a small smile - I wasn't sure if this would be something she was capable of at all."

#-# >Claes exits to right
show claes P1_E1:
  easein 1.0 xalign 0.6 alpha 0.0
#--#

n "With nothing but another terse nod as acknowledgement she opens the door and steps inside. I only notice the noise that had been coming from the classroom in its absence as it dies down almost immediately. I stare at the doorway."

n "Now or never."

n "I take a deep breath in a failed attempt to steady my nerves and follow the teacher inside, where she's already begun to address the class."

#-# >door opening sound effect
play sound "music/effects/door open and close.mp3"
#--#
#-# >Ms.Claes classroom BG
scene PitchBlack
with Dissolve(1)
scene classroom1
with Dissolve(2)
#--#
#-# >Idle chatter sound fades in
play ambience "music/effects/muffledchatter.ogg" loop fadein 3.0
#--#

n "The classroom is just as you'd expect of a normal classroom, there's desks, a large blackboard and students dressed in the same red uniform as me."

n "There must only be 12 students in this class, including me."

#-# >Idle chatter fades out
stop ambience fadeout 3.0
#--#

n "The few students chatting to each other wrap up their conversations as Ms. Claes takes her place at the front of the class."

n "I'm left awkwardly standing by the door."

claes "\"Okay class, today we'll be holding an introduction, so let's all move to the relaxation room.\""

n "{i}Relaxation room?{/i}"

n "The students seem to know what this is, and all stand before making their way towards a door at the back of the classroom."

n "Ms. Claes turns her attention to me, and beckons me to follow her."

n "I follow obediently, walking into the \"relaxation room\" behind her."

#-# >Relaxation room bg
scene PitchBlack
with Dissolve(1)
scene relaxroom
with Dissolve(2)
#--#

n "The room is about half the size of the classroom, painted in neutral, warm colors and dotted with small book shelves and tables."

n "A circle of chairs has been formed in the center of the classroom, some of the students have already taken seats, while a few are more content to choose seats outside of the circle."

n "There's a girl over there listening to music; is that allowed?"

n "I'd much rather take a seat at the edge and listen to music, but I guess it's not really an introduction if I'm as far away from anyone's attention as I can be."

n "I take a seat between two classmates, and wait until the rest of the class has found somewhere to sit."

n "..."

n "This process takes a lot longer than expected. A few students seem unsure as to where they want to sit, but Ms. Claes seems fine waiting for them."

n "..."

n "Once everyone is seated, Ms. Claes begins speaking."

claes "\"Okay everyone, as I said, we'll be holding an introduction for a new student today, so I'll explain the rules.\""

n "{i}Rules?{/i}"

n "Ms. Claes reaches for a shelf behind her, and retrieves a small pillow."

claes "\"This is the talking pillow, we'll be passing this around the circle. If you're holding the pillow, you can introduce yourself if you like, and if not, you can pass it along.\""

n "This has got to be the strangest introduction I've ever found myself in."

n "Is this the norm here?"

claes "\"I'll begin. I'm Ms. Claes, and I'll be your homeroom teacher. I've been teaching for many years, and my hobbies include reading and puzzles.\""

n "The class is quiet for a moment before Ms. Claes passes the pillow to her right. That student immediately passed it on again, apparently unwilling to introduce themselves."

student "\"Uh, Hi everyone, I'm Andre. I'm in the literature club, that's pretty much all I do.\""

n "Andre considers adding more, before passing the pillow on further."

n "We spend the next twenty minutes passing the pillow around the circle and introducing ourselves."

n "Some simply say their name, while some take the time to explain why their favorite food is their favorite."

n "It seems so... childish."

n "Before long the pillow is in my hands, and all eyes are on me."

n "They're not judging. Not mean, or expectant. Some are even bored."

erik "\"I'm Erik, I used to like hiking... geography too, I guess.\""

n "And just like that, my introduction is over."

n "Maybe I was hyping this up too much."

n "I pass the pillow to Fran. He likes steak and goes to the newspaper club."

n "He seems like a pretty nice guy, actually."

n "After a few more introductions, few of which I will remember, the pillow is handed back to Ms. Claes."

claes "\"Okay class, that was very good.\""

claes "\"We'll split into some smaller groups now.\""

n "More introductions?"

n "Ms. Claes splits us intro groups of four and encourages us to ask each other \"icebreaker questions,\" whatever those are."

n "I don't really get the point of all of this, but I guess I've got to play along."

n "Luckily one of the people in my group seems happy to talk about herself at length."

frauke "\"What about you, Erik?\""

erik "\"Huh? What was that, sorry?\""

frauke "\"What's your ideal job?\""

erik "\"Oh, uh... I'm not sure really. I never really think about that.\""

frauke "\"Same here, to be honest.\""

amala "\"I think I'd be an investment banker.\""

n "And investment banker?"

erik "\"Ah, that's interesting.\""

amala "\"Interesting? How?\""

erik "\"I'd have guessed that most people would have chosen something exotic is all.\""

amala "\"Why's that?\""

n "Her tone is getting sharper with each response. Did I mess up?"

erik "\"I, uh, I'm not sure, really.\""

amala "\"Just because we're here doesn't mean we can't do normal stuff you know, Erik.\""

erik "\"Oh, no, that's not what I meant, I-\""

amala "\"What's wrong with wanting to do investments, anyway?\""

n "{i}Crap.{/i}"

erik "\"I'm s-sorry, I misspoke, I...\""

n "{i}Oh man...{/i}"

n "What should I do?"

claes "\"Erik, Amala.\""

#-# >Claes in, frowning
show claes P1_E2:
  xalign 0.2 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.4 alpha 1.0
show claes P1_E2 alpha 1.0
#--#

n "Now I'm in trouble. Great."

claes "\"Amala, I'm sure Erik misspoke, he didn't mean to imply that. Right Erik?\""

erik "\"Right, I'm sorry.\""

n "Amala opens her mouth to respond, but reconsiders for a second."

amala "\"You're right, I'm sorry.\""

#-# >Claes neutral
show claes P1_E1
with Dissolve(0.25)
#--#

claes "\"That's fine Amala, introductions can be stressful for everyone. Are you two okay, now?\""

amala "\"Yeah, I'm okay.\""

erik "\"Yeah. Again, sorry.\""

amala "\"It's fine, man, let's just get on with the introduction stuff.\""

erik "\"Right.\""

#-# >Claes out
show claes P1_E1:
  easein 1.0 xalign 0.6 alpha 0.0
#--#

n "The introductions continue. Frauke likes ham sandwiches, Niklaus wants to be a lawyer and Amala likes swimming in lakes."

n "After a tedious hour of carefully choosing my words, my first period at Saint Dymphna's is over."

n "{i}Thank god{/i}"

#-# >end scene
scene classroom1 at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with Clockwipe
#--#

########

jump A1_08 # jump A?_??
