
label A1_08:
###############

  $ persistent.scene_number = "A1_08" # current scene


# A1_08

# 
# Requirements stolen from another script, will fill in later.
# Backgrounds:
# Dorm Hall
# Bedroom
# Outside Dorm
# Something to do with a bush?

# 
# Sprites:
# Lena
# Irene
# Isolda
# Katja

# 
# Music:
# Schooltheme

# 
# Sound Effects:
# door closing
# 4th wall breaking
# 4th wall reassembles

# 
#-# >Sound of the 4th wall being demolished
todo "{color=#ff8c00}>Sound of the 4th wall being demolished{/color}"
#--#
scene bg black
with Dissolve(2)

show irene U_P1_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.5 yalign -0.3 alpha 1.0
  

irene "\"Hey reader! Just so you know, this scene isn’t going to show up at all in the final game - it exists purely to show off some more sprites we already have for characters that wouldn’t appear in the alpha otherwise. Please enjoy!\""

#-# >4th wall is reassembled. Thanks Trump.
todo "{color=#ff8c00}>4th wall is reassembled. Thanks Trump.{/color}"
hide irene

#--#
scene MainGate
with Dissolve(2)

n "I watch my family as they get into the car and wave one last time. It still feels sort of unreal."

n "Get a hold of yourself, Erik. You’re a grown man."

n "As the car pulls away I take a deep breath and turn, making my way along the path that leads around the side of the school’s main building towards the dormitories."

scene outsidemaledorm
with Dissolve(2)

n "When I get to the steps in front of the boy’s dorm I stop for a moment to take it in, squinting in the sun as I look up at the building."

n "It looks kind of gothic, like a haunted house. Or Hogwarts. Not the sort of place that people actually live in."

n "It’s home now."

n "I head inside."

#-# >Transition to Dorm Interior
todo "{color=#ff8c00}>Transition to Dorm Interior{/color}"
#--#
scene dormhall
with Dissolve(2)

n "The corridor I find myself in has that familiar musty smell that this sort of place always has."

n "What is that? B.O.? Expired milk? Wet dog?"

n "I settle on a combination of all three."

n "Despite the very student-y smell, the place is clearly kept in good condition. Looks like the walls have been repainted recently and the carpet tiles are stain-free."

n "I make my way along the corridor, very aware of my echoing footsteps and the presence of the dorm’s potential inhabitants behind the hall’s many doors."

#-# >Transition to Erik’s Room
todo "{color=#ff8c00}>Transition to Erik’s Room{/color}"
#--#

n "The flight of stairs up to the first floor tires me out more than I’d care to admit. After pausing for a second to catch my breath, I finally reach door number 101, open it, and stand for a moment in the doorway of the uninhabited room."

n "My room. Gotta think of it as my room now. Weird."

scene bedroom
with Dissolve(2)

n "Stepping inside, the door swings shut behind me."

n "I didn’t meet anyone between here and the main building, but hearing the sounds of the dormitory’s other inhabitants from outside the door makes me anxious, as if everyone else is somehow aware of my presence and might barge in and start interrogating me at any moment."

n "I feel like I should have some sort of responsibility at this point, but looking around the room I can’t think of anything I need to do."

n "Everything has already been put away - even the clothes from my suitcase."

n "I slump down onto my neatly-made bed and my gaze lands on a few papers on the bedside table. For lack of anything better to do I pick some up and rifle through them."

n "They aren’t anything very interesting."

n "A leaflet that I’ve already seen. It was mailed to us along with everything else a while ago."

n "Under that, a quaint newsletter that looks as though it’s put together by the students. Nothing too surprising here either, though there are a few pages dedicated to advertising the school’s apparently numerous clubs that catch my attention. Cooking, knitting, anime, track, gaming... Potholing. Bomb construction."

n "Okay, I might have made the last couple up. Still, it sounds like there’s plenty of interesting stuff to do. Maybe I’ll check some of them out at some point. Might as well make the most out of my time here, though I doubt I’ll be running on the track team any time soon."

