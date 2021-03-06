
label A1_17:
###############

$ persistent.scene_number = "A1_17"  # current scene_number
$ persistent.scene_name = "Juxtaposing"  # current scene name
$ renpy.save_persistent ()


# Juxtaposing
# Scene Name: Juxtaposing

## BG: Hallway, Gymnasium, Nurse's Office
## Music: Jeanne's Theme, school theme

## <Fade into Hallway (Day)>
## >start school theme
scene classroomhall
with Dissolve(2.0)

play music "music/Be_Green.mp3"
n "I’m finally free of those horrible jokes."

n "At least there’s physical education later this morning. Maybe I can get my mind off of them by moving around and sweating a bit."

##<Timeskip to Gym (Day)>
scene PitchBlack with ImageDissolve("Transitions/clock.png", 1.0)
scene gym with ImageDissolve("Transitions/clock.png", 1.0)
n "Entering the gym, about half of these students I can see are from my class, but I notice some new faces mixed in. "

n "All of us are wearing the same white-and-blue gym uniforms provided to us by the school, of course."

n "I recall when Mum got the gym uniform from the school. She called it “drab and boring,” then immediately tossed it into the washing machine before I had a chance to look at it."

n "It feels a bit snug, but at least the fabric is breathable."

n "The gym here is a bit smaller than the one at my previous school - with soft, rubberised floors and a lack of any bleachers, it’s more suited to a playroom than a gym proper. "

n "Outdoor sports like track and football are done as part of class occasionally, but I read that this course is just something low-impact for all students."

n "I’d prefer to be in the more active phys ed courses, but my leg could cause problems, according to the physical I had before transferring here."

n "Walking is fine, though."

n "I decide to warm up my leg by milling around the small space, where clusters of students are having small conversations."

n "Most of the conversations revolve the latest school gossip I’m not aware of, the latest internet trends I’ve missed out on because of my non-stop treatments, and, naturally, homework."

n "Seems fairly standard."

n "Maybe I can meet people who aren’t as pun-obsessed as Natalya, or as silent as Annaliese."

##<gym door open>
play sound "music/effects/door open and close.mp3"
##<Clap>

n "Suddenly, a loud clap bursts from the side doors, where a young woman – probably in her late twenties – strides over to us. "

n "Oh, it's Hertha. I wasn't expecting her to show up here. It's kind of interesting to see teachers in multiple roles in this school."

## >Hertha (smile)
show hertha U_P3_E2:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show hertha U_P3_E2 alpha 1.0
hertha "\"Hello, students! I’m Ms. Wieck, and I’ll be substituting for this class.\" "

n "Everyone pauses for a moment, unsure what to think."

n "A hand shoots up from the crowd of students gathering around this new face."

## >Hertha (neutral)

hertha "\"Yes?\""
show hertha U_P3_E1
with Dissolve (0.25)
student "\"Where’s Dr. Berhn? He’s supposed to teach us, right?\"" 

## >Hertha (smile)
show hertha U_P2_E2
with Dissolve (0.25)
hertha "\"Dr. Berhn is very busy this school year – he’s been invited to several international conferences across Europe and in the United States. I’m sure he misses teaching all of you, though.\""

n "Several students nod – I guess this Dr. Berhn was pretty popular with the students here."

hertha "\"I know I’m not him, but let’s do our best to get along and have some fun, okay?\""

n "Some students give a smile, but most of the others sigh and shrug their shoulders. "

## >Hertha out
show hertha U_P2_E2:
  easein 0.5 xalign 1.0 alpha 0.0

n "Everyone lines up into rows to get started on some calisthenics. However, despite her cheerful demeanor, many of the students don’t seem all that interested, many putting in a minimal effort to appear active. "

n "I figure it wouldn’t hurt to get some exercise in – I’ve been cooped up in a hospital and my own home for months now. I wasn't moving a lot while I was recuperating, so being able to freely move around is a nice change of pace."

n "It reminds me of all the times I warmed up to go outdoors with Gustav."

n "..."

## <Pan right>

n "Am I the only one actually putting effort into this? Looking to my right yields two lanky males from my class who are sort of doing some half hearted jumping jacks."

n "To my left, however..."

## <Pan left>

## <Dark shape zoom>

n "The person to my left has apparently tripped. "

## <Crash>

n "Right into me."

n "Both of us take a sharp fall into the ground, and I brace for impact."

## <black>
scene PitchBlack
with Dissolve (0.5)
n "So today, I was asked to stare into the sun, endured some terrible puns, and now have had someone crash into me."

n "What is this, a cartoon?"


