
label A1_03:
###############

$ persistent.scene_number = "A1_03" # current scene
$ persistent.scene_name = "A Teenager's Guide to Vienna" # current scene name
$ renpy.save_persistent()


# Scene 03 - A Teenager's Guide to Vienna
# Scene name: A Teenager's Guide to Vienna
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
#
#--#
#-# >open to Apartment Exterior (day)
scene SisAptOutside at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
with Dissolve(0.5)
#--#
#-# >Hilda_neutral.png enters left to center
show hilda P2_E1:
  alpha 0.0 xalign 0.3 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.5 alpha 1.0
show hilda P2_E1 alpha 1.0
#--#

n "I follow Hilda as we both wait for Beatrice to finish up."

n "The morning air is thankfully nice and cool, and hopefully a solid indication for the upcoming weather."

hilda "\"So, I've been meaning to ask, but...\""

erik "\"Hm?\""

n "She hesitates, looking as if she's carefully crafting her next words."

#-# >Hilda_frown.png
show hilda P2_E5
with Dissolve(0.25)
#--#

hilda "\"How's...\""

n "She pauses, a clear twitch on her usually imperturbable face, as she mulls over how to broach the question hanging on her lips."

hilda "\"How's the leg?\""

n "{i}There it is,{/i} the question I've been dreading ever since I got here."

n "It's not like I wasn't expecting this from her. She's never been one to dance around issues."

n "There's no use evading the question or brushing her off. I know that look in her eyes – she has to know, or it'll eat at her all day."

erik "\"Well, it's fine, I guess. It's still attached and all.\""

hilda "\"That's not what I meant! Is it still... numb?\""

n "I mean, I could go on about how it kept me up last night, or how it keeps reminding me of the accident, or how it sometimes decides to stop working entirely."

n "But I don't have the heart to tell her those things. I can't bear to make my family more upset at their broken Erik."

n "And it's not like I don't know why she asked that question. Her little brother going through something that she can't figure out or solve – it must be frustrating for her. Hell, it's frustrating for me."

n "Right now, all I can do is reply with a simple answer."

erik "\"Simply put, yes, it's still pretty numb. Today it seems to be okay – enough to go around town with you and Beatrice, at least.\""

#-# >Hilda_neutral.png
show hilda P2_E1
with Dissolve(0.25)
#--#

hilda "\"... I see.\""

n "Silence. When is Beatrice coming out? She's taking her time..."

hilda "\"I know this isn't my place to say this, but...\""

erik "\"But?\""

hilda "\"... Wouldn't it be better for you to work with a physical therapist back at home? What will a school do for you that a dedicated doctor can't?\""

n "Her question cuts to the heart of the conversation I'm pretty sure she's wanted to have with me for a while. While in most cases she'd be correct, there's something else that's been driving my motivations to come here."

erik "\"I...\""

label A1_03_menu:
label MENu1:
#-# [Menu choice:]
if (persistent.skip_menus):
  "{color=#ff8c00}[[Menu choice:]{/color}"
  jump A1_03a
menu:
#--#
#-# [1] "...just wanted to get back into school." (+1 Lena, Jeanne, Twins)
  "\"...just wanted to get back into school.\"":
    $ persistent.l_tot += 1
    $ persistent.nh_tot += 1
    $ persistent.nl_tot += 1
    $ persistent.j_tot += 1
    $ persistent.A1_03 = 1
    jump A1_03a
#--#
#-# [2] "...want to get better." (+1 Isolda, Anna)
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
erik "\"I... just wanted to get back into school. Mom and Dad approved; they think the environment here is a good thing.\""

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
erik "\"I... want to get better. I don't just want my leg back – I want to feel like I was before all of this happened to me.\""

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

n "I hug her back in response. She can't see it, but I'm sporting a big smile."

erik "\"At least I'm taller.\""

hilda "\"You ruin everything, you know.\""

#-# <resume here>
label A1_03c:
#--#

#-# >door open
play sound "music/effects/door open and close.mp3"
play music "music/Ditzy.mp3" loop
#--#
#-# >Beatrice_smile.png enter left to leftcenter
show beatrice P2_E4:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.3 alpha 1.0
show beatrice P2_E4 alpha 1.0
#--#
#-# >Hilda to rightcenter
show hilda P2_E1:
  easein 1.0 xalign 0.7 alpha 1.0
show hilda P2_E1 alpha 1.0
#--#

beatrice "\"Sorry to keep you waiting!\""

n "As if on cue, Beatrice pops out of the front door, apparently finished with cleaning up inside."

hilda "\"What took you?\""

#-# >Beatrice frustrated
show beatrice P2_E5
with Dissolve(0.25)
#--#

beatrice "\"Lots of dishes, plus Mom wanted to talk.\""

erik "\"Anything important?\""

#-# >Beatrice smile
show beatrice P2_E2
with Dissolve(0.25)
#--#

beatrice "\"Just that we should visit her more often, eat healthier, flip our mattresses and fix that rattling noise our ventilation system makes when it turns on before it gets worse.\""

erik "\"The usual, then.\""

beatrice "\"Pretty much.\""

#-# >Hilda small smile
show hilda P2_E2
with Dissolve(0.25)
#--#

hilda "\"She's worried about us, is all. You should both be a little more understanding.\""

beatrice "\"You say that, but I'm pretty sure you waited until she wasn't looking before you bolted for the door.\""

#-# >Beatrice big smile
show beatrice P2_E3
with Dissolve(0.25)
#--#

hilda "\"Hmph. Coincidence. Shall we get going?\""

beatrice "\"Yeah! Let's go!\""

n "She does her best to get us moving, but it's not long before things slow down thanks to yours truly."

erik "\"... Sorry. Leg's still out of order.\""

#-# >Beatrice P2_E6
show beatrice P2_E6
with Dissolve(0.25)
#--#
#-# >Hilda P2_E6
show hilda P2_E6
with Dissolve(0.25)
#--#

beatrice "\"Oh. Erik, I'm sorry, I just –\""

erik "\"It's fine. Just give me a minute.\""

n "I give my leg a few experimental shakes to see if I can't coax it into moving more for me today. Months of therapy have allowed me to walk unassisted, but I can still only manage a leisurely stroll."

n "It must be tough to get used to the fact that your younger brother can't move like he used to."

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

#-# >Both sisters dissolve
hide hilda
with Dissolve(0.25)
hide beatrice
with Dissolve(0.25)
#--#
#-# >to city streets (day)
scene ViennaStreet1 at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
with Dissolve(2)
#--#
#-# >Town Theme
stop music fadeout 5.0
pause 0.5
play music "music/Sacher and Karlsbader.mp3" fadein 2.5 loop
#--#

#-# > fade through other bgs
scene ViennaStreet3 at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
with Dissolve(2)
#--#

n "It's a pretty good crowd, for a Saturday. There are lots of people out today – everyone's shopping, eating, and walking around. Beatrice takes us around the streets, pointing to the many landmarks scattered around the city, an excited grin on her face like the hypercaffeinated tour guide she is."


n "Hilda does her best to provide some sense of where we are in relation to the school and to their apartment in case I ever get lost. We all take a U-Bahn route that has a stop one block away from St. Dymphna's shuttle pickup zone, according to the information we got from the brochure."


n "If the brochure is anything to go by, the school encourages students to explore the city (within limits, I assume) for a weekend or class trip. With careful supervision, most students get to visit the city every week."

#-# >Hilda_smile.png center
show hilda P2_E2:
  alpha 0.0 xalign 0.4 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.5 alpha 1.0
show hilda P2_E2 alpha 1.0
#--#

hilda "\"Any place in particular you want to see, Erik? We don't have to follow Beatrice all day, you know.\""

erik "\"Hmm, I'm interested in Stadtpark... Beatrice said that's on this route, right?\""

hilda "\"Yes, it's just a few stops from here.\""

#-# >clear screen
show PitchWhite
#--#
#-# >fade to Park
scene ViennaStreet2 at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
with Dissolve(2)
#--#