n "A schedule of upcoming events is next, followed by a map of the grounds - though I already have one of those."

n "Finally, to my surprise, a personal timetable with all my classes. I’d expected that I would’ve had to pick that up in homeroom tomorrow or something. They must really look after you here."

n "All it serves to do is to remind me of what kind of place this is."

n "The timetable tells me that dinner isn’t served until 6pm. Glancing at the clock next to my bed I see I have some time to kill, but no idea how to kill it."

n "For a moment, I consider calling Ela. I mean, she said I could if I needed to."

n "Though... it has only been half an hour. Would that be weird?"

n "It would definitely be weird. I’m at a loss."

n "I look to the laptop set up for me on the desk in the corner. The internet is tempting."

n "But no - I have a whole new school to explore! I mean, I may have only just been given the tour, but who knows what I could find on my own? Looks like it’s time for that walk I pretended to want to go on earlier."

n "Feeling somehow self-conscious about leaving my room less than a minute after I entered it, I head back out."

#-# >Transition to (OutsideDorms)
todo "{color=#ff8c00}>Transition to (OutsideDorms){/color}"
#--#
scene outsidemaledorm
with Dissolve(2)

n "It’s only as I get outside that I realise I left the map behind."

n "Time to find out how much of the tour I remember."

n "The air outside is bracing and autumnal and I inhale it deeply. The forest surrounding the school gives the air a fresh, invigorating smell and the constant whispering of the trees in the slight wind is welcomely calming."

n "There are still a few hours of daylight left, but the shadow cast by the building behind me is growing long."

n "I look across the shadowed lawn to the dormitory opposite."

n "The girls’ dorm. Despite being almost identical to the boys’ it exudes an ethereal quality. What wonders lie within?"

n "I doubt I’ll find out any time soon. Besides, I’m sure there’s some sort of draconian limitation on male access to the place."

n "After all, everybody knows as soon as a man gets within fifty feet of a woman he completely loses control of himself."

n "Nevertheless I decide to head in that direction, thinking I’ll roughly follow the treeline to my left that borders the grounds. I make my way across the lawn between the two dormitories."

scene outsidefemaledorm
with Dissolve(2)

n "In the centre of the lawn are a few benches and a small fountain, whose single lacklustre spout dribbles unimpressively. It pales in comparison to the spectacular water feature in front of the main building - the one the parents see. I wonder how often the students actually congregate here, if ever."

n "As I pass, a few pigeons that I hadn’t noticed pecking around on the floor take flight, rushing into the air towards the forest. My gaze following the birds, I lose sight of them as they vanish beyond the forest’s border. It must be nice to be able to just take flight like that and disappear whenever you want."

n "I wander aimlessly in the direction of the building ahead. I guess when I reach it I’ll just bump off the wall, turn a little bit and keep walking in a straight line until it happens again. Like a Roomba."

n "As I approach the dormitory I feel a great disturbance in the air, as if a cute girl felt a great rage well up inside her that was suddenly silenced."

n "The feeling sends a chill down my spine. Right on cue, the building’s double doors swing open, drawing my attention to the girl emerging from them."

n "Irene. She seems to be in very high spirits. She spots me almost immediately and jogs over across the grass almost skipping in excitement, grinning broadly."

#-# >Ms. Holmes, I presume? (enter Irene)
todo "{color=#ff8c00}>Ms. Holmes, I presume? (enter Irene){/color}"
#--#
show irene U_P1_E2:
  alpha 0.0 xalign 0.0 yalign -0.3
  easein 1.0 xalign 0.5 alpha 1.0

irene "\"Erik, long time no see!\""

erik "\"It’s been, like, 2 hours, tops.\""

irene "\"Still, a lot has happened in that short time. Crime never sleeps.\""

irene "\"Nor do St. D’s students. Well, some of them anyway. Insomnia is rife amongst the mentally ill. It’s like New York, only involuntarily.\""

irene "\"I feel like I’ve become side-tracked. My point is, Katja is pretty mad right now and while I’m not admitting any fault here it’s totally my fault.\""

