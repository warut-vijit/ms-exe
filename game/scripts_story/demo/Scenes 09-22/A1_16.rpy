
label A1_16:
###############

$ persistent.scene_number = "A1_16" # current scene
$ persistent.scene_name = "Breakfast and Cramming" # current scene name
$ renpy.save_persistent()


# A1_16
# Scene Name: Breakfast and Cramming
# Bgs:
# Sprites:
# Special Effects:
#-#>open to Cafeteria
scene cafeteria
with Dissolve(2)
#--#
n "Before I knew it, I had already wandered into the cafeteria."
n "Looking around, it’s still almost deserted barring a few early-risers shambling around with their food trays or shifting drowsily in their seats, but that didn’t make it any less lively than it was yesterday."
n "Some are happily chatting over coffee; some are hunched over piles of textbooks and notes; while a group in similarly designed tracksuits over there talks about what I figure to be strategies for some sport."
n "Looks like I’m the only one who’s alone right now."
n "I make my way to the counter. Being as early as it is, there’s still no queue to speak of, and the woman on the other side greets me with a perfectly-rehearsed spiel and a nice, small smile."
lunchlady "\"Good morning! What will you be having today, my dear?\""
n "I scan the counter for choices. I’m not particularly picky with food, so I guess it doesn’t really matter much as long as it’s filling enough. I ask for some pancakes, and a cup of café au lait to go with it."
n "It takes no more than a couple minutes before the server returns with my tray of food. I carefully lift it, only to nearly send its contents flying off when a cold, rasping voice breathes down my neck."
natalya "\"Доброе утро, Erik.\""
erik "\"WHOA!\""
n "I swivel around to face the source of the voice. What hellish beast could’ve produced that unearthly—"
#-#>Nat in, P2_E9, center
show natalya U_P2_E9:
  xalign 0.45 yanchor 1.0 ypos 1080+425+345 alpha 0.0 zoom 1.3
  easein 1.0 xalign 0.45 alpha 1.0
