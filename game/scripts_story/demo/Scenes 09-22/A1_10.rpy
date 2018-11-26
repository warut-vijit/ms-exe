
label A1_10:
###############

$ scene_number = "A1_10" # current scene
$ scene_name = "Privet!" # current scene name
$ renpy.save_persistent()


# A1_10
# Scene name: Privet!
# Backgrounds: Classroom, cafeteria
# Sprites: Natalya, Sofiya, Fran, Annaliese
# Music: Natalya Theme, Be Green Afternoon, St. D's Ghost, Formal Meetings Casual Greetings, Be Pious, Ditzy, A Busier Sort of Day
# Sound Effects: Crowd sounds
#-# <#Homeroom>
scene classroomhall
with Dissolve(2)
#--#
#-# >CLASSROOM BG
scene classroom1
with Dissolve(2)
#--#
#-# >CLOCK WIPE TO CLASSROOM BG
#
#--#
#-# >BE GREEN AFTERNOON
play music "music/Be Green (Afternoon).mp3" loop
#--#
köhler "\"Okay, that'll do for today. Make sure to review the notes on the board and we'll have a short quiz on them tomorrow. Au revoir, á demain.\""
n "The sternness on his face unfaltering, the teacher slides a redoubtable pile of books back into his bag, gives us a cursory parting wave, and marches out of the room to take his break."
n "I lean back into my seat and stretch, trying to slough off the heavy blanket of boredom that has begun to fog up my consciousness."
n "My notebook is spotless save for a bunch of flowers I must have doodled at some point. If there was anything I cared about in the lesson, the end-of-class bell must've thoroughly washed it away already."
n "French isn't my favorite subject. I know a fair bit from back home – Mom and Dad were fluent speakers – but while I can't really say I'm awful at it, it's not something I relish studying."
n "The teacher's monotonous droning didn't instill any burning passion to pay any heed either. How someone manages to make learning the language of love such a dreary affair, I'll never know."
n "And so, most of my classmates file immediately out of the classroom, like inmates freshly released from their scholastic prison, their collective chatter filling the air with a garbled mess of sounds."
n "I think I see a few of them throw cautious glances back at me, their faces furrowed, like they're actually considering whether to approach me or not."
n "They soon elect to go for \"not\". They might've decided that I'm not worth the trouble."
n "Fair enough. It's not as if I would know how to respond to them, anyway."
n "I prop my head on my arm and fiddle with my notebook's pages."
n "While the people I've met up to now have each shown their share of peculiarities, the classes themselves were surprisingly, comfortingly normal."
n "We had Math, English, History, among others – same old stuff I knew back home, same old boredom and apathy as I've always felt about them. I don't know what I was expecting, really."
n "Aside from the first period in the relaxation room, it almost does feel just like any other school."
n "Almost being the operative word."
n "I look to my side, and notice the girl sitting beside me finally stirring, rubbing her eyes on her jacket sleeve."
#-# >ST. D'S GHOST IN
#
#--#
#-# >ANNA UNIFORM BUDS P2_E1 FADE IN
show anna U_B_P2_E1:
  xalign 0.45 yanchor 1.0 ypos 1080+425+350 alpha 0.0 zoom 1.3
  easein 1.0 xalign 0.45 alpha 1.0
show anna U_B_P2_E1 alpha 1.0
#--#
n "She sweeps the room with a tentative glance, like a groundhog on the first day of spring, plucking off her earbuds and whipping out her phone."
#-#>ANNA UNIFORM BUDS P1_E4
show anna U_B_P1_E4
with Dissolve(0.25)
#--#
#-# >ANNA UNIFORM NO BUDS P1_E5
show anna U_P1_E5
with Dissolve(0.25)
#--#
n "Don't tell me all she did was listen to music through all of French class?"
n "The teacher didn't really strike me as exceedingly lenient throughout his lecture, so she's either got a lot of guts or was just too bored to care. Can't blame her for the latter, though, if that's the case."
n "Now that I've been reminded of her existence, I find myself in the same internal argument I had this morning: should I continue my attempts at talking to her or cut my losses while I'm ahead?"
n "My efforts to get her to speak back in Math class weren't very fruitful, to say the least. Perhaps that Katja was right – you can't reasonably expect to approach every new person the same way."
#-# >ANNA UNIFORM NO BUDS P1_E3
show anna U_P1_E3
with Dissolve(0.25)
#--#
n "The girl probably noticed me taking glances, as she sinks into her seat, her eyes flitting around the classroom as if desperately searching for an immediate escape route."
#-# >ANNA UNIFORM NO BUDS P1_E4
show anna U_P1_E4
with Dissolve(0.25)
#--#
n "I rummage through my mind for something to strike up a conversation with."
erik "\"Hey, are you feeling okay?\""
n "She doesn't answer, of course, and instead just clutches her sleeves and shifts in her seat."
n "Christ, think of something, Erik. Start with something inoffensive, something to put her at ease. Try to strike a common ground."
n "The weather thing's been done to death already. I've already asked her about music, but even that didn't do wonders for establishing a connection between us."
n "Not that I'd know where to take the discussion on that had it continued, seeing as I'm virtually musically illiterate."
n "Getting more and more anxious by the second, she's now nervously crumpling in her hands what I recognize to be an empty vending-machine sandwich wrapper that had been lying around on her desk."
n "Our gazes meet for a moment, and spurred on by a feeling of urgency I blurt out the first thing that comes to mind."
erik "\"Er, so, what kind of sandwiches do you like?\""
#-# >MUSIC STOP
stop music2 fadeout 5.0
#--#
#-# >ANNA UNIFORM NO BUDS P2_E7
show anna U_P2_E7
with Dissolve(0.25)
#--#
n "The girl's body stiffens as if flash-frozen, and the whole universe screeches to a grinding halt as I realize what just tumbled out of my stupid mouth."
n "The mercifully few people still left in the classroom turn to my direction, and I could hear my very soul shrink back in embarrassment and disappointment."
n "That sounded much better in my head."