n "She glances meaningfully up at the first floor window."

irene "\"There’s a reason the windows here are as thick as they are.\""

irene "\"Well, multiple reasons. Fits of manic rage like this one are definitely one of them.\""

erik "\"I wondered what that feeling I got just now was.\""

irene "\"Oh, you felt that too? I thought I might have been the only one. For a moment I felt like I’d made a... I dunno... a mistake making her that mad?\""

irene "\"But nah. It’s all in good fun.\""

irene "\"Anyway, Katja is responsible for her own outbursts, frequent as they are. This is a good one though.\""

erik "\"This can’t be a common occurrence, surely?\""

irene "\"Well, no, I wouldn’t want to sell Katja short. They aren’t that frequent. And don’t call me Shirley.\""

irene "\"But of course, you haven’t met Katja yet, have you?\""

erik "\"No, and with the first impression I’ve been given I feel that I’ve been quite lucky.\""

irene "\"Oh, naaah, she isn’t that bad. Actually, she can be quite fun sometimes.\""

irene "\"I mean, I’m having fun right now!\""

irene "\"That said, I think it’s time I made myself scarce. You know what they say, it’s all fun and games until someone loses your eye.\""

erik "\"That’s… not how that saying goes.\""

irene "\"And I plan on keeping it that way. Try and distract her for me, would you? And history will remember your valiant sacrifice. Probably.\""

erik "\"What?! Irene, hold on, what’s she going to -\""

#-# >The game is afoot (exit Irene)
todo "{color=#ff8c00}>The game is afoot (exit Irene){/color}"
#--#
show irene U_P1_E2:
  alpha 1.0 xalign 0.5 yalign -0.3
  easeout 1.0 xalign 1.0 alpha 0.0
  
n "But I blink and she’s gone. I see the hem of her skirt flitting out of sight around the corner of the girl’s dorm building."

n "My mind fills with blind panic as I hear the the dorm’s doors opening once more."

n "It has to be Katja. Who is this terrible person who can strike fear even into the heart of Irene? For whom such violent rage seems to be commonplace? What kind of a monster am I doing to see emerge from that doorway?"

#-# > Enter Lena
todo "{color=#ff8c00}> Enter Lena{/color}"
#--#
show lena U_M_P1_E6:
  alpha 0.0, xalign 1.0 yalign -0.4
  easein 1.0 xalign 0.5 alpha 1.0

  
n "Dear God. That’s it, I’m dead. I’m not going to survive this."

maskedgirl "\"Yo.\""


n "Death, I embrace - wait, what?"

n "This masked girl doesn’t seem in the least bit like she wants to kill the first person she sees. Something tells me this isn’t Katja."

erik "\"...You aren’t Katja, are you?\""

maskedgirl "\"Haha. No.\""

n "The laugh is totally deadpan."

maskedgirl "\"I can understand why you’d worry about that though. You could hear all that from out here, right?\""

erik "\"Yeah. That, and Irene warned me about her.\""

maskedgirl "\"Oh, you saw Irene? Where’d she go?\""

n "I figure this girl isn’t about to give the game away to Katja."

erik "\"Just round the side of the building there.\""

maskedgirl "\"Thanks. I’m gonna go after her.\""

maskedgirl "\"...You wanna tag along?\""

erik "\"Uh, sure. Why, though?\""

maskedgirl "\"Morbid curiosity. Plus, you don’t want to be around when Katja shows up, do you?\""

erik "\"Well, I dunno, I got kind of mixed messages from Irene. One minute it was all in good fun, the next she was about to be beaten to a bloody pulp.\""

maskedgirl "\"Let’s just assume the bloody pulp thing is more accurate, yeah? Better safe than sorry.\""

erik "\"Fair enough.\""

maskedgirl "\"Name’s Lena.\""

erik "\"Erik.\""

n "We move off around the side of the girl’s dorm."

erik "\"So what happened? Irene honestly made out as if Katja was a harbinger of the apocalypse when she’s in this sort of mood.\""

