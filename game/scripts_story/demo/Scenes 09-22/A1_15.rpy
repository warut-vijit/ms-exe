
label A1_15:
###############

$ scene_number = "A1_15" # current scene
$ scene_name = "Practice Believing" # current scene name
$ renpy.save_persistent()


# Practice Believing
# Scene name: Practice Believing
#-# <Scene Opens>
scene PitchBlack
with Dissolve(5.0)
#--#
#-# >>Music: Traumen (continuing from A1_14)
#
#--#
#-# >>Several second pause
#
#--#
#-# >>Eyes opening slowly to <Erik's Room (night)>
scene erikdormnight at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/eye.png", 5.0)
#--#
n "I wake up after what feels like far too much time and too little sleep later, swearing into my pillow and wondering groggily just how many times it's been tonight."
n "I thought the nightmares I've been having since this whole mess started were beginning to go away, but tonight's really been something else."
n "Do I dare pick my phone to check the time?"
n "It's not like I really need to. I know that it's late enough to be bad."
n "If not early enough."
n "Seeing just what time it is exactly would just stress me out. If anything, it'd make it harder to go back to sleep."
n "Make it so I couldn't stop thinking about just how much sleep I've missed."
#-# >>Phone mini-CG
show EriksPhone
with Dissolve (2.0)
#--#
n "04:36."
n "The numbers look back it me, calm and defiant, from the blinding, blue glow of the screen."
n "There. Happy now, Erik?"
n "Now you know exactly in what bad shape you are."
#-# >>End Phone mini-CG
hide EriksPhone
with Dissolve (2.0)
#--#
n "This is all so stupid. I've been rolling around like this for hours now and I don't feel like I've had a minute of real sleep."
n "I just keep turning around, waking up from nightmare after nightmare, gasping for air through a flood of childish worries and panic."
n "One time, I sat down to meet Dr. Faber and he told me I'm one of the worst cases he's ever seen and I'm never going to be able to function in society again."
n "In others, I woke up in the middle of a classroom filled with mocking, faceless students, to find that I'd had a seizure in front of everyone and wet myself and screamed something I can't remember."
n "It's probably just the stress. I'm still not used to sleeping in this bed, in this room, with this window and this closet and this ceiling, and it's been so long since I've had to fall asleep the night before a school day. It's not bad or scary so much as strange."
n "At least, it shouldn't be."
n "I think back to the e-mail I read before going to sleep. Dr. Faber wanting to have a meeting with me to \"get to know me better\". He's going to be my counsellor for the rest of the year, so I suppose it makes sense."
n "Yeah."
n "I'm going to have a regular, expert counsellor."
n "I'm going to meet him three times a week, and he's going to frown and nod and tell me to think logically about things while I tell him about my fears. That is, of course, assuming he doesn't just give up on me, like in my dreams."
n "Maybe this really is more than just what I'd like to think of as run-of-the-mill \"first week at a new boarding school\" kind of stress."
n "Still, one way or another, I need to get some rest. I don't want to make a bad impression before I've even really started my life here. Besides, I might miss something important if I go to my first real day of school tired."
n "I'm too sleepy to think properly, but by this point, I'm far too awake to go back to sleep. I just lie on my bed for a few more minutes, face still buried inside my pillow."
n "I'm really sweaty under the sheets. It's not very comfortable."
#-# >>Music: Fade out of "Traumen" over a reasonably long timeframe
stop music fadeout 10.0
#--#
n "..."
n "...."
n "....."
n "Sigh."
n "I'm not going to sleep tonight. Today. Is it \"today\" already? Pretty sure it is. I'm definitely not going to sleep."
n "I sit up on my bed and stretch my sore arms."
n "What now?"
n "School doesn't start for four more hours. No point leaving my room just yet."
n "But what point is there to staying? I'm already done unpacking my stuff, I don't have any real homework right now, and even if I did, I'd be too tired to really handle it."
n "My head aches, and my mouth tastes of sleep despite having not gotten any. I'm sweaty, I'm smelly, and my hair probably looks like something a cat threw up."
n "First order of things should be taking a shower. I pick my glasses up from the nightstand, gather a new set of clothes and head out."
#-# >>Music: The Hero's Theme fades in
play music "<from 0.0 to 162.0627 loop 13.1302>music/The Hero's Theme.mp3" loop fadein 5.0
#--#
#-# <Schoolgrounds Vista (through window, night)> crossfade to <Dorm Corridor (night)>
show dormhallnight
with Dissolve(0.25)
#--#
n "A short while later, I'm already dressed up, clean and presentable."
n "Too bad school doesn't start for at while. What exactly am I supposed to do now? Sit in my room and wait?"
n "I think the common room's still open, but other than making myself some coffee and sitting down on a couch, I don't know what I'd do there, either. I can't turn the television on with everyone else still sleeping, and I haven't brought any books to read."
n "This can't be just my problem, right? Someone must've come up with something at some point."
#-# >>pause
$ renpy.pause (1.0)
#--#
n "My eyes wander quietly over the school grounds past the window."
n "That gives me an idea..."
n "Ela never said they locked the dorms down at night, did she? I mean, it makes sense on the one hand, what with some students possibly wandering off unsupervised, but on the other hand, didn't I think the same thing about the cafeteria? This isn't a prison."
n "I could go for a stroll outside. Get some fresh air, stretch my limbs. Get a hang of the surroundings, if nothing else."
n "It'd be just like old times."
n "I should check this out."
#-# <Dorm Corridor (night)> crossfade to <Dorm Exterior (night)>
show outsidemaledormnight
with Dissolve(0.25)
#--#
#-# >>Sound Effect: Birds tweeting
play sound "music/effects/birdsandwind.ogg" fadein 5.0
#--#
n "What do you know? They really do leave the door unlocked."
n "I step outside and take a big breath of the early morning air."
n "It's moist and frigid, so I cough it all back out a second later, but I'll be damned if it doesn't feel good."
n "With everything that happened, it must've been months since I've been outside like this. Not just free to walk around the backyard of some hospital so the doctors can see how long I can manage, but actually out in the open, by myself."
n "It's so different out at this hour. You can hear the birds and the breeze so clearly."
n "The faint light gives the dorm the air of a scene from a movie."
n "I still can't believe just how ornate that old building is. I should go on a tour of the city sometime – Viennese architecture is amazing. Close to home, but with just enough exotic flourishes to capture the eye."
#-# <Dorm Exterior (night)> crossfade to <Generic School Grounds (night)>
show mainbuildingnight
with Dissolve(0.25)
#--#
#-# >>Sound Effect: Slow footsteps on grass
play sound "music/effects/WalkingGrass.mp3" fadein 5.0
#--#
n "I limp leisurely down the path from the courtyard, rubbing my hands together against the cold and trying to take in as much the surroundings as possible."
n "Sometimes, I think I can make out the silhouette of another student passing by, but it's hard to tell in the darkness."
n "It's a pretty crazy picture, just imagining it from afar. Bunch of boys in pajamas and school uniforms shambling around aimlessly in the middle of the night. Like a scene from a zombie flick."
n "In a different sense, though, it's relaxing. The fact that there are others there means I'm not alone."
n "Sure, I may be weird, but so are they. If you divide it, it's like each one of us is a little less weird on their own."
#-# >>Music: The Hero's Theme fades out
stop music fadeout 5.0
#--#
n "Moving away from the dorms in a wide, winding circle through the campus, I eventually make my way nearly to the school building's doors, before turning back."
n "As I'm about to begin walking, though, my attention is caught by a familiar sound, making me freeze in place."
#-# >>Music: Be Blue fades in
play music "music/Be_Blue.mp3" loop fadein 5.0
#--#
n "Sounding clearly in the empty air is a soft, melodious humming, not the same but vaguely similar to the one I've heard yesterday."
n "I turn around slowly to the find the source. It's faint, but given that I'm hearing it at all, how far could it be?"
#-# <Generic School Grounds (night)> crossfade to <School_Grounds2_Night.png>
scene schoolnight1
with Dissolve(2.0)
$ renpy.pause (1.0)
scene schoolnight2
with Dissolve(2.0)
#--#
n "A few steps past the school corner, I find what I've been looking for."
#-# >Katja_P5_E1 enter from the left to center
show katja U_P1_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show katja U_P1_E5 alpha 1.0
#--#
n "Katja, the girl with the eyepatch from yesterday, is leaning lazily against a garden terrace wall, staring at the ragged horizon stretching behind the lake and humming to herself."
n "She's way louder about it than she was yesterday, sometimes nearly opening her mouth and spelling out words. Maybe she doesn't think there's anyone around."
n "It's sort of cute. Like catching someone singing in the shower."
n "I move more closely –"
#-# >>Music fades abruptly into silence
stop music fadeout 1.0
#--#
katja "\"Good morning, Erik.\""
n "She's not even looking my way."
erik "\"Err –\""
erik "\"Morning –\""
erik "\"I – I mean, sorry, I didn't think you saw me. I mean, I didn't think I'd meet you here.\""
erik "\"I mean, what are you doing here?\""
katja "\"Taking a walk. I do believe this came up in our talk yesterday.\""
katja "\"How about you?"
katja "\" Not working on your stealth skills, I hope.\""
katja "\"My blind side's the whole other way.\""
n "I'm about to start muttering an apology when her expression melts into the same thin smile I saw last time."
#-# >>Music: The Hero's Theme begins to fade back in, slowly
play music "<from 0.0 to 162.0627 loop 13.1302>music/The Hero's Theme.mp3" loop fadein 5.0
#--#
#-# >Katja_P5_E2
show katja U_P5_E2a
with Dissolve(0.25)
#--#
katja "\"Have you decided to try out my idea?\""
erik "\"Well... no. I mean – not specifically. I just thought I'd... go out, or something. You know. Explore around a little bit, breathe some air. Cool my head.\""
erik "\"Maybe it had something to do with what you said yesterday, I don't know. Back of my mind, or something.\""
katja "\"I see. That's good to hear. How do you like it so far?\""
erik "\"It's nice, actually. Really beautiful place, when you don't have to think about making it to dinner in time.\""
erik "\"Crazy cold, though.\""
katja "\"Try putting on something, next time. The winter uniform is a lot fancier than it's warm. Maybe an undershirt?\""
erik "\"I guess. You learn something new every day.\""
n "I want to comment on the fact that Katja herself doesn't seem to be excessively dressed yet barely looks like she's even aware of it, but something tells me she won't take too well to me asking what's under her jacket."
erik "\"You mind if I join you there? It feels weird to be standing like this.\""
katja "\"Not at all. Be my guest\"."
n "She moves a step right and I carefully move in beside her, resting my leg against the wall and hoping I don't look weird standing."
n "I know it's hypocritical, after I've spent half of our last meeting staring her in the eye, but that just makes me feel more self-conscious about it. I don't want her to see me stumbling."
n "After a momentary silence, she turns back to me and speaks."
katja "\"Are you still having trouble sleeping?\""
erik "\"More or less. I'm pretty sure it's just the stress keeping me up. I gave up on trying at some point and thought I'd try a different approach.\""
n "She nods, stifling a little chuckle."
#-# >Katja_P5_E2b
show katja U_P5_E2b
with Dissolve(0.25)
#--#
katja "\"A wise move. You'll do yourself much better that way. Sleep is important, but there's no forcing it when it doesn't come.\""
erik "\"Are you talking from experience?\""
#-# >Katja_P5_E2 2
show katja U_P5_E2b
with Dissolve(0.25)
#--#
katja "\"Mine and others', actually. Almost every student I've ever met here has had trouble sleeping at some point."
katja "\"Insomnia can be a symptom of any number of problems, and the few times it isn't, it could still be a side effect of your medicines.\""
erik "\"... Oh.\""
erik "\"I never thought about it like that. I knew I saw some others while walking here.\""
katja "\"Probably not even all of them. As you've so keenly mentioned yourself, it's little bit cold. Most of the ones who are already up are probably staying inside.\""
erik "\"Can't say I blame them.\""
n "Her face lights up in a mischievous smile."
#-# >Katja_P5_E8
show katja U_P5_E8b
with Dissolve(0.25)
#--#
katja "\"You could still go back if you want to. It's not like I was expecting there to be anyone I could talk to. Maybe you'll catch a couple more hours of sleep. Go on, I won't be angry.\""
katja "\"Just leave me here all by myself with the crickets. Nothing but the sound of my heartbeat and the sorrowful wail of the wind to remind me that I'm still alive. All alone in the dark and the cold, not a soul in the world I could possibly pour my heart out to.\""
katja "\"Forever to keep all the thoughts and the feelings I'm having right now on my mind.\""
katja "\"Go ahead, go back to sleep. Dream of whatever you like. Wake up, go to school. Maybe find another pretty lady to talk to in the small hours of the morning. Maybe you'll never have to think back to this moment and wonder, what if –\""
erik "\"Okay! Okay! Fine. I'll stay with you. Talk about a hard bargain.\""
#-# >Katja_P5_E3a
show katja U_P5_E3a
with Dissolve(0.25)
#--#
katja "\"Talk about an easy sale.\""
#-# >Katja_P4_E8
show katja U_P4_E8
with Dissolve(0.25)
#--#
katja "\"Speaking of which, I think you still owe me lunch from our last meeting.\""
#-# >Music: The Hero's Theme fades out quickly
stop music fadeout 1.0
#--#
erik "\"What?\""
#-# >Music: Library Theme fades in
play music "music/Library Theme.mp3" loop fadein 5.0
#--#
katja "\"Lunch. The meal between breakfast and dinner. Usually eaten at midday.\""
erik "\"I know what a lunch is...\""
katja "\"Then you've recognized I gave up on mine yesterday so I could talk with you. It'd have been rude otherwise.\""
erik "\"Rude? How'd it have been rude? People can talk over food.\""
#-# >Katja_P1_E10
show katja U_P1_E10
with Dissolve(0.25)
#--#
n "Katja looks at me like I've suggested we take our pants off."
katja "\"Not like that! You need a proper seating, and plates, and some drinks to go with it all.  You can't just have any kind of talk you want at any time. That's completely inappropriate.\""
erik "\"But I was eating the whole time yesterday!\""
katja "\"I know! How awful is that? Good thing I'm willing to let bygones be bygones.\""
#-# >Katja_P1_E3a
show katja U_P1_E3a
with Dissolve(0.25)
#--#
katja "\"How does kaiserschmarrn sound? I probably shouldn't have any, but this is a treat, isn't it? With raisins, and plums, and some applesauce on the side...\""
katja "\"It should be alright on a weekend.\""
erik "\"That's... good?\""
katja "\"Wonderful. All's well that ends well. Don't worry too much about it; we can settle your debts at a later date.\""
n "She uses the same formal tone to say it that she did while introducing herself, but her expression is far more relaxed now."
n "I think it's safe to assume that she's joking – and you know what? For a quiet moment out here, standing back and talking about nothing with somebody friendly, I don't even mind. I'll buy them lunch."
#-# >>Music: Library Theme fades out
stop music fadeout 5.0
#--#
erik "\"So... what do you usually do out here when you're up?\""
#-# >Katja_P5_E10
show katja U_P5_E10
with Dissolve(0.25)
#--#
katja "\"Depends on how long I've been up. Mostly, I'm happy just walking and thinking. It's a pretty underrated activity.\""
#-# >>Music: The Hero's Theme fades in slowly
play music "<from 0.0 to 162.0627 loop 13.1302>music/The Hero's Theme.mp3" loop fadein 5.0
#--#
#-# >Katja_P5_E2b 2
show katja U_P5_E2b
with Dissolve(0.25)
#--#
katja "\"If I wake up early enough, like today, I like to go here and wait for the sun to rise. It's gorgeous, if the weather is right.\""
#-# >Katja_P1_E2b
show katja U_P1_E2b
with Dissolve(0.25)
#--#
n "As if to make a point, she lifts her sleeve slightly and takes a quick glance at her watch. Once again, I notice a flash of white gauze on her wrists."
n "Once again, I stop myself from commenting on it."
erik "\"Checking how much time we've got?\""
#-# >Katja_P1_E3a 2
show katja U_P1_E3a
with Dissolve(0.25)
#--#
katja "\"Wouldn't want to miss it.\""
erik "\"Huh. I know that feeling.\""
#-# >Katja_P1_E2a
show katja U_P1_E2a
with Dissolve(0.25)
#--#
katja "\"Really?\""
erik "\"Yeah. I'm actually really into... I mean, I used to –\""
n "Standing outside in that pitch blackness, shivering in clothes. Looking towards the horizon in expectation like we're expecting something other than the very definition of \"regular\"."
n "It reminds me of all those early mornings in Grindelwald or Freiburg, back when Gustav and I went out camping. I'd make a challenge out of trying to wake up before him."
n "Never made it work. No matter what I tried, if I ever went to sleep, he'd be sitting nearby as soon as I've opened my eyes, already fiddling with the burner and brewing coffee. I'm pretty sure he was doing it on purpose."
erik "\" – point is, I like that kind of thing, you know?\""
#-# >Katja_P1_E2b 2
show katja U_P1_E2b
with Dissolve(0.25)
#--#
katja "\"Obviously, no.\""
erik "\"Haha.\""
erik "\"I mean, not specifically the 'waiting for the sun' thing. More of a... general 'outdoors' thing.\""
erik "\"Hiking, trekking, mountain climbing. Geography, too.\""
#-# >Katja_P4_E2
show katja U_P4_E2
with Dissolve(0.25)
#--#
katja "\"A veritable adventurer.\""
erik "\"I guess you could say that.\""
#-# >Katja_P4_E8 2
show katja U_P4_E8
with Dissolve(0.25)
#--#
n "An impish glint flares in Katja's eye."
katja "\"Is that so?\""
erik "\"Yeah. I mean, not on, like, a professional level, or anything. As a hobby.\""
katja "\"I see. Okay, then –\""
katja "\"How about you tell me something I don't know about geography?\""
erik "\"What, like a challenge?\""
katja "\"If you'd like to call it that way. Why? Would it be a challenge?\""
erik "\"Oh, you did not just say that. You better prepare yourself –\""
erik "\"Okay, how about this: Mt. Kilimanjaro is the highest mountain in Africa.\""
#-# >Katja_P4_E8 3
show katja U_P4_E8
with Dissolve(0.25)
#--#
n "She pouts."
katja "\"Do you take me for an ignoramus, sir? I know that much.\""
erik "\"Sure, sure. Just getting started.\""
erik "\"So, like I said, it's the highest mountain in Africa. That makes it one of the Seven Summits, which is a list of the highest mountains on each continent. It's a bit less than 6 kilometers above sea level, which makes it the fourth on that one, right behind Mt. McKinley in North America.\""
erik "\"It's located in the northeast end of Tanzania, near Moshi. It's a dormant, three-cone stratovolcano, and the cones are called Kiba, Mawenzi and Shira.\""
erik "\"The actual summit – that's the highest point on the entire mountain – is called Uhuru Peak, and it's found around what is technically the crater of the Kibo cone.\""
erik "\"The word 'Kilimanjaro' comes from the regional word for 'white', since it snows on it during the rainy season – it's like, one of those places where you don't really have a \"winter\" and \"summer\", just \"dry\" and \"wet\".\""
erik "\"So far so good?\""
#-# >Katja_P4_E10
show katja U_P4_E10
with Dissolve(0.25)
#--#
n "The look on Katja's face is absolutely priceless."
n "It's only once I give it some thought that it dawns on me that I've been grinning like an idiot half the time."
n "It might not be the prettiest or cheeriest smile I've had, but... but it's so {i}genuine{/i}. It feels so {i}real{/i}. I didn't have to force it."
n "It feels so good to do that again. I don't even remember when was the last time I did."
n "It's proud. It's... it's exciting. It makes my stomach turn, but in a good way."
n "I don't want to stop now. I want to keep doing this for as long as Katja would let me."
erik "\"So, how was it so far?\""
katja "\"Is there more?\""
erik "\"Man, I could keep going for hours.\""
erik "\"So hear me out: the two most famous routers to the summit are called \"Marangu\" and \"Machame\", but to most climbers, they're \"Coca-Cola\" and \"Whiskey\". The idea is that \"Whiskey\" is for more experienced types, while \"Coca-Cola\" is for beginners.\""
erik "\"In practice, though, it may not be that much easier since it has a way shorter acclimatization period. So the start is milder but then you end up with breathing difficulties.\""
erik "\"Now, Whiskey, on the other hand, takes about a week to climb up, and –\""
erik "\" – and...\""
#-# >>The Hero's Theme fades out
stop music fadeout 5.0
#--#
n "And the only reason I know that is because until just a couple months ago, I'd planned on one day making it."
#-# >Katja_P4_E5
show katja U_P4_E5
with Dissolve(0.25)
#--#
n "I had a stupid, childish dream of making it. Me and Gustav. All the way up to the summit."
n "Didn't know when I'd get around to it, just that I would. It felt certain."
#-# >>Music: Traumen fades in
play music "music/Traumen.mp3" loop fadein 5.0
#--#
n "And it was certain that Gustav will be there with me."
n "It feels so... infantile, thinking about it right now. Like a child dreaming about what they're going to be when they grow up and thinking they'll be an astronaut. Or a president."
n "Hell, the way I'm now, this is just as silly as if I'd wished to grow up to be a dinosaur."
n "It's meaningless. It's all completely, absolutely meaningless."
n "I let my back sink a bit down the wall."
n "I shift my weight a little bit to the side, trying to calm down, and then catch myself by holding the wall back with one hand."
n "My leg feels like it's made of insects."
n "For a moment, it was like I've almost completely forgotten about it."
n "Now it's gone."
n "Katja stands wordlessly, waiting for me to continue speaking."
n "It takes me a while to realize that her eye's affixed on my leg."
n "How long has it been this way?"
n "I begin moving it on instinct, but then it occurs to me that if she really did somehow notice my limp in the minute or so we were both standing, trying to hide it now would only just make it worse."
n "She opens her mouth to speak, and I can already imagine her face twisting as she tries to find how to politely ask why a wimpy, whiny invalid would ever talk like they planned to climb mountains –"
#-# >Katja_P4_E2 2
show katja U_P4_E2
with Dissolve(0.25)
#--#
katja "\"... Goodness, do I know somebody you'll get along with just fine.\""
n "Huh?"
n "I look up to see if she's kidding. Her smile is as honest and caring as ever."
n "No hint of pity, no disgust, not even confusion."
erik "\"... heh.\""
n "I try to respond, but my throat suddenly feels like I've swallowed an entire sea sponge."
erik "\"What, they're into African trivia or something?\""
#-# >Katja_P1_E3b
show katja U_P1_E3b
with Dissolve(0.25)
#--#
katja "\"Something like that.\""
n "I don't know how to respond to this."
#-# >>Music: Traumen fades out
stop music fadeout 5.0
#--#
n "The tight feeling in my stomach is beginning to fade away. My muscles are still all wound up, and I feel like I'm about to fall, but other than that, it's fine."
n "Could it be that she hadn't noticed after all?"
n "Carefully, not to let go of the chance, I start slightly pushing myself up the terrace wall. If I do this correctly, it wouldn't even look like I –\""
#-# >>Music: the Hero's Theme fades in, slowly
play music "<from 0.0 to 162.0627 loop 13.1302>music/The Hero's Theme.mp3" loop fadein 5.0
#--#
#-# >Katja_P1_E1
show katja U_P1_E1
with Dissolve(0.25)
#--#
katja "\"Please, don't. It's nothing that you should be ashamed of.\""
erik "\"I –\""
erik "\"I know.\""
erik "\"I just didn't think you've –\""
n "She lets out a dry, bitter laugh and raises a finger to point towards her own face."
#-# >Katja_P1_E2a 2
show katja U_P1_E1
with Dissolve(0.25)
#--#
katja "\"Don't you think I know a thing or two about that? You happen to be talking to a bit of an expert here.\""
katja "\"At least you could probably fake walking right if you put enough effort into it. My choice mostly comes down to whether to rip off the eyepatch, and it's not like that'd make stand out less.\""
katja "\"And let me tell you: it's {i}amazing{/i} how fast the novelty wears off of having guys looking at your face for a change.\""
erik "\"It's just that... I thought I was doing fine.\""
#-# >Katja_P1_E1 2
show katja U_P1_E1
with Dissolve(0.25)
#--#
katja "\"I could hear you coming from behind the corner. You have a gait.\""
erik "\"...\""
erik "\"... I guess I do.\""
#-# >Katja_P1_E2b 3
show katja U_P1_E2b
with Dissolve(0.25)
#--#
katja "\"And my point is that I don't mind it, and neither does anyone I can think of that you might like talking to.\""
#-# >Katja_P1_E1 3
show katja U_P1_E1
with Dissolve(0.25)
#--#
#-# >>pause 2
$ renpy.pause (1.0)
#--#
#-# >Katja_P1_E2a 3
show katja U_P1_E2a
with Dissolve(0.25)
#--#
n "She takes another look at her watch. When she looks back up, it's with a face as cheerful as if the subject's never changed."
katja "\"That was pretty impressive. I didn't know most of it.\""
katja "\"It's good for you to have something that you're so passionate about.\""
katja "\"I may not know as much as you about Africa, but I think I might get why you'd like strolling around like that. I used to like going on walks, too. Vienna isn't quite a mountaineering challenge, but it does have some beautiful parks.\""
katja "\"Of course, lately I've been forced to make do with the lawns around here. I'll give it to the faculty – the garden is magnificent, considering the circumstances.\""
katja "\"Have you been to the city of Vienna yet? The city proper, that is. Not the school that's technically in it.\""
erik "\"Just a little bit. I spent a while there before moving in. Why? Were you going to offer me a tour?\""
#-# >Katja_P1_E6
show katja U_P1_E6
with Dissolve(0.25)
#--#
katja "\"Well, I certainly don't anymore. Don't act so smugly about this!\""
#-# >Katja_P1_E3b 2
show katja U_P1_E3b
with Dissolve(0.25)
#--#
katja "\"That said, I still won't mind showing you around some if we ever get to spend a day outside. Assuming you'd be paying, of course.\""
#-# >Katja_P1_E8a
show katja U_P1_E8a
with Dissolve(0.25)
#--#
katja "\"That would be the gentlemanly thing to do.\""
erik "\"Huh. You know, it's not very ladylike of you to ask like this.\""
n "Her cheeks puff in an expression of feigned outrage."
#-# >Katja_P4_E9
show katja U_P4_E9
with Dissolve(0.25)
#--#
katja "\"The gall! You're not helping yourself one bit after yesterday's lunchtime scandal.\""
#-# >Katja_P1_E3a 3
show katja U_P1_E3a
with Dissolve(0.25)
#--#
katja "\"But that's fine. All of it goes on your tab.\""
#-# >Katja_P1_E2b 4
show katja U_P1_E2b
with Dissolve(0.25)
#--#
katja "\"Seriously, though. I think you might enjoy Vienna. Think of it as like the school here, but with more people, better shopping, and less fences.\""
#-# >Katja_P1_E2a 4
show katja U_P1_E2a
with Dissolve(0.25)
#--#
n "For a second, her mouth hangs open, like she was about to add something else, but she seems to close it as soon a she's noticed me looking."
erik "\"I'll keep it in mind.\""
erik "\"For now, though, I should probably start looking into other things to do. I, uh –\""
erik "\"– Let's face it, I'm not doing any hiking any time soon.\""
erik "\"I've looked into joining the newspaper club. Do you know a girl named Lena Forst?\""
#-# >Katja_P1_E10 2
show katja U_P1_E10
with Dissolve(0.25)
#--#
katja "\"You could say that. I did hear something about a new applicant.\""
erik "\"Oh, oka –\""
erik "\" – wait, what?\""
n "This is giving me flashbacks from yesterday's dinner."
erik "\"Why would you hear about that? Who talks about this kind of thing?\""
#-# >Katja_P5_E8a
show katja U_P5_E8a
with Dissolve(0.25)
#--#
katja "\"Small community, Erik. Ladies talk.\""
#-# >Katja_P5_E6
show katja U_P5_E6
with Dissolve(0.25)
#--#
katja "\"Not that there's usually much to talk about.\""
katja "\"With Ms. Forst, at least you know whatever it is, it's bound to be interesting.\""
erik "\"Right. I can... see that. I'll keep that in mind for... uh, you know. Next time the boys and I come back from a hunt, or something.\""
#-# >Katja_P5_E8b
show katja U_P5_E8b
with Dissolve(0.25)
#--#
katja "\"Save some venison.\""
erik "\"Not with this leg, there won't be.\""
n "Seems like as much of an explanation as I'm going to get for now."
n "Might as well, then –"
#-# >>pause 3
$ renpy.pause (1.0)
#--#
erik "\"How about you? In terms of hobbies, I mean. Hobbies, extracurricular activities...\""
katja "\"Avocations.\""
erik "\"Right. I already told you mine, so it's only fair that you tell me a little about yours, isn't it? What do you like to do in your spare time?\""
#-# >Katja_P5_E3a 2
show katja U_P5_E3a
with Dissolve(0.25)
#--#
n "There's a demure smile on her lips, but between the puffed out chest and the proud glint in her eye, she's not fooling anyone."
katja "\"I sing.\""
erik "\"Oh. Like, in a band, or something?\""
#-# >Katja_P5_E6 2
show katja U_P5_E6
with Dissolve(0.25)
#--#
katja "\"A band? Is that the kind of impression I've been making this whole time?\""
#-# >Katja_P1_E3b 3
show katja U_P1_E3b
with Dissolve(0.25)
#--#
katja "\"I sing in the school choir.\""
n "I suppose that does make a lot of sense. It'd explain the humming, and she definitely has the voice for that. I'm not sure if that's the image I'd have had in mind for a choirgirl, but it isn't too far off, either."
erik "\"That does sound a lot more like you.\""
erik "\"Is there anywhere I could hear you perform?\""
n "She blinks an eye in thought."
#-# >Katja_P4_E1
show katja U_P4_E1
with Dissolve(0.25)
#--#
katja "\"Well, we do have the holiday coming up. The choir will be participating both in the opening event and the gala, so I suppose I'll be spending most of the next two weeks somewhere around the chapel.\""
katja "\"It's where the choir practices. Practice, practice, practice. You can never do without enough practice, you know. No matter how good you think you are.\""
#-# >Katja_P5_E1
show katja U_P5_E1
with Dissolve(0.25)
#--#
n "Sounds like a solid plan, if I ever run out of stuff to do. I've been wanting to check out the chapel anyway."
erik "\"I'll be sure to give you a visit sometime. You won't mind it, right?\""
n "I wait for an answer, but none comes."
n "Given that we were just talking, it takes me an embarrassingly long time to realize that Katja's fallen completely silent. Following her gaze towards the lake, I can make out the first glimmers of the sunrise behind the mountains in the horizon."
erik "\"Hey –\""
n "She raises one hand for silence and blurts something out in a tone that sounds almost angry."
#-# >Katja_P5_E5
show katja U_P5_E5
with Dissolve(0.25)
#--#
katja "\"Quiet now. We've waited here all this time; take a deep breath and savor the moment.\""
n "I do as she says, resting back against the wall and holding my breath in silence. For someone who's so against rudeness, she sure knows how to cut a conversation when it suits her."
#-# >Katja out
show katja U_P5_E5:
  easein 1.0 xalign 0.35 alpha 0.0
