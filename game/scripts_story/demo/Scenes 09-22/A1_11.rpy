
label A1_11:
###############

$ scene_number = "A1_11" # current scene
$ scene_name = "Halitosis" # current scene name
$ renpy.save_persistent()


# Halitosis
# Kosherbacon
# Scene name: Halitosis
# 
# BGs:
# School Cafeteria, Erik's Classroom, School Hallway, Newspaper Club Room.
# 
# Sprites:
# Edna, Fran, Hertha, Lena
# 
# Special Effects:
# 
# Music:
# Be Green (Afternoon)
# 
#-# <Scene opens>
#
#--#

#-# >generic school exterior bg
scene school1
with Dissolve(2.0)
#--#

#-# >Fran enter from left to center(Neutral P1E1)
show fran P1_E1:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show fran P1_E1 alpha 1.0
#--#

#-# >School Grounds Theme.mp3 In
play music "music/Be Green (Afternoon).mp3" loop
#--#

n "The sun's already about to set by the time Fran got bored of the cafeteria and dragged me back outside."

n "As if the ruthless teasing right after French class wasn't enough, Fran continues pressing at my comfort levels with conversation."

n "It started as a simple back-and-forth about ourselves, and somehow meandered into an anecdote about losing virginities."

fran "\"So then I decided, if it's going to happen at all, then it needs to be before vacation ends and I have to go back to Vienna.\""

erik "\"Uhuh...\""

fran "\"So me and my best friend at the time, we went around our neighbourhood, hitting up every boy we knew. And you wouldn't believe what happened!\""

erik "\"I have a feeling you're going to tell me...\""

#-# >Fran(Giggling P2E7)
show fran P1_E4
with Dissolve(0.25)
#--#

fran "\"They {i}all{/i} got scared. One boy couldn't even make up his mind, asked for some time to gather up his nerves. I mean really, with two babes, who in their right mind wouldn't want to?\""

n "A grin and a flutter of her eyebrows demand an answer."

n "Fran seems to like putting people on the spot. Either I act disgusted, or envious of all her childhood friends she propositioned. Either way, they get a laugh at my expense."

erik "\"Only an imbecile.\""

n "My correct answer gets me a quick chuckle. At least I didn't go far enough as saying \"Gee, I wish I knew you back then.\" I'm not sure I'd be able to handle the consequences."

erik "\"So then what happened?\""

#-# >Fran(Winking P3E5)
show fran P1_E4
with Dissolve(0.25)
#--#

fran "\"My friend and I decided to take care of things ourselves.\""

erik "\"Oh.\""

n "..."

erik "\"{i}Oh.{/i}\""

n "Fran snorts. {i}That{/i} was the reaction they were hoping for."

#-# >Fran(Neutral P1E1)
show fran P1_E1
with Dissolve(0.25)
#--#

fran "\"So what about you?\""

erik "\"Well, uh. Wait, how long have you been here for again?\""

#-# >Fran(Pouty P1E6)
show fran P1_E3
with Dissolve(0.25)
#--#

fran "\"Oh no you don't. Don't tell me you're still some kissless virgin at this age?\""

erik "\"Sorry, I'd like to keep myself mysterious for now. \""

#-# >Fran(Neutral P1E1) 2
show fran P1_E1
with Dissolve(0.25)
#--#

fran "\"Yep, sounds like something a kissless virgin would say.\""

n "I don't reward them with a reply, knowing anything I say can and will be used against me."

n "The conversation changes direction three or four times as our seemingly aimless stroll progresses, going from mopeds to mobile phones to permanent markers."

n "I may look like I'm following Fran like a lost puppy, but really it's the other way around. They've found a shiny new thing from outside and she's going to get her playtime in while it's still interesting."

#-# >Fran exit right
show fran P1_E1:
  easein 1.0 xalign 1.0 alpha 0.0
#--#


n "I do feel fortunate, though. Making friends can't be easy here, and it wouldn't surprise me if students here tend to avoid making lasting connections."

n "While I'm on a roll, I should try getting to know more people. Someone as energetic as Fran probably gets bored easily, and I'm not totally sure I can survive any more of Natalya's puns, or Irene's... whatever you call that..."


erik "\"Hey, so how often do they collect homework again?\""

fran "\"It depends. I usually just copy down the answers when we review them in class.\""

