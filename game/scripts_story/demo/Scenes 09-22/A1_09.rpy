
label A1_09:
###############

$ scene_number = "A1_09" # current scene
$ scene_name = "The Art of Introduction " # current scene name
$ renpy.save_persistent()


# Scene name: The Art of Introduction 
#-# <Scene Opens>
stop ambience fadeout 1.0
#--#
#-# <Boy's Dorm Exterior (morning)> crossfade to <School Cafeteria (morning)>
scene outsidemaledorm
with Dissolve(2)
scene cafeteriaoutside
with Dissolve(2)
#--#
#-# >>Cafeteria Background Sounds
play ambience "music/effects/covfefeshop.ogg" fadein 3.0 loop
$ renpy.music.set_volume(0.2, 0.0, "ambience")
scene cafeteria
with Dissolve(2)
#--#
#-# >>Music: Be Violet (1), Be Violet (2) playing underneath at 0 volume
play music "music/Be Violet 1.mp3"
$ renpy.music.set_volume(0.0, 0.0, "music2")
play music2 "music/Be Violet 2.mp3"
#--#

n "The cafeteria's already half full by the time I make it. I don't even need to limp all the way inside to tell. You can hear the students inside talking right from the hallway. I'd hoped for some half empty table, but wherever I look, it's just people sitting and talking."
n "Some converse over their food. Others are shouting jokes and insults to friends on the other side of the room. A few actually look like they've finished and just don't feel like getting up."
n "A line of students holding out trays and clutching handfuls of plastic utensils stretches through the hall, all chattering excitedly at each other."
n "Before coming here, I had this mental image of patients queuing up at an institution, lining up in their sterile gowns for the nurse to fill their little polystyrene cups with their ration of color-coded pills."
n "I knew that it couldn't be that bad, but a part of me wouldn't believe that."
n "I was afraid that coming here would bring it back up, but the reality just doesn't sustain it."
n "That bleak fantasy demands an air of oppressive silence, but everyone here is so lively and active. It demands that it smell of antiseptic and bleach, but all I can make out is meat and pastries and sliced fruits."
n "And that's great. That's better than great. It's reassuring. It's normal."
n "So why do I feel like I just can't blend in?"
#-# >>Music: Slow crossfade Be Violet (1) into Be Violet (2)
stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 5.0, "music2")
#--#
n "Everyone's just so busy doing things that they know how to do, talking to people they're already friends with. Everyone looks like they have such a clear direction, and I don't even know where to start."
n "I'm not really 'with' these people. What if we talk and they don't like me? What if they make fun of my limp? Just because they are childish fears doesn't mean they don't matter."
n "And it's not just that, too. They all look fine right now, but I can't just forget where I am. This place can't be just like any other school, by definition."
n "The rules for fitting in here can't possibly be the same. What if I make some terrible faux-pas because I don't know how things work here and they take offense?"
n "I stop a few paces past the door, before even taking my own tray."
n "I don't need this headache right now. It's a little defeatist, but I genuinely think that at this point just getting some fresh air would be better."
n "Vending machine food was good enough for me this morning; if it means not having to sit down in here, it's going to do just fine now."
n "I didn't have much of an appetite, anyway. And I can always come back here once I've made myself a little more comfortable. I've got almost the entire year ahead of me. There'd be nothing to gain from forcing myself over ten more minutes."
#-# <School Cafeteria (morning)> crossfade to <School Corridor (morning)>
stop music fadeout 5.0
scene cafeteria
with Dissolve(2)
scene classroomhall2
with Dissolve(2)
#--#
n "There's a sitting area next to the cafeteria, complete with benches and a vending machine. A few students are gathered around it, but they seem to be going through pretty quickly. I pull out my wallet and get in line, hoping no one will try to talk to me."
n "Thankfully, most just take their sandwiches and leave rather than lingering around. Soon, the corridor is left blissfully silent and the only person besides me is the tall, blonde girl in front of me in line."
n "She hums softly to herself as she approaches the machine. Thinking about it now, maybe she has been for a while, and it was just hard to hear because of everyone else. It's not something you normally notice, but crazy as it sounds, she hums... {i}really{/i} well."
n "The tune is clear, yet complex enough to catch the ear. The high and low notes mix so seamlessly you barely notice them shifting. I've heard people singing on purpose and not sounding so good."
n "I lift my eyes to her in time to see her reaching down for her purse, but before she can pull out any change, she instead stops humming and turns around to face me."
#-# >Katja_P5_E1 enter from right to center (named "Humming Girl")
show katja U_P1_E5:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show katja U_P1_E5 alpha 1.0
#--#
n "What draws my attention, though, is her eyes. Or rather, eye."
n "I can see she has one, the left."
n "Piercing, golden brown, expertly made-up. Long, mascaraed lashes."
n "By contrast, if she even still has it, her right one is covered with a large, sterile medical bandage."
n "Call it stupid, but my first instinct is to point it out somehow. Maybe ask her if she's okay."
n "Because, you know. She's got a bandage over her right eye. What if she hadn't noticed?"
n "Luckily, I think better of it before I can open my mouth."
#-# >>Music: Slow Fade into Katja's Theme (Susanne's, currently WIP). Placeholder: Be Blue
stop music2 fadeout 5.0
play music "music/Be_Blue.mp3" fadein 5.0 loop
#--#
humminggirl "\"Would you like to go before me?\""
erik "\"...?\""
n "Is she talking to me?"
n "She's looking right at me. All signs do seem to be pointing towards that being the case."
erik "\"N-no, it's alright. You go ahead.\""
humminggirl "\"Please, I insist. It is no trouble.\""
#-# >Katja moves right
show katja U_P5_E1:
  easein 1.0 xalign 0.7
