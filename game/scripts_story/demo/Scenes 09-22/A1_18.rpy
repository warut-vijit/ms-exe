label A1_18:
###############

$ scene_number = "A1_18" # current scene
$ scene_name = "Ela Sahin's Checkup"
$ renpy.save_persistent()

# Scene 18
# Scene name: Ela Sahin’s Checkup
# 
# BGs:
#     Erik's room (night)
#     Claes' classroom (afternoon)
#     cafeteria (afternoon)
# 
# Music:
#     ?
# Sprites:
#     Ela
#     Claes

#--# <[timelapse to] Erik's room (evening)>
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene erikdormnight with Clockwipe
#--#

n "Hours later, I'm holed up in my dorm room, buried in physics equations."
n "It's amazing how fast this stuff piles up. Two nights ago, I was wondering how I would ever pass the time. Here's my answer, I guess."
n "I scratch the last answer down on the bottom of the notebook page and sit back in the chair."
n "45?"
n "It's wrong. It's definitely wrong. But it's also the last problem of the night and I can't convince myself to work the numbers again."
n "I close the notebook with a satisfying thump, happy enough to be done with the work, compromise or no."
n "Coasting through material like this probably shouldn’t be so easy, but being the new kid surely gives me some leeway."
n "Surely."

#--# <[timelapse to] Claes' classroom (morning)>
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene classroom1 with Clockwipe
#--#

n "Class the next day is rather uneventful. Most periods are taken up by lecture time except for a small class discussion in philosophy."
n "I'm awake through all of them, at least. I slept better last night. Still woke up early – and didn't watch the sunrise with any pretty girls, but I still think it's an improvement."
n "At the very least, let's call it an even trade."

show claes P1_E1:
  xalign 0.4 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.4 alpha 1.0

claes "\"And the last equation? Don't be afraid to give the wrong answer; I expect it gave you all some trouble.\""

n "Ms Claes' question nudges me back into the present. I've been absent-mindedly ticking off the problems as we go, and even if I got them right, I wasn't listening closely enough to know why I got them right."

n "No one's jumping to answer this last question, though."

claes "\"Anyone?\""

n "The silence is killing me. I raise my hand."

erik "\"I got 45.\""

show claes P1_E5
with Dissolve(0.25)

claes "\"45 Newtons? That's correct. Did anyone else find the same answer?\""

n "Only a couple other hands go up. One of them belongs to Ela, who glances in my direction with a proud smile."

#--# <[minor timelapse]>
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene classroom1 with Clockwipe
#--#

n "Class breaks for lunch, a small crowd forming around the door as my fellow students rush for the exit."

n "I take my time packing my bag, not wanting to shove my way through, before a voice pulls my attention from the door."

# >ELA IN
show ela P1_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.75 alpha 1.0

ela "\"I see you’re adjusting well!\""

n "Ela bounds over, having only just finished stowing her own books, standing in my peripheral vision with hands neatly clasped behind her back."

#-# >Ela(Smiling P1E2)
show ela P1_E2
with SDis
#--#

erik "\"Thanks. It’s been going better than I thought it would.\""

ela "\"I’m glad to hear it, and to see you answering tough questions like that shows great initiative in your studies.\""

n "Does it?"

ela "\"...It was more of a guess than anything…\""

ela "\"An educated guess. Don’t sell yourself short!\""

n "She punctuates the word with a little flourish, far prouder of my accomplishment than I am."

ela "\"Sorry, just trying to be humble. That way when I suck, no one will be surprised.\""

n "Ela’s good cheer seems to sour a little, but she falls into step with me as I zip my bag regardless."

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"Besides, you raised your hand, didn’t you? I don’t see you bragging.\""

ela "\"Yes, but I’ve been in this class since the start of the semester. It’s not unusual for transfer students to come here with a few holes in their studies.\""

ela "\"That’s not to say they aren’t intelligent, but every school has a different curriculum , after all, so I’m always a little worried.\""