n "Lena’s laugh is once again very dry."

lena "\"Haha. At its worst, she’s only slightly hyperbolising.\""

lena "\"This was the result of one of Irene’s little investigations.\""

erik "\"Investi -\""

lena "\"Don’t ask. Or, you know, do. But I won’t be able to give you a satisfactory answer. I’ve never been able to get one myself.\""

lena "\"Irene just investigates. It’s her thing.\""

erik "\"Investigates what?\""

lena "\"Good question.\""

n "I feel bad when I catch myself mentally sifting through all the mental illnesses I’m aware of, trying to link one to a knack for investigation."

erik "\"Has she always been like that?\""

lena "\"What, you think it might be a phase? Whatever you do, don’t suggest that to her, she takes it very seriously.\""

lena "\"Besides, she’s been like that for as long as I’ve known her. I don’t think it’s a phase. It’s just what she does.\""

lena "\"Anyway, keep an eye out for her. She likes to play up her vanishing acts, but the truth is she’s probably in a broom closet or something.\""

n "By this point we’re about halfway along the side of the girl’s dorm, passing rows of hedges. No sign of Irene, or anyone else."

erik "\"...So, that’s what Katja as talking about when she mentioned Sherlock Holmes?\""

lena "\"Yep.\""

lena "\"I’m not sure Irene sees the connection, to be honest. I had to warn her.\""

erik "\"I can’t be the only one who thinks that’s a little bit ridiculous.\""

lena "\"Believe me, you’re not alone. Better get used to it if you’re going to be here a long time, though.\""

irene "\"Hey!\""

n "A familiar voice seems to emanate from nowhere. I’d been keeping an eye out for Irene, as had Lena, but hadn’t seen anything."

n "My confusion is resolved immediately, however, as one of the bushes to our left rustles and a face appears from between the leaves."

#-# >Have Irene’s head poking in from the left side of the screen at like a 45 degree angle because comedy
todo "{color=#ff8c00}>Have Irene’s head poking in from the left side of the screen at like a 45 degree angle because comedy{/color}"
#--#
show irene U_P1_E4:
  rotate 45
  alpha 0.0 xalign -1.3 yalign -0.4 
  easein 1.0 alpha 1.0
irene "\"Were you guys talking about me?\""

lena "\"Oh, hi Irene.\""

show lena U_M_P1_E6:
  xalign 0.5
  easein 1.0 xalign 0.7
  
show irene U_P1_E4:
  xalign -1.3 yalign -0.4 
  easein 1.0 rotate 0 xalign 0.2 yalign -0.3

n "Lena doesn’t seem at all surprised to see Irene’s face appear out of a bush. Apparently this is totally normal behaviour, at least for her."

irene "\"...Well?\""

n "She doesn’t look amused."

lena "\"Yes, of course we were talking about you.\""

irene "\"Hmph!\""

irene "\"It’s rude to talk about someone behind their back, you know.\""

lena "\"Is it rude to talk about someone when they’re hiding in a bush a few feet away from you and hearing every word?\""

n "Irene fails to withhold a smile and a chuckle."

irene "\"Okay, you got me. Why are you so interested in the whole Katja thing anyway?\""

lena "\"Eh, nothing better to- wait, shut up a sec.\""

n "I do as I’m told and talk even less than I already was. In the silence, I hear the sound of the dorm building door slamming and somehow, despite the door being a fair distance away and around a corner, ominous, thundering footsteps."

irene "\"Oh crumbs, she’s on her way. You lot had best get in here.\""

erik "\"‘Get in here’?! Irene, you’re inside a - AUCH.\""

n "My voice is cut off as I’m pulled into the bush by my collar."

hide lena U_M_P1_E6

scene inabush
with Dissolve(2)

show irene U_P1_E4:
  xalign 0.5 yalign 0.1 zoom 3.0

#-# >SUPER CLOSE UP OF IRENE lets seem dem freckles
todo "{color=#ff8c00}>SUPER CLOSE UP OF IRENE lets seem dem freckles{/color}"
#--#