#--#
n "Above us, the deep purple of the night sky is gradually giving way to a paler shade of blue. Slowly enough that if you looked at it at any one time you won't know it, but by the time you've thought about it, the image changed."
n "I glance aside to Katja to say something, but she look like she isn't with me any longer. For all of how involved she's been so far, now she just stands there, enraptured."
n "Then again, after all this gushing about mountains and sunrises I've done, it's not like I've got any right to talk."
erik "\"You know, I heard looking at the sun rise without protection can hurt your –\""
erik "\"Err.\""
erik "\"Uhm. Nevermind.\""
n "No response. Probably better if she didn't pay attention, in this case."
n "Forgetting about our talk for the time being, I decide to just relax and take-in the view. Protection can go screw itself. I already wear glasses."
#-# >>CG of the sun rising
show CG07
with Dissolve(0.25)
#--#
n "At first, it doesn't look like there's much to see at all. The harder I squint, though, and the more I look at it, the brighter the picture becomes, and the more details are added."
n "First the patch of light rising behind the mountains, surrounding a cold, near colorless sun. Then, with every passing second, more and more rays breaking through and against the thin clouds."
n "When they hit the water just right, you can actually see the reflection of it shining on the far side of the lake. Hilda used to say that it looks like the water's on fire, back when the entire family went walking together. Beatrice said it looked like paint spilling."
n "Hilda told her that sounded stupid, and she said, 'at least I'm being honest.'"
n "Feels like an eternity since then, but I can still imagine that scene. Not just the way it looked, but the entire experience of it. The sounds. The smells. How unusually hot it was, that day."
n "Looking higher up to the sky helps with that. Once you've stretched your neck far enough you can't see the mountains, it's the same old purple and blue whether you're in Switzerland or in Austria."
n "Or... or even Africa."
n "Who's to say that it isn't? So long as you can't see the stars, it's the same sky wherever you're looking."
n "It could be any time. Like life's never changed."
n "I don't know what passes through Katja's mind right now. Hope  she's getting as sentimental as I am. It'd be seriously dorky of me to have been going through this whole thing by myself here."
#-# >>vision blurs
#
#--#
n "Soon enough, the light just gets too bright to look at. My eyes are burning by the time I realize that, and for a good half a minute after I take off my glasses to rub them, all I can see is dancing blotches of green and purple."
#-# >>Fade to black
scene PitchBlack
with Dissolve(0.25)
hide CG07
#--#
#-# >>Slow fade in to <School_Grounds2>
scene schoolground2
with Dissolve(5.0)
#--#
#-# >Katja is already on screen, P1_E2a
show katja U_P1_E2:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show katja U_P1_E5 alpha 1.0
#--#
n "When my vision clears, Katja's already stopped staring, having since moved to checking her watch with a busied expression."
katja "\"So? Was it worth not going back to sleep?\""
n "She lifts her face back to look at me."
label A1_15_menu:
label MENu2:
#-# >Question time
if (persistent.skip_menus):
  "{color=#ff8c00}>Question time{/color}"
  jump A1_15a