ela "\"That makes two of us...\""

n "We follow our classmates as they file into the hallway, joining the river of students on their way to lunch."

#--# <[timelapse to] cafeteria (afternoon)>
scene PitchBlack with Clockwipe
$ renpy.pause(1.0)
scene cafeteria with Clockwipe
#--#

## ela sprit1 still in scene##
show ela P1_E1:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0

n "For all its concessions and planning, the cafeteria is still ordered chaos, and Ela wastes no time scouting out a location for us."

n "I can’t help but feel out of place, watching the other students all file to their routine seats while I stand to the side, awkwardly holding a tray of sandwiches."

n "Sandwiches might be the only constant in my life right now."

n "Fortunately, Ela waves me over from a table, sitting alone at a comfortable distance from all the established cliques."

n "Her lunch is a picturesque assortment of items, and I can’t shake the feeling that she’s chosen it specifically to meet, but not exceed, all her nutritional needs."

n "I try not to think about what my selection says about me as I sit across from Ela."

erik "\"Thanks. I was just going to eat alone; I’m not sure who I should be sitting with yet. Don’t want to impose, you know?\""

n "Ms. Claes’s advice on ‘social pressure’ seemed a little too direct to be dismissed out of hand."

show ela P1_E2
with SDis

ela "\"Of course! It’s definitely good to give people space, but you’re a new student: most of us are more than happy to get to know you. I’m sure you’ll fit right in.\""

ela "\"With your uniform on, sometimes I forget you’ve only just gotten here.\""

n "She points at the jacket, which reminds me just how weird I feel in this outfit."

erik "\"Well, you know. I thought it would be best if I started dressing like the locals.\""

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

n "Ela lets out a polite laugh and leans over to straighten out my collar."

ela "\"It looks good on you. Really.\""

n "That compliment is a little too sincere for me, but I manage to mumble a ‘thanks’."

n "To her credit, Ela is quick to change the subject."

ela "\"So, what do you think of our teachers?\""

erik "\"Well, Ms. Claes isn't too bad. Hertha seemed nice. And... um... Mr. Köhler? I guess he's okay.\""

#-# >Ela(Smiling P1E2)
show ela P1_E2
with SDis
#--#

n "Every second I fumble around looking for names, the smile on Ela's face gets wider."

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"Okay, okay! I get it. Too early for that question. You'll get a better feel for them after a few days.\""

ela "\"A lot of people aren’t too fond of Ms. Claes, I’ll admit. I think it's because she's kind of strict about the rules. Just be sure not to get on her bad side and you'll be fine.\""

n "Don't get on her bad side... "

n "Seems more like the kind of general advice that would apply to just about anyone, though."

erik "\"Got it.\""

n "She nods, turning to her lunch again."

ela "\"Made any friends yet?\""

n "Fran comes to mind first. There’s a terrifying thought. "

n "There's also Natalya, and Katja seems pleasant. I might even consider Jeanne a friend, although right now our only shared experience involves a nosebleed."

ela "\"What's on your mind? How are you holding up? Come on – you must have a ton more questions. Hit me.\""

label A1_18_menu:
label MENu3:
if (persistent.skip_menus):
  "{color=#ff8c00}>Question time{/color}"
  jump A1_18a
menu:
  "\"I'm fine.\"":
    $ kb_tot += 1
    $ ak_tot += 1
    $ persistent.A1_18 = 1
    jump A1_18a

  "\"I'd like to meet people. Maybe join a club.\"":
    $ lf_tot += 1
    $ nv_tot += 1
    $ persistent.A1_18 = 2
    jump A1_18b

  "\"I'm worried I might fall behind.\"":
    $ jl_tot += 1
    $ persistent.A1_18 = 3
    jump A1_18c

  "\"It's a little overwhelming.\"":
    $ ig_tot += 1
    $ persistent.A1_18 = 4
    jump A1_18d

