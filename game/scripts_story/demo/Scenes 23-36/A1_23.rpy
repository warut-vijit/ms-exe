
label A1_23:
###############

$ persistent.scene_number = "A1_23" # current scene
$ persistent.scene_name = "Morning, With Additions" # current scene name
$ renpy.save_persistent()

#-# <scene open>
scene erikdormcloudy
#Temporary audio stops
stop music fadeout 1.0
stop music2 fadeout 1.0
stop ambience fadeout 1.0
stop ambience2 fadeout 1.0
#--#

#<Erik's room (evening)#>

n "Wise or not, I leave the door to my room open for the first time while I run to the toilet and get ready for bed."

n "The only person I can imagine sneaking in there to cause mischief is Irene, and she's filled her quota for the day. I'd say the risk is relatively low."

n "All washed and minty-breathed, I return to the room to find it seemingly un-molested. A minute later, my uniform traded for something a little more comfortable, I settle in for some late-night web-surfing."

n "Mostly, though, my web-surfing involves floundering around in the shallows of my email, getting tired, and then deciding to go to sleep instead."

n "Tonight, aside from the ubiquitous daily newsletter, there's only one message to read:"

#<CG of Erik's phone#>
show EriksPhone
with Dissolve (1.0)
#

n "{i}Mr. Wilhelm,{/i}"

n "{i}If you would be so kind, please stop by my office before class tomorrow morning. There are several things regarding your studies which I would like to discuss with you.{/i}"

n "{i}Best regards,{/i}"

n "{i}Edna Claes.{/i}"

#
hide EriksPhone
with Dissolve (1.0)
#

n "Short and to the point, as I've come to expect of her. If to the point means being vague and conjuring up a thousand and one possible horrible reasons for Claes to email me."

n "Did I fail that first test? Am I failing? Getting expelled?"

n "All of the above?"

n "Well, sitting here and worrying about it won’t be good for my health."

n "For a few more minutes, I click back through previous emails. I read a few older newsletters – that I skipped over the first time – and scan the \"What's new on campus!\" sections, full of events that have already gone by."

n "When I'm tired of that, I close up shop and take my metaphorical surfboard to bed."

##>timeskip
scene PitchBlack
with Clockwipe
scene erikdorm
with Clockwipe
##>show Erik’s room (day)

n "I know I've only been in class for a few days, and that I'm a new student here…"

n "But still, I hope that that email I got doesn’t mean anything serious is going to happen."

n "I suppose there’s no worrying about it at this hour. I’m too tired to think about it too much."

##>crossfade to classroom (day)
scene classroom1
with Dissolve (2.0)
#

n "Before the rest of the students even arrive I find her at my classroom, where she's getting today's lesson plan ready."

erik "Uh, good morning, Ms. Claes. I got your email the other night – you had something to talk to me about?"

#>show claes neutral at center

claes "Ah, thank you for coming, Mr. Wilhelm. I've been meaning to talk to you about your studies for a while."

erik "Is there something wrong?"

n "Might as well clear the air. No sense beating about the bush."

##>claes smile

claes "No, Mr. Wilhelm, not at all. I asked for you to come in before class because I would like to offer you some help in regards to your future schoolwork."

n "Not as bad as I thought, I guess."

erik "What do you mean?"

claes "Well, St. Dymphna's has had a proud tradition of accommodating students who require study materials, resources, and on-campus tutoring."

#>claes neutral

claes "I think you could excel here, but after looking at your scores from your entrance exams, you could use some help."

n "She's right on that one. Math and science never came easily to me. The only subjects I excelled at were history and geography, mainly because of my interests in hiking and being outdoors. "

n "It also doesn't help that this antidepressant I'm on causes drowsiness, too. It’s tough getting out of bed, let alone staying awake in class. I’m pretty sure Ms. Claes has noticed that part by now."

#>claes smile

claes "If possible, I'd like for you to–"

#>knock

claes "Oh, come in!"

#>claes move to left
#>show jeanne neutral at right

n "From outside, a girl enters the room. Surprisingly, I've met her before."

erik "Jeanne?"

jeanne "Oh, hello Erik!"

#>claes surprise

claes "You two have met?"

#>jeanne smile

jeanne "Yes, we're in the same physical education class."

#>claes neutral

n "One could say we had an \"impactful\" encounter, so to speak."

#>click

claes "I see, then that makes things a bit easier if you two know each other already."

erik "What brings you here, Jeanne?"

#>jeanne neutral

claes "As I had been saying previously, we have on-campus tutors for students that need an extra hand with assignments."

claes "Ms. Lefevre is one of the few student tutors here on campus, and I asked her to assist you with your schoolwork."

#>claes smile

claes "I recommend you try studying with Jeanne for a few sessions. If it’s not something you like, we can work out something for you later."

n "Well, what have I got to lose? It’s not often that things like this happen – free help with schoolwork, that is – and I would probably have asked for help at some point during the school year. How bad could it be?"

erik "Alright, I’ll give it a shot."

claes "Well, that settles it. Jeanne, why don't you set up a schedule with Erik here? I'll leave you to it."

#>jeanne smile

jeanne "Yes, ma’am!"