n "It feels hard to breathe. I try to lift myself up, but I can’t move. There’s something really heavy on top of me."

##<CG – Jeanne Intro>

## <eye opening>
show CG_A1_17
with Dissolve (2.0)
n "Before me is a girl splayed on top of my chest. Well, that explains why I can’t move. Or… breathe..."

erik "\"Ack...need to…\""

n "The girl who fell on me feebly squeaks out in surprise and scrambles off of me before I suffocate."

jeanneunknown "\"S-sorry! I’m so sorry!\""

n "Her face is tinged red with embarrassment. I try and say something, but Hertha quickly approaches the two of us before I can reply."

hertha "\"Woah, everything okay here?\""

jeanneunknown "\"Hertha! I um… I...\""

## >click
## >click

n "The girl is pretty stressed out. She’s rhythmically snapping her fingers for some reason."

n "She sniffles a little bit, clearly trying not to cry."

n "..."

jeanneunknown "\"!\""

n "Blood starts trickling down her nose - a nosebleed?"

n "Almost instantly she clamps her hand over her nose to try and plug it."

n "That was a serious blow - my guess is she landed nose-first into me when she fell over. "

n "I hear Hertha sharply inhale as she realises what’s happened."

hertha "\"Oh God, Jeanne...\""

n "The girl starts moving in an attempt to get up, Ms. Wieck gently supporting her."

## <End CG>
scene gym
with Dissolve (2.0)
## >show Jeanne/Hertha moved down
show hertha U_P1_E4:
  xalign 0.30 yanchor 1.0 ypos 1080+425+300 alpha 1.0
  
show jeanne G_P1_E1:
  xalign 0.70 yanchor 1.0 ypos 1080+425+300 alpha 1.0
  
## BLOOD ##
## >Hertha up, slow
## >Jeanne up, wobble animation
show hertha U_P1_E4:
  easein 3.0 ypos 1080+425
  
show jeanne G_P1_E1:
  easein 3.0 ypos 1080+425-30
  
## BLOOD ##
n "She stumbles in an attempt to get up, wincing as she rises to her feet."

## >Jeanne (pain/frown)
show jeanne G_P1_E8
jeanne "\"Oww...\""

n "She must have rolled one of her ankles pretty badly in the fall. Could it be a sprain?"

hertha "\"This is bad...\""

n "Ms. Wieck turns to me."

hertha "\"Sorry to put this on you, uh - wait, you’re...\""

erik "\"...From the newspaper club yesterday. I’m Erik?\""

## >Hertha smile
show hertha U_P1_E2
n "Ms. Wieck’s face lights up in recognition."

hertha "\"Oh, thought you looked familiar!\""

##>Hertha frown
show hertha U_P1_E5
hertha "\"Sorry this happened. But, could you help out Jeanne here? I can’t leave these students here unsupervised, but she needs to see the nurse for school injuries.  Do you know where the nurse’s office is?\""

n "I shake my head. It was probably pointed out to me briefly in Ela’s tour, but I can't seem to recall where it was."

## >Hertha neutral
show hertha U_P1_E4
hertha "\"Well, from those doors over there, just take a left and head all the way down until you see a fork in the hall. Take the left one – the nurse’s office is the second door on the right. There’s a sign that says ‘First Aid’ over the door. Got it?\""

erik "\"Got it. I’ll take her there.\""

## >Hertha exit left
show hertha U_P1_E4:
  easein 0.5 xalign 0.0 alpha 0.0
## >Jeanne move center
show jeanne:
  easein 0.5 xalign 0.5
n "Hopefully my own leg doesn’t give out while guiding her down there."

n "I reach out to Jeanne, who is still focusing on trying not to stain her gym shirt with blood."

erik "\"Hey, let me help you up.\""

n "I offer my arm as she climbs onto her feet. Her nose has started to bleed even more now, to the point that she has to hold it shut to keep from getting stains on her uniform."

n "The girl wobbles a bit, but manages to balance herself on my shoulder and her good leg. "

erik "\"Easy now. Try to keep off that foot.\""

n "Slowly, we make our way to the doors outside."

## <Cross to Hallway (day)>
scene classroomhall2
show jeanne G_P1_E8:
  xalign 0.50 yanchor 1.0 ypos 1080+425-30 alpha 1.0
n "It feels weird saying nothing while walking down the hallway. I don't know her all that well, and she looks pretty shaken up. But..."

n "Maybe I should talk to her, to get her mind off of things. It is kind of awkward walking down here without trying to say anything."

n "Wait... how do you make small talk with a girl on your arm that also has a nosebleed?"

n "Looking closer, she's… kind of cute. I'm usually not a fan of thick-rimmed glasses, but it works pretty well on her."