n "The intention was to pull off something like what Katja did during lunch, but all this does is make it crystal clear to me that, with handling social encounters, she's ahead by miles – no, {i}lightyears.{/i}"
n "What little colour in the girl's face drains out completely, biting so hard on her lip she could tear it right off. She looks like she'd sooner jump off a balcony than reciprocate my attempt at conversation."
n "She blinks once, twice, as if she can't believe someone would just up and ask such a thing. Truth be told, I didn't expect I'd just up and ask such a thing."
n "I scramble to salvage my dignity."
erik "\"O-Oh, sorry! Just that, that's a vending machine sandwich, isn't it? I just thought...\""
n "The sentence dissolves into nothingness unfinished."
#-#>ANNA UNIFORM NO BUDS P2_E4
show anna U_P2_E4
with Dissolve(0.25)
#--#
n "Her body's tense and rigid like a wooden mannequin, quivering ever so slightly, like I'm the villain in some gory slasher flick, and she's my latest unfortunate victim cornered at the end of a dark alley."
#-# >ANNA SPRITE RISES TO SYMBOLIZE STANDING UP
show anna U_P2_E4:
  easein 0.25 yanchor 1.0 ypos 1080+425 xalign 0.45 alpha 1.0 zoom 1.0
show anna U_P2_E4 alpha 1.0
#--#
n "A humiliating moment of silence trickles by until she lowers her head, a fringe of dark brown hair curtaining her eyes, and stands up, turning her back on me."
#-# >ANNA SLOW EASE OUT RIGHT
show anna U_B_P2_E1:
  easein 3.0 xalign 1.0 alpha 0.0