#-# >Claes in from right to right(Frowning P1E2)
show claes P1_E2:
  xalign 1.0 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.7 alpha 1.0
show claes P1_E2 alpha 1.0
#--#

#-# >Fran move to left(Pouty P1E3)
show fran P1_E3:
  xalign 0.1 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0
show fran P1_E3 alpha 1.0
#--#

claes "\"Ah, Erik, there you are.\""

n "I see Ms. Claes walking up to us, a pile of books under her arm. She tries for a congenial smile, but I think a passing expression of concern flits across her face once she recognizes my companion."

fran "\"Eeeehhh, I'll see you later.\""

#-# >Fran exit to the left
show fran P1_E3:
  easein 1.0 xalign 0.2 alpha 1.0
#--#

claes "\"You too, Fran.\""

#-# >Fran enter from left to left(pouty P1E3)
show fran P1_E3:
  xalign 0.2 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 1.0 xalign 0.25 alpha 1.0
show fran P1_E3 alpha 1.0
#--#

n "Fran tenses up for a moment, takes in a breath, and relaxes their posture in preparation for having to talk herself out of a situation. I get the feeling they exercise this skill often."

claes "\"Mr Wilhelm, I'm pleased to see that you've made friends so quickly.\""

#-# >Claes(Neutral P3E1)
show claes P1_E1
with Dissolve(0.25)
#--#

n "Given her tone, I'm expecting a 'but'."

erik "\"Thank you...?\"."

claes "\"Of course, we're always glad to see our students adjusting well, but it's important you understand the... unique circumstances many of your peers face.\""

n "There's something canned about this line, something well-rehearsed in its delivery."

erik "\"I'm sorry?\""

n "Ms. Claes sighs, then continues with a bit more sincerity."

claes "\"No, I'm the one at fault here. This conversation is something I normally cover prior to the start of the school year.\""

claes "\"It's easy to forget that some students don't respond well to social pressure. Some don't respond at {i}all{/i}. Although we'd like to see these students learn to function in a typical environment, it's not something you can force on them.\""

fran "\"She's saying you need to handle people here with kid gloves.\""

n "Ms. Claes gives Fran a disapproving glance before turning her eyes back to me."

claes "\"{i}In a sentence{/i}, yes. On {i}that{/i} subject, Fran, you could afford to {i}educate{/i} your peers on this rather than make a {i}spectacle{/i} of it. Mr. Kohler had heard of it from your classmates, and he was {i}very{/i} disappointed in your behavior.\""

fran "\"I'm sorry, Ms. Claes. I assure you, it was entirely out of my control this time.\""

erik "\"I'm sorry, but I'm not certain I follow. Am I not supposed to be talking to people?\""

claes "\"Of course not. All I'm saying is to use a little more caution with how you approach people. A few minor observations can go a very long way, and you can always ask your new friends about how best to handle these things.\""

n "Her arms crossed, her gaze slides back to Fran."

claes "\"Can I trust you with that?\""

n "Fran's smile was disconcertingly well-crafted."

fran "\"Of course!\""

n "Ms. Claes's expression tells me she's no more convinced than I am, but apparently it was as far as she was willing to pursue the topic."

claes "\"In any case, you mean well enough, so I'm sure you'll find a balance soon enough.\""

claes "\"With all of that out of the way, there are still a few items left to address. Have you been addressed a student ID yet?\""

erik "\"Um... no?\""

claes "\"You will need to be photographed, then.\""

erik "\"Is it mandatory?\""

claes "\"No, but it is helpful to have some photographic record should something unfortunate happen.\""

n "I wonder if that \"unfortunate something\" she's talking about is finding me face down in the Danube, or what they'd put on wanted posters at the borders."

erik "\"I go to... the front office for that?\""

claes "\"The school newspaper can take care of you. Room 160.\""

#-# >Fran (Neutral P1E1)
show fran P1_E1
with Dissolve(0.25)
#--#

n "Ms. Claes turns her glare towards Fran."

claes "\"Fran, you are still a member of the newspaper club, are you not?\""

fran "\"Yes, Ma'am. How can I be of service?\""

claes "\"It would be appreciated if you could see to it that Mr. Wilhelm makes his way there safely.\""

#-# >Fran (winking P3E5)
show fran P1_E4
with Dissolve(0.25)
#--#