n "Wait, is she…?"

n "Yep, I’m not seeing things - she’s missing part of one her left hand’s finger. Yikes."

## >start Jeanne’s theme
## >Jeanne (nosebleed)
play music "music/Shades of Echo.mp3"
jeanne "\"Umm...\""

n "Crap, I think she noticed me peeking at her. Look away, look away..."

erik "\"Um, hey, are you gonna be okay? You took quite a fall there.\""

jeanne "\"Ah subose I did...\""

n "The girl trails off for a moment."

jeanne "\"Umm, thad is...I shoobd be fyn.\""

##>snap

n "As if on instinct, her body stiffens a little and the fingers on her right hand snap. It's quick, but it's quite loud. She turns a gaze in my direction."

show jeanne G_P1_E6

n "Is it a nervous tic? I remember hearing about those on some documentary I watched. She was doing it after she collided with me, so maybe this is something related to that?"

erik "\"Uh...\""

jeanne "\"Oh, thad’s just me. I do thad, um, ad ramdun. Turrette’s Syundronme.\""

n "Tourette’s Syndrome?"

n "Isn’t that the disorder that makes people swear uncontrollably?"

n "I guess this shows how little I know of other people’s disorders. I’m sure she’s probably never heard of a somatic disorder."

erik "\"I see.\""

n "All I can do is accept it and move on, I guess."

n "Maybe she only does it when she’s not bleeding from the nose. No idea."

erik "\"Well, in any case, glad I was there to cushion you from the fall. That could have been worse.\""

n "Jeanne solemnly nods."

jeanne "\"...Sobby about dat.\""

erik "\"No, no, don’t be. I’m not injured, and at the very least you avoided getting hurt more.\""

n "Geez, I sound like my sisters now. They’d always get a little overprotective if I got hurt."

n "Gustav did the same thing."

jeanne "\"Are yoob okady?\""

n "I try to reassure her with a grin."

erik "\"Don't worry, I've had worse. The doctors say I'm pretty sturdy.\""

n "I pat my chest to show that I’m still intact."

jeanne "\"Thabt's goob to hear.\""

n "I can see a small smile forming underneath her hands."

erik "\"Oh, I should introduce myself. My name's Erik.\""

n "The girl releases her hold on her nose. Looks like the bleeding has stopped for now."

## >Jeanne (smile, small bit of blood)
show jeanne G_P1_E9
## MINI BLOOD ##
jeanne "\"My name's Jeanne. Thanks for your help, and once again, I'm really, {i}really{/i} sorry for knocking you over.\""

##>click

n "Her body stiffens and she snaps her fingers once more. She doesn’t seem bothered by it, so my guess is that I can safely ignore it as well. "

erik "\"Don't worry about it. I'm fine!\""

##>Jeanne (smile)
show jeanne G_P1_E9
##  BLOOD ? ##
jeanne "\"So you're a transfer student, correct? I don't think I've ever seen you here before.\""

erik "\"Guilty as charged. I just started here this week.\""

## >Jeanne (surprise)
show jeanne G_P1_E4
##  BLOOD ? ##
jeanne "\"Oh! I was right.\""

## >Jeanne (smile)
show jeanne G_P1_E9
##  BLOOD ? ##
jeanne "\"Welcome to St. Dymphna's, then.\""

erik "\"Thanks.\""

## >Jeanne (neutral)
show jeanne G_P1_E2
##  BLOOD ? ##
jeanne "\"What do you think of the school so far?\""

##>click

erik "\"It's all right. Can't say I love it or hate it just yet, you know?\""

jeanne "\"Mm, I understand. I was the same way when I first started going here a few years ago. Don't worry – this place grows on you after a while.\""

##>click

erik "\"How long did that take for you?\""

jeanne "\"Oh, it didn't take that long. Maybe a few months?\""

n "So there are some students who have been here quite a while. Jeanne's reassurance that the school would grow on me is nice to hear."

n "Still, I'm going to remain skeptical as a matter of principle. The week isn't even over and I've run into – in Jeanne’s case, quite literally –  some rather “interesting” characters."

n "Jeanne and I make some more small talk until we reach the nurse's office."

##<Crossfade to Nurse's office – Day>
scene nursesoffice

show jeanne G_P1_E2:
  xalign 0.50 yanchor 1.0 ypos 1080+425 alpha 1.0
  
n "The nurse on staff greets us, then notices Jeanne on my shoulder. I take a moment to explain what happened."

erik "\"She rolled her ankle a bit in gym class, and she had a slight nosebleed.\""