erik "\"What the hell, man?\""

irene "\"You’ll thank me later.\""

n "To my surprise, Lena also forces her way into the bush without any persuasion."

#-# >now we’re seeing them BOTH super close up
todo "{color=#ff8c00}>now we’re seeing them BOTH super close up{/color}"
#--#

show lena U_M_P3_E4:
  easein 1.0 xalign 0.0 yalign 0.05 zoom 2.0

show irene U_P1_E4:
  easein 1.0 xalign 1.0 yalign 0.1 zoom 2.0


n "I look at her disbelievingly."

lena "\"You’ll be thanking Irene later.\""

erik "\"I doubt -\""

lena "\"She’s coming, shut up.\""
hide lena 
hide irene


n "I fall silent and strain my ears. From outside the bush, I can hear the sound of heavy footfalls approaching - but, to my surprise, no shouting. Given how angry Katja had been just a few minutes earlier, I would have thought I’d be able to hear her coming from a mile off."

n "Instead, aside from the sound of dull footsteps in the grass, she approaches silently as a trained assassin."

n "The mounting feeling of dread inside the bush is palpable. Our breath seems to hang in the air in clouds and our sweat streaming from our every pore turns to icicles as she draws nearer."

n "Simultaneously we draw a long, slow, silent breath, holding it as she comes into view."

#-# >do the real big visual introduction of Katja right here the sprite isn’t ideal for this situation but i can make it work
todo "{color=#ff8c00}>do the real big visual introduction of Katja right here the sprite isn’t ideal for this situation but i can make it work{/color}"
#--#
todo "KATJA SPRITES?"

scene outsidefemaledorm
with Dissolve(2)

show katja:
  xalign 0.5 yalign -0.3
  
##show Katja

n "Her face is not contorted with rage as I expected it to be. Instead, it is overcome with an expression of forced calm that somehow still looks frighteningly intense."

n "It’s the one visible eye that give it away. A cold dead stare straight ahead, fixated on something in her mind’s eye - as she looks she doesn’t move her eye, instead rotating her entire head."

n "We become somehow even more motionless as she stops by our bush, just a few feet from us."

n "I could swear I hear her smelling the air, as if searching for an olfactory clue of Irene’s location."

n "As she looks around stiffly, her single menacing eye glancing over the bush but thankfully not noticing us, Irene whispers almost imperceptibly."

irene "\"Is this really- \""

lena "\"Shhh!\""

irene "\"- the best place we could have chosen to hide?\""

n "Even Irene seems to understand the gravity of our situation, though - I suspect this is the quietest she has even been."

n "After a few more tense seconds that seem to drag on forever, Katja takes one more suspicious look around and finally moves on."

##hide Katja

n "It strikes me as odd that she chose to stop here in the first place. There’s nothing particularly suspicious about the area. Could she... sense us?"

n "For a few seconds we remain silent, allowing the last vestiges of dread to dissipate."

##back to the bush
##show irene
##show lena
hide katja

scene inabush
with Dissolve(2)

show lena U_M_P3_E4:
  easein 1.0 xalign 0.0 yalign 0.05 zoom 2.0

show irene U_P1_E2:
  easein 1.0 xalign 1.0 yalign 0.1 zoom 2.0

irene "\"...Holy shit that was hot.\""

erik "\"What?\""

irene "\"I mean fun. Not hot.\""

lena "\"She totally gets off on this.\""

irene "\"You have no proof of that.\""

lena "\"But you aren’t going to deny it, are you?\""

irene "\"Well now you’re just being rude.\""

n "Despite the banter, we’re all grinning like idiots."

n "Although I can’t quite see myself getting off to something like that, the thrill of it - being hunted down like that - was kinda fun. At least, something similar to fun. It certainly got my heart racing."

irene "\"Oi Erik, stick your head out and make sure the coast is clear.\""

erik "\"Why me?\""

irene "\"Because I don’t want Katja to kill me, and in the interest of maintaining a healthy relationship with someone who lives in the same building as me I have to pretend I don’t want her to kill Lena either.\""