menu:
  "\"Absolutely. I didn't even realize how much I missed watching the sunrise.\"":
    $ ig_tot += 1
    $ persistent.A1_15 = 1
    jump A1_15a
  "\"It was. This whole conversation was just what I needed to cheer me up.\"":
    $ kb_tot += 1
    $ persistent.A1_15 = 2
    jump A1_15b
#--#
#-# >CHOICE #1: "I don't know if I'll make a habit of it, but I guess it really was nice." (+1 Isolda)
label A1_15a:
#--#
erik "\"It's... yeah.\""
erik "\"It is beautiful. It's great.\""
erik "\"I'd be honest, I'm not sure if I'd like to do that every morning, but it probably was good that I stayed today.\""
erik "\"I was getting pretty bummed up back in my room just before, and this really took me back to happier times. Cheered me up right when I needed.\""
erik "\"Could've used that sleep, but I guess it's nothing that a few cups of coffee can't handle. Wouldn't be much of an adventurer if that's what it took to break me, right?\""
n "Katja smiles politely, but doesn't say anything. I wonder if I've disappointed her a little by not acting excited enough. It's not like she forced me to stay, but it was pretty much her idea."
n "I hope I didn't make the impression that I didn't like it."
n "With how reserved she's always acting, there's no way to tell what's going through her mind. It'd have been a tiny bit disturbing if she wasn't so nice about everything."
n "Deciding to cheer her back up again, I return the question."
erik "\"How about you? You come here every day?\""
#-# >Katja_P5_E2b 3
show katja U_P5_E2b
with Dissolve(0.25)
#--#
katja "\"No. I specifically said that I didn't. Please try to pay more attention.\""
katja "\"Still, it's a pleasure when I can help it. Sometimes I tell myself I should wake up early more often.\""
katja "\"Like you said, though, it's something to take in moderation. If I'd come here every day, I'd be too tired to work afterwards. Everyone needs to sleep sometime.\""
erik "\"I'll make sure to keep working on that.\""
n "I step forward from the wall and stretch my arms with a tired sigh that evolves halfway through to a yawn. I'm going to feel like a dump by dinner, but screw that. This was a pretty great time."
n "I should definitely keep this in mind for the next time something like this happens. Katja or no Katja, I feel more alive now than I've felt in a while."
erik "\"You want to head over for breakfast in a couple of minutes?\""
katja "\"Thank you, but I'm going to have to decline. I still need to do a few things before classes start, and I'd {i}really{/i} prefer not to be late.\""
erik "\"Okay. Good luck with whatever it is.\""
erik "\"It was really good talking to you.\""
katja "\"It's no problem. You made a good pastime too.\""
katja "\"See you around!\""
#-# >Katja exit to left
show katja U_P1_E1:
  easein 1.0 xalign 0.35 alpha 0.0