nurse "\"Goodness, are you okay, young lady?\""

##>Jeanne (frown)
show jeanne G_P1_E6
jeanne "\"Well, my nose has stopped bleeding, but my ankle still hurts.\""

##>click

nurse "\"All right, let’s head back to my office and I’ll take a look.\""

erik "\"Need me to help take her back, miss?\""

nurse "\"That would be very helpful, thank you. You'll have to wait in the lobby afterward, though – patient privacy, you know.\""

erik "\"Of course.\""

n "The nurse guides us to her office in the back, a small room stocked with bandages and some basic first aid tools. It's well-equipped, almost overly so for what appears to be an area for small injuries. "

n "I help Jeanne up onto the patient table. The nurse props up her leg in order to keep it elevated."

nurse "\"Would you mind waiting here for a bit? I need to fetch something from the supply closet.\""

n "The nurse steps out, leaving the two of us in the room."

erik "\"All good up there?\""

jeanne "\"I'm fine. I just hope it's not a sprain.\""

erik "\"Mind if I take a look?\""

jeanne "\"... Sure?\""

n "I take a closer look at her ankle. No swelling yet..."

n "If it were a sprain, her ankle would definitely be puffed up and red right about now."

erik "\"I don't know if it's sprained. Does it still hurt?\""

n "Jeanne nods."

erik "\"Then it's probably just the pain from rolling your ankle so suddenly.\""

jeanne "\"You sure know a lot about ankles, Erik. Are you studying to be a doctor? Or a physical therapist?\""

erik "\"Hm? Nah, nothing like that. My family and I do a lot of hiking, and when I was younger, I twisted my ankle on a rough patch of the trail we were on.\""

n "Coincidentally, it was on the same leg that’s been giving me trouble as of late."

## >Jeanne (shock)
show jeanne G_P1_E5

jeanne "\"Did it hurt?\""

erik "\"Yeah, it was pretty bad. I was on crutches for a few weeks so it could heal properly. But I learned a lot about how important my ankles were, that's for sure.\""

erik "\"But you should definitely be alright.\""

## >Jeanne (smile)
show jeanne G_P1_E9
jeanne "\"That’s good to hear!\""

n "Just then, the nurse re-enters the room."

nurse "\"Okay, I'm back. Everything good here?\""

n "The two of us nod, which seems to satisfy her."

erik "\"I guess this is my cue to leave. See you in a bit, Jeanne.\""

jeanne "\"Okay. See you soon!\""

## >click

nurse "\"She won't be long. Please, take a seat outside.\""

## >Jeanne out
## >start school theme

## >TO Lobby <Day>
scene mainlobby
n "A large stack of colorful pamphlets next to me catches my eye."

n "\"Sign up for Flu Shots!\""

n "\"Eating Right – A Primer on Good Fruits and Vegetables!\""

n "\"Use Protection!\""

n "I don't need to read these."

n "Looking around, the office actually extends a little bit past the lobby I'm currently in; several doors lead into what I assume to be beds or private offices."

n "I can hear some muffled voices behind some of them – I guess it's a nurse or two helping another student."

n "I guess I can just relax for a bit. The lobby seems to be pretty new in comparison to the rest of the building, with a secretary clacking away on a computer."

n "Some social media site is up – guess there isn't much to do here, aside from students and staff visiting."

n "A slight rumble in my stomach reminds me that taking most of my time at breakfast helping Natalya meant that I didn’t have much time to actually eat anything."

n "Thankfully, there's a water cooler right next to me. I take a paper cup and wash out the sour taste in my mouth."

n "Right next to the cooler is a small candy dish with some wrapped chocolates. It's not exactly breakfast, but it's something to eat. I take a few to nibble on while I wait."

## <timeskip>
scene PitchBlack with ImageDissolve("Transitions/clock.png", 1.0)
scene mainlobby with ImageDissolve("Transitions/clock.png", 1.0)
## >Jeanne enter smile
show jeanne G_P1_E9:
  xalign 0.5 yanchor 1.0 ypos 1080+425-30 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0

n "Soon after, Jeanne returns, minus the blood on her face. The worried, embarrassed look she had is also gone, replaced with a gentle, friendly smile. The nurse turns to me."

nurse "\"She's got a cold compress on her ankle, but she should take it easy for a little while longer.\""

erik "\"That’s good.\""

## <Cross to Hallway – Day>
scene classroomhall2
show jeanne G_P1_E9:
  xalign 0.5 yanchor 1.0 ypos 1080+425-30 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
n "Jeanne still has a slight limp to her step, but she looks much better after getting cleaned up. Her eyes, which were sullen and a bit red a few minutes ago, look to be a lot brighter now that she's cheered up a bit."