#--#
#-# >Katja_P1_E1
show katja U_P1_E1
with Dissolve(0.25)
#--#
n "She steps aside and keeps quietly looking at me, motioning with a hand towards her place."
n "Even when not humming, her voice has a clear, musical quality."
n "I'm not sure if she's making fun of me or if she's just being polite, but I'm not going to look a gift horse in the mouth."
n "Or potentially set off a crazy person."
#-# >Katja exit to right
show katja U_P5_E1:
  easein 1.0 xalign 1.0 alpha 0.0
#--#
n "Moving forward, I pick a different kind of sandwich from yesterday and a bottle of lemonade to wash it down with before sitting down on a nearby bench."
n "I set aside the bottle and bite into my sandwich, but as soon as I've started to enjoy it, I'm interrupted by the girl."
#-# >>Stop Cafeteria Background Sounds
stop ambience
#--#
#-# > Katja_P5_E2a enters from left to center
show katja U_P5_E2a:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
show katja U_P5_E2a alpha 1.0
#--#
humminggirl "\"Excuse me, would you mind it if I sat here with you?\""
n "Looking up, I see her standing right near the bench in front of me, daintily gesturing towards it as if intending to illustrate the concept of sitting."
n "Mouth too full to do much but mumble, I make with an indifferent shrug."
n "She nods, then sets her purse slowly on the bench and sits down."
#-# > Katja_P2_E2
show katja U_P2_E2
with Dissolve(0.25)
#--#
n "Her smile is refreshingly friendly, after what happened in class. I try to force myself to focus on it, rather than how creepy her one good eye looks as it moves up and down to examine me."
n "I get so absorbed in following her brown iris spinning about, I think that by the time I've noticed her talking to me she's already had to repeat herself once."
erik "\"Uh... what?\""
humminggirl "\"That sandwich.\""
n "She speaks in a patient, measured tone."
humminggirl "\"Why did you choose it?\""
#-# >Katja_P5_E2b (smile)
show katja U_P5_E2b
with Dissolve(0.25)
#--#
humminggirl "\"That machine offers several kinds of sandwiches. Why did you pick this one?\""
n "What an odd question."
n "I guess I could just not answer, but she looks perfectly serious. Besides, she did move aside for me in line. It'd be rude to stay silent now that I've made it clear I did hear her."
erik "\"Let's see...\""
erik "\"I didn't have anything last night, and all I had for breakfast was a cereal bar.\""
erik "\"I don't know. I was hungry, it felt like a good choice.\""
erik "\"I mean, it's a sandwich, right? How bad could it be? Hard to screw something like that up.\""
humminggirl "\"I see. Do you like it, then?\""
erik "\"Eh, sure. It's... egg or something, I think. Got some vegetables in it. Definitely beats having nothing.\""
"{color=#FF8c00}>Katja_P5_E2a{/color}"
humminggirl "\"Hunger is the best sauce in the world, isn't it?\""
erik "\"Yeah. Didn't even realize how hungry I was until now.\""
"{color=#FF8c00}>Katja_P1_E2b{/color}"
humminggirl "\"Don't we wish you had a cent for every time that happened?\""
humminggirl "\"One moment you're having an interesting thought, and the next time you look at the clock, you've already missed dinner.\""
erik "\"Sorta. I just wish it'd been an interesting thought, rather than just... I don't know. Not feeling like it, or whatever.\""
n "I take another, experimental bite to see if she'd object, and she doesn't. Her eye keeps following me, though, turning silently under the lid while the girl sits in silence."
n "Did I do something wrong? Did I give a wrong answer?"
erik "\"Uh... Not to sound rude or anything, but why exactly did you ask me that? You know... just so we're all, uh, clear about that.\""
#-# >Katja_P1_E8a (smirk)
show katja U_P1_E8a
with Dissolve(0.25)
#--#
n "Her lips stretch into a coy smile."
humminggirl "\"Protocol.\""
n "I put down my sandwich and swallow, waiting for her to elaborate, but she doesn't say anything more."
n "Back home, I'd have immediately dismissed that reaction as her being obnoxious. I don't know anyone our age who uses that word unironically, and smirking like that just feels like she's trying to act mysterious."
n "Here, though, there's always the chance that she's serious about it and I'll come off as a world-class douchebag for calling her out."
n "Besides... There's something about her delivery. It doesn't feel ironic. It doesn't feel like \"acting\", either. It's feels every bit as sincere as her previous sentence."
n "Until I'm sure, I'm going to give her the benefit of the doubt."
erik "\"...I'm not sure I understand. You'd have to forgive me, I...\""
erik "\"The truth is I'm really new here. Like, I only arrived last night. This is my first day around. I don't really know how this works.\""
n "She puts the back of her hand to her mouth to stifle a giggle. I think I can make out a flash of gauze on her wrist when her sleeve flits. I hope it was just my imagination."
"{color=#FF8c00}>Katja_P1_E3b{/color}"
humminggirl "\"Well, I wouldn't go so far as to say that I {i}have{/i} to forgive you...\""
humminggirl "\"But given your circumstances, and seeing as you haven't done anything wrong that I know... Fine.\""
humminggirl "\"I forgive you.\""
#-# >Katja_P1_E2b 2
show katja U_P1_E2b
with Dissolve(0.25)