#-# >CHOICE #1: "I'm fine." (+1 Katja, Anna)
label A1_18a:
#-#

erik "\"I'm fine.\""

#-# >Ela(Disappointed P1E8)
show ela P1_E8
with SDis
#--#

n "The exaggerated disappointment on her face makes me feel like I’ve kicked a puppy."

ela "\"Oh, c’mon, Erik. ‘I’m fine’ is the most worrying thing you can say around here.\""

n "Am I not allowed to be fine?"

erik "\"I’m just saying my problems aren’t something anyone should worry about.\""

erik "\"They’re tiny, stupid problems.\""

ela "\"No one has tiny, stupid problems.”\""

erik "\"Okay, {i}fine{/i}, but they still aren’t something you should worry about.\""

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

n "Ela breaks eye contact, putting her hands up in a gesture of surrender, turning back to her food, and I relax a little."

n "I wasn’t even aware I was tense."

n "This happened last time we talked, didn’t it? Ela wants to help me, I know. Everyone does."

n "What would help me most right now is having a normal, friendly conversation for once."

erik "\"Sorry, that probably came out wrong. I’m just saying— \""

show ela P1_E6
with SDis

ela "\"I know, I know, I’m probably pushing too hard. Dr. Faber said the same thing.\""

ela "\"I tend to get ahead of myself a lot, and it makes people defensive. You don’t have to talk about anything if you don’t want to.\""

n "And now I have to."

erik "\"I just don’t have anything to talk about. I’m really not that interesting, and I barely know anyone’s names yet.\""

ela "\"Well, that's normal for a transfer student, isn't it?\""

erik "\"I suppose you're right.\""

show ela P1_E1
with SDis

ela "\"Just take things at your own pace and you'll know plenty of people before the month is over.\""

ela "\"Besides, you've already talked to some classmates, right?\""

n "A few classmates have asked me questions and had snippets of conversations in passing, so I guess that counts as something?"

erik "\"Yeah, I suppose.\""

#-# >Ela(Smiling P1E2)
show ela P1_E2
with SDis
#--#

ela "\"See? That's progress!\""

show ela P1_E1
with SDis

n "It's like she said earlier."

n "{i}Don't sell yourself short.{/i}"

erik "\"All right. I'll take your advice and do things at my pace for now.\""

show ela P1_E2
with SDis

ela "\"Sure!\""

erik "\"Also, thanks for talking to me. It's… nice being able to talk to someone about this.\""

n "Ela gives me a sympathetic nod."

ela "\"You're welcome.\""

ela "\"Anything else you need from me?\""

erik "\"Nah, I think if I have anything else, I'll be sure to ask you about it. Sound good?\""

ela "\"Perfect!\""

n "Ela looks down at her watch."

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"Well, sorry to cut this short, but I have to head off now. I'll see you later, Erik!\""

#>ELA OUT
show ela P1_E1:
  easein 1.0 xalign 0.55 alpha 0.0

n "I give her a wave as I bite into my sandwich."

n "Soon after, the cafeteria empties out as students start up their afternoon classes."

n "I dutifully take my leave as well, mulling over Ela's advice."

#-# <END>
jump A1_18end

#-# >CHOICE #2: "I'd like to meet people. Maybe join a club." (+1 Lena, Nat)
label A1_18b:
#-#

erik "\"Now that you mention it, I'd like to get to know more people around here.\""

n "\"Get to know\" being the key phrase. Not just meet. Preferably without injuring them."

erik "\"I guess I'm kind of interested in joining a club, maybe?\""

#-# >Ela(Smiling P1E2)
# Needs to have a more excited expression here
show ela P1_E2
with SDis
#--#

n "Ela’s eyes light up, immediately shoving her plate to one side to make room for her backpack."

ela "\"Ah, well, there are lots to choose from! Chess club, newspaper club, book club, art club... A lot of smaller ones, too... I couldn't possibly remember all of them off the top of my head.\""

ela "\"Here, hold on a sec.\""