erik "\"Feeling better?\""

jeanne "\"Yeah. Thanks for helping me get to the nurse.\""

erik "\"Like I said, it's no big deal.\""

## >Jeanne (neutral)
show jeanne G_P1_E4
jeanne "\"You were right, you know. It was just sore from the rolling.\""

##>click

erik "\"She said that?\""

n "Jeanne nods."

jeanne "\"According to her, it would have been swollen much sooner.\""

n "Ha, I was right."

erik "\"That's a relief then. Trust me, you do not want a sprained ankle during school.\""

jeanne "\"Right! I'll have to be careful.\""

## >click

erik "\"Want some chocolate? I got a few extras from the front desk.\""

n "I pull out a small piece of candy that I swiped from the secretary's candy bowl."

n "Jeanne's eyes light up."

##>Jeanne smile
show jeanne G_P1_E2
jeanne "\"Thanks!\""

n "In one smooth motion, she unwraps and pops the candy into her mouth."

erik "\"So, what do you think of our substitute teacher?\""

## >Jeanne smile

jeanne "\"Oh? Well, she's my floor's dorm mom, so I already know her through there.\""

## >click

## >Jeanne big smile
show jeanne G_P1_E9
jeanne "\"She's really nice to all of us at the dorm, so it's nice to see her helping out at school, too!\""

erik "\"Sounds like we'll be fine in gym then.\""

## Jeanne smile
show jeanne G_P1_E2
jeanne "\"You bet!\""

## <Cross to Gym – Day>
scene gym
show jeanne G_P1_E2:
  xalign 0.7 yanchor 1.0 ypos 1080+425-30 alpha 0.0
  easein 1.0 xalign 0.7 alpha 1.0
n "I lead Jeanne back over to Hertha, who jogs up to greet us."

## >show Hertha neutral
show hertha U_P3_E1:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.3 alpha 1.0
hertha "\"Ah, you guys are back. How’s everything?\""

## >Jeanne neutral
show jeanne G_P1_E4
jeanne "\"Well, the nurse says I just rolled my ankle badly – it's not a sprain, thank goodness.\""

## >click

## >Hertha smile
show hertha U_P1_E2
hertha "\"That's good to hear! Just sit out for the rest of class, okay?\""

##>Jeanne (neutral)

jeanne "\"Okay, sure.\""
show jeanne G_P1_E4:
  easein 1.0 xalign 1.0 alpha 0.0
n "I go to walk her to the bleachers."

## >Hertha frown
show hertha U_P1_E4
hertha "\"And you, young man, don't have a sprained ankle, last I checked.\""

n "Well, shoot."

## >Hertha grin
show hertha U_P1_E1
hertha "\"Get some laps in, all right? Jeanne will be fine.\""

erik "\"Yes, ma'am.\""

## >Hertha smile
show hertha U_P1_E2
hertha "\"Oh, don't be so formal – you're making me sound old!\""

n "I nod as I head back to the track as the two girls take a seat and start talking."

##<timeskip>
scene PitchBlack with ImageDissolve("Transitions/clock.png", 1.0)
scene gym with ImageDissolve("Transitions/clock.png", 1.0)
n "After finishing up, Hertha meets me before I head to the locker room."

## >Hertha neutral
show hertha U_P3_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
hertha "\"Hey, thanks for your help, Erik.\""

## >Hertha smile
show hertha U_P3_E2
hertha "\"It's good of you to help out other students here.\""

erik "\"No problem. Just doing the right thing.\""

hertha "\"Jeanne certainly appreciates it.\""

erik "\"Really?\""

hertha "\"She’s not one to mince words — she told me she’s really grateful to you for carrying her to the nurse’s office.\""

n "I recall her face when she thanked me back in the hallway."

n "It was warm, cheerful, and charming — I could tell Jeanne was the type of girl to be a little more grateful than usual over things like this."

hertha "\"I hope you two continue to get along! It’ll be nice to have two great students leading everybody in class.\""

## >Hertha neutral
show hertha U_P1_E1
hertha "\"I’m not usually teaching these courses, so having some students help out would be a huge relief to me.\""

erik "\"I’ll do what I can.\""

## >Hertha smile
show hertha U_P1_E2
hertha "\"Great to hear!\""


hertha "\"Well, see you around, Erik.\""

## >hide Hertha
show hertha U_P1_E2:
  easein 1.0 xalign 1.0 alpha 0.0

n "As she leaves, I can’t but feel a surge of pride after helping out Jeanne."

n "This’ll keep me going for the rest of the day."

## <END>

jump A1_18