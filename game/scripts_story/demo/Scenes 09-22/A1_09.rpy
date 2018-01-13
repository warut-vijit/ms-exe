
label A1_09:
###############

$ persistent.scene_number = "A1_09" # current scene
$ persistent.scene_name = "The Art of Introduction" # current scene name
$ renpy.save_persistent()


# Scene 9 - The Art of Introduction - Annaliese
# Scene name: The Art of Introduction
# Ultra_HR
# 
# Backgrounds:
# Erik's room (early morning)
# Boy's dorm exterior
# School corridor/s
# Lobby (main entrance)
# Classroom
# Sprites:
# Ms. Claes
# Annaliese
# Sound effects:
# Window opening
# Window closing
# Birds tweeting and general morningtime nature sounds
# Paper handling
# Quiet crowd
# School bell
# Visual effects:
# Waking up
# Passage of time
# 
# Scene Opens
#-# >> Wakeup Effect to <School_ErikRoom_NOPAN.png>
scene PitchBlack
with Dissolve(1)
scene erikdorm
with Dissolve(2)
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
play ambience "music/effects/birdsandwind.ogg" loop fadein 2.0
#--#

n "It's heavy, but it does open. Why wouldn't it? They said my room had been fitted for a low-risk student."

n "The air streaming in through the crack smells faintly of freshly cut grass and dew. It's numbingly cold, but I let it linger for a moment."

n "Just as much as having that window here in the first place feels stifling, knowing that it can be opened feels relatively comforting. A small measure of control over my life. Tiny and inconsequential, maybe, but it's something."

n "I take one final deep breath to clear my head and shut the window."

#-# >> Music: New Beginnings Arise from Old Endings
play music "<from 0.0 to 181.0826 loop 10.1653>music/New Beginnings Arise from Old Endings.mp3" loop
#--#
#-# >>window closing
play sound "music/effects/window.mp3"
#--#
#-# >>outside SFX stop
stop ambience fadeout 2.0
#--#

n "Control's fine and all, but it probably isn't worth coming back to a freezing room."

n "I should get ready for school. No sense in getting all mopey about nothing before I've even started."
n "I put on my glasses and check my phone for the time."

n "6:55."

n "Just too late to get a bit more sleep. Ugh. With an involuntary groan, I grab my clothes bag to hit the shower."

#-# >>passage of time
scene PitchBlack with ImageDissolve("Transitions/clock.png", 1.0)
$ renpy.pause(1.0)
scene erikdorm with ImageDissolve("Transitions/clock.png", 1.0)
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
scene outsidemaledorm
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
scene mainlobby with ImageDissolve("Transitions/clock.png", 1.0)
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

claes "\"Erik! I'm glad you found your way here. I wasn't sure if you'd have been shown the way to your dorm room, so I thought it best to wait for you here.\""

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
scene PitchBlack
with Dissolve(1)
scene classroomhall2
with Dissolve(2)
#--#

#-# >Edna_P1_E1.png enters from left
show claes P1_E2:
  xalign 0.2 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.4 alpha 1.0
show claes P1_E2 alpha 1.0
#--#

n "As we reach the top of the stairs and enter another corridor, rather more clinical than the last, she seems to pick up on my nerves, cocking her head as she looks at me. Her expression softens somewhat."

claes "\"Nervous?\""

n "Despite her apparent concern, her voice remains quite harsh. I suppose I can forgive her; I wouldn't know how to behave in her shoes."

erik "\"Honestly, yeah.\""

claes "\"That's perfectly understandable. It's completely natural to feel nervous in new situations.\""

n "I can tell Ms. Claes is genuinely trying to reassure me but she isn't very good at it; it comes off feeling sort of forced and awkward."

claes "\"Especially in circumstances like these.\""

n "Yeah. No kidding."

claes "\"But I assure you, you really have nothing to worry about.\""

#-# >Edna_P1_E5.png
show claes P1_E5
with Dissolve(0.25)
#--#

n "Ms. Claes stops in front of a door and turns to me. Apparently, this is my form room. She glances at the door, then at me. To my surprise, she actually gives me a small smile - I wasn't sure if this would be something she was capable of at all."

claes "\"I'm just going to ask you to introduce yourself to the class, then you can take a seat.\""

n "Of course, there it is. I have to introduce myself. Suck it up, Erik, you've done stuff like this before."

erik "\"Yep.\""