#>claes exits
#>jeanne move to center

n "Jeanne turns to me, handing me a small folder."

jeanne "Since I'm going to tutor you, I'd like to ask you a few questions, just to break the ice a little."

#>click

n "It's still way too early for an interview. But, I did say I'll try this."

n "I try to hold in a yawn. I fail."

erik "Sure. Have at it."

jeanne "Okay, so, question one: Where are you from?"

erik "Basel-Stadt. I lived on the outskirts."

jeanne "So... near Switzerland, right? We have a few students from there, last I checked."

#>click

n "Neat, I suppose." 

erik "What about you?"

#>Jeanne laugh

jeanne "Couldn't you tell? I'm a proud French<i#>woman.</i#>"

#>jeanne smile

n "She speaks the last syllables with an even heavier French accent."

jeanne "I’m from the west coast, near Nantes."

#>click

erik "Well, bonjour to you, mademoiselle."

#>Jeanne laugh

n "She raises her eyebrows in mock surprise."

jeanne "So polite!"

#>Jeanne neutral

jeanne "Now, ask me a question. Anything you want to learn about me, go ahead."

n "Ah, there was that thing I was interested in…"

erik "This is something I was curious about. You mentioned you had Tourette’s, right?"

n "Jeanne nods."

erik "Don’t take offense but... Is yours, um, different than others?"

#>jeanne puzzled

jeanne "Hmm… Like, different from how the media plays it out? Constant, vulgar language at the ends of my sentences? Random screaming and twitching?"

#>click

erik "Uh, yeah. That."

n "I feel really awkward asking that, but Jeanne doesn’t look phased at all." 

#>jeanne neutral

jeanne "Well, that’s actually a very small number of people with Tourette’s. It gets a lot of media attention because it’s so shocking. But in reality, most patients just have minor verbal or motor tics."

erik "Ah, okay, makes sense. Sorry for asking that all of a sudden."

#>jeanne smile

jeanne "No worries! Lots of my classmates asked the same questions when I first transferred. I’m used to it."

n "Clearly, she’s practiced this speech before."

erik "I was afraid I’d asked something a little too personal."

#>jeanne neutral

jeanne "Well, for some people, it would be. Students here are have varying degrees of openness. I just happen to be more open about my Tourette’s."

jeanne "It’s something I’ve come to terms with, and I do my best to make sure everyone’s questions are answered."

#>click

jeanne "After all, I’ll be tutoring you. It’s part of my job to answer your questions."

n "I wish I could have the same attitude about my problems. Jeanne’s honesty is really refreshing, especially at this hour."

erik "That’s pretty cool, Jeanne. I’m glad I learned that from you!"

#>jeanne smile

jeanne "Really? You’re welcome! I’m always happy to help."

#>click

jeanne "Now I’d like to ask you a question."

erik "Sure, ask away."

jeanne "Do you have any hobbies? Anything unique?"

n "How do I answer this one tastefully?"

n "{i}Yeah, I used to hike until I fell off a mountain.{/i}"

erik "Well, I do a lot of outdoors stuff."

n "Okay, that’ll do."

erik "Mostly hiking nowadays."

n "Not bad."

erik "Other than that not much else. I’m glad there’s a walking trail here on campus, or I’d probably get some kind of cabin fever."

#>jeanne smile

jeanne "Sounds like a very involved hobby. I walk the trails too; it’s where my club meets up. Oh — I run the astronomy club here on campus, so I’m used to going out to do some stargazing."

erik "Really? That sounds pretty interesting. What do you all do?"

jeanne "The way I run things, we generally do research activities to learn more about topics related to astronomy. We also do bi-monthly stargazing sessions using telescopes!"

#>click

erik "Wow, almost sounds like another class from the way you describe it."

#>jeanne laugh

jeanne "Well, I’m not as strict a teacher, that’s for sure!" 

#>jeanne smile

jeanne "It’s pretty laid-back, but I try my best to encourage participation."

erik "How long have you been doing it?"

jeanne "I became President only recently, but I’ve been in the club my whole time here. It’s been a lot of fun."

n "Maybe joining a club full-time wouldn’t be half bad. The newspaper club is at least led by Lena, who’s probably just as passionate about journalism as Jeanne is."

n "Jeanne’s given me something to think about."

erik "I’m glad you’ve had fun with your club. That’s really neat stuff you’re doing." 

#>jeanne smile

jeanne "I sure think so!"

#>click

#>jeanne neutral

n "Jeanne reaches into her bag and opens up a small notebook."

jeanne "Oh, before I forget, let’s see… my schedule is pretty open today for tutoring. How about we meet up in the school library at… 17:30?"

#>click

erik "That works for me. I don’t have anything going on after school."

#>jeanne smile

jeanne "Perfect!"

jeanne "I'll see you later, Erik! Gotta get to my next class."

erik "Sounds good. See you later."

jeanne "Okay!"

n "Jeanne makes her exit."

#>claes neutral enter from left

claes "Ah, did Jeanne leave already?"

erik "Yeah, she had to get to class."

#>claes smile

claes "I see. Well, take your seat for now. Your classmates will be here in a minute."

########

jump A1_24 # jump A?_??