show natalya U_P2_E9 alpha 1.0
#--#
erik "\"N-Natalya?\""
natalya "\"Helloooo. You look to be a bit surprised.\""
n "Natalya gives me a groggy smile, rubbing her eyes on her sleeve. Her hair is sticking out every which way like an unruly patch of crabgrass, eyes barely even half-open."
n "She’s carrying a few books and a notebook under her arm. Her shoulders are drooping, and her gait seems kind of unsteady."
n "The thought that she’s actually sleepwalking occurs to me. Her blazer isn’t even buttoned completely."
erik "\"G-Good morning.\""
erik "\"Not to sound rude, but, uh, shouldn’t you fix the buttons on your uniform, Natalya?\""
#-#>Nat P2_E6
show natalya U_P2_E6
with Dissolve(0.25)
#--#
n "She lets out a feeble \"Oh!\" before trying to button the jacket up with a single hand, with only the faintest blush on her face."
natalya "\"Ah, sorry. I, uh, didn’t notice. Still too sleepy . . . There, all tidy now.\""
n "I wanted to interject how little it improved since she otherwise still looked about as tidy as a Kansas farm freshly ravaged by an EF5 tornado, but I have a feeling she wouldn’t really care."
n "If I had any previous preconceptions of this girl being anything like a proper lady, those have now been blasted to kingdom come."
n "After she gets her breakfast of pancakes and orange juice, we walk over to the same corner of the cafeteria we hung out in yesterday, and take our seats."
#-#>Nat P2_E7a
show natalya U_P2_E7a
with Dissolve(0.25)
#--#
natalya "\"Sorry, Sonechka always fixes my clothes for me… anyway, Erik, how are you?\""
erik "\"Pretty fine . . . ? All things considered.\""
erik "\"I don’t quite think that I’ve already found my footing here yet, but baby steps, I guess? I mean, I checked out the newspaper club yesterday too.\""
erik "\"It’s pretty fun, I think. If I have the time or energy I’ll probably check in for the next meeting.\""
erik "\"Lena was a pretty intense person, but I guess I can work with that.\""
#-#>Nat P2_E9
show natalya U_P2_E9
with Dissolve(0.25)
#--#
n "Her features brighten as she, apparently, recognises the name. She lets out a short laugh."
natalya "\"Oh! The . . . girl with the mask, yes? We are classmates!\""
natalya "\"She is very strange! She even interviewed me when I first came here. She asked me questions and things.\""
#-#>Nat P2_E8
show natalya U_P2_E8
with Dissolve(0.25)
#--#
natalya "\"Lots of questions!\""
natalya "\"But she didn’t let me ask anything in return. I was ready to ask her all about that mask on her face. What do you think is under that mask, Erik?\""
erik "\"The rest of her face, I guess?\""
natalya "\"I wonder about this! Do you think we should investigate? Like Russian spy in action movies?\""
natalya "\"Since I’m Russian, I’m probably good spy, so I think it’s worth trying. Maybe Sofiya is already one, what do you think? Do you think we’ll need to ask her for help?\""
erik "\"... Speaking of her, she’s not here with you today, huh?\""
natalya "\"Nyet! She promised to visit sometime this week, though! She lives in an apartment just a few kilometers away from here! Is it not cool?\""
#-#>Nat P2_E1
show natalya U_P2_E1
with Dissolve(0.25)
#--#
natalya "\"But please do not change the topic! Perhaps we can launch some secret attack into Miss Lena’s room and search for any clue about her magical mask.\""
natalya "\"We need to conduct a raid.\""
#-#>Nat P2_E9
show natalya U_P2_E9
with Dissolve(0.25)
#--#
natalya "\"... a masqueRAID.\""
n "For a few seconds after that, we just exchange unblinking stares. Come on, Natalya. At least try. "
natalya "\"Also, before I forget, Erik! Sorry about yesterday! The croissant, that is. I had flu during weekend and I still didn’t have much appetite.\""
erik "\"Sure, I didn’t really mind...\""
natalya "\"I know! That’s what I said to Sonechka! But she still told me to apologize.\""
erik "\"Well, water under the bridge, then. I’m not sure there was any harm done in the first place, but I appreciate the thought.\""
n "This seems to console Natalya."
n "She runs her fingers over her hair, a token attempt at grooming herself. She lets out a big yawn and stretches, which has the effect of disengaging the top button of her uniform yet again."
n "This time, she fixes it up more quickly, followed by a nearly inaudible groan."
#-#>Nat P2_E7a
show natalya U_P2_E7a
with Dissolve(0.25)
#--#
natalya "\"I might need to buy a new one. Don’t you... think so?\""
erik "\"Uh...\""
n "She sighs."
natalya "\"Lately I feel like life is nothing but suffering, Erik.\""
n "Relief washes over me as I realize she’s dropped the subject of her own accord. But that doesn’t mean I understand what the hell she’s on about now."
erik "\"What brought this about...?\""
#-#>Nat P2_E10
show natalya U_P2_E10
with Dissolve(0.25)
#--#
n "She begins twiddling her thumbs with a nervous smile."
natalya "\"I have some homework due today...\""
erik "\"Ah! I see. So that’s why you’re up early?\""
n "Natalya nods, her eyes not meeting mine."
natalya "\"D-Da. I wanted to review my notes some more before classes start...\""
erik "\"Wow, that’s very diligent of you!\""
n "Maybe I assumed too much from little interaction we had yesterday, but I didn’t think her the type to do that. That’s actually pretty admirable of her."
n "The remark, however, earns me a weird look from her.  She gives me a nervous smile, then scratches the back of her head with an off-sounding giggle."
n "An awkward silence falls between us. Her eyes begin flitting to and fro, sweeping the entire room, but not meeting mine. She idly drums her fingers on the pile of books beside her."
n "Hmmm..."
#-# choice
menu:
    "Don't make a big deal of it.":
        jump A1_16a
    "Ask her what's wrong.":
        $ persistent.nv_tot += 1
        jump A1_16b