lena "\"Full points.\""

erik "\"What, and you wouldn’t care if she tore my head off?\""

n "Lena and Irene exchange a quick but meaningful glance before turning back to me."

irene "\"Not as… much?\""

n "Damn it."

n "Steeling myself and inhaling deeply what might be my last breath, I part some of the dense foliage that had been our salvation and expose my head to the dangerous world outside the bush."

#-# >Background: Back outside the bush
todo "{color=#ff8c00}>Background: Back outside the bush{/color}"
scene outsidefemaledorm
with Dissolve(2)
#--#

#-# >and then Isolda appears because it seems as good a time as any to introduce her.
todo "{color=#ff8c00}>and then Isolda appears because it seems as good a time as any to introduce her.{/color}"
#--#
##show isolda

show isolda U_P1_E8:
  xalign -1.3 yalign -0.4 
  easein 1.0 xalign 0.5 yalign -0.3

n "I flinch on impulse and almost retract my head when I see someone outside of the bush - but I quickly realise that it isn’t Katja."

n "I can see both her eyes, for one."

n "She looks shocked for a moment, before her expression shifts to one of concern."

brunettegirl "\"...Hello.\""


n "I’m not sure how to respond, well aware that the rest of my body is still inside a bush."

erik "\"Hi.\""

brunettegirl "\"Why are you in a bu- \""

#-# >Lena and Irene stick their heads out too
todo "{color=#ff8c00}>Lena and Irene stick their heads out too{/color}"
#--#

n "At this point, Lena and Irene decided the coast is clear and make their presence known, sticking their heads out of the bush either side of me."
##show lena
##show irene

show lena U_M_P1_E6:
  xalign 1.0 alpha 0.0 yalign -0.3
  easein 1.0 xalign 0.7 alpha 1.0
  
show irene U_P1_E4:
  xalign -1.3 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.2 yalign -0.3 alpha 1.0
  
n "The girl jumps slightly in shock at the unexpected company."

irene "\"Oh, hey Isolda!\""

n "With narrowed eyes the girl called Isolda looks suspiciously between the three of us."

isolda "\"What were all three of you doing in a bush?!\""

irene "\"Isn’t it obvious?\""

isolda "\"...?\""

n "Isolda’s silence echoes across the the group, clearly not grasping what Irene was implying."

lena "\"We were totally getting it on.\""

n "Irene snorts loudly, unable to contain her mirth."

isolda "\"Getting...what on?\""

lena "\"Oh boy.\""

n "Lena looks disapprovingly at Irene, who is now quietly laughing to herself, her shoulders shaking."

n "Isolda continues to have a look of utter confusion, painfully trying to understand what’s so funny."

lena "(Sigh)"

lena "\"We were hiding from Katja, obviously. Don’t tell me you didn’t hear that whole thing?\""

isolda "\"Oh, that. I did. I just didn’t care about it.\""

lena "\"I thought you were following her or something.\""

isolda "\"I might not care for her outbursts but I’m not stupid.\""

isolda "\"I was actually going to look for Jeanne. Have you all seen her?\""

n "Everyone shakes their head, leaving the girl with an even more pained expression."

isolda "\"I need to find Jeanne. The atmosphere in the dorm is... fractious, to say the least.\""

lena "\"How come?\""

isolda "\"Katja kicked a door down.\""

lena "\"Sounds pretty standard.\""

isolda "\"Not really. It fell against the wall and broke a fire alarm. The sprinklers went off. Everyone’s soaked.\""

n "Irene, who has been laughing to herself the whole time, emits another snort of laughter and pays Isolda some attention again."

irene "\"Really?! I gotta see this. Later!\""

#-# >Irene away
todo "{color=#ff8c00}>Irene away{/color}"
#--#
##hide irene

show irene U_P1_E4:
  xalign 0.2 yalign -0.3 alpha 1.0
  easein 1.0 xalign 1.5 yalign -0.3 alpha 0.0

n "And, flashing a boyish grin in our direction, she heads back to the dorm."