n "Fran snaps their heels together and does a pantomime of a salute with the back of their hand smacking her forehead."

fran "\"Thy will be done!\""

#-# >Claes exit to right
show claes P1_E1:
  easein 1.0 xalign 1.0 alpha 0.0
#--#

#-# >Fran exit to right
show fran P1_E4:
  easein 1.0 xalign 1.0 alpha 0.0
#--#

#-# <hallway(afternoon)>
scene classroomhall
with Dissolve(2)
#--#

n "We exit briskly, as though our teacher would give chase. Friend or not, I'm glad I have someone showing me how to get to where I'm going. Everyone else already knows their way around, and being the new guy, I'll be at a disadvantage for a while."

#-# >Fran enter from left to center(neutral P1E1)
show fran P1_E1:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show fran P1_E1 alpha 1.0
#--#

erik "\"So... you're in the school newspaper?\""

fran "\"I wear many hats, darling.\""

erik "\"Wait, isn't that it there?\""

#-# >Fran(annoyed P1E4)
show fran P1_E4
with Dissolve(0.25)
#--#

fran "\"Oh. We're really going there? {i}I suppose if you have to...{/i}\""

#-# >Fran exit to right 2
show fran P1_E4:
  easein 1.0 xalign 1.0 alpha 0.0
#--#

#-# <newspaperclub(afternoon)>
scene clubroom1
with Dissolve(2)
stop music fadeout 5.0
#--#

#-# >Be Green in
play music "music/Be_Green.mp3" loop
#--#

n "The room that the newspaper club uses doesn't look like it's used for regular lessons."

n "Up against the walls are shelves stocked with tubs of crusty art supplies, posters that have faded to blue over time, and a row of computer terminals. In the centre of the room is a cluster of tables littered with notebooks and pencils."

n "The disorganisation adds flavour to a school that seems too stately for its own good, a breath of fresh air against the Stepford-level neatness of the other rooms. Aside from Fran and myself, I see only three students here, and they don't look like they want to be disturbed."

n "At one of the computers is whom I assume to be the teacher in charge. She looks to be about my sisters' age and smells of strawberries. Well, not like actual fresh strawberries, but the artificial flavouring from strawberry candies."

#-# >Hertha enter from left to center(Annoyed P3E4)
show hertha U_P1_E4:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show hertha U_P1_E4 alpha 1.0
#--#

teacher "\"I really don't know what you did here. Are you sure you didn't mess with the settings?\""

n "A muffled response from somewhere in the room denies responsibility."

teacher "\"Well, save your work and try another computer later. I'll get IT to look at it this weekend.\""

n "The woman shoves the troublesome keyboard away, having decided to make the computer into someone else's problem."

#-# >Hertha(Smile P2E2)
show hertha U_P2_E2
with Dissolve(0.25)
#--#

teacher "\"Oh! Sorry! I was just in the middle of something. How can I help you?\""

#-# >Hertha(neutral P3E1)
show hertha U_P3_E1
with Dissolve(0.25)
#--#

#-# >Hertha move to right
show hertha U_P3_E1:
  easein 1.0 xalign 0.65 alpha 1.0
#--#

#-# >Fran enter from left to left(kissy P3E3)
show fran P1_E4:
  xalign 0.1 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0
show fran P1_E4 alpha 1.0
#--#

fran "\"Special delivery!\""

teacher "\"Oh, you wrote something?\""

#-# >Fran(wink P1E5)
show fran P1_E2
with Dissolve(0.25)
#--#

fran "\"Well, no. Writer's block and all. But I do have something just as good, a new student!\""

#-# >Fran(neutral P1E1)
show fran P1_E1
with Dissolve(0.25)
#--#

teacher "\"Oh! You must be Erik. Am I right?'"

teacher "\"I've read your file. From Ms. Claes's class, right?'"

n "My legend precedes me, apparently."

#-# >Hertha(neutral P1E1)
show hertha U_P1_E1
with Dissolve(0.25)
#--#

wieck "\"I'm Hertha Wieck. And this here is the newspaper and publication club. Are you interested in joining?\""

erik "\"Maybe, but I'm told this is where I can get my photo taken.\""

wieck "\"Of course. We do both ID and yearbook photos. Would you like to do both today?\""

n "Yearbook too? I figured that I missed the chance to be in this year's edition."