#--#
#-# > CHOICE #1: Don’t make a big deal of it.
label A1_16a:
n "Unsure of how to proceed with the conversation, I begin work on my pancakes, while she starts eating hers. Throughout the meal, neither of us expressed any interest in talking any further."
n "She finishes her food ahead of me. Not wasting a second, she gathers her books and notebooks and gives me a bashful smile."
#-#>Nat P2_E1
show natalya U_P2_E1
with Dissolve(0.25)
#--#
natalya "\"W-Well then, I’ll be preparing for school, too. Uh, see you later, Erik.\""
erik "\"Ah, sure. See you later, Natalya.\""
n "She waves in farewell and heads out without looking back."
n "I glance at my watch.  I need to be preparing too."
jump A1_16end
#-# > CHOICE #2:  Ask her what’s wrong. NAT +1
label A1_16b:
n "I’m pretty sure something’s on her mind."
#-#>Nat P2_E6
show natalya U_P2_E6
with Dissolve(0.25)
#--#
natalya "\"H-Huh? No! Nothing...\""
erik "\"You sure?\""
natalya "\"Er, yeah... well...\""
natalya "\"Um, uh, Erik... about the homework...\""
erik "\"Hm?\""
#-#>Nat P3_E3
show natalya U_P3_E3
with Dissolve(0.25)
#--#
natalya "\"Actually... I, uh, last night I... got distracted by this new romance fan fiction I was reading on the Internet, and, well, before I knew it I... have fallen asleep and, well...\""
natalya "\"I forgot about doing it. Gladly I woke up rather early today, but then I, well...\""
natalya "\"...I kinda, sorta, how you say it . . . just forgot the lesson we had yesterday.\""
n "I remember calling her diligent earlier. I take the compliment back."
erik "\"What? How? I mean, don’t you at least have notes?\""
n "She just answers with an awkward giggle and a slow, embarrassed shake of her head."
n "GIVE ME MY COMPLIMENT BACK!"
natalya "\"Um, so...\""
#-#>Nat P4_E8
show natalya U_P4_E8
with Dissolve(0.25)
#--#
natalya "\"Say, would you... help me do my homework? It is just a few questions on Geography. You’re good at this, da? Da?\""
erik "\"Wait, what? How do you figure that?\""
#-#>Nat P2_E9
show natalya U_P2_E9
with Dissolve(0.25)
#--#
natalya "\"You’re wearing glasses. That means you are smart person. I know this much, you know!\""
n "Not... necessarily. But I think she’s not far off the mark this time."
n "Geography is one of the few subjects I consistently had good grades in; I also have atlases and piles of mountaineering magazines back home, mostly gifts from my family and the occasional friend from school."
n "Even so..."
erik "\"Shouldn’t you be-\""
#-#>>Nat P2_E6
show natalya U_P2_E6
with Dissolve(0.25)
#--#
n "Correctly sensing the forthcoming objection, though, she grabs my hands and once again looks at me straight in the eye—wide and beseeching, like a little, lost puppy silently imploring you to bring it back to its mother."
natalya "\"Please?\""
n "Obviously, my resistance barely lasts me a couple of seconds."
erik "\"...Sure, I’d be happy to.\""
#-#>>Nat P1_E9
show natalya U_P1_E9
with Dissolve(0.25)
#--#
n "I guess this is a good enough gesture of gratitude for her company yesterday and this morning. I look at my wristwatch."
n "Still more than an hour before school."
n "I can still make it even if I stay here for a while more, with all luck."
natalya "\"Oh! Oh! Really? Thank you sooooo-\""
erik "\"Promise me two things, though.\""
#-#>>Nat P2_E7a
show natalya U_P2_E7a
with Dissolve(0.25)
#--#
natalya "\"E-Eh? What are . . . those?\""
erik "\"I agree to help you catch up with yesterday’s lesson, but you’ll have to answer your homework on your own.\""
natalya "\"Whaaat?\""
natalya "\"O-Okay, then. Um, the second is...?\""
erik "\"Promise me you’ll study properly starting tomorrow, okay?\""
#-#>>Nat P2_E4
show natalya U_P2_E4
with Dissolve(0.25)
#--#
n "She crosses her arms over her chest and pouts in disappointment."
natalya "\"You are starting to sound like Sofiya, Erik! Are you planning to replace her somehow as my twin sister? You will need a sister licence for that, first!\""
erik "\"What? S-Sister licence?\""
erik "\"I just thought helping you study a bit is the least I can do to thank you for yesterday, you know?\""
#-#>>Nat P1_E1
show natalya U_P1_E1
with Dissolve(0.25)
#--#
n "Natalya’s eyes widen, and her cheeks blossom into a faint, but unmistakable blush. She fiddles with her hair a bit as her features revert to her usual carefree smile."
natalya "\"I... I see. Thank you very much. You are... a very, very nice person, Erik.\""
n "I can’t help but smile at the remark."
erik "\"Uhm, sure, no problem. So! Shall we get started?\""
natalya "\"Da!\""
#-#timeskip
scene PitchBlack with Clockwipe
scene cafeteria with Clockwipe
#--#
#-#>>Nat P2_E2
show natalya U_P2_E2:
  xalign 0.45 yanchor 1.0 ypos 1080+425+345 alpha 0.0 zoom 1.3
  easein 1.0 xalign 0.45 alpha 1.0