#--#
n "Feeling utterly defeated, all I could do is watch her as she awkwardly shuffles out of the room, her gait even stiffer than earlier, almost as if her legs had just magically turned to bricks."
n "I mentally slap myself."
n "What was I thinking? Jesus, Erik, you were never this socially inept."
n "But what could I have said, then? What should I have said?"
n "I don't want to feel alone and excluded in this school, but that's very difficult to do when I don't have the flimsiest grasp on how I should handle the people here."
n "I'm an astronaut who's just stumbled into a colony of Martian people, flailing around like an idiot in low-gravity just to convey to them that I've come in peace."
n "Just thinking that leaves me a bitter aftertaste. God, I must sound so condescending right now."
n "Deep breaths. It's the anxiety. My anxiety's getting the better of me once again."
#-# >BE GREEN AFTERNOON 2
play music "music/Be Green (Afternoon).mp3" loop
#--#
voice "\"Pff... hee hee...\""
n "Huh?"
#-# >FRAN UNIFORM P1_E1 FADE IN
show fran P1_E1:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0
show fran P1_E1 alpha 1.0
#--#
n "I turn to the source of the sound, and sure enough, there it is: Fran, the guy from the first period, sitting behind me, clutching at his stomach and mouth, his body quivering so convulsively I thought he was having a seizure."
n "He's on the verge of falling out of their seat trying to contain his giggling, before at last giving in and exploding into a laughing fit so loud I swear it shook the whole room."
#-# >FRAN UNIFORM P1_E3
show fran P1_E3
with Dissolve(0.25)
#--#
fran "\"What the actual hell was {i}that{/i} about?!\""
fran "\"I swear – I {i}swear{/i}– that has got to be the worst pickup line I've ever heard in my life!\""
erik "\"Hey, knock it off!\""
n "He doesn't, at least, not for a while. I think he laughed for a solid minute before even showing any intention of calming down."
n "I was pretty sure he was a guy earlier, but now looking at him--at them?--I'm not quite so sure anymore."
#-# >FRAN UNIFORM P1_E1
show fran P1_E1
with Dissolve(0.25)
#--#
n "Their voice is too high-pitched to be identifiably masculine, but it also has a husky, raspy quality that wasn't quite feminine either."
n "They have a tall, spindly build, with facial features that tread precariously on the line between mild and sharp that you can't tell whether you're supposed to call them pretty or handsome."
n "They're also wearing a female student's jacket and cravat, but it's coupled with long, black trousers."
erik "\"...\""
#-# >FRAN P1_E2
show fran P1_E2
with Dissolve(0.25)
#--#
fran "\"Whoa, whoa there, darling! No need to be so serious! Life's too short to go on living like that!\""
erik "\"Uh...\""
suspiciousperson "\"But oh, man, oh man. Christ on a bike, I needed that laugh.\""
erik "\"Glad to have served, then.\""
#-# >FRAN P1_E5
show fran P1_E5
with Dissolve(0.25)
#--#
fran "\"Oh, c'mon, don't be like that! Jeez, so glum!\""
#-# >FRAN P1_E4
show fran P1_E4
with Dissolve(0.25)
#--#
fran "\"I have to give points to you, though. A lot of people give up on talking to her after the first try. She's, uh, a very skittish person.\""
erik "\"You don't say.\""
#-# >FRAN P1_E1
show fran P1_E1
with Dissolve(0.25)
#--#
suspiciousperson "\"So, uh, is she your type?\""
n "The unexpected question hits me like a piano dropped from the Roche Tower hitting a run-down pinto on the streets of Basel-Stadt on a sultry Sunday morning. My face burns as hot as the resultant fire."
erik "\"What?\""
n "I try to stammer out an answer to shut them up, but my confusion and embarrassment only make their features curl into a thin, mischievous leer."
#-# >FRAN P1_E4 2
show fran P1_E4
with Dissolve(0.25)
#--#
suspiciousperson "\"I can see it in your eyes! Clear as day, as open as a book! I've had years of training, reading people's faces, you know?\""
erik "\"Well, you were reading wrong. I was just trying to start a conversation! Come on, what the hell's wrong with you?!\""
#-# >FRAN P1_E2 2
show fran P1_E2
with Dissolve(0.25)
#--#
n "My frustration leaks into my voice, causing the words to come off more harshly than intended. They fall dead silent, and the room temperature plunges into a nosedive."
n "The bubbly smile drains out of their face, darkening into a cold, horrified stare that sends a twinge of panic up my spine."
n "Should I not have said that?"
n "I should not have said that."
n "Oh, crap."
erik "\"Look, I didn't mean to–\""
n "Before I can finish my sentence, they slap me on the shoulder and burst into hyena-esque laughter again."
#-# >FRAN P1_E4 3
show fran P1_E4
with Dissolve(0.25)
#--#
fran "\"Haha! Gotcha!\""
n "I groan. Well, isn't this quite the life I've gotten myself into?"
fran "\"How was my acting? A thespian miracle worthy of Hollywood, huh? Huh?\""
n "My face curdles into a grimace. I didn't find it nearly as amusing as they did. I decide against rewarding them with a response."
n "That said, should I really even be engaging this... person, to begin with? The impish light in their eyes sends various warning sirens in my head blaring at full volume."
n "I turn away from them and begin packing my things without further comment. I can think of a few better ways to spend my afternoon than being mocked by a stranger."
#-# >FRAN P1_E3
show fran P1_E3
with Dissolve(0.25)
#--#
fran "\"Hey, hey, man! Okay, okay, I get it! No need to get all cranky, now; I understand. Sorry, I didn't mean to sound like a total jerk, alright?\""
#-# >FRAN P1_E1 2
show fran P1_E1
with Dissolve(0.25)
#--#
fran "\"Just a little bit of a jerk.\""
fran "\"Besides, you're too stuffy! You wanna grow up to be like that French teacher dude or something? Sometimes you have to forgive a gentleman her amusements.\""
erik "\"Gentle – what?\""
n "They snap their fingers, and continue on, as if the topic wasn't up for discussion in the first place. They extend a hand to me."
#-# >FORMAL MEETINGS CASUAL GREETINGS IN
stop music fadeout 5.0
play music "music/Formal Meetings Casual Greetings.mp3" loop
#--#
#-# >FRAN P1_E5 2
show fran P1_E5
with Dissolve(0.25)
#--#
fran "\"So! I know we've been introduced earlier, but I'm Fran Dragovic, at your service!\""
fran "\"I'm more of a roast beef sandwich kind of person, but ham and beetroot will do the trick, too. Is that the type you usually fall for?\""
n "They will never let me live this down, will they?"
erik "\"I'm Erik, but you know that already, right?\""
fran "\"Of course! Not every day we get a new face around here! A pretty one, at that! Have you got any idea where you're gonna eat dinner already, Erik? I'm starving here already.\""
fran "\"Cafeteria? Some fancy-ass resto outside campus? Cook your own? Man, I wish I could cook my own food. School grub is very much hit-or-miss here.\""
n "I raise my finger to answer, but retract it when I find I have no clue whatsoever. Also, did they just call me pretty?"
n "As for the topic of dinner, that's... actually a good question. Where, indeed? I know for a fact I can't possibly live my life here subsisting on vending machine sandwiches."
erik "\"I... don't know.\""
#-# >FRAN P1_E4 4
show fran P1_E4
with Dissolve(0.25)
#--#
fran "\"I see! That's perfect! Absolutely perfect! You've gotta come with me!\""
n "Simpering like a used car salesman who's just conned someone into a shady deal, Fran yanks me onto my feet, pulling me after them with such force that I would've tripped on my numb leg had they not caught me by my other arm."
#-# > FRAN P1_E2
show fran P1_E2
with Dissolve(0.25)
#--#
fran "\"Ah! Sorry, love! You okay?\""
erik "\"Yes, yes, it's alright. It's just...\""
erik "\"It's nothing, don't mind it.\""
n "Fran raises an eyebrow, but they loosen their hold on me and decides against inquiring further with a nonchalant shrug."
#-# >FRAN P1_E3 2
show fran P1_E3
with Dissolve(0.25)
#--#
fran "\"Right. After me, then!\""
erik "\"Huh? Where to?\""
#-# >FRAN P1_E5 3
show fran P1_E5
with Dissolve(0.25)
#--#
n "Fran simply begins humming a tune as they waltz out of the room with me in tow. I try to object, but they flagrantly refuse to hear me out."
#-# >FRAN SLIDE OUT RIGHT
show fran P1_E1:
  easein 1.0 xalign 0.0 alpha 0.0