lena "\"Wait, Isolda, did the sprinklers go off in the rooms as well?\""

isolda "\"They did.\""

n "Lena slaps her palm to her forehead."

lena "\"My report! I left it open on my desk!\""

#-# >Lena pls go
todo "{color=#ff8c00}>Lena pls go{/color}"
#--#
##hide lena

show lena U_M_P1_E6:
  xalign 0.7 alpha 1.0 yalign -0.3
  easein 1.0 xalign -.5 alpha 0.0

n "Without a backwards glance, she shoots off in the same direction as Irene about as quickly as I’ve ever seen a human move."

n "I’m left alone with Isolda as we watch the odd couple depart."

erik "\"...Well, this was a great introduction to the school.\""

isolda "\"You’re new?\""

erik "\"You’ve never seen me before, right?\""

n "I can see her now giving another confused expression, before slowly shaking her head at my remark."

isolda "\"Well, I could have forgotten you.\""

n "Before I can cut in and reassure her we’ve never met she continues to talk."

isolda "\"Not that you’re forgettable or anything, I don’t mean to be rude. Though it was quite rude now that I come to think of it. I probably wouldn’t want someone to tell me they could have forgotten me.\""

isolda "\"Being forgotten is bad. But I suppose it could be useful sometimes.\""

isolda "\"And there are a lot of people at this school. It would be easy to forget someone. A lot of potentially hurt feelings, there.\""

isolda "\"Anyway, I’m Isolda. Who are you?\""

n "It takes me a second to process that she had asked me a question."

erik "\"Erik.\""

isolda "\"That’s good.\""

erik "\"It is?\""

isolda "\"I’m never sure what to say when someone tells me their name. ‘Pleased to meet you’ seems so predictable.\""

isolda "\"Anyway, don’t let what had happened with everyone muddy your impression of St. Dymphna’s, okay? Some of us are marginally more normal than that.\""

n "I raise an eyebrow in mock skepticism."

isolda "\"...Marginally.\""

isolda "\"Sorry, I can’t stick around. I need to find Jeanne. See you around, Erik.\""

erik "\"Right. See ya.\""

n "Wait, who’s Jeanne?"

#-# >Isolda fucks off.
todo "{color=#ff8c00}>Isolda fucks off.{/color}"
#--#
##hide isolda
show isolda U_P1_E8:
  xalign 0.5 yalign -0.4 alpha 1.0
  easein 1.0 xalign -0.3 yalign -0.3 alpha 0.0

n "Without any further ado, she departs."

n "It might have been an, eh, eventful introduction to the place, but at least it wasn’t boring."

n "I think I’m gonna like it here."

scene bg black
with Dissolve(2)
show irene U_P1_E4:
  xalign 0.0 yalign -0.3 alpha 0.0
  easein 1.0 xalign 0.5 yalign -0.3 alpha 1.0

#-# >Hostess Irene pops up one last time.
todo "{color=#ff8c00}>Hostess Irene pops up one last time.{/color}"
#--#
##shatter the wall.  again.
irene "\"Wow, Erik, that was a cheesy last line, huh? But wait... breaking the fourth wall is even cheesier! I just made it worse! And is it now even worse that I broke the- uh, what’s the word for the wall that’s in front of the fourth wall? Is there a word for that? Whatever it is, I’ve broken that too.\""

irene "\"Anyway, thanks for reading this tiny, tiny peek into the world of St. Dymphna’s. We’ll see each other again soon!\""

##fade all to black.
hide irene

pause 3.0

##pause
#-# APPEND
# End of Act 1
$config.allow_skipping = False
"{size=24}{color=#FFFFFF}Annaliese=[persistent.a_tot] Isolda=[persistent.i_tot]\nJeanne=[persistent.j_tot] Lena=[persistent.l_tot]\nKatja=[persistent.k_tot] Twins=[persistent.nh_tot]\nAnne-Marie=[persistent.am_tot]{/color}{/size}"
return
#--#

########

jump A1_09 # jump A?_??