#>Katja_P1_E2b 2
show katja U_P1_E2b
with Dissolve(0.25)
#--#
erik "\"Gee. Thanks.\""
n "From her smile, you'd almost think she was going to answer \"you're welcome.\""
#-# >Katja_P1_E2a
show katja U_P1_E2a
with Dissolve(0.25)

#>Katja_P1_E2a
show katja U_P1_E2a
with Dissolve(0.25)
#--#
n "Before I can make up my mind on whether to roll my eyes or politely laugh at her joke, the girl's expression softens."
n "When she next speaks, it's with a warm, motherly tone."
humminggirl "\"Are you not comfortable eating with all of the others?\""
erik "\"...It sounds stupid when you say it like that.\""
humminggirl "\"Does it? I apologize, then. That wasn't my intention.\""
humminggirl "\"I was there before. I hope that you realize that.\""
humming "\"Everything made me nervous. Nothing anyone said cheered me up.\""
humming "\"I felt sick of being told that everyone's been there at some point. It made me feel like I've missed something everyone else figured out.\""
erik "\"Then why does everyone keep saying that all the time? What's the point? Everyone says that they've \"been there\", so how come they don't get it doesn't work? It never – it doesn't make me feel {i}any{/i} better.\""
n "The girl nods matter-of-factly."
humminggirl "\"It almost never does.\""
#-# >Katja_P1_E2b 3
show katja U_P1_E2b
with Dissolve(0.25)
#--#
humminggirl "\"It is simply a true statement. I think there's a value in that.\""
humming "\"Knowing that other people were nervous at first doesn't mean it's a fine thing to be. It means that you aren't any worse than them because of it. You {i}haven't{/i} missed out anything that they didn't in your place. At least not in that regard.\""
humminggirl "\"How {i}that{/i} makes you feel is an entirely different question.\""
erik "\"...Maybe it is. I know it's just a matter of time, or whatever, it's just...\""
erik "\"Look, I don't want to talk about this. I don't even know what's the problem. Maybe I'm just tired. Woke up a bit earlier than I'm used to, and now it's like that morning daze just wouldn't pass.\""
"{color=#FF8c00}>Katja_P5_E2b{/color}"
humminggirl "\"The next time that happens, try going for a walk. It might help to get your blood running. That's what I do when I wake up too early.\""
erik "\"Um... okay. Thanks, I guess.\""
n "I'm torn between looking back at her and looking away. I know  or at least, I hope that she did mean to, but I really do feel stupid right now. It's weird, but I can't tell if I'm glad or embarrassed."
n "Just as I resolve to pathetically gaze at my sandwich, the blonde girl talks."
humminggirl "\"It isn't as silly as you might be thinking right now. I won't claim to know what your troubles are, and it isn't my place to ask.\""
humminggirl "\"Remember, though, that whatever they might be, you probably aren't the first here to have had them.\""
humminggirl "\"We all develop our small ways of coping. Even if all that means is eating the occasional meal outside the cafeteria.\""
"{color=#FF8c00}>Katja_P2_E2{/color}"
humminggirl "\"I'm here for a similar reason, in fact. I'll admit - I don't usually like to eat by myself, but every once in a while, even I feel like having some space.\""
erik "\"Would you rather I go?\""
n "She shakes her head lightly, motioning with her hand for me to remain seated down."
humminggirl "\"No, but it's sweet that you ask. I was the one who started this talk, wasn't I?\""
humminggirl "\"It's not every day that you happen to meet a new student.\""
#-# >>Initiate Glorious Katja CG (Katja's Curtsy)
show CG04 at Pan((0, 900), (0, 0), 18.0)
with Dissolve(2)
#--#
n "With a long, graceful step, she stands up in front of me."
humminggirl "\"My name is Katja Böhm, from Mr. Rosenstein's class.\""
#-# >>From now own, the textbox shall refer to the Humming Girl as Katja
#
#--#
katja "\"You may call me Katja, if you wish.\""
katja "\"I'm originally from Linz, Austria, though I've been living in Vienna for the past few years now.\""
katja "\"I'm sure that you've already been given the customary tour, but nevertheless, allow me the honor of welcoming you to our school.\""
katja "\"I hope your stay will be pleasant and beneficial.\""
n "She adds a little flourish of her hand and a bow, and by now I honestly can't tell if she's serious."
n "Her smile looks like something from a poster. Even the way the light reflects off her lipstick looks like art."
n "Even and inscrutable. Teasing? Humorous?"
n "Will she start laughing soon? Or is that just a thing they do in Austria?"
n "I try to remember if anyone introduced themselves like that outside the school. How awkward would it be to find out this is actually normal, and all this time I've been the one who was being impolite?"
n "That can't be the case, right? Someone would've definitely said something."
n "This is just... Katja's thing."
n "Her unusual, anachronistic, incredibly striking {i}thing{/i}."
n "I think I'd put her somewhere between Ela and Irene on the weirdness scale."
n "Leaning heavily towards the first. I mean, she is being polite."
n "And I can't complain about the view, either."
n "Wait... Is that intentional?"
n "I mean, I am staring pretty hard here. Should I be staring this hard? She {i}has{/i} to know how this looks like, right? She wouldn't be doing this otherwise, right?"
n "Am I being a huge creep now? This is like puberty all over again."
n "Not cool, Erik. Women are not for staring. Abort! Abort!"
n "Just as I begin averting my eyes, she sits back down like nothing's happened. The whole ordeal couldn't have lasted longer than five seconds, but man, did that feel like it."
#-# >>End glorious CG
hide CG04
#--#
#-# >Katja_P1_E2a 2
show katja U_P1_E2a
with Dissolve(0.25)
#--#
erik "\"Wow. Umm... thanks.\""
erik "\"Hmm...\""
erik "\"My name's Erik Wilhelm, and... I guess you can call me Erik?\""
n "I'm not sure why she added that part, but whether that's just standard \"protocol\" or Katja's own idea of manners, I don't see a reason not follow."
erik "\"I'm from Ms. Claes' class, and...\""
erik "\"I'm originally from Basel, Switzerland. The city, not the canton.\""
n "She nods carefully, looking far more interested than I'd have thought anyone should be."
"{color=#FF8c00}>Katja_P1_E5{/color}"
katja "\"I thought one was inside the other.\""
erik "\"Well, yes, but not everyone knows that and it can be confusing. Also, the second's technically called Basel-Stadt, if you care about it.\""
"{color=#FF8c00}>Katja_P1_E8a{/color}"
katja "\"So much as you do. I do admire specificity.\""
n "When I don't respond, she straightens up in her seat and gives another short, dignified bow."
"{color=#FF8c00}>Katja_P1_E2b{/color}"
katja "\"It's a pleasure to meet you, Erik.\""
n "I thank her, and then the air grows silent. Neither of us says a word."
erik "\"Just, for the record, you know. I don't normally eat vending machine sandwiches either.\""
#-# >Katja_P1_E8b
show katja U_P1_E8b
with Dissolve(0.25)
#--#
katja "\"I'd never have thought to imply that.\""
erik "\"Yeah. I mean, it's not like it's disgusting or anything, but it's sort of bland, right?\""
#-# >Katja_P1_E2a 3
show katja U_P1_E2a
with Dissolve(0.25)
#--#
katja "\"That is true. As you said yourself, though, there's a reason you've chosen to.\""
erik "\"Because it's lunchtime and that's just what was here?\""
n "Katja snickers. It's a beautiful, ringing sound."
katja "\"Precisely. I can empathise with that choice.\""
erik "\"... The choice to go with whatever's in front of you?\""
katja "\"The choice to eat for its own sake when you know you couldn't enjoy it. I don't think that there's anything shameful about it. If anything, I think it's wise.\""
katja "\"It wouldn't do you good not to eat, and it would've have felt wasteful to me to eat something I might've enjoyed when my mind wasn't really on it. It might've just made me feel worse.\""
n "I take one more peek at my sandwich to make sure it hasn't turned into something profound while I wasn't looking."
n "Should I feel more offended or more complimented that Katja's giving my judgment that much credit? None of what she's saying is {i}wrong{/i}, but it's still not the kind of thing you normally actually {i}think{/i} of."
n "Unless, that is, the thought to eat when you're hungry doesn't just come to you naturally. But I probably really shouldn't be going that way."
n "Frankly, I'm not really sure where to go from here. What is with this girl?"
#-# >>pause
$ renpy.pause (2.0)
#--#
n "This is just getting silly. If I'm not eating, I might as well ask a question that's been bothering me."
erik "\"Can I ask something?\""
#-# >Katja_P1_E3a
show katja U_P1_E3a
with Dissolve(0.25)
#--#
katja "\"Feel free to. I might even answer.\""
#-# >Katja_P5_E2a 2
show katja U_P5_E2a
with Dissolve(0.25)
#--#
erik "\"Huh. Good to know I got nothing to lose, then\""
erik "\"Why that last part of the introduction? With the cities and countries, and all that? It sounds like it's something formal. Do they just do that in Austria in general, or just here?\""
katja "\"Once again, protocol. This is, as Mr. Bosworth likes to brag so much, a rather multinational institution.\""
katja "\"It's a friendly way of finding out what languages a new student speaks. People default to English because it's the most common teaching language, but since very few come here from the Anglosphere, that tends to just make both sides equally uncomfortable.\""
katja "\"If you find out you have a shared language, it becomes far easier to have a conversation. Aside from that, sometimes it puts new students at ease.\""
katja "\"It doesn't happen every time, but a lot that I've met who were not comfortable talking about nearly anything else were eager to bring up a familiar subject, like their hometown.\""
#-# >Katja_P5_E2b 2
show katja U_P5_E2b
with Dissolve(0.25)

