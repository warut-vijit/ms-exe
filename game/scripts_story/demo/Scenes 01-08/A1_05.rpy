
label A1_05:
###############

$ persistent.scene_number = "A1_05" # current scene
$ persistent.scene_name = "A Wilhelm Goodbye (I'll probs change this)" # current scene name
$ renpy.save_persistent()


# A1_05
# Scene name: A Wilhelm Goodbye (I'll probs change this)
# Asset list and direction is incomplete atm
# Backgrounds:
# School Entrance (day)
# Sprites:
# Ela
# Irene
# Mr Wilhelm
# Mrs Wilhelm
# Beatrice
# Hilda
#-# <timeskip>
scene School_MainBuildEntrance at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5) with ImageDissolve("Transitions/clock.png", 1.0)
#--#
#-# >Background: School Entrance (day)
scene School_MainBuildEntrance
#--#
#-# >Show Ela at centre
show ela P1_E1:
 alpha 1.0 xalign 0.5
#--#
#-# >Show Irene at middle right
show irene P1_E1:
 alpha 1.0 xalign 0.75
#--#
n "Mostly recovered - save for with my heart still beating like a drum - we turn a corner and return to the school's entrance."
ela "\"Okay! Here we are. All done. You sure you'll be able to find your way to the medical wing?\""
erik "\"Yeah. Orienteering is kind of my thing.\""
ela "\"Alrighty then. I should probably get back to work. Lots to do!\""
ela "\"It was really nice meeting you, Erik. I'll see you around - and call me if you have any questions, okay?\""
#-# >Ela exit to right
show ela P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#
n "With a brilliant smile, Ela departs, heading into the school through its heavy double-doors."
n "She's clearly dedicated to her role, and the tour was... informative. I just wish she hadn't sprung the concept of a medical wing on me like that."
n "I don't know; perhaps I'm being oversensitive."
irene "\"You're looking pensive, Erik. Bee in your bonnet?\""
n "I'd forgotten Irene was still here. Her stature makes her easy to miss."
n "I'm not sure if my face really gives away much, or if it was another lucky guess. Either way, I don't know how I feel about her gleeful expression."
erik "\"It's just a lot, isn't it? All this.\""
n "I gesture to the expansive grounds."
erik "\"For us?\""
irene "\"Don't look at it that way. Just think about how much there is to do here, and how much to explore.\""
n "Her grin becomes more sincere."
irene "\"It's just a school, really.\""
irene "\"Just a school with interesting buildings. I mean, I haven't found any secret passageways yet - but y'know... still pretty cool.\""
n "Her absurdity forces a laugh out of my dry mouth, but it doesn't untie the knot in my stomach."
erik "\"Man, you think they'd have thought to cater to people who like secret passageways when they were designing this place.\""
irene "\"Right? But no. Just miles and miles of boring corridors. What were they thinking?\""
irene "\"Aaanyway, I should probably be off. Oh, hello!\""
n "The doors behind her open again, and she spins on the spot to see who it is."
#-# >Irene exit to right
show irene P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#
#-# >Beatrice enter from left to middle left
show beatrice P1_E1:
  alpha 0.0 xalign 0.65 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.25 alpha 1.0
show beatrice P1_E1 alpha 1.0
#--#
#-# >Hilda enter from left to middle right
show brunhilde P1_E1:
  alpha 0.0 xalign 1.0 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show brunhilde P1_E1 alpha 1.0
#--#
erik "\"Hey guys.\""
beatrice "\"Hey Erik! How was the tour? And who was that girl?\""
erik "\"Was? She's just-- \""
n "I turn to my right, but Irene is gone."
erik "\"Uh. Okay. Well, she {i}was{/i} right there. It was Irene. She joined us halfway through the tour.\""
beatrice "\"Ooo, look at you! Escorted 'round the school with a girl on each arm.\""
n "She gives me a little punch on the shoulder."
erik "\"You have to admit, I've got game.\""
n "Hilda steps in as Beatrice winds up to give me another whack."
brunhilde "\"It was all okay though, right? Everything looked good?\""
erik "\"I mean, as far as a school campus can, I guess. There was...\""
n "For a moment, I consider confiding my reaction to the medical wing in them."
n "But no, I feel like I shouldn't. After all, the {i}\"world-leading\"{/i} psychiatric facilities are part of the reason I'm here - as much as I hate to admit it."
erik "\"...There's this nice little path I'll be able to walk around. And Ela was nice.\""
#-# >Beatrice big smile
show beatrice P1_E3
with Dissolve(0.25)
#--#
beatrice "\"Whoa, there. Come on, Erik. She's way out of your lea--\""
n "Hilda elbows Beatrice to the side and butts in."
#-# >Beatrice neutral
show beatrice P1_E1
with Dissolve(0.25)
#--#
brunhilde "\"You think you'll be able to find your way around okay? This campus looks pretty big.\""
beatrice "\"Way bigger than mine...\""
erik "\"Yeah, I'm sure I'll be fine. They gave me a map, anyway.\""
beatrice "\"The teachers are nicer here, too.\""
brunhilde "\"There's nothing wrong with your teachers, Bea. You just keep fighting with them.\""
beatrice "\"Can you blame me with all the work they expect me to do? It's inhuman.\""
brunhilde "\"You are literally paying them thousands of euros to have the privilege of {i}doing{/i} that work.\""
n "Beatrice freezes; a look of realisation crosses her face."
n "I'm going to miss hearing my sisters' banter...."
n "The door behind them opens again."
#-# >Hilda move to right
show brunhilde P1_E1:
  easein 1.0 xalign 0.95 alpha 1.0
