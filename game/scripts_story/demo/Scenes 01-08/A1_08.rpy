
label A1_08:
###############

$ scene_number = "A1_08" # current scene
$ scene_name = "The Art of Introduction" # current scene name
$ renpy.save_persistent()


# Scene 8 - The Art of Introduction - Annaliese
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
# 
# 
n "I follow everyone back into the classroom as Ms. Claes had instructed, and attempt to find myself a seat."
# 
n "Most of the students around me, and all those directly adjacent to my desk, get up to move off to their next lesson. I remain where I am though – I have maths with Ms. Claes."
# 
n "The classroom quickly fills up with other students again. This time, it looks like the desk next to mine by the window might be occupied; a girl enters the classroom and makes a beeline right for it."
# 
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

#-# >Edna_P1_E1.png
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
show anna U_P1_E3
#--#

#-# >CG Out with fade
# done above
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
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene classroom1 with Clockwipe
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
show CG03E2
with Dissolve (0.25)
hide CG03E1
#--#

n "Without even acknowledging me, she turns to her desk and starts writing again. After a minute of copying down my answers she stands up, walks up to the front of the class and hands Ms. Claes our work."

#-# >Anna out
show anna U_B_P1_E4:
  easein 1.0 xalign 0.9 alpha 0.0
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
  easein 1.0 xalign 0.9 alpha 0.0
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
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene erikdorm with Clockwipe
#--#

########

jump A1_09_5 # jump A?_??