n "I catch a glimpse of the neatly organised folders and several binders of color coded notebooks, each with its own array of divider tabs."

n "It's the purple one that she pulls out and flips through until she's found whatever it is she's looking for."

ela "\"Here.\""

n "The notebook is simply labeled ‘Clubs’, but even a cursory glance shows dozens of tabs, presumably one for each of them."

n "The list of organisations is staggering. I don't know where to begin."

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"This is all the officially recognised clubs, anyway. So, it's a place to start.\""

erik "\"Wow... this is...\""

show ela P1_E3
with SDis

ela "\"Too much?\""

erik "\"You could say that.\""

show ela P1_E1
with SDis

ela "\"It's not as bad as it looks. You could narrow it down a little, too. What are you interested in?\""

n "History is the first thing that comes to mind, but history clubs tend to be... stuffy, to say the least."

n "Hiking… is probably off the table for the time being."

erik "\"I'm not sure.\""

ela "\"There's always the newspaper club. Since you're new here, it would be a great way to get a feel for the school. But it's also a pretty daunting job.\""

ela "\"...Since you're new here.\""

erik "\"I've been down there already, actually. It was, uh... interesting.\""

ela "\"So you've run into Lena already, huh? Don't let her scare you off. She's not as scary as she looks.\""

erik "\"Uh-huh.\""

ela "\"Really! You should give it another shot. Besides, you'd get to hang out with Hertha. Miss Wieck, I mean.\""

erik "\"I'll think about it.\""

n "I don't know what sort of help I can be to the school newspaper if I know nothing about the school.  Still, it's worth a shot, and there's plenty of time to look at the other clubs too."

erik "\"What time do they meet?\""

#-# >Ela(Smiling P1E2)
show ela P1_E2
with SDis
#--#

ela "\"That's what the list is for, silly.\""

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

n "Sure enough, there are room numbers and meeting times printed down the right side of the sheet of paper I'm still holding in my hand."

erik "\"I guess I'll probably take a look.\""

ela "\"Great! If you do, just don't let them scare you away, okay?\""

erik "\"You already said that.\""

ela "\"Of course, you’re right, don’t worry about it.\""

n "I’m fairly worried about it now."

ela "\"Let me know how it goes. And if you have any more questions, don’t hesitate to ask!\""

n "Ela rushes through the rest of her food before neatly tucking her myriad folders back into her bag."

ela "\"Gotta go! See you around, Erik!\""

#>ELA OUT
show ela P1_E1:
  easein 1.0 xalign 0.55 alpha 0.0

n "I give her a little wave, my mouth occupied with a sandwich as Ela heads off."

n "I'm left to finish my lunch alone, but at least I've got something to think about."

#-# <END>
jump A1_18end

#-# >CHOICE #3: "I'm worried I might fall behind." (+1 Jeanne)
label A1_18c:
#-#

erik "\"I'm a little worried I might fall behind.\""

#-# >Ela(Serious P1E6)
show ela P1_E4
with SDis
#--#

ela "\"Oh, no. You did pretty well on that homework last night.\""

erik "\"I guess. But I kind of muddled through it. I'm not sure how I got that last question right, honestly.\""

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"We could get you a tutor!\""

n "A bit too much excitement there, Ela."

erik "\"I don't think I'm that far gone yet. Just trying to stay ahead of things.\""

ela "\"Right, that's the perfect time for a tutor! It's easier to help you out if you aren't behind yet.\""

n "True, but..."

erik "\"I don't know.\""

ela "\"Some friends of mine have a study group, if you're interested.\""

erik "\"I guess I'd be okay with it if it wasn't one-on-one.\""

ela "\"I'll talk to them. We'll get everything sorted out no problem. You're in good hands, Erik!\""

#-# >Ela(Smiling P1E2)
show ela P1_E2
with SDis
#--#

n "Her job well done, any worry that was on Ela's face is replaced with a grin."

