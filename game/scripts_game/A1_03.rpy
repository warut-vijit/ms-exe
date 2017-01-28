
label A1_03:
###############

  $ persistent.scene_number = "A1_03" # current scene


# Scene 03
# 
# Backgrounds:
# Apartment Exterior (day)
# City streets (day)
# Bookstore (day)
# 
# Sprites:
# Beatrice, Hilda
# 
# Music:
# Town theme
# 
# Sound Effects:
# door closing
# city noises (loop)
# bell tinkle
# 
#-# >transition_end
todo "{color=#ff8c00}>transition_end{/color}"
#--#
#-# >open to Apartment Exterior (day)
image SistersAppartment_Outside:
  im.Scale("images/Backgrounds/SistersAppartment_Outside.png", config.screen_width, config.screen_height)
scene SistersAppartment_Outside
with Dissolve(0.5)
#--#
#-# >Hilda_neutral.png enters left to center
show hilda P2_E1:
  offscreenleft
  alpha 0.0 xalign 0.45 yalign -0.2
  easein 1.0 xalign 0.5 alpha 1.0
#--#

n "I follow Hilda as we both wait for Beatrice to finish up."

n "The morning air is thankfully nice and cool, and hopefully a solid indication for the upcoming weather."

hilda "\"So, I've been meaning to ask, but...\""

erik "\"Hm?\""

n "She hesitates, looking as if she’s carefully crafting her next words."

#-# >Hilda_frown.png
show hilda P2_E5
with Dissolve(0.25)
#--#

hilda "\"How's the leg?\""

n "There it is, the question I’ve been dreading ever since I got here."

n "It’s not like I wasn’t expecting this from her. She's never been one to dance around issues, even over the most minor things."

n "There's no use evading the question or brushing her off. I know that look in her eyes – she has to know, or it'll eat at her all day."

erik "\"Well, it's fine, I guess. It's still attached and all.\""

hilda "\"That's not what I meant! Is it still… numb?\""

n "I mean, I could go on about how it kept me up last night, or how it keeps reminding me of the accident, or how it sometimes decides to stop working entirely."

n "But I don't have the heart to tell her those things. I can't bear to make my family more upset at their broken Erik."

n "And it’s not like I don’t know why she asked that question. Her little brother going through something that she can't figure out or solve – it must be frustrating for her. Hell, it’s frustrating for me."

n "Right now, all I can do is reply with a simple answer."

erik "\"Simply put, yes, It's still pretty numb. Today it seems to be okay – enough to go around town with you and Beatrice, at least.\""

#-# >Hilda_neutral.png
show hilda P2_E1
with Dissolve(0.25)
#--#

hilda "\"...I see.\""

n "Silence. When is Beatrice coming out? She's taking her time..."

hilda "\"I know this isn't my place to say this, but…\""

erik "\"But?\""

hilda "\"...Wouldn't it be better for you to work with a physical therapist back at home? What will a school do for you that a dedicated doctor can't?\""

n "Her question cuts to the heart of the conversation I'm pretty sure she’s wanted to have with me for a while. While in most cases she'd be correct, there's something else that's been driving my motivations to come here."

erik "\"I…\""

label A1_03_menu:
label MENu1:
#-# [Menu choice:]
if (persistent.skip_menus):
  "{color=#ff8c00}[[Menu choice:]{/color}"
  jump A1_03a 
menu:
#--#
#-# [1] “...just wanted to get back into school.” (+1 Lena, Jeanne, Twins)
  "\"...just wanted to get back into school.\"":
    $ persistent.l_tot += 1
    $ persistent.nh_tot += 1
    $ persistent.nl_tot += 1
    $ persistent.j_tot += 1
    $ persistent.A1_03 = 1
    jump A1_03a
#--#
#-# [2] “...want to get better.” (+1 Isolda, Anna)
  "\"...want to get better.\"":
    $ persistent.a_tot += 1
    $ persistent.i_tot += 1
    $ persistent.A1_02 = 2
    jump A1_03b
#--#

#-# <if menu choice 1>
label A1_03a:
if (persistent.skip_menus):
  "{color=#ff8c00}<if menu choice 1>{/color}"
  "{color=#ff8c00}[[1] \"...just wanted to get back into school.\" (+1 Lena, Jeanne, Twins){/color}"
#--#
erik "\"I just wanted to get back into school. Mum and Dad approved; they think the environment here is a good thing.\""

hilda "\"Really?\""

erik "\"Plus, I still want to go to university, so I have to keep up my studies and do something with my time.\""

#-# >Hilda_smile.png
show hilda P2_E2
with Dissolve(0.25)
#--#

hilda "\"I guess when you put it like that, it makes sense. That's quite responsible of you.\""

n "She turns to put her hands on my shoulders."