erik "\"Yeah, I think I'm as ready as I'll ever be.\""

#-# >Hertha(smile P2E2)
show hertha U_P2_E2
with Dissolve(0.25)
#--#

wieck "\"Great. I'll see if Lena can help you out.\""

#-# >Hertha (Neutral P1E1)
show hertha U_P1_E1
with Dissolve(0.25)
#--#

#-# >Fran(concerned P1)
show fran P1_E3
with Dissolve(0.25)
#--#

n "Fran suddenly checks her phone to see if they have an excuse to leave, and they pretend to have found one."

#-# >Fran (annoyed P1E4)
show fran P1_E4
with Dissolve(0.25)
#--#

fran "\"Well, love, that's my cue to go.\""

n "Fran hastily scribbles down a number on a scrap of paper nearby and tosses it to me."

fran "\"Text me if you need rescueeeee!\""

#-# >Fran fast exit to right
show fran P1_E4:
  easein 0.25 xalign 1.0 alpha 0.0
#--#

erik "\"Uh, well, okay.\""

n "It's strange to see Fran take off so abruptly after clinging to me most of the afternoon. Either they just hit their boredom threshold, or something got them spooked."

n "I look around to see if any of the other students are Lena, but Ms. Wieck isn't heading over to talk to any of them."

n "Instead, she turns to a desk just beyond a line of cabinets and addresses a spindly pair of booted legs sticking out from under the desk."

wieck "\"Lena, we have a new student here. Would you take care of him, please?\""

n "Lena's legs lay motionless for a moment, pretending to have not heard Ms. Wieck. They eventually stir to life when it becomes clear that I'm not going away."

#-# >Lena(Neutral) enters up from bottom
show lena U_M_P3_E8:
  xalign 0.03 yanchor 1.0 ypos 1080+425+600 alpha 0.0
  easein 1.0 ypos 1080+425 xalign 0.23 alpha 1.0
show lena U_M_P3_E8 alpha 1.0
#--#

#-# >Music fades out
stop music fadeout 3.0
#--#
#-# >Music: Big Bad Wolf starts
play music "music/Big Bad Wolf.mp3" loop
#--#

n "Her joints pop and crack as she unfolds into a standing position. Lena's arms swing around to stretch and her head lazily circles around to so she could make sure it's attached correctly."

n "Lena's almost as tall as I am, built with long legs and a skinny, nearly-flat torso. If it wasn't for her name, I probably would have mistaken her for a boy."

n "Looks like she works out as well, based on her tan and broad shoulders."

#-# >CG_06_01 starts (crossfade)
show CG06E1
with Dissolve (1.0)
#--#

n "And then... there's that {i}mask{/i}. It's a fitted, metal device, with a small opening for her mouth, but not a whole lot of room for much else."

n "I'm trying really hard not to stare at the mask, but I can't help it. Is it protective gear for something she was doing inside the cabinet?"

n "No, I don't see any sort of filtering element, and the mask looks as bespoke as it does functional. Maybe it's a mouth guard for some sport, like ice hockey or boxing? Maybe she just drools a lot."

n "Or maybe she bites."

n "She shakes the drowsiness out of her system and locks her piercing green eyes at me."

erik "\"Hi. I'm Erik.\""

n "She snorts."

lena "\"So I've heard.\""

erik "\"I just started today.\""

n "She gives me a quick once-over, assessing my \"new student\" status."

lena "\"{i}Sprichst du Deutsch?{/i}\""

erik "\"{i}Un peu.{/i}\""

#-# >CG_06_02
show CG06E2
with Dissolve (0.25)
hide CG06E1
#--#

n "Lena's brow crinkles and she sighs. Well, {i}I{/i} thought it was funny."

n "She picks up a folder stuffed with loose papers off the counter and hands it to me."

lena "\"I want the English ones translated into German and the German ones translated into English. And the French ones in the trash.\""

wieck "\"Actually, Erik is here to get his photos taken.\""

#-# >CG_06_01
show CG06E1
with Dissolve (0.25)
hide CG06E2
#--#

lena "\"Don't do it. The cameras here will steal your soul. We'd get that fixed but the warranties are expired.\""

wieck "\"I would greatly appreciate it if you could help me with that while I sort out the mess with the computers.\""

lena "\"Okay, but it will cost you. Dearly.\""

#-# >Crossfade back to original classroom setup, with Hertha(Neutral) on right, Lena(Neutral) in the center
hide CG06E1
with Dissolve (1.0)
#--#

#-# >Hertha exit to right
show hertha U_P3_E1:
  easein 1.0 xalign 1.0 alpha 0.0
#--#

n "The two of us go over to Ms. Wieck's desk and Lena drags out one of those stands that hold up projector screens. She draws down a bland looking backdrop with a mottled blue and white cloudy pattern."

n "I take my place in front of the background and Lena shoves me around by the shoulders before screwing a rather beat-up looking camera onto an equally worn looking tripod."

#-# >Lena(Neutral with camera P4E1)
show lena U_M_P4_E1
with Dissolve(0.25)
#--#

lena "\"Kay. First up is your ID card. Say 'whiskey.'\""

erik "\"Whiskey!\""

#-# >>click
play sound "music/effects/cameraclick.ogg"
#--#

#-# >Lena move to right
show lena U_M_P3_E1:
  easein 1.0 xalign 0.7 alpha 1.0
#--#

#-# >Hertha enter from left to left(concerned P2E5)
show hertha U_P2_E5:
  xalign 0.15 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.35 alpha 1.0
show hertha U_P2_E5 alpha 1.0
#--#

lena "\"And now for the yearbook.\""

wieck "\"Oh no no no no no no. You can do better than that!\""

erik "\"Is there something wrong?\""

wieck "\"Obviously! Nobody ever uses that backdrop for their {i}good{/i} photos. Do you really want the most important photos of your life having you look like a square?\""

#-# >Hertha (concerned P1E5)
show hertha U_P1_E5
with Dissolve(0.25)
#--#

erik "\"Well, I don't mind.\""

n "Ms. Wieck wrestles an old yearbook out of a tightly packed bookshelf and cracks the stiff, seldom-turned pages open on the desk in front of me."

wieck "\"Here. Most people opt for casual photos.\""

lena "\"Actually, most people opt out entirely. I did.\""

wieck "\"Shush. Your picture is included this year.\""

#-# >Lena(Annoyed with camera P4E4)
show lena U_M_P4_E4
with Dissolve(0.25)
#--#

lena "\"Over my objections and without my consent. My dad is a lawyer and he'll have your head for this violation of my civil rights.\""

wieck "\"{i}Your father{/i} purchased a yearbook along with school portraits and that's what he's going to get. He wants to see how lovely his offspring has become, and last I checked, he was an architect.\""

#-# >Lena(Neutral with camera P4E1) 2
show lena U_M_P4_E1
with Dissolve(0.25)
#--#

n "Indeed, the majority of yearbook photos appear to have been taken at various outdoor locations around the school, with the students out of uniform."

n "A few do pose in front of the backdrop, but they make up for the blandness with some special outfit like an athletic uniform or academic medals."

n "I would've been the plainest photo in the book."

#-# >Hertha(smile P1E2)
show hertha U_P1_E2
with Dissolve(0.25)
#--#

wieck "\"See, now don't these look better?\""

n "Flipping along, I find a plain page near the end with scores of faceless names crammed into sections by year. The print is so small that it's clear that the need for saving printing costs outweighed the desire to have a dozen pages dedicated to students who were unable or unwilling to show up for picture day."

wieck "\"So how about you two go off somewhere nice for Erik's picture? Who knows, you might even find a friend.\""

lena "\"Actually, the school pharmacist says I don't need 'friends' on my prescription any more. It turns out they give me a rash.\""

n "Ms. Wieck dismisses Lena's rebuff of any future association between us and hands her an expensive looking camera from inside her locked desk. My picture is apparently a special occasion that warrants the use of the {i}good{/i} camera and not one of the heaps off the shelf."

erik "\"Should I change?\""

n "I ask, seeing that most of the examples I was shown were out of uniform."

wieck "\"I would appreciate that. Everyone knows what the uniform looks like, so there's no need to remind everybody with every single portrait.\""

n "Hertha turns her attention to Lena."

#-# >Hertha(neutral P1E1) 2
show hertha U_P1_E1
with Dissolve(0.25)
#--#

wieck "\"Make sure he puts on something nice, okay?\""

lena "\"I'll just meet you in the courtyard in twenty.\""

#-# >Lena Out
show lena U_M_P4_E1:
  easein 1.0 xalign 0.0 alpha 0.0
#--#

#-# >Music fades out 2
stop music fadeout 3.0
#--#
#-# >Music: Be Green starts
play music "music/Be_Green.mp3" loop
#--#

n "Lena dismisses herself, giving me an opportunity to size up the situation here."

erik "\"Ms. Wieck?\""

#-# >Hertha(smileP1E2)
show hertha U_P1_E2
with Dissolve(0.25)
#--#

hertha "\"Please, call me Hertha.\""

erik "\"So, the school newspaper...\""

hertha "\"Would you like to know more?\""

erik "\"Yeah. I'm curious about what kind of activities I could do once I get settled in here.\""

hertha "\"Well, we'd love to have you around, as long as it doesn't interfere with your studies. As far as clubs go, we're actually pretty flexible.\""

student "\"Uh. I have to go now.\""

#-# >Hertha(neutralP1E1)
show hertha U_P1_E1
with Dissolve(0.25)
#--#

n "I hadn't noticed that the other students have been gradually leaving the club room one-by-one."

hertha "\"Okay, Marco. See you around.\""

n "Ms. Wieck groans as that one last student leaves. She falls back into her chair and cracks her knuckles."

erik "\"If I'm in the way, I could go now.\""

hertha "\"Oh, it's nothing. Honest. Just a busy day. Relax.\""

#-# >Hertha(smokingP3E7)
show hertha U_P3_E7
with Dissolve(0.25)
#--#

n "Ms. Wieck follows her own instructions and plucks a sleek little electronic cigarette out from her shirt pocket. She glances over to make sure Marco closed the door behind him and starts puffing thick, strawberry-scented vapour."

hertha "\"Do you smoke?\""

erik "\"No, ma'am.\""

#-# >Hertha(Smoking, ah-ha! P2E7)
show hertha U_P2_E7
with Dissolve(0.25)
#--#

hertha "\"Good. No smoking allowed indoors.\""

#-# >Hertha(Smoking P1E7)
show hertha U_P1_E7
with Dissolve(0.25)
#--#

hertha "\"So, you're thinking of joining the club? Have you ever been on a school newspaper or publishing committee?\""

erik "\"No, but I had friends who worked on the yearbook at my old school. They seemed to have a good time.\""

hertha "\"It is pretty fun. We publish once a month now, so you can work almost at your own pace. We used to do a newspaper every other week, but it didn't always work out because of everyone's personal schedules. Do you enjoy writing?\""

erik "\"I'd be lying if I said it was a hobby of mine, but I usually do pretty well on compositions and essays.\""

hertha "\"If you want to be extra useful, it helps if you can write pretty well in both English and German. Well, I'm sure Lena told you that. Otherwise, take on the assignments you can do, and submit them when you can. Do you like photography?\""

erik "\"Well, my phone does have a camera...\""

hertha "\"Funny. Are you good with computers?\""

erik "\"I'm not here to fix them, if that's what you're asking.\""

n "Ms. Wieck laughs, having just been reminded of the club's technical difficulties."

hertha "\"Our publishing software is pretty easy. Lena will show you how to use it. Speaking of which, don't you have a photo-shoot to attend to?\""

erik "\"Oh, right. Thanks. I'll be back...?\""

hertha "\"Next meeting is officially the day after tomorrow, but there's usually someone here after classes every day.\""

#-# >Hertha exit to right 2
show hertha U_P1_E7:
  easein 1.0 xalign 0.55 alpha 0.0
#--#

n "I wave goodbye and head back to my room so I could change. By now, the halls around the classrooms are empty enough that I can't help but feel like some staff member will come by and shoo me away for being somewhere I don't belong."

n "Am I really going to join the school newspaper? I feel like I don't quite have a whole picture of how it is. One moment, it looks like Ms. Wieck could barely manage the club, the next moment it seems that a comparatively sloppy and casual operation is exactly how she wants it."

n "At the very least, watching her and Lena interact could provide me with some entertainment. Fran doesn't seem to want to stick around, if she is in fact a member. Maybe she's got a grudge against Lena."

n "Maybe they used to date."

#-# <end>
stop music fadeout 5.0
#--#

########

jump A1_12 # jump A?_??