ela "\"Um, do I get to know whose hands those are?\""

ela "\"If I can get them to agree to it, sure, but I don’t want to pressure anyone. I’m sure they’ll be happy to help!\""

erik "\"All right. I'll trust you on that front. Thanks, Ela.\""

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"Uh huh! Any time."

n "She scoops up the rest of her lunch and starts to head off."

ela "\"I have something I need to take care of now, so I'll see you later!\""

#>ELA OUT
show ela P1_E1:
  easein 1.0 xalign 0.55 alpha 0.0

n "I wave her off as I finish my lunch."

n "The prospect of a tutor feels daunting, but I feel that Ela's probably right in that I should take care of things now before I fall behind."

#-# <END>
jump A1_18end

#-# >CHOICE #4: "It's a little overwhelming." (+1 Isolda)
label A1_18d:
#-#

erik "\"I don't know... It's a little overwhelming.\""

#-# >Ela(Serious P1E6)
show ela P1_E6
with SDis
#--#

ela "\"What is?\""

erik "\"The school. Everything. I'm not complaining; I guess you could just say I'm not quite sure where I fit in here yet.\""

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

ela "\"Hey, that's nothing to worry about. You'll figure it out in no time!\""

ela "\"A lot of kids feel that way when they first get here, but I think you'll end up loving it as much as I do.\""

n "Ela, sometimes I worry that you're too optimistic for your own good. On the other hand, it seems to work out pretty well, so maybe if you could infect me with some of that optimism..."

ela "\"It's a big family here. I know it's a little tough when you haven't grown up here like a lot of the students have, but it was the same for me, you know.\""

ela "\"Did I tell you that?\""

n "I try to answer, but she's on autopilot."

ela "\"Just make sure you meet lots of people, and get into school activities... clubs, that sort of thing.\""

ela "\"There's also a Erntedankfest celebration coming up, with an open house, gala, everything. It's a lot of fun, and you get to dress up all fancy!\""

erik "\"Isn't that next weekend?\""

ela "\"The one after this one, yeah.\""

erik "\"That's kind of short notice.\""

ela "\"Oh, come on! It'll be fun. You've got plenty of time.\""

#-# >Ela(Winking P1E5)
show ela P1_E5
with SDis
#--#

ela "\"You might even be able to find a nice girl to go with.\""

#-# >camera shake
scene cafeteria with hpunch 
show ela P1_E5:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0

n "Is she... hinting at what I think she's hinting at? I really can't tell with Ela, unfortunately."

#-# >Ela(Neutral P1E1)
show ela P1_E1
with SDis
#--#

erik "\"That doesn't seem very likely.\""

ela "\"You never know. I have faith in you, Erik.\""

n "I open my mouth to speak but receive a boop on the nose instead."

ela "\"So, you're coming?\""

erik "\"Maybe.\""

ela "\"So, you're coming.\""

erik "\"Perhaps.\""

n "She shrugs. "

ela "\"Eh, I guess that's good enough for now. I've actually got to go help out with some of the decorations for the dance right –\""

#-# >Ela(Alarmed P1E4)
show ela P1_E4
with SDis
#--#

ela "\"Wah! Oh my gosh!\""

n "She does a quick double-take on her phone's screen."

erik "\"Huh?\""

ela "\"How did it get to be this late? Sorry, I've got to go!\""

erik "\"Um... okay.\""

n "There isn't a chance to say much more before Ela flutters off toward the door. As she jogs between cafeteria tables, I can hear her say,"

ela "\"I'll see you later, Erik!\""

#>ELA OUT
show ela P1_E4:
  easeoutright 1.0 xalign 0.55 alpha 0.0

n "The lunch period is almost over, so I hurry to finish what turns out to be a rather unappealing meal. I wouldn't call them plans, but I've got some stuff I can check out later, and that's something."

#-# <END>
jump A1_18end

label A1_18end:
scene PitchBlack with Clockwipe

jump A1_19 # jump A?_??