stop music fadeout 5.0
#--#
n "I'm about to come up with something to say, but by the time I've opened my mouth she's already given another one of her bows and made off. She moves fast, for a choirgirl."
n "As for myself, I'm going to give the cafeteria another check. Or at least the vending machine."
n "Maybe this might turn out to be an okay day despite the nightmares."
#-# <END>
jump A1_15end
#--#
#-# >CHOICE #2: "Absolutely. Thanks for staying here with me for it." (+1 Katja)
label A1_15b:
#--#
erik "\"Wouldn't have believed that I'd say that an hour ago, but yes. It really was worth it.\""
erik "\"It couldn't have been that long ago, but I can't remember the last time I did something like that.\""
erik "\"Brings back so many memories from before. Got me thinking about all sorts of stuff.\""
erik "\"What's a few hours of sleep compared to that?\""
#-# >Katja_P5_E8a 2
show katja U_P5_E8a
with Dissolve(0.25)
#--#
katja "\"That's the spirit.\""
erik "\"Wouldn't be a mountaineer without it. You won't get anywhere nice if you're not willing to risk hypothermia.\""
n "Katja nods in bemused approval. I think I've made a good impression on her."
n "It kind of makes me want to –"
erik "\"Hey, uhm... I hope it doesn't sound too weird, but, I mean... thanks.\""
erik "\"Like, for having this whole conversation with me.\""
erik "\"Just... standing there, and listening and being all nice and stuff while I'm talking your ear off about mountains.\""
erik "\"Sometimes, just having company can make all the difference. Doesn't even matter what you do with it.\""
erik "\"Not that the sunrise wasn't great, obviously.\""
#-# >Katja_P5E2b
show katja U_P5_E2b
with Dissolve(0.25)
#--#
katja "\"You're welcome. It's nice to know that I've helped.\""
erik "\"Do you do this every day?\""
katja "\"No. I specifically said that I didn't. You should probably find a backup plan for passing the time.\""
katja "\"Just on the off chance you're bored one of these days and I can't be there to assist.\""
#-# >Katja_P5E2a
show katja U_P5_E2a
with Dissolve(0.25)
#--#
katja "\"But I doubt that would be a problem. You've already made other friends, isn't it?\""
katja "\"I'll leave convincing them to go out with you in the morning to talk about mountains to your enterprising acumen.\""
erik "\"Yeah, that might take some figuring out. I'll come up with something eventually.\""
katja "\"Then you'll be alright.\""
katja "\"It's like you said: the company's what really does it. Some mornings, coming out here can be lonely. Sometimes there's nobody friendly.\""
katja "\"It's not always bad, but it's different. It sure isn't always as enjoyable as this one.\""
erik "\"Glad that I wasn't a bother.\""
n "I step forward from the wall and stretch my arms with a tired sigh that evolves halfway through to a yawn. I'm going to feel like a dump by dinner, but screw that. This was a pretty great time."
n "I should definitely keep this in mind for the next time something like this happens. Katja or no Katja, I feel more alive now than I've felt in a while."
erik "\"You want to head over for breakfast in a couple of minutes?\""
katja "\"Thank you, but I'm going to have to decline. I still need to do a few things before classes start, and I'd {i}really{/i} prefer not to be late.\""
erik "\"Okay. Good luck with whatever it is.\""
erik "\"It was really good talking to you.\""
katja "\"It's no problem. You made a good pastime too.\""
katja "\"See you around!\""
#-# >Katja exit to left 2
show katja U_P1_E1:
  easein 1.0 xalign 0.35 alpha 0.0
stop music fadeout 5.0
#--#
n "I'm about to come up with something to say, but by the time I've opened my mouth she's already given another one of her bows and made off. She moves fast, for a choirgirl."
n "As for myself, I'm going to give the cafeteria another check. Or at least the vending machine."
n "This might turn out to be an okay day despite the nightmares."
#-# <END> 2
label A1_15end:
scene PitchBlack
with Dissolve(3)
########

jump A1_16 # jump A?_??