#--#
n "I think of running off, but I figure I'd rather spare myself from another embarrassment. It's not like I can get very far away at any speed they can't beat."
#-# >Music fade out
stop music fadeout 5.0
#--#
n "Needless to say, I have a bad feeling about this."
#-# >clock wipe transition
# done below
#--#
#-# >BE VIOLET IN
play music "music/Be Violet 1.mp3" loop
#--#
#-# >CAFETERIA EXTERIOR BG
scene cafeteriaoutside with Clockwipe
#--#
#-# >FRAN P1_E1 EASE IN FROM RIGHT
show fran P1_E1:
  xalign 0.8 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.6 alpha 1.0
show fran P1_E1 alpha 1.0
#--#
fran "\"And so, voila! Welcome to our destination!\""
n "I scratch my head and sigh. All throughout the five-minute walk my mind was running with possibilities about all the places they could've led me, and absolutely none of them were good."
n "Even provided that I was too anxious to put a foot inside this place earlier today, I guess it's still leagues better than what I had in mind."
erik "\"It's the cafeteria.\""
n "Because of course it would be."
#-# >FRAN P1_E1 3
show fran P1_E1
with Dissolve(0.25)
#--#
fran "\"Haha, what gave it away, Monsieur Poirot? The big sign saying 'St. Dymphna's Cafeteria?' You were thinking I was going to haul you off somewhere dangerous, weren't you?\""
n "At the very least it's not something reprehensible like a secret den for druggies, or the ceremonial grounds of some underground Satanic cult, or a club for Japanese tentacle porn aficionados."
erik "\"Well, kind of? I mean, you don't exactly strike me as a rule-abiding student.\""
#-# >FRAN P1_E4 5
show fran P1_E1
with Dissolve(0.25)
#--#
fran "\"And yet you followed, how naughty! You were thinking I was gonna take you someplace with just the two of us, weren't you? Where we can, you know...\""
erik "\"That I wasn't.\""
fran "\"Bah, you're no fun! Anyway, let's go get some grub already. With all luck, the girls might also be here.\""
erik "\"Girls? Who?\""
n "Ignoring my question for around the 50th time now, Fran pulls me inside the cafeteria."
#-# >CAFETERIA INTERIOR
scene cafeteria
with Dissolve(2)
#--#
n "The warm, inviting smell of food and fruit and the lively chatter of students greet me at the door."
n "Fran stands on their toes and looks around the place, then waves and smiles at someone they seem to have recognized in one of the building's farthest corners."
#-# >FRAN P1_E5 4
show fran P1_E5:
  xalign 0.6 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.6 alpha 1.0
show fran P1_E5 alpha 1.0
#--#
fran "\"Fantastic! There's our seat. But let's get our food first, deal?\""
n "I nod, and we join the queue in front of the counter. Curious, I try to search for whoever it is they were looking at, but the current of moving people obstructs my view."
n "Quite thankfully so, the line moves pretty quickly, and soon enough we're each carrying a tray of food: fruit slices, a glass of juice, and a plate of steaming paella."
n "A simple meal, but I've got to admit, this looks infinitely more appetising than I expected. My stomach rumbles in assent."
n "Fran takes the lead as we weave our way through the still-growing mass of people. We bump into a few students and probably even a teacher or two in her rush, but I'll be damned if Fran cared at all."
n "Eventually, we end up at a booth at the far nook of the cafeteria."
n "Fran waves coolly at its lone occupant: a delicate-looking young woman with short, well-groomed golden hair, sipping a glass of water, fiddling with her phone."
#-# >CG 4 EXPRESSION 1 IN
show CG05E1
with Dissolve(2)
#--#
n "I think she looked a bit tense when she lifted her eyes from her phone to acknowledge Fran, but nonetheless she quietly and gracefully waves back and gestures for us to take our seats."
#-# >FRAN P1_E1 4
show fran P1_E1
with Dissolve(0.25)
#--#
fran "\"Hello, love! What's cooking? I caught our newest victim today! Natalya dear, meet Erik! Erik, meet Natalya, and all that.\""
n "Victim?"
erik "\"Um, uh, hello. I'm new here; first day at school, in fact. Nice to meet you. I'm Fran's classmate; she invited me to have lunch here. I hope I'm not causing trouble.\""
natalya "\"...\""
#-# >CG 4 VARIATION 2
show CG05E2
with Dissolve(2)
hide CG05E1
#--#
natalya "\"Good afternoon, Mister Erik. It is nice to meet you, too. Welcome to cafeteria.\""
n "The greeting, though said with a conspicuous Eastern European accent, is otherwise delivered with lyrical finesse, with an air of uncrackable composure so strikingly distinct from the hubbub of our immediate surroundings."
erik "\"Thanks. And no need to be so formal! Erik is fine.\""
natalya "\"Hm. How so unlucky. I was hoping your name would be Peter.\""
n "Would be what, now?"
erik "\"I'm sorry? Peter?\""
n "She nods, brows knitted in rumination."
natalya "\"It is wasted chance. Wasted chance, yes.\""
erik "\"W-Why?\""
n "Great. First day here, and I run into not just one, but two tall, pretty blondes with a flair for the cryptic within a few hours of each other. I might as well buy a lottery ticket after this."
#-# > NAT THEME IN / PLACEHOLDER: BE VIOLET IN
# already playing
#--#
#-# > CG VARIATION 3
show CG05E3
with Dissolve(2)
hide CG05E2
#--#
natalya "\"Because~ if you were named Peter I could say, 'Hello, Peter! Welcome to caPETERia!\""
n "Or not."
erik "\"... Uhm...\""
n "Her prim, reserved smile breaks and turns into a goofy, childish giggle that shatters my first impression of her so hard I could hear the shards crashing in my mind."
n "What the hell is going on?"
#-# >CG OUT
hide fran
hide CG05E3
#--#
#-# >NAT UNIFORM P1_E9
show natalya U_P1_E9:
  xalign 0.52 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.72 alpha 1.0