n "Stadtpark is quieter than the rest of the city, but there are still a lot of people around today. Most people are walking or riding bicycles. Others are enjoying a late lunch at one of the cafes just outside the park."

n "I'm impressed – it's a lot more lively than I expected. Tourists are clustered around a few notable statues, taking selfies and group shots with their smartphones."

#-# >Hilda_neutral.png enter left
show hilda P2_E2:
  alpha 0.2 xalign 0.3 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.4 alpha 1.0
show hilda P2_E2 alpha 1.0
#--#

hilda "\"Erik, this cafe is fantastic! Let's go inside.\""

#-# >fade to cafe
scene ViennaCafe at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
with Dissolve(2)
#--#

n "The cafe is busy during the lunch hour, with a long line working its way from the entrance to the counter."

#-# >Hilda_smile in to leftcenter
show hilda P2_E2:
  alpha 0.0 xalign 0.2 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.3 alpha 1.0
show hilda P2_E2 alpha 1.0
#--#
#-# >Beatrice_smile in to rightcenter
show beatrice P2_E2:
  alpha 0.0 xalign 0.85 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.75 alpha 1.0
show beatrice P2_E2 alpha 1.0
#--#

beatrice "\"This place has a lot of great snacks and drinks. They cater to the people who come to the park to take walks and exercise here.\""

erik "\"So the fare is pretty light, then?\""

n "Beatrice nods."

hilda "\"We both work near here, so we usually meet up for lunch and a quick walk. It's become one of our favorite hangouts.\""

n "I take a look at what's available. Lots of prepackaged sandwiches, salads, and beverages occupy the shelves."

erik "\"Are these any good?\""

hilda "\"Of course! They make them fresh every day. Here, try this one.\""

n "I don't see how prepackaged chicken can live up to her endorsement, but I accept the sandwich offered. Free sandwiches have their own scale of quality."

hilda "\"This one's my personal favorite. Anything else? I'll buy for you today.\""

n "I dutifully pick out a canned drink and follow Hilda to the cashier."

erik "\"Thanks for lunch.\""

hilda "\"No problem! It's my sisterly duty to treat my little brother on special occasions like this.\""

n "You too, Hilda?"

#-# >Beatrice moocher
show beatrice P1_E3
with Dissolve(0.25)
#--#

beatrice "\"Feel free to treat your little sister as well.\""

#-# >Hilda why
show hilda P2_E1
with Dissolve(0.25)
#--#

hilda "\"What's your special occasion...?\""

#-# >Beatrice cooked
show beatrice P2_E2
with Dissolve(0.25)
#--#

beatrice "\"I cooked breakfast? Aaaaaaand you still owe me from that one time you got drunk and called –\""

#-# >Hilda dubious
show hilda P2_E2
with Dissolve(0.25)
show beatrice P2_E2:
  linear 0.090 xoffset -5
  linear 0.090 xoffset 5
  linear 0.090 xoffset -5
  linear 0.090 xoffset 5
  linear 0.090 xoffset 0
#--#
#-# >Beatrice P2_E6 2
show beatrice P2_E6
with Dissolve(0.25)
#--#

n "A sharp jab into Beatrice's side stops her short."

hilda "\"Ahem.\""

#-# >Hilda ahem
show beatrice P1_E8
with Dissolve(0.25)
#--#

hilda "\"... Chicken or ham, Beatrice?\""

#-# >beatrice_smile.png
show beatrice P1_E4
with Dissolve(0.25)
#--#

n "Beatrice grins in delight, eager to get her free sandwich."

beatrice "\"Ham. And don't worry, I'll pay for my own drink.\""

n "It sounds like they still have that same complex dynamic that still eludes me. With Beatrice being able to cook so well (as well as help out in other places), it seems that she has a lot of influence."



n "As we sit down, the two sisters talk about what they've been up to in the months since I last saw them at home. Beatrice, as usual, dominates the conversation, going on about term papers and unfair professors and how Hilda still couldn't get a boyfriend after all these years, at which point the latter elbow-jabbed her once more into silence."