#--#
#-# >Beatrice move to middle right
show beatrice P1_E1:
  easein 1.0 xalign 0.75 alpha 1.0
#--#
#-# >Mr Wilhelm enters from left to middle left
show dad P1_E1:
  alpha 0.0 xalign 0.0 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.25 alpha 1.0
show dad P1_E1 alpha 1.0
#--#
#-# >Mrs Wilhelm enters from left to left
show mum P1_E1:
  alpha 0.0 xalign 0.0 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.05 alpha 1.0
show mum P1_E1 alpha 1.0
#--#
wilhelm "\"We're finally done!\""
erik "\"Finally? Were you getting bored of being told how great this place is?\""
wilhelm "\"Oh, don't be so cynical, sweetheart. It {i}is{/i} a great place.\""
wilhelm "\"Mr. Bosworth just had a lot to say about it. It may have been a bit... over the top, but he's clearly very passionate.\""
n "Yeah. {i}Passionate{/i} is the right word to describe him."
wilhelm "\"He talked a lot about the clubs and other extracurricular things they have going on. Do you think you might get involved in any of that?\""
n "Mum looks hopeful."
erik "\"Maybe.\""
n "And now she looks a little worried."
erik "\"I promise I'm not going to turn into a moping zombie. I'd miss the outdoors too much.\""
wilhelm "\"Good. I'm sure you must be nervous - but try not to let it get the better of you, okay?\""
wilhelm "\"Mm. Make the nervousness work for you.\""
n "The knot in my stomach tightens, almost to breaking point. It's such an intense, physical swoop of emotion that I almost double over."
n "I feel my quickening heartbeat and hear it in my ears; my head throbs."
n "No. Not again!"
n "I clench my hands into fists; my nails dig into the palms.  Focussing on that pain, I try to breathe deeply, breaking through the bonds around my chest. They're all in my head."
n "Nobody's noticed. Mum's started speaking. I focus on her words."
wilhelm "\"I'm sure some days you'll feel like not leaving your room at first, but don't...\""
n "It's working. I can feel myself coming back to reality."
wilhelm "\"...And if you're really struggling, you can always give me a call, okay?\""
n "Just in time."
erik "\"I will.\""
n "I swallow and force a smile. This time, it looks like Mum might have noticed."
wilhelm "\"Are you okay, sweetheart? Really?\""
n "I put a bit more effort into my expression."
erik "\"Yeah, for real. I'm fine. This place is great.\""
wilhelm "\"Well, if you're sure. Come here.\""
n "She pulls me into a tight hug and rubs my back."
wilhelm "\"It's going to be great for you, Erik.\""
wilhelm "\"Just go into it with an open mind, okay?\""
n "Yeah, I get it; everyone's telling me the same things."
n "She releases me after another extra-tight squeeze."
n "Hilda and Beatrice are next, embracing me in unison  though they let me go in a much more sensible amount of time than Mum, who didn't seem to want to let go."
beatrice "\"We'll miss you, bro!\""
brunhilde "\"But we're closer to him than we were before.\""
beatrice "\"Yeah, but it seems like a time to say goodbye, you know?\""
brunhilde "\"Okay Beatrice. I mean, that doesn't make any sense, but okay.\""
wilhelm "\"Come on, girls. Bye Erik. Love you! Be good, and please keep in touch!\""
erik "\"Love you too.\""
#-# >Mum exits to right
show mum P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#
#-# >Beatrice exits to right
show beatrice P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#
#-# >Brunhilde exits to right
show brunhilde P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#
n "Dad stays behind; I don't spend much time with him one-on-one, so this is kind of weird."
n "Unexpectedly, he claps a heavy hand on my shoulder and looks me right in the eye. Although firm and unwavering, his expression isn't intimidating."
wilhelm "\"I know how you feel, son.\""
erik "\"Really? Because-- \""
wilhelm "\"Yes. Really.\""
wilhelm "\"You've probably heard a lot of words today that have been completely meaningless to you, and a lot of placations that felt totally hollow.\""
n "I'm not sure what's going on, but Dad's right."
wilhelm "\"It's not going to be like that forever.\""
n "After a second, he seems to notice his hand is still on my shoulder and swiftly removes it. He clears his throat, no longer looking directly at me."
wilhelm "\"I'm sure you'll make the most of your time here.\""
n "And his gaze returns to meet mine."
wilhelm "\"And I'm sure you'll make me proud.\""
#-# >Mr Wilhelm exits to right
show dad P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#
n "He departs."
n "I'm left alone."
n "Just me and the knot in my stomach, tighter than ever."

########

jump A1_06 # jump A?_??