#-# >Claes exits to right
show claes P1_E1:
  easein 1.0 xalign 0.6 alpha 0.0
#--#

n "With nothing but another terse nod as acknowledgement she opens the door and steps inside. I only notice the noise that had been coming from the classroom in its absence as it dies down almost immediately. I stare at the doorway."

n "Now or never."

n "I take a deep breath in a failed attempt to steady my nerves and follow the teacher inside, where she's already begun to address the class."

#-# <Crossfade to School_Classroom1_NOPAN.png>
scene PitchBlack
with Dissolve(1)
scene classroom1
with Dissolve(2)
#--#
#-# >Music fades out and stops
stop music fadeout 5.0
#--#
#-# >Sound effects: Ambient crowd noise, no chatter. Occasional clearing of throats and coughs.
play ambience "music/effects/muffledchatter.ogg" loop fadein 3.0
#--#

claes "\"Simmer down everyone, simmer down. I'd like you all to give a warm welcome to Erik Wilhelm. He'll be joining our class today.\""

n "I can't help but be aware of the faces staring in my direction. As Ela said, the class is small – only a dozen or so students – yet I can't help but feel intimidated."

n "Though most of them seem vacant, or indifferent, I can't help but assume they're all wondering the same thing."

n "\"Why are {i}you{/i} here? What's wrong with {i}you?{/i}\""

n "And as I look around the class, I find myself wondering the same thing about them."

n "A sudden tap-tap sound drags me back to reality and I realise I've been spacing out here, at the front of the class, gawking at nothing. I turn to see Ms. Claes tapping her foot impatiently."

n "Now that she has my attention, she clears her throat before continuing."

claes "\"Erik, why don't you introduce yourself to the class briefly?\""

n "My brain frantically searches for anything interesting to say. Why didn't I think of something when she told me the first time?"

n "But nope. I got nothing."

n "I hear someone snicker quietly, but then I catch a glimpse of Ela, who gives me a small smile and a double thumbs-up."

n "I decide to open my mouth and let it do the talking, without engaging my brain at all."

#-# <Crossfade to Erik Introduction CG>
show CGErik
with Dissolve (2.0)
#--#

erik "\"Uh, hi. I'm Erik.\""

n "A short pause. Apparently that's all my mouth's giving me. Great start."

n "Think, you moron."

erik "\"I, uh, I used to like hiking. And other things.\""

n "Insightful. This is probably the part where I impress them with some cool trivia I've gleaned from my years in the mountains to show off my experience, but the words fail to come and the nerves continue to tangle."

n "Besides, the barely-hidden disinterest in their faces tell me they're not the type to care to learn, for instance, that the closest place is to space on Earth is not Mt. Everest, but Mt. Chimborazo in Ecuador."

erik "\"And I just started here. Uh, today.\""

n "Jesus Christ, man."

erik "\"So hello.\""

n "Yep, that's done it. I'm a laughing stock. Surely I will never be one of the cool kids after that."

n "Thankfully, though, no one seems to care any more at the end of it than they did it at the beginning. It might be that in a few years I could maybe, possibly, begin to forget that ever happened."

claes "\"Thank you, Erik. Now, if you would please take your seat we'll get on with the day.\""

#-# <Crossfade to School_Classroom1_NOPAN.png>d
hide CGErik
with Dissolve (2.0)
#--#

n "She indicates a seat at the far right of the classroom. I consider taking the desk next to the one she indicated - it's empty and is right next to a window. Imagine how asocial I could be!"

n "Instead, though, I resolve to be just a little more social and position myself further towards the centre of the class, at the adjacent desk."

n "I hurry over, attempting to make myself as small as possible – though I realise after the fact that this combined with my slight limp gave me the appearance of some sort of hunched-over, and very conspicuous, goblin person."

#-# >Ambient noise builds back to more regular classroom chatter
# todo no different yet
#--#

#-# >Music: A Busier Sort of Day
play music "music/A Busier Sort of Day (Based on St. Paul's Suite by Gustav Holst).mp3" loop
#--#

n "I take my seat as Ms. Claes begins rattling off the morning's announcements. She seems to give it only the most perfunctory attention and most students are either idly chatting, fidgeting or simply not paying attention. Everybody seems to have completely lost interest in me already. Am I okay with this? I'm not sure."

#-# >Class bell
play sound "music/effects/schoolbell.ogg"
#--#