n "On the surface, they're pretty much the same girls I knew, but years of independence have certainly molded them into something more... mature, I guess? Hearing them talk, and feeling how much they support me after the accident, they now give off a more reliable kind of aura that feels like they've got things all sorted out."

n "Then you have me, crying in the middle of the night and needing to be tucked back into bed by Mummy so the bad dreams don't come back. It feels a bit pathetic. My sisters even went through the effort of going on this little tour to cheer me up."

n "I feel thankful that they're such supportive people, though. I just wish I weren't such a burden to them."


#-# >sister talk
show beatrice P1_E1
with Dissolve(0.25)
#--#

beatrice "\"... Ahh, I remember my time in secondary school, back in Basel. So much drama. So much comforting Hilda after a boy rejec–\""

#-# >jab
show beatrice P1_E1:
  linear 0.090 xoffset -5
  linear 0.090 xoffset 5
  linear 0.090 xoffset -5
  linear 0.090 xoffset 5
  linear 0.090 xoffset 0
#--#

n "Another jab from Hilda and laughter from Beatrice, which thankfully takes me out of my little mental detour before it went some other dark direction again."

hilda "\"Okay, you got me. I suppose I miss secondary school and university a bit. You two should try and enjoy your time in school. Especially you, Erik.\""

n "Since my previous year of school was interrupted, it could be said that I have a lot of youthful escapades that I need to catch up on."

n "How much of those are allowed at St. Dymphna's? No clue."

hilda "\"What I meant was that you should make sure you get the most out of your year at St. Dymphna's. Your therapy obviously comes first, but don't be afraid to let loose every once in a while.\""

erik "\"I'll keep that in mind, thanks.\""

#-# >timeskip
scene ViennaStreet4 at Position(xpos = 1.0, xanchor=1.0, ypos=0.5, yanchor=0.5)
with Dissolve(0.5)
#--#

n "Despite the allegedly light fare, the sandwich is actually pretty filling. Cleaning up the table, all of us head back into the city."

erik "\"So, what's next? Anything you guys want to show me?\""

#-# >Hilda show
show hilda P2_E1:
  alpha 0.0 xalign 0.8 yanchor 1.0 ypos 1080+425+85
  easein 1.0 xalign 0.6 alpha 1.0
show hilda P2_E1 alpha 1.0
#--#
#-# >Beatrice_smile enter right
show beatrice P2_E3:
  alpha 0.0 xalign 0.1 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.3 alpha 1.0
show beatrice P2_E3 alpha 1.0
#--#

beatrice "\"Oh? Well, I guess we can show you some nice date spots around! Right, Hilda?\""

erik "\"Date spots?\""

hilda "\"Of course! There's a lot of good restaurants and parks here if you're going to take someone to a date. Believe me, we've tried them all out. In fact, here. We even arranged a little list of recommendations for you.\""

n "She produces a small piece of blue stationery from her pocket and shoves it in my hand. True enough, it's riddled with a long list of nigh-unpronounceable restaurant names and their addresses, complete with a 10-point scale rating for each of them."

erik "\"That's...\""

n "Beatrice crosses her arms and pouts to silence any forthcoming objection."


beatrice "\"Erik, you're eighteen now, and that means you're a man in the Wilhelm household. If one of our siblings doesn't know the lay of the land, he is doomed to romantic failure. It's our duty as sisters to help you out!\""

erik "\"... Did you bug Gustav like this too before he moved out? That'd explain why he'd rather be out in the mountains...\""

n "..."

#-# >Beatrice P2_E6 3
show beatrice P2_E6
with Dissolve(0.25)
#--#
#-# >Hilda P2_E6 2
show hilda P2_E6
with Dissolve(0.25)
#--#

n "I meant it as a joke, but it looks like it fell flat, and then some."

beatrice "\"Uh, well, that is...\""

n "..."

erik "\"I'm sorry, I was just kidding.\""

hilda "\"... that's not it, Erik. It's just...\""

n "..."

n "I feel my face burning red from embarrassment. I just made an entire afternoon incredibly awkward."

n "Great job, me."