hilda "\"But if things get bad, I want you to know that we're here for you, Erik.\""

erik "\"Yeah. Thanks, Hilda.\""

#-# <if menu choice 2>
if (not persistent.skip_menus):
  jump A1_03c
label A1_03b:
if (persistent.skip_menus):
  "{color=#ff8c00}<if menu choice 2>{/color}"
  "{color=#ff8c00}[[2] \"...want to get better.\" (+1 Isolda, Anna){/color}"
#--#
erik "\"I want to get better. I don't just want my leg back – I want to feel like I was before all of this happened to me.\""

erik "\"No more guilt, no more stress, no more anxiety. I think this school is the best chance I've got.\""

n "Hilda gives me an incredulous look for a second."

#-# >Hilda_smile.png 2
show hilda P2_E2
with Dissolve(0.25)
#--#

hilda "\"You've really grown, Erik. I guess you're not the baby of the family anymore.\""

erik "\"I'm just being honest.\""

hilda "\"Heh, I'm glad that you know what you want. I was worried that you weren't sure if you wanted to come here.\""

erik "\"Hilda...\""

n "She hugs me."

hilda "\"But... I'm your sister – it's natural for me to worry about you, baby or not.\""

n "I hug her back in response. She can’t see it, but I’m sporting a big smile."

erik "\"At least I’m taller.\""

hilda "\"You ruin everything, you know.\""

#-# <resume here>
label A1_03c:
#--#

#-# >door open
todo "{color=#ff8c00}>door open{/color}"
#--#
#-# >Beatrice_smile.png enter left
show beatrice P2_E4:
  offscreenleft
  alpha 0.0 xalign 0.15 yalign 1.0
  easein 1.0 xalign 0.2 yalign 1.0 alpha 1.0
#--#

beatrice "\"Sorry to keep you waiting!\""

n "As if on cue, Beatrice pops out of the front door, apparently finished with cleaning up inside."

hilda "\"What took you?\""

#-#
show beatrice P1_E2
with Dissolve(0.25)
#-#

beatrice "\"Lots of dishes, plus Mum wanted to talk.\""

erik "\"Anything important?\""

beatrice "\"Just that we should visit her more often, eat healthier, flip our mattresses and fix that rattling noise our ventilation system makes when it first cuts on before it gets worse.\""

erik "\"The usual, then.\""

beatrice "\"Pretty much.\""

hilda "\"She’s worried about us, is all. You should both be a little more understanding.\""

beatrice "\"You say that, but I’m pretty sure you waited until she wasn’t looking before you bolted for the door.\""

#-#
show beatrice P1_E3
with Dissolve(0.25)
#-#

hilda "\"Coincidence. Shall we get going?\""

n "She does her best to get us moving, but it’s not long before things slow down thanks to yours truly."

erik "\"...Sorry. Leg's still out of order.\""

#-# >Beatrice_frown.png
show beatrice P2_E5
with Dissolve(0.25)
#--#

#-# 
show hilda P2_E1
with Dissolve(0.25)
#--#

beatrice "\"Oh. Erik, I'm sorry, I just – \""

erik "\"It's fine. Just give me a minute.\""

n "I give my leg a few experimental shakes to see if I can't coax it into moving more for me today. Months of therapy have allowed me to walk unassisted, but I can still only manage a leisurely stroll."

n "It must be tough to get used to the fact that your younger brother, who loves hiking, can no longer do so."

erik "\"Okay. Ready.\""

#-# >Hilda_smile.png 3
show hilda P2_E2
with Dissolve(0.25)
#--#
#-# >Beatrice_smile.png
show beatrice P2_E2
with Dissolve(0.25)
#--#

n "We exit the complex together, both sisters now keeping up with my slower pace."

n "It's a small thing, but it really makes me appreciate that I have such caring sisters."

#-# >to city streets (day)
image ViennaStreet1:
  im.Scale("images/Backgrounds/ViennaStreet_1.png", config.screen_width, config.screen_height)
scene ViennaStreet1
with Dissolve(2)
#--#
#-# >Town Theme
todo "{color=#ff8c00}>Town Theme{/color}"
#--#

#-# > fade through other bgs
image ViennaStreet2:
  im.Scale("images/Backgrounds/ViennaStreet_2.png", config.screen_width, config.screen_height)
scene ViennaStreet2
with Dissolve(2)
#--#

n "It's a pretty good crowd, for a Saturday. There are lots of people out today – everyone's shopping, eating, and walking around."

n "Beatrice is our guide, taking us around the streets, showing me the various tramway lines and nearby stations, shortcuts behind some of the buildings, and pointing out some places that I can visit when I don't have classes or homework."

n "Honestly, it's a lot to take in. Years of navigating one of the oldest cities in Europe have clearly molded my sisters into true city-dwellers."

n "Hilda does her best to provide some sense of where we are in relation to the school and to their apartment in case I ever get lost."

n "We all take a U-Bahn route that has a stop one block away from St. Dymphna's shuttle pickup zone according to the information we got from the brochure."

#-# >
show beatrice P2_E2:
  xalign 0.5 yalign 1.0 alpha 0.0
  easein 0.25 alpha 1.0
#--#

beatrice "\"It's a great route for you, because it goes straight into the heart of the city! Stadtpark is a short walk from there, and the restaurants along Kärnter Ring are the best!\""

erik "\"Sounds like you've done your research.\""

#-#
show beatrice P2_E3
with Dissolve (0.25)
#--#

beatrice "\"What can I say? It's my sisterly duty to help out my brother with city navigation.\""

#-#
hide beatrice
with Dissolve (0.25)
#-#

n "I’m not so sure about that, but I decide not to deflate her swelling pride and allow her to continue on about shopping. As she speaks, I skim through the school brochure."

n "Apparently, the school encourages students to explore the city (within limits, I assume) for a weekend or class trip. With careful supervision, most students get to visit the city every week."

#-# >Hilda_smile.png 4
show hilda P1_E2:
  xalign 0.5 yalign -0.2 alpha 0.0
  easein 0.25 alpha 1.0
#--#

hilda "\"Anywhere you want to see, Erik? We don't have to follow Beatrice all day, you know.\""

erik "\"Hmm, I am interested in Stadtpark… Beatrice said that's on this route, right?\""

hilda "\"Yes, it's just a few stops from here.\""

#-# >clear screen
image PitchWhite = Solid("#FFF")
show PitchWhite
#--#
#-# >fade to Park
image MainGate:
  im.Scale("images/Backgrounds/MainGate.png", config.screen_width, config.screen_height)
scene MainGate
with Dissolve(2)
#--#

n "Stadtpark is quieter than the rest of the city, but there are still a lot of people around today. Most people are walking or riding bicycles. Others are enjoying a late lunch at one of the cafes just outside the park."

n "I'm impressed – it's a lot more lively than I expected. Tourists are clustered around a few statues."

#-# >Hilda_neutral.png enter left
show hilda P2_E2:
  offscreenleft
  alpha 0.0 xalign 0.35 yalign -0.2
  easein 1.0 xalign 0.4 alpha 1.0
#--#

hilda "\"Erik, this cafe is fantastic! Let’s go inside.\""

#-# >fade to cafe
image ViennaStreet3:
  im.Scale("images/Backgrounds/ViennaStreet_3.png", config.screen_width, config.screen_height)
scene ViennaStreet3
with Dissolve(2)
#--#

n "The cafe is busy during the lunch hour, with a long line working its way from the entrance to the counter."

#-#
show hilda P2_E2:
  offscreenleft
  alpha 0.0 xalign 0.7 yalign -0.2
  easein 1.0 xalign 0.6 alpha 1.0
#--#

#-#
show beatrice P1_E2:
  offscreenleft
  alpha 0.0 xalign 0.2 yalign 1.0
  easein 1.0 xalign 0.3 alpha 1.0
#--#

beatrice "\"This place has a lot of great snacks and drinks. They cater to the people who come to the park to take walks and exercise here.\""

erik "\"So the fare is pretty light, then?\""

n "Beatrice nods."

hilda "\"We both work near here, so we usually meet up for lunch and a quick walk. It’s become one of our favorite hangouts.\""

n "I take a look at what’s available. Lots of prepackaged sandwiches, salads, and beverages occupy the shelves."

erik "\"Are these any good?\""

hilda "\"Of course! They make them fresh every day. Here, try this one.\""

n "I don’t see how prepackaged chicken can live up to her endorsement, but I accept the sandwich offered. Free sandwiches have their own scale of quality."

hilda "\"This one’s my personal favorite. Anything else? I’ll buy for you today.\""

n "I dutifully pick out a canned drink and follow Beatrice to the cashier."

erik "\"Thanks for lunch.\""

hilda "\"No problem! It’s my sisterly duty to treat my little brother on special occasions like this.\""

#-#
show beatrice P1_E3
with Dissolve(0.25)
#-#

beatrice "\"Feel free to treat your little sister as well.\""

#-#
show hilda P2_E1
with Dissolve(0.25)
#-#

hilda "\"What’s your special occasion…?\""

#-#
show beatrice P2_E2
with Dissolve(0.25)
#-#

beatrice "\"I cooked breakfast?\""

#-#
show hilda P2_E2
with Dissolve(0.25)
#-#

hilda "\"Just the one sandwich, thank you.\""

#-#
show beatrice P1_E8
with Dissolve(0.25)
#-#

beatrice "\"...Seems like a double standard, that’s all I’m saying...\""

n "It sounds like they that same complex dynamic that still eludes me."

n "With Beatrice being able to cook so well, it seems that she has a lot of influence."

n "As we sit down, the two sisters talk about what they’ve been up to in the months since I last saw them at home."

#-#
show beatrice P1_E1
with Dissolve(0.25)
#-#

beatrice "\"I’ve been prepping for my final year at MDW. Gonna’ be a long year with all the papers I have to write…\""

erik "\"Music theory is that intensive?\""

n "Beatrice slumps in her chair with a big sigh."

#-#
show beatrice P1_E8
with Dissolve(0.25)
#-#

beatrice "\"Not really, it’s just that 20 pages on contemporary jazz gets to you in the long hours of the night.\""

hilda "\"Ah, I remember you not being able to sleep because the music you were studying got stuck in your head.\""

erik "\"Sounds more like too much coffee.\""

#-#
show beatrice P1_E7
with Dissolve(0.25)
#-#

beatrice "\"...\""

n "She does nothing but glower in my direction as she sips her drink - which is, naturally, an iced coffee."

hilda "\"Erik, be nice.\""

erik "\"It’s my brotherly duty to annoy Beatrice, though. Gotta do it.\""

n "Beatrice’s glowering continues as I take a bite out of my sandwich."

#-#
show beatrice P1_E5
with Dissolve(0.25)
#-#

erik "\"Anyway, what have you been up to, Hilda? Still researching?\""

hilda "\"Pretty much. We’re working on developing new surgical tools. Can’t give you the details, but I’m proud of what our team has done so far.\""

erik "\"Sounds interesting.\""

hilda "\"It’s certainly better than mountains of research papers, that’s for sure. I’m not envious of you two.\""

#-#
show beatrice P1_E1
with Dissolve(0.25)
#-#

beatrice "\"But what about your youthful escapades?\""

erik "\"Or procrastinating on your homework?\""

beatrice "\"Surely you miss those?\""

#-#
show hilda P1_E4
with Dissolve(0.25)
#--#

hilda "\"Okay, you got me. I suppose I miss secondary school and university a bit. You two should try and enjoy your time in school. Especially you, Erik.\""

n "Since my previous year of school was interrupted, it could be said that I have a lot of youthful escapades that I need to catch up on."

n "How much of those are allowed at St. Dymphna’s? No clue."

n "The rest of our lunch is more playful banter, teasing Beatrice, and enjoying time with my family."

#-# >timeskip
todo "{color=#ff8c00}>timeskip{/color}"
scene ViennaStreet3
with Dissolve(0.5)
#--#

n "Despite the allegedly light fare, the sandwich is actually pretty filling. Cleaning up the table, all of us head back into the city."

#-#
show hilda P2_E1:
  offscreenleft
  alpha 0.0 xalign 0.2 yalign -0.2
  easein 1.0 xalign 0.3 alpha 1.0
#--#

hilda "\"So, what do you think of Vienna, Erik?\""

erik "\"I can see why you moved here, it's a great city. I wish we had more time to explore.\""

#-# >Hilda_smile.png 6
show hilda P2_E2
with Dissolve(0.25)
#--#

hilda "\"Well, you're free to come visit us if you're lonely!\""

#-# >Beatrice_smile enter right
show beatrice P2_E3:
  offscreenright
  alpha 0.0 xalign 0.7 yalign 1.0
  easein 1.0 xalign 0.6 alpha 1.0
#--#

beatrice "\"We'd never turn you away! You mean so much to us, Erik.\""

n "My sisters may be overly doting, but it's definitely sincere."

#-# >ping
todo "{color=#ff8c00}>ping{/color}"
#--#
#-# >Beatrice_neutral.png
show beatrice P1_E1
with Dissolve(0.25)
#--#

n "Beatrice's cell phone pings with a notification. She takes it out to read it, then frowns."

#-# >Beatrice_frown.png 2
show beatrice P1_E5
with Dissolve(0.25)
#--#

beatrice "\"Sadly, this concludes our regrettably brief tour of Vienna. We need to meet back with Mum and Dad for dinner.\""

#-# >Hilda_neutral.png 2
show hilda P2_E1
with Dissolve(0.25)
#--#

hilda "\"Really? It's that late?\""

#-# >Beatrice_neutral.png 2
show beatrice P1_E1
with Dissolve(0.25)
#--#

beatrice "\"Yeah. We need to catch the U-Bahn back to our place. Let's go!\""

n "We make a dash back to the station, almost missing the next tram back home."

#-# >fade to black
image PitchBlack3 = Solid("#000")
show PitchBlack3
with Dissolve(2.0)
#--#

#-# <end>
#
#--#


########

jump A1_04 # jump A?_??