n "Before I've built up the courage to introduce myself to some of the students around me, though, the bell's already ringing for the next period. Most of the students around me, and all those directly adjacent to my desk, get up to move off to their next lesson. I remain where I am though – I have maths with Ms. Claes."

n "The classroom quickly fills up with other students again. This time, it looks like the desk next to mine by the window might be occupied; a girl enters the classroom and makes a beeline right for it."

#-# >Annaliese_UniformBuds_P2_E1.png enters from left to middle right
show anna U_B_P2_E1:
  xalign 0.5 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.7 alpha 1.0
show anna U_B_P2_E1 alpha 1.0
#--#

#-# >Annaliese_UniformBuds_P2_E7.png
show anna U_B_P2_E7
with Dissolve(0.25)
#--#

n "As she notices me, she falters, visibly shocked. It seems my new and unexpected presence might not be entirely welcome."

#-# >Annaliese_UniformBuds_P2_E1.png
show anna U_B_P2_E1
with Dissolve(0.25)
#--#

n "She regains her composure quickly, though, fixing back her resolutely neutral expression and taking her seat by the window without saying a word to me or, aside from the slight hesitation, acknowledging my existence at all."

n "The first thing that catches my eye about her is how little she catches my eye. Sitting still and staring out the window, oblivious to the rest of the class, wearing a hoodie rather than the standard blazer everyone else seems to wear. I wonder how she gets away with that?"

n "Despite being out of uniform, she almost blends into the wall. If she hadn't sat next to me, I doubt I would have noticed her at all."

n "She hasn't looked my way at all and the fancy-looking metallic earbuds in her ears make trying a verbal introduction seem foolish."

n "I'm not sure why I'm focussing on this girl over any of the other students in the class. Maybe her inconspicuousness makes her somehow more conspicuous?"

#-# >Annaliese exits to right
show anna U_B_P2_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#

#-# >Edna_P1_E2.png enter from left to middle left
show claes P1_E2:
  xalign 0.2 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.4 alpha 1.0
show claes P1_E2 alpha 1.0
#--#

n "Ms. Claes taps the whiteboard and clears her throat for the class's attention."

claes "\"Okay, so today we'll be reviewing the material we covered in the previous lesson. These worksheets...\""

n "She brandishes a sheaf of papers."

claes "\"... comprise a thorough test of it all. To be finished by the end of the lesson, please.\""

n "As she starts handing them down the class, she looks at me, an expression of realisation on her face."

#-# >Edna_P1_E1.png 3
show claes P1_E1
with Dissolve(0.25)
#--#

claes "\"Ah, Erik, of course, you won't know what we covered last time. Would you like to partner up with someone? Take your pick, I imagine it would be good to get to know some of your fellows.\""

n "I'm not sure what to say except 'Sure', which I do, sheepishly."

#-# >Edna exits to left
show claes P1_E1:
  easein 1.0 xalign 0.2 alpha 0.0
#--#

n "Scanning the material on the sheet Ms. Claes has placed in front of me, it doesn't seem to be too challenging. Maths isn't exactly my forté, but this is relatively simple stuff. I might have missed the previous lesson but it's nothing I couldn't handle on my own."

n "Still, it wouldn't hurt to partner up, introduce myself, socialize a little bit. That would be the normal thing to do. Well, who knows what's normal here? Might as well try, though."

#-# >Annaliese_UniformBuds_P2_E1.png enters from right to middle right
show anna U_B_P2_E1:
  xalign 0.8 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.6 alpha 1.0
show anna U_B_P2_E1 alpha 1.0
#--#

#-# >CG in
# done below
#--#
#-# >CG_03_E1.png
show CG03E1
with Dissolve (1.0)
#--#

n "The girl next to me is still staring out the window, the muffled and tinny beat from her headphones bleeding into the room around her, barely audible to me over the noise of the class. Presumably in time with the music she's listening to, her fingers are drumming out a beat on the desk in front of her."

n "Actually, it looks more like someone playing an imaginary piano than imaginary drums. Her fingers appear spider-like, splayed across the desk."

n "If wonder if she's aware that she's doing that. She must be really into whatever she's listening to."

n "In my distraction, it seems like everyone else in the class has already partnered up or started the work themselves, leaving this girl as my only choice. Working with someone who seems so strongly not to want to be noticed probably isn't a good idea, and I'm sure I could take care of the relatively simple-looking worksheet by myself, but Ms. Claes did seem very keen for me to work with a partner."