hilda "\"Do you miss him, Erik?\""

n "That's hard to say. I mean, what happened between us was..."

erik "\"... A bit, yeah.\""

beatrice "\"Well, we do too. He's been distant from most of us.\""

n "I guess it's good to know that I'm not all alone in this."

n "... But it still hurts."

erik "\"Anyway! I guess I've got to thank you guys. For today... for all this. This was really nice.\""

n "My voices falters a bit, as a small lump coalesces within my throat."

n "I try to mask it with a little chuckle as soon as the words leave my lips, but the slight furrowing of my sister's brows tells me they easily caught the hesitance in my tone."

#-# >both sisters out
#
#--#
#-# >both sisters in closer (both smiling)
show hilda P1_E4:
  easein 1.0 alpha 1.0 xalign 0.6 yanchor 1.0 ypos 1080+425+85+500 zoom 1.5
show hilda P1_E4 alpha 1.0
show beatrice P1_E2:
  easein 1.0 alpha 1.0 xalign 0.3 yanchor 1.0 ypos 1080+425+500 zoom 1.5
show beatrice P1_E2 alpha 1.0
#--#
n "Before I could say anything else, they give me two big, comforting smiles, walk up to me and wrap their arms tightly around my shoulders in a group hug."

erik "\"Hey... what the hell...\""

n "Any other time I would've objected to this kind of gesture especially since we're in public, but I don't put up much resistance."

n "It feels nice – their warmth a gentle, familiar reassurance in the midst of this deluge of strange new sensations and confusing stew of thoughts and emotions."

#-# >both sisters back in, smiling
show hilda P1_E4:
  easein 1.0 alpha 1.0 xalign 0.6 yanchor 1.0 ypos 1080+425+85+250 zoom 1.25
show hilda P1_E4 alpha 1.0
show beatrice P1_E2:
  easein 1.0 alpha 1.0 xalign 0.3 yanchor 1.0 ypos 1080+425+250 zoom 1.25
show beatrice P1_E2 alpha 1.0
#--#

n "As they release me, I feel as if something heavy in my chest is melting gradually into nothingness."

beatrice "\"Anything for you, baby bro! We're family – we'll always stick together!\""

hilda "\"Yep. That's our duty.\""

beatrice "\"Also, you look a lot uglier when you're sad, you know? I mean, more so than usual, that is. Haha!\""

erik "\"Hey, that's just uncalled for.\""

n "I take in a lungful of the cool afternoon air and return a big smile to match theirs. They may be overly doting at times, but I know it's always sincere."

#-# >both sisters move out
show hilda P1_E4:
  easein 1.0 alpha 1.0 xalign 0.6 yanchor 1.0 ypos 1080+425+85 zoom 1.0
show hilda P1_E4 alpha 1.0
show beatrice P1_E2:
  easein 1.0 alpha 1.0 xalign 0.3 yanchor 1.0 ypos 1080+425 zoom 1.0
show beatrice P1_E2 alpha 1.0
#--#

hilda "\"Feeling better now?\""

erik "\"... Yeah.\""

n "Knowing that my sisters have my back is reassuring. I know it probably never had to be said out loud, but for me right now, this is something I think I needed to hear before I go to Saint Dymphna's."

#-# >ping
play sound "music/effects/Phone alert.mp3"
#--#
#-# >Beatrice_neutral.png
show beatrice P1_E1
with Dissolve(0.25)
#--#

n "Beatrice's cell phone pings. She takes it out to read it, then frowns."

#-# >Beatrice_frown.png
show beatrice P2_E5
with Dissolve(0.25)
#
show hilda P2_E1
with Dissolve(0.25)
#--#

beatrice "\"Sadly, this concludes our regrettably brief tour of Vienna. We need to meet back with Mom and Dad for dinner.\""

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

n "We make a dash, or the best I can manage with my leg, back to the station, almost missing the next tram back home."

#-# >fade to black
stop music fadeout 5.0
show PitchBlack
with Dissolve(2.0)
#--#

#-# <end>
#
#--#

########

jump A1_04 # jump A?_??