show natalya U_P1_E9 alpha 1.0
#--#
natalya "\"Haha! It is funny, yes?\""
n "All I could afford her in my state of utter surprise was a blank, confused stare. That is the last thing I expected to hear from her."
#-# >FRAN P1_E4 6
show fran P1_E4:
  xalign 0.1 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.2 alpha 1.0
show fran P1_E1 alpha 1.0
#--#
fran "\"Nah. That sucked. Two outta' ten.\""
#-# >NAT P1_E10
show natalya U_P1_E10
with Dissolve(0.25)
#--#
natalya "\"Aw... But Sonechka laughed when I told her yesterday...\""
n "A little disappointed by the less-than-rave reception after a few seconds, she snaps her fingers, looking like she just remembered a subject she almost forgot to bring up."
#-# >NAT P1_E8
show natalya U_P1_E8
with Dissolve(0.25)
#--#
natalya "\"Right! Right! More importantly, would you like croissant, Erik?\""
n "Natalya quickly pushes her plate over to my side of the table, her eyes almost sparkling as they lock onto me in expectation."
erik "\"What?\""
erik "\"I mean, thanks for the offer, but what for?\""
natalya "\"Um, ah, well...\""
#-# >NAT P2_E3
show natalya U_P2_E3
with Dissolve(0.25)
#--#
natalya "\"A gift to, um, remember our first meeting by, I guess?\""
erik "\"Huh? Are you really sure?\""
#-# >FRAN P1_E3 3
show fran P1_E3
with Dissolve(0.25)
#--#
fran "\"Uh, Erik?\""
n "Natalya's eyes flit furtively back and forth between me and the cafeteria counter."
n "My concern and suspicion must've shown on my face, since her smile cracks a little bit and her voice becomes tinged with urgency."
natalya "\"No, no, please, I insist! I do this with all my new ac-tain-quances? Acquaintances? That! And now we are acquaintances too, so there!\""
#-# >NAT P2_E7A
show natalya U_P2_E7a
with Dissolve(0.25)
#--#
natalya "\"Also, can you please to eat it right now? Please? Like, quick?\""
n "If this is a hazing or something, it's a very strange one. Maybe I really just got myself into a sketchy cult, after all?"
erik "\"Right now? What?\""
femalevoice "\"Natasha! What're you doing?!\""
n "A voice with a similar, distinctive Russian accent comes approaching from behind us."
#-# >FRAN P1_E5 5
show fran P1_E5
with Dissolve(0.25)
#--#
#-# >NAT P1_E6
show natalya U_P2_E6
with Dissolve(0.25)
#--#
fran "\"Yo, Sofiya!\""
n "I turn my head and find yet another blonde girl standing beside me – quite a bit shorter and has far longer hair, but by no means any less pretty for it."
#-# >SOFIYA P2_E7 SLIDE IN FROM LEFT
show sofiya C_P2_E7:
  xalign 0.2 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.51 alpha 1.0
show sofiya C_P2_E7 alpha 1.0
#--#
n "Her arms are folded in front of her, drumming her fingers on her sleeve,  as she glares at Natalya with an exasperated look, the latter having nothing but a nervous smile for a reply."
#-# >NAT P1_E8 2
show natalya U_P1_E8
with Dissolve(0.25)
#--#
natalya "\"H-Hello, Sis!\""
sofiya "\"You promised me you're to eat better now, right?\""
natalya "\"Yes, but...!\""
#-# >SOFIYA P1_E2
show sofiya C_P1_E2
with Dissolve(0.25)
#--#
sofiya "\"Mum and Dad would to worry if they hear you skip meals again. Surely you do not want that?\""
#-# >NAT P2_E6
show natalya U_P2_E6
with Dissolve(0.25)
#--#
natalya "\"Of course not. I am very sorry, I just...\""
n "Natalya's sister sighs in dismay, her gaze shifting to Fran. The latter puts up their hands in defense."
#-# >FRAN P1_E3 4
show fran P1_E3
with Dissolve(0.25)
#--#
fran "\"Hey! Don't blame me! I was gonna stop him, but Erik accepted it, after all, so it's totally on him!\""
n "Hey! No passing the buck!"
n "But I guess I did {i}almost{/i} accept it, but still..."
#-# >FRAN P1_E5 6
show fran P1_E5
with Dissolve(0.25)
#--#
#-# >SOFIYA P1_E9
show sofiya C_P1_E9
with Dissolve(0.25)
#--#
n "The sister's features begin to soften from annoyance to apology as she acknowledges my presence with a nod and sets her food tray across from me, taking her seat beside Natalya."
n "I lay down the croissant sandwich on the table and clear my throat."
#-# >SOFIYA P1_E1
show sofiya C_P1_E1
with Dissolve(0.25)
#--#
sofiya "\"Hello there, mister. I am hoping my sister was not much trouble for you.\""
erik "\"No, no, not at all. I'm sorry, is there a problem?\""
#-# >SOF P2_E9
show sofiya C_P2_E9
with Dissolve(0.25)
#--#
sofiya "\"Well, how do you say it...\""
sofiya "\"Natasha should not really skip meals right now. It is the, well, what the doctor tells us.\""
erik "\"Ah.\""
n "As expected of a smooth, suave guy like myself, I immediately draw a blank the size of Jupiter as to where to take the conversation from that bit of information."
n "Thankfully, Sofiya takes charge quickly enough, reaching out for a handshake with an airy but perfectly unruffled smile."
#-# >SOFIYA P1_E8
show sofiya C_P1_E8
with Dissolve(0.25)
#--#
sofiya "\"But I'm being rude, no? My name is Sofiya Volkova, Natalya's sister. It is glad to meet you. Your name is...?\""
erik "\"Erik. Erik Wilhelm. Nice to meet you too.\""
#-# >NAT P3_E8
show natalya U_P3_E8
with Dissolve(0.25)
#--#
natalya "\"We're twins, Erik!\""
erik "\"Yeah, well, I sort of figured.\""
#-# >NAT P2_E1
show natalya U_P1_E1
with Dissolve(0.25)
#--#
#-# >SOF P1_E1
show sofiya C_P1_E1
with Dissolve(0.25)
#--#
sofiya "\"Let us eat now, shall we?\""
n "Natalya gingerly pulls back her croissant and sets to work, daintily slicing it with her knife into small pieces, nibbling on each little cut much like a little hamster."
sofiya "\"Do you want some fruit too, Natasha?\""
#-# >NAT P3_E3
show natalya U_P3_E3
with Dissolve(0.25)
#--#
natalya "\"Ah, t-thanks. Alright.\""
n "It doesn't seem like it's alright, but she takes a few slices of apples and tangerines from Sofiya's tray."
#-# >NAT P2_E1 2
show natalya U_P2_E1
with Dissolve(0.25)
#--#
#-# >SOF P1_E5
show sofiya C_P1_E5
with Dissolve(0.25)
#--#
sofiya "\"So you are the new student Fran yesterday said to transfer in his class, I assume?\""
erik "\"Y-Yeah, that would be me, most likely.\""
n "Strange. How Fran got a hold of info about my move here before I even arrived, I'll never know. Is she in cahoots with Irene? It seems kinda likely; their personalities are quite similar."
sofiya "\"I'm not student here myself, but I visit Natasha often to make sure she is doing well.\""
#-# >SOF P1_E9
show sofiya C_P1_E9
with Dissolve(0.25)
#--#
sofiya "\"Will it be hard for Natasha to adjust here, you think?\""
erik "\"I still don't know about that, I've only arrived here yesterday myself.\""
#-# >SOF P2_E4B
show sofiya C_P2_E4b
with Dissolve(0.25)
#--#
sofiya "\"Oh, is that so? That is interesting. You two are in same boat, then.\""
n "Swallowing her food, Natalya arranges her features into a smile and rejoins the conversation, nodding enthusiastically to confirm Sofiya's statement."
#-# >NAT P2_E3 2
show natalya U_P2_E3
with Dissolve(0.25)
#--#
natalya "\"It is very difficult to make many new friends here, especially since we're new.\""
natalya "\"I tried to go lunch with some of my classmates few days ago, but, uh, well, they are plenty nice and friendly, but, when I am with them, uh...\""
natalya "\"How do you say it... I kind of feel like square hole entering round peg.\""
#-# >SOF P2_E6
show sofiya C_P2_E6
with Dissolve(0.25)
#--#
sofiya "\"Other way around.\""
natalya "\"Peg round entering hole square?\""
#-# >SOF P2_E4A
show sofiya C_P2_E4a
with Dissolve(0.25)
#--#
n "Sofiya's palm meets her face, swift as lightning."
sofiya "\"But yes, horrible jokes aside, Natalya is right. It is our first time out of Russia, and we're still a ways to go for learning English, and we do not speak German at all.\""
sofiya "\"Just fitting in is very, insanely difficult. Making new friends, much, much more.\""
n "Huh."
n "Now there's a kindred spirit. In fact, that's exactly what had been bugging me all day, isn't it?"
n "Many of the students here have already had years to get to know each other, hundreds of thousands of moments' worth of experiences shared, and as a result have formed their little, tight-knit groups."
n "Newcomers like us suddenly appearing and forcing ourselves on them would be like dropping a raw ingredient into an already cooked dish. We'll never really belong."
n "From that particular point of view, it's really sad."
#-# >NAT P3_E7B
show natalya U_P3_E7b
with Dissolve(0.25)
#--#
natalya "\"And that is exactly why we newcomers need to support for each other, right?\""
erik "\"Um, right, sure.\""
#-# >NAT P2_E9
show natalya U_P2_E9
with Dissolve(0.25)
#--#
natalya "\"Exactly, Erik understands! So, we should be friends, okay? We can be friends, right? We can hang out at lunch here, talk about things, and even share jokes!\""
natalya "\"I practiced lot of jokes before going here! Wanna hear one? Wanna hear one?\""
n "Somehow, her deep emerald eyes piercing my very soul are telling me that she's going to make me hear the joke anyway, consequences be damned."
erik "\"Uh, shoot away.\""
n "Her face lights up, reminds me of a kid pressing her nose on a shop window looking at the shiny new toy on display."
#-# >NAT P1_E1
show natalya U_P1_E1
with Dissolve(0.25)
#--#
natalya "\"Okay, okay! Here goes, get ready: why is six afraid of seven?\""
erik "\"... Because seven ate nine, right?\""
#-# >NAT P2_E6 2
show natalya U_P2_E6
with Dissolve(0.25)
#--#
natalya "\"O-Oh!\""
n "And just like that, her exhilaration vanishes like a popped balloon."
#-# >NAT P3_E10
show natalya U_P3_E10
with Dissolve(0.25)
#--#
n "She puffs her cheeks out in annoyance, and fixes me with the dourest glare she can muster."
n "It's supposed to be intimidating, I think, but the downright affectedness of the gesture elicits less of abject dread from me and more of an amused chuckle."
natalya "\"But I should be the one giving out punchline, Erik! That is how a joke works!\""
erik "\"Sorry! But it's a really, really old joke, you know?\""
n "It's probably one of the first jokes I heard in English, even."
#-# >SOF P2_E6 2
show sofiya C_P2_E6
with Dissolve(0.25)
#--#
sofiya "\"Don't mind Natasha, Erik. She likes to think she is witty. It helps with her improvement of English... she says.\""
#-# >NAT P1_E4
show natalya U_P1_E4
with Dissolve(0.25)
#--#
natalya "\"But it is funny!\""
#-# >FRAN P1_E4 7
show fran P1_E4
with Dissolve(0.25)
#--#
fran "\"Hey, that's not as bad as her joke last week about giraffes and Rasputin, so maybe we shouldn't be so hard on her, haha!\""
natalya "\"That is true, Sonechka!  It is your fault for not recognizing good joke. You should not be so hard on me! Soft instead!\""
#-# >NAT P1_E8 3
show natalya U_P1_E8
with Dissolve(0.25)
#--#
natalya "\"... because your name is SOFT-fiya!\""
#-# >SOF P1_E7
show sofiya C_P1_E7
with Dissolve(0.25)
#--#
sofiya "\"On the other hand, we should not encourage to this sort of behavior.\""
#-# >NAT P2_E8
show natalya U_P2_E8
with Dissolve(0.25)
#--#
natalya "\"Anyway, Erik! What of you? You have joke of your own?\""
erik "\"W-What? Me? I don't know...\""
#-# >FRAN P1_E1 5
show fran P1_E1
with Dissolve(0.25)
#--#
fran "\"Come on, don't be a buzzkill now, darling! Do me proud! Surely you brought along some of that authentic Swiss humor to share with us, eh?\""
n "Not exactly. The only things I brought here with me in Vienna are crippling anxieties, existential fears, and Mum's totally uncool knitted sweaters."
n "Even so, I rack my brain to recall any joke I could. The first thing that comes up is one I heard Gustav telling Beatrice over breakfast a few years ago."
erik "\"Let's see, well, what did the cheese say when it saw itself in the mirror?\""
#-# >NAT P2_E1 3
show natalya U_P2_E1
with Dissolve(0.25)
#--#
natalya "\"Yes, yes, what?\""
erik "\"Halloumi.\""
n "As expected, for the first few seconds, the joke is received with only lukewarm, polite smiles from Fran and Sofiya."
n "Yeah, just because my life right now feels like a really shitty joke didn't really make me any more of a comedian."
#-# >NAT P2_E9 2
show natalya U_P2_E9
with Dissolve(0.25)
#--#
n "Thankfully, I'm saved from further humiliation by Natalya spontaneously bursting into laughter. Is there anything that doesn't immediately send this girl blasting off to cloud nine?"
n "At first blush, you'd surely peg her as someone graceful and elegant, and that's what I thought, for one."
n "Looking at her now, though, she seems less like a regal young lady, and more like a kid going uptown for the first time."
n "Sofiya, on the other hand, just shakes her head. Being sisters, she's probably had years of experience with this."
erik "\"It's not that funny, I know...\""
#-# >NAT P2_E7B
show natalya U_P2_E7b
with Dissolve(0.25)
#--#
natalya "\"Haha! No, it is not!\""
#-# >NAT P3_E5
show natalya U_P3_E5
with Dissolve(0.25)
#--#
natalya "\"You are not good teller of jokes, Erik.\""
n "Hey, look who's speaking!"
#-# >NAT P2_E9 3
show natalya U_P2_E9
with Dissolve(0.25)
#--#
natalya "\"But you did your best! I praise that.\""
n "She smiles the smile a mother gives her child to encourage him after he had just horribly messed up a test. It only serves to make me more disappointed in my admittedly terrible joke-cracking abilities."
#-# >SOF P2_E1
show sofiya C_P2_E1
with Dissolve(0.25)
#--#
#-# >FRAN P1_E5 7
show fran P1_E5
with Dissolve(0.25)
#--#
sofiya "\"If it is fine to ask, where are you from, Erik?\""
n "Finally, a line of conversation I can get behind."
erik "\"I'm from Switzerland. Basel City, to be exact. Pretty nice place, I guess. And where in Russia are you guys from?\""
#-# >NAT P1_E1 2
show natalya U_P1_E1
with Dissolve(0.25)
#--#
natalya "\"St. Petersburg, yes!\""
natalya "\"But I think it should be called St. Petersberg! You know, like iceberg!\""
natalya "\"... Because very cold!\""
#-# >SOF P1_E2
show sofiya C_P1_E2
with Dissolve(0.25)
#--#
sofiya "\"How is your opinion of Vienna so far, Erik?\""
erik "\"Let's see... my sisters took me sight-seeing around the city yesterday, but I don't think I've seen enough of it to form a solid opinion yet. At least, I guess, it looks really nice. Very lively.\""
#-# >SOF P1_E5 2
show sofiya C_P1_E5
with Dissolve(0.25)
#--#
sofiya "\"We are thinking it an amazing place, also. The food is also very good. I am looking forward to try cooking some of the new dishes I saw here.\""
erik "\"Oh, you're into cooking?\""
sofiya "\"Just little bit.\""
n "There's a glint of pride in her eyes as she says that, so I'll be assuming that her interest, and most likely her experience and skill, in the field is not actually  limited to \"just a bit.\""
#-# >NAT P3_E7
show natalya U_P3_E7a
with Dissolve(0.25)
#--#
natalya "\"You should bring some of your food here too sometime, Sonechka! Is very good! Sonechka's food can send people to heaven, Erik, Miss Fran!\""
#-# >SOF P1_E4A
show sofiya C_P1_E4a
with Dissolve(0.25)
#--#
sofiya "\"Are you saying my cooking is {i}lethal{/i}?\""
n "The affected offense in Sofiya's tone flusters Natalya, who, realising the implications of her previous statement, hurriedly and panickedly stutters out an apology."
#-# >NAT P1_E3
show natalya U_P1_E3
with Dissolve(0.25)
#--#
natalya "\"What? {i}Nyet, nyet{/i}! That's not what I meant! It is really delicious!\""
n "Her embarrassment and subsequent clumsy apology make Sofiya and Fran laugh, and even I soon join in."
#-# >NAT P1_E1 3
show natalya U_P1_E1
with Dissolve(0.25)
#--#
#-# >SOF P1_E1 2
show sofiya C_P1_E1
with Dissolve(0.25)
#--#
#-# >FRAN P1_E5 8
show fran P1_E5
with Dissolve(0.25)
#--#
n "The rest of the lunch goes on pleasantly, as we regale each other with stories of our hometowns and our impressions of Vienna and the school, with Natalya interjecting with the occasional lame joke."
n "I begin to lose track of the time, with only the ringing bell to remind me that lunch break has winded to a close."
#-# >SOF P1_E4A 2
show sofiya C_P1_E4a
with Dissolve(0.25)
#--#
sofiya "\"Ah! There's the bell. We should be going, yes, Natasha? You might miss remedial class.\""
#-# >NAT P3_E3 2
show natalya U_P3_E3
with Dissolve(0.25)
#--#
natalya "\"Aw, see you then, Miss Fran, Erik.\""
#-# >SOF P1_E6
show sofiya C_P1_E6
with Dissolve(0.25)
#--#
sofiya "\"Fran's a boy, silly.\""
#-# >NAT P3_E5 2
show natalya U_P3_E5
with Dissolve(0.25)
#--#
natalya "\"Huh? What're you talking about, Sonechka? Miss Fran is {i}Miss{/i} Fran!\""
sofiya "\"Fran's a boy.\""
natalya "\"A girl!\""
sofiya "\"Boy.\""
natalya "\"But that is not right! Tell Sonechka she's wrong, Miss Fran!\""
n "Fran merely smiles at this little argument, very much entertained."
n "I throw them an inquisitive glance; I've been asking myself that question this whole afternoon, but they haven't really shown any evidence to confirm or disprove either case."
#-# >FRAN P1_E4 8
show fran P1_E4
with Dissolve(0.25)
#--#
fran "\"I dunno. Depends on the weather. You kids be off now, and tell Mr Zhang I said hi!\""
n "Put like that, it doesn't seem they'll be telling us anytime soon. The fox-like grin on their face tells me they're savoring every last drop of our utter bewilderment."
erik "\"Well then, see you later, Sofiya, Natalya.\""
#-# >NAT P2_E1 4
show natalya U_P2_E1
with Dissolve(0.25)
#--#
natalya "\"До свидания, Эрик!\""
#-# >SOF P2_E5
show sofiya C_P2_E5
with Dissolve(0.25)
#--#
sofiya "\"It is very nice meeting you.\""
#-# >Music fade out 2
stop music fadeout 5.0
#--#
n "We give them a wave as we go."
#-# >CAFETERIA BG
#scene cafeteria # still in cafeteria
#with Dissolve(2)
#--#
#-# >A BUSIER SORT OF DAY IN
stop music fadeout 5.0
play music "music/A Busier Sort of Day (Based on St. Paul's Suite by Gustav Holst).mp3" loop
#--#
#-# >SOFIYA, NAT OUT
show sofiya C_P2_E5:
  xalign 0.51 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 1.0 xalign 0.31 alpha 0.0
show natalya U_P2_E1:
  xalign 0.72 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 1.0 xalign 0.52 alpha 0.0
#--#
#-# >FRAN P1_E1 6
show fran P1_E1
with Dissolve(0.25)
#--#
n "Fran turns to me with a wide smile."
fran "\"Now, that wasn't too bad, was it? You've got new friends! A new guy should be out there exploring instead of moping around like a dummy or something, sweetheart!\""
fran "\"You're going to spend nearly a year here; wasting all that time in the dumps might kill you. Yep! Dead as a fly in a cup of morning joe!\""
erik "\"You don't have to speak to me like I'm a child or something. And stop calling me sweetheart.\""
#-# >FRAN P1_E4 9
show fran P1_E4
with Dissolve(0.25)
#--#
fran "\"Roger, honeycakes.\""
erik "\"I... ugh.\""
erik "\"But yeah, you're right. I guess they're not bad at all.\""
n "The answer visibly pleases Fran."
fran "\"Uh-huh, that's the news I wanna hear!\""
n "She pats my back and gives me a devious smile."
fran "\"I see you're still a bit jittery, but don't you worry about a thing, Erik Wilhelm. Trust me, I have a feeling we're gonna have a grand time together.\""
n "That may or may not be so, but my only hope right now is that I come out of this still alive afterward."
#-# >end
stop music fadeout 0.5
#--#

########

jump A1_11 # jump A?_??