n "I wonder if she'll even hear me if I talk to her."

erik "\"Hello.\""

n "You have to start with hello."

#-# >CG_03_E2.png
show CG03E2
with Dissolve (0.25)
hide CG03E1
#--#

n "She turns her head in my direction though still doesn't face me properly, instead focussing on some spot on the wall behind me. It's not much, but at least she's noticed my presence and is no longer gazing absentmindedly out the window."

n "I can already feel that this is going to be difficult."

erik "\"I'm Erik.\""

n "In a daring move, I stretch out a hand in introduction."

#-# >CG_03_E3.png
show CG03E3
with Dissolve (0.25)
hide CG03E2
#--#
#-# >Music stops
stop music fadeout 5.0
#--#
#-# >Ambient crowd noise
play ambience "music/effects/muffledchatter.ogg" fadein 3.0 loop
#--#

n "The look of confusion and surprise on her face is almost pitiful. The girl looks worried and shocked beyond belief, turning away from me again"

n "Is this some great unforgivable faux-pas I was unaware of?"

#-# >Ambient crowd noise stops
stop ambience fadeout 3.0
#--#
#-# >Music: St. D's Ghost
play music "music/St. D_s Ghost.mp3" loop
#--#
#-# >CG_03_E4.png
show CG03E4
with Dissolve (0.25)
hide CG03E3
#--#

n "I am about to withdraw my hand and apologise when she gingerly grabs it through her sleeve. She shakes my hand with just her thumb and her index finger so delicately that if I hadn't watched it happen I might not have noticed, before abruptly dropping it and withdrawing."

#-# >Annaliese_UniformBuds_P2_E6.png
# skip
#--#

n "Somehow she looks more surprised than before. Her eyebrows look like they're just about ready to fly off her face and she stares at her own hand as if it had committed some foul act of betrayal. Aside from in that one brief moment of shock, she still hasn't looked me in the eye."

n "I feel pretty bad for worrying her and try to think of a way to move the conversation past this."

erik "\"Nice headphones.\""

#-# >CG_03_E5.png
show CG03E5
with Dissolve (0.25)
hide CG03E4
#--#

n "Clearly noticing my attempt to move past my initial, horrific mistake, she turns in my direction again and smiles slightly haltingly, looking only a little less hesitant than before – but this time definitely and deliberately looking me in the eye."

n "Once again I notice the music faintly leaking out. It may be just that it's very faint, but I don't recognise it at all."

erik "\"What are you listening to?\""

#-# >Annaliese_UniformBuds_P1_E3.png
hide CG03E5
with Dissolve (1.0)
show anna U_P1_E3
#--#

#-# >CG Out with fade
# todo done above?
#--#

n "She shrugs, and looks thoughtful for a moment."

#-# >Annaliese_UniformNobuds_P1_E5.png
show anna U_P1_E5
with Dissolve(0.25)
#--#

n "Sliding her headphones out of her ears, she moves to get something out of her bag."

n "Maybe it's time to give up. If she really isn't going to communicate with me –"

#-# >Annaliese_UniformNobuds_P1_E1.png
show anna U_P1_E1
with Dissolve(0.25)
#--#

n "But then, from her bag, she pulls out the smartphone her headphones are connected to and shows me the screen. A music player open, I catch a glimpse of what she's listening to. I've never heard of the artist, and the album art – a photo of a couple of people sitting on a cliff by the sea – doesn't give anything away about the type of music."

erik "\"Oh. Cool. Uh...\""

#-# >Annaliese_UniformNobuds_P1_E3.png
show anna U_P1_E3
with Dissolve(0.25)
#--#

n "What do you say in this situation? It's not like I'm going to get a response if I ask what kind of music it is."

erik "\"... Do you like it?\""

#-# >Annaliese_UniformNobuds_P1_E2.png
show anna U_P1_E2
with Dissolve(0.25)
#--#

n "Clearly, judging from her expression she understands the problem in communication as well. Nonetheless, her only response is to nod once and smile almost imperceptibly."

n "Being unable to think of anywhere else to take the conversation, I change tack and tap the worksheet on my desk with a pencil."

erik "\"You want to work on these together?\""

#-# >Annaliese_UniformNobuds_P1_E1.png 2
show anna U_P1_E1
with Dissolve(0.25)
#--#

n "She nods again. She seems to be getting over the initial shock of me talking to her, but anything else about her is difficult to gauge."

n "I'm not exactly sure how we're going to work on these together, seeing as she's apparently incapable of speech."

erik "\"Alright, let's divide up the work I suppose. I do odd numbered questions, you do evens?\""

#-# >Annaliese_UniformNobuds_P2_E1.png
show anna U_P2_E1
with Dissolve(0.25)
#--#

n "Without a word she nods one final time, takes a copy of the sheet from me, scans the second question for only a few seconds and starts scribbling nonchalantly on a page from her workbook. Doesn't exactly look like she's writing – her hand movements are weirdly erratic – but who am I to say?"

n "Seems like she's glad to have an excuse not to interact any more."

erik "\"Okay then...\""

#-# >Annaliese_UniformNobuds_P2_E1.png exits to right
show anna U_P2_E1:
  easein 1.0 xalign 0.8 alpha 0.0
#--#

n "I sigh and settle down to my work, with only the occasional glance at the strange girl sitting next to me."

#-# <timelapse>
scene PitchBlack with ImageDissolve("Transitions/clock.png", 1.0)
$ renpy.pause(1.0)
scene classroom1 with ImageDissolve("Transitions/clock.png", 1.0)
#--#

n "A quarter of an hour later, as I'm in the middle of my work a sheet of paper falls unceremoniously onto my desk."

#-# >Annaliese_UniformBuds_P2_E1.png enters from right to middle right 2
show anna U_B_P2_E1:
  xalign 0.9 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.7 alpha 1.0
show anna U_B_P2_E1 alpha 1.0
#--#

n "I look at my mysterious neighbour who is already staring out the window once more, headphones back in her ears. I take a look at her worksheet."

n "The edges of the paper are covered in small doodles and scribblings. Apparently that's how this girl works. Nevertheless, she has managed to finish all of the even-numbered questions."

n "And here I thought she wasn't doing any work."

n "I finish off quickly and pass my answers to her."

#-# >Annaliese_UniformBuds_P2_E3.png
show anna U_B_P2_E3
with Dissolve(0.25)
#--#

erik "Sorry, I don't know if it's all right. Seemed simple enough though."

#-# >Annaliese_UniformBuds_P1_E4.png
show anna U_B_P1_E4
with Dissolve(0.25)
#--#

n "Without even acknowledging me, she turns to her desk and starts writing again. After a minute of copying down my answers she stands up, walks up to the front of the class and hands Ms. Claes our work."

#-# >Anna out
#
#--#

n "Once Ms. Claes has thanked her she seems to hesitate, glancing furtively in the direction of my desk. I feel like I shouldn't be watching her so I look out of the window instead, but keep her in my peripheral vision."

n "After a few seconds of consideration, she seems to come to a decision. She heads back over to her desk and sits down again."

#-# >Annaliese_UniformBuds_P1_E4.png moves from middle left to middle right
show anna U_B_P1_E4:
  easein 2.0 xalign 0.55 alpha 1.0
#--#

#-# >Annaliese_UniformBuds_P2_E6.png 2
show anna U_B_P2_E6
with Dissolve(0.25)
#--#

n "She takes a deep breath and glances at me once again – though I don't think she knows I can see her as I'm doing a good job of keeping her exclusively out of my direct line of sight."

n "After another few seconds that feel strangely tense, she exhales, shakes her head, grabs her bag and exits swiftly."

#-# >Annaliese out
show anna U_B_P2_E6:
  easein 1.0 xalign 0.75 alpha 0.0
#--#

#-# >Music fades out
stop music fadeout 5.0
#--#
#-# >Ambient crowd noise 2
play ambience "music/effects/muffledchatter.ogg" fadein 3.0 loop
#--#

n "I look up at the clock. There are still 10 minutes of the lesson to go, but Ms. Claes said nothing about the girl leaving early."

n "\"The girl\". Huh. Didn't even learn her name. I don't know how to feel about what just happened."

n "Somehow, despite having done very little, I feel exhausted."

n "First period isn't even over yet. I sink into my chair, ready to admit defeat."

n "Is every day going to be as awkward as this?"

#-# >TIMESKIP
scene PitchBlack with ImageDissolve("Transitions/clock.png", 1.0)
$ renpy.pause(1.0)
scene erikdorm with ImageDissolve("Transitions/clock.png", 1.0)
#--#

########

jump A1_09_5 # jump A?_??