show natalya U_P2_E9 alpha 1.0
#--#
natalya "\"Um... the answer should be... uh, the letter C, right? A continental shelf?\""
erik "\"Brilliant! You’re doing very well. Now, how about this problem?\""
n "Natalya’s brows furrow as she tries to crack the next question. I don’t think my last statement was an exaggeration—at least, not by much."
n "She’s actually not all that difficult to tutor, to be honest. She listened well to everything I told her and did everything I asked her to, so she wasn’t much of a problem as long as you kept her concentrated."
natalya "\"Erik, do you think Santa Claus... votes at the North Poll?\""
n "... There are some hurdles in communication, of course."
n "By the time we’re done, there’s only fifteen minutes to go before homeroom."
erik "\"I guess that about wraps it up, huh?\""
n "Natalya looks at her notebook, now full of notes and side-notes we accumulated over our hour-long discussion of landmasses, mountains and seas, and happily nods. "
#-#>>Nat P1_E9
show natalya U_P1_E9
with Dissolve(0.25)
#--#
natalya "\"I guess it does! You’re such a candy, Erik! A lifesaver, is what I mean! Thank you, thank you, thank you!\""
erik "\"The pleasure’s mine.\""
#-#Transition to hallway
scene classroomhall
with Dissolve(1)
#--#
#-#Nat p1_e1
show natalya U_P1_E1:
  xalign 0.45 yanchor 1.0 ypos 1080+425+345 alpha 0.0 zoom 1.3
  easein 1.0 xalign 0.45 alpha 1.0
show natalya U_P2_E9 alpha 1.0
#--#
n "I stand up and stretch. She follows suit, gathering her books.  With that, we walk out of the cafeteria--well, I walked, while she was pretty much bouncing with every step, humming a little tune to herself."
n "I decide to accompany her throughout the walk back until she reaches the girl’s dormitory."
erik "\"So, see you later, then? I need to prepare for school too. I still had quite a few points I would’ve liked to discuss with you there, but man, time flies fast.\""
natalya "\"Okay, I agree. I . . . still have few things to get from my room, too. I must hurry. If time flies fast for you, then it is more for me. Time flies lots faster.\""
erik "\"Oh? Why is that?\""
#-#Nat p2_e9
show natalya U_P2_E9
with Dissolve(0.25)
#--#
n "Natalya tries to bury a chuckle in her hand. She walks up to the building entrance before she turns to me with a coy grin."
natalya "\"... Because I am always Russian.\""
n "I walked right into that, didn’t I?"
#-# >end
stop music fadeout 0.5
#--#

########
label A1_16end:
jump A1_17 # jump A?_??