#>Katja_P5_E2b 2
show katja U_P5_E2b
with Dissolve(0.25)
#--#
katja "\"They get to talk about something they're confident in, I know whether we have a shared language, and every once in a while, I learn something. Not a bad deal, if you ask me.\""
katja "\"I'm assuming you speak native German? I know I'd be more comfortable if I were speaking my native language.\""
n "I nod, vaguely aware that the sandwich in my hand is still not even half eaten."
erik "\"Yeah. Basel-Stadt's right across the Rhine from Germany, so that's what we speak. Is it unusual?\""
katja "\"Ganz und gar nicht.\""
n "I sit dumbfounded for what feels like far too long while my brain switches gears back to German."
n "Either Katja hasn't noticed, or she doesn't mind. Her German is as rapid and precise as her English before."
n "All in all, I suppose that's a good thing."
katja "\"Most students are still from around Austria, and those that aren't do tend to speak German, with the exception of a significant French minority. As I said, though, it can lead to trouble on those cases they're not.\""
n "Sounds simple enough. I should probably remember that for the next time I run into someone."
erik "\"Hey, it's not all that bad, right? Encouraging a little multilingualism, and all that.\""
"{color=#FF8c00}>Katja_P5_E2b{/color}"
katja "\"That does make you sound very Swiss.\""
erik "\"No, I'm serious. They say there are proven benefits in child development.\""
erik "\"I think.\""
"{color=#FF8c00}>Katja_P5_E5{/color}"
n "She rests back in seat with an intrigued expression."
katja "\"Is that so? Do you think they tried that research on high-schoolers?\""
erik "\"Well... no. I think it mostly just applies to young children.\""
erik "\"But, like... you know. I'm cool with that.\""
#-# >Katja_P5_E8b
show katja U_P5_E8b
with Dissolve(0.25)
#--#
katja "\"Young children?\""
erik "\"Multilingualism.\""
n "She lets out a quiet laugh, crossing her arms and absentmindedly letting her gaze wander up the corridor."
"{color=#FF8c00}>Katja_P4_E10{/color}"
katja "\"That's interesting. Do you think that it works every time? Do the languages have to be similar, or something of that sort?\""
n "I shrug halfheartedly. I don't even know why this topic came up. She's asking me like I'm some kind of expert, but honestly, most of that's just stuff I think I remember reading once in a popular science magazine. I could be talking out of my ass."
erik "\"I guess it can depend on a lot of things.\""
"{color=#FF8c00}>Katja_P4_E1{/color}"
n "She doesn't respond, and I'm left to finish my sandwich."
n "If you ignore her weird manner of speech, Katja's not all that bad. Shame about the eyepatch, though. It makes looking at her... awkward, somehow."
n "I can't look her in the face without feeling like I'm staring at something I shouldn't. I can't just look somewhere else while she's talking to me, since that'd be rude, and I obviously can't keep my eyes on any other part of her. I'm feeling sleazy enough just thinking about this."
n "She's just so striking. Everything about her is. How much work does she have to put every day into looking like that?"
n "The hair, the makeup, the way she wears her clothes –"
n "Does that mean she's okay with being looked at?"
n "Jesus, I can't believe I went there. It sounds like something a weirdo would say to the judge."
n "I wonder if I'm the first one who has ever had this problem with her, or if... if maybe she's used to this, by now. I wonder which would make me feel better."
n "I mean, this is just one, tiny part of her appearance but it happens to be the one everyone looks to at first."
n "Could you blame someone for seeing that and feeling uneasy?"
n "Especially if they also saw the gauze on her wrists."
erik "\"You still haven't explained that part of the protocol where you ask me about the sandwich.\""
katja "\"Correct. Our conversations topic has changed, and I didn't see all that much need to.\""
katja "\"You could call it a precaution, for when confronting newly met students.\""
erik "\"... A precaution? Against what? Offering them the wrong sort of appetizer?\""
#-# >Katja_P4_E2
show katja U_P4_E2
with Dissolve(0.25)
#--#
n "She smirks slightly, but doesn't laugh."
katja "\"To be honest, the question itself doesn't matter much. It's the way it is answered that does.\""
erik "\"... Meaning?\""
katja "\"Whether there is a reply and how clear it is. Whether it makes sense. Whether it's stammered or mumbled, or implies offense.\""
katja "\"It's a crude instrument, but it can be invaluable in gauging how to proceed  or even if  when talking to someone new.\""
n "She says it with the flagrant carelessness of someone who knows that they're saying something outrageous. At least she understands that it is."
erik "\"Wait. So if I'd answered more slowly, or not to the point, or if I didn't, you'd have known to keep talking to me in little words?\""
"{color=#FF8c00}>Katja_P4_E1{/color}"
katja "\"No. That would have been reckless of me. However, given my personal experience, I would have been able to make a better-informed guess. If I'd guessed wrong, I could've apologized.\""
erik "\"Sounds like a small comfort, if you've made that kind of wrong assumption about someone.\""
katja "\"But worse than assuming that they think and talk just like yourself, and behaving on that? Potentially saying something that hurts them? Using figures of speech that they won't understand? Pushing them to talk when they don't even want to?\""
katja "\"It's an unfortunate truth of our life here that not everyone can be approached the same ways.\""
katja "\"Some students don't get metaphors. Others are not always in the mood to talk, or never want to talk about something that seems natural to you. Some don't want to be talked to at all.\""
n "I nod thoughtfully."
erik "\"Why the sandwich thing, then? If the question itself doesn't matter, why not just ask how I'm doing? Or something about the weather?\""
#-# >Music fades out
stop music fadeout 5.0
#--#
katja "\"It was the first one that came to mind. Optimally, the question needs to be unexpected and not have an objective answer, since many students who would've been able to answer ones that aren't can't carry a conversation otherwise.\""
katja "\"From there, it's simply a matter of prodding and probing and coming to conclusions as you go. You'll probably get used to it after a while.\""
#-# >>Music: Slow Fade into Be Violet (2)
stop ambience fadeout 3.0
stop music2 fadeout 5.0
play music "music/Be Violet 2.mp3" fadein 5.0 loop
#--#
n "She studies me carefully while I ponder her words."
n "I can get what she's saying from a, well, clinical viewpoint."
n "Assuming she does have enough experience to \"tell\", it can certainly be useful if she wants to avoid making social blunders. In a school like St. Dymphna's, where everyone has their issues, it's probably a crucial skill to learn."
n "At the same time, there's something definitely off about making that judgement of someone based on their answer to a single, pointless question."
n "What if I just hadn't felt like responding? Could she have just gone away, pegging me down as... what? A boy with autism? Depression?"
n "This whole conversation could have looked entirely different."
n "Then again... she's a pretty, blonde girl with an eyepatch who goes to a special school. She probably knows all about people judging her based on first impressions."
n "Even I may have done it a little bit when I first saw her. And then once more, when we just started talking and she didn't seem to be making sense."
n "That's another thing I should probably keep to mind. Be cautious, but try not to judge people {i}too{/i} quickly."
n "It's hard to shake off the feeling that I'm missing something. Is this really as hard as it seems?"
n "Maybe I really should try going about introductions a bit differently from now on."
#-# >>School Bell
play sound "music/effects/schoolbell.ogg"
#--#
n "The first warning bell pulls me back to reality. From the way it makes Katja get up and turn to look at her watch, I'm assuming it's the same for her."
"{color=#FF8c00}>Katja_P1_E2a{/color}"
katja "\"Don't you have classes to attend?\""
erik "\"Yeah. Don't you?\""
n "She nods, getting up while I push myself off the bench, trying to keep the weight of my bad leg. This'd be a terrible time to trip like an idiot."
erik "\"See you around, or something.\""
katja "\"Likewise. I enjoyed our conversation.\""
#-# >Katja exit to left
show katja U_P1_E2a:
  easein 1.0 xalign 0.35 alpha 0.0
stop music fadeout 5.0
#--#
n "I turn away and back towards the classes, leaving Katja behind with the vending machine."
#-# <END>
#
#--#




########

jump A1_10 # jump A?_??
