
label A1_24:
###############

$ persistent.scene_number = "Second Contact" # current scene
$ persistent.scene_name = "Second Contact" # current scene name
$ renpy.save_persistent()


# Scene Scene 24 - Second Contact
# Scene name: Second Contact"
# Backgrounds:
# Main Building (interior)
# Erik's Classroom
# Sprites:
# Ms. Claes
# Annaliese
# Sound effects:
# Paper handling
# Quiet crowd
# School bell

#init passednote to false
$ passednote = False

#-# <scene open>
#--#

#-# <School_Classroom1_NOPAN.png> (should still be active from previous scene?)
#--#

#-# >Ms. Claes exit to left
#--#

n "I have to say, that went better than expected. Jeanne wasn't what I expected from a student tutor. Nothing like the hard-nosed stuffed shirts I had as tutors at my old school."
n "It's still disappointing to know that the administration has already figured out that I'm not the best student."
n "Maybe I'm putting too much weight on this morning's meeting, but I'd like to think that I could have faked the star student role for at least a week."
n "Maybe I can turn it around today. Yeah, if I keep telling myself that I'm sure it will happen."
n "The small victories are already starting to pile up, as I manage to make my way to my seat without embarrassing myself while everyone else filters into the class for homeroom."

#-# >timeskip
#--#

n "The morning's announcements pass by with little fanfare, and before I know it, it's time for maths. About half the class get up to leave, the others staying behind."
n "They're soon replaced by other students, and among them I spot my neighbour from last time — the girl with the perpetual earphones."
n "She drifts over to her desk next to mine without looking around, seemingly unaware of the world around her."
n "I realise I haven't seen her around the school since we met on Monday. I might still be at the stage of not quite being able to put a name to every student, but I am starting to recognise quite a few faces — I'm sure I haven't seen her a single time since then."
n "Taking a chance, I give her a wave and a nod in greeting."
n "I half expected she might not notice at all with her earbuds already in, but she falters for a moment, and the slightest flicker of movement in her hand (that I choose to interpret as a wave) and a glance in my direction tells me that she did."
n "Before I can say good morning, though, Ms. Claes purposefully reenters the room, needing to do nothing more to signal the start of class."
n "Once everyone has settled down, she begins a lecture on a body of mathematics I’m completely unfamiliar with. Last lesson covered topics I already knew, but this time it’s all fresh. Still, I think I can handle this."

#-# <timeskip>
#--#

n "Amazingly, I managed to stay awake throughout the entire lecture and I feel like I have a pretty good grasp on the subject matter."
n "As I start to work on the practice problems, I notice the girl next to me is once again listening to music, this time under her hood. Was she listening to music during the lecture?"
n "Maybe she doesn't even need to be in this class — she certainly seems to be writing plenty, and with confidence."
n "That said, she could just be doodling meaninglessly like last time. Her hand movements do have that distracted, erratic look about them."

#-# <timeskip>
#--#

n "I'm actually a little proud of myself. I managed to get through all of the problems with very little difficulty. Maybe I could even get to like maths a little?"
n "Okay, that might be pushing it."
n "I give my answers one last look-through along with everyone else as Ms Claes stands back up in front of the board to wrap up the class."
#Anna in somewhere here?
n "I notice the girl next to me is still listening to music, now with her eyes closed. Does she know class is almost over?"
n "People are starting to filter out of the room now, and she doesn't seem to notice. Does she just have her music really loud, or are does she have those fancy noise-cancelling headphones? Maybe she's just really good at tuning out the world."
n "I'd better try to get her attention. Apparently, I'm the only one who's noticed her."
erik "Hey."
n "Nothing."
erik "Uh, class is almost over."
n "No response. I suppose I should expect that at this point. I notice Fran laughing and shaking her head across the room."
n "Nice to know they have my back on this one."
n "I feel like I need to get her attention somehow, though. She's going to miss the homework assignment and somehow I doubt she'd be able to ask anyone what it is."

#-#
#[Menu choice: How do I get her attention?]
#[1] Give up.
#[2] Tap her on the shoulder.
#[3] Pass a note.
#
#<How do I get her attention?>

menu:
    "How do I get her attention?"
    
    "Give up.":
        jump A1_24a
    "Tap her on the shoulder.":
        jump A1_24b
    "Pass a note." if persistent.ak_tot > 0:
        jump A1_24c
#--#
label A1_24a:
    n "I consider my options. Her eyes are still firmly closed and I’m not sure she even knows she’s sitting in a classroom, let alone that other students are vacating the desks around her."
    n "On the other hand, maybe I just shouldn't bother her anymore. She clearly doesn’t want to be disturbed, and she seems to be doing fine without me. I’m sure she’ll realise where she is eventually."
    n "With the matter settled, I think no more of it and continue packing my bag to leave."
    n "As I do, I notice someone slip out the door just before me — the last to leave. Looked like the girl who was sitting next to me."
    jump A1_24_continue

label A1_24b:
    n "She probably can’t hear me with those earbuds in. Maybe if I tap on her shoulder to get her attention."
    
    #-# <slight screen shake>
    #--#
    
    n "She's giving me a piercing glare that cuts right through every bit of confidence I had about this idea. I should probably explain myself."
    erik "Hey, uh, sorry to bother you. It's just, class is over. Thought you might not have noticed. And, uh, the homework — "
    n "Without letting me finish, she glances up at the clock above the board at the front of the class, and back at me."
    n "Now appearing quite embarrassed, she grabs her bag and begins packing it as quickly as possible."
    n "For God's sake, Erik. "
    n "Having made a fool of myself, I take her lead and begin packing my bag myself, trying to focus my mind on something else."
    n "As I do, I notice someone slip out the door just before me — the last to leave. Looked like the girl who was sitting next to me."
    jump A1_24_continue

label A1_24c:
    $ persistent.ak_tot += 1
    $ passednote = True
    
    n "The world doesn't exist to her. I need some physical way of getting her attention, but actually touching her might be a bit much. Maybe a note?"
    n "Man. Passing notes in class. It’s like I’m 14 again."
    n "What to write? \"Class is almost over\" would probably do the trick, but..."
    n "A perfectly enunciated voice swims into my mind, goading me for being so predictable and {i}objective{/i}. What would Katja ask?"
    n "I quickly scribble out a question, \"Hey, what are you listening to today?\" and slide it across her desk."
    n "This does the trick. She looks up, more dazed than surprised, as though someone has disturbed a pleasant dream."
    n "Then, realising what has happened, her eyes shoot open and she comes perilously close to making eye contact with me."
    n "For a moment I feel like I’ve made a mistake as she looks kind of shocked, but when I glance down at the note and she follows my line of sight, she actually looks pleased."
    n "In fact, that might have been the biggest smile I’ve seen on her yet. Not that that’s saying much, but still, it’s something."
    n "She leans over and shows me the screen of her phone. Another artist, album and song I’ve never heard of. Today’s album art is a very blue scene with a snowy mountain behind a lake with a flock of swans."
    n "I don't recognise it."
    n "I'm hardly a music buff, but I feel as though I definitely wouldn't be alone in not having a clue what it is. I also have no idea which of the few words on the cover is the artist and which is the album, either."
    n "My brain scrambles a little trying to think of a worthwhile response to this, but nothing is forthcoming. A lame \"Cool\" is all that it can muster, which I don't bother saying."
    n "In any case, I managed to get her attention without annoying her. That's a start, at least."
    n "She plucks out one of her earbuds, as if expecting me to say something. Pressure's on. I decide to avoid my lack of music knowledge completely."
    erik "By the way, I never got your name."
    n "The girl ponders this question for a second, before flipping over the note I passed her and scribbling something. She finishes and slides it back to me."
    n "{i}Annaliese Koell.{/i}"
    n "Just a name and nothing else. Annaliese. At least that's one mystery solved. I look back up at her, smiling. Again, she fails to look me in the eye, but looks a little pleased with herself nonetheless."
    # wouldn't it make sense to have Ms. Claes' sprite show up for this line?
    n "Before I get the chance to respond, though, a shadow falls over my desk. Ms. Claes peers ominously at the note lying on my desk and quietly asks me to see her after class."
    n "Fuck me for trying to communicate with my fellow students, I guess. It’s not like there’s any other way of talking to this girl."
    n "My gaze follows Ms. Claes as she pads back to her desk, unfolding the note. As she looks down at the creased piece of paper in her hands she hesitates for a moment, as if second-guessing herself, and glances briefly back at Annaliese and I."
    n "Without saying anything else, though, she clears her throat and goes about explaining today's homework assignment."
    n "For a moment, I wonder why I even bothered writing the thing. Annaliese doesn’t seem to care all that much about talking to me. She smiled, sure, but her note was hardly receptive, and now I'm probably going to get some sort of undeserved reprimand at the end of class."
    n "When I shift my gaze to her, though, the guilty expression on her face melts any animosity I felt towards her. She clearly feels bad about getting me in trouble."
    n "It’s not like Ms. Claes is going to find anything incriminating on the note, either. A trivial question and a name. Nobody’s going to get in trouble for that, although the teacher's strange hesitation is still playing on my mind a little."
    n "After another few seconds of looking a little uneasy, Annaliese takes the chance to pass me another note while Ms. Claes has her back turned."
    n "{i}Sorry{/i}"
    n "And when I raise my vision again, she has already put her earbuds back in and apparently tuned out the world. Man, Annaliese, way to lay on the guilt trip. How did that one word make me feel like the bad guy?"
    
    #-# <timeskip>
    #--#
    
    #claes in?
    erik "You said you needed to see me? It’s not about the note is it?"
    claes "Of course it's about the note, Erik, yes. Don't think — "
    erik "I hadn't forgotten about what you said this morning. I wasn't neglecting the class or anything."
    claes "I know, I mean — "
    erik "I really paid attention this lesson. I think I did really well on the workbook questions and I'm going to do that homework straight away this evening."
    claes "I'm sure you did, that's not what I — "
    erik "What you said this morning — "
    claes "Stop right there, Mr Wilhelm, you {i}aren't{/i} in trouble!"
    erik "...I'm not?"
    claes "No, you're not. I just wanted to say... well, I don't mean to be nosey or anything, but I noticed how sensitive you've been with Ms. Koell in this lesson and the last. I'm quite impressed."
    erik "What's impressive about it?"
    claes "Well... hmm, how can I put this?"
    claes "Annaliese hasn't had the easiest time at St. Dymphna's. I'm sure she appreciates you interacting with her while giving her some space. It's a difficult balance to strike."
    claes "Ah, but I probably shouldn't have said anything. It's Annaliese's business and yours, not mine."
    claes "Just keep it up, Erik. I'm sure you're going to fit in well here. Oh, and well done in today's lesson, I did notice you working hard on the practise questions."
    n "This makes me feel disproportionately proud. I'm just glad she noticed."
    erik "Thanks, I tried."
    claes "I hope you continue to bear what we talked about this morning in mind. Off you go, now."
    n "With an uncharacteristically warm smile, Ms. Claes returns to a stack of papers on her desk and gets marking. I swing my bag over my shoulder and turn to exit."
    n "As I do, I notice someone slip out the door just before me — the last to leave. Looked like Annaliese."
    jump A1_24_continue
    
label A1_24_continue:
    n "Had she been hanging back to listen to our conversation or something? The way she left, slinking silently from the room, leads me to believe she was trying to be covert. Then again, there's nothing I haven't seen her do silently."
    if passednote == True:
        n "I wonder if I should try to catch up with her. Judging from what Ms. Claes said she could do with a friend. Would she appreciate that? Part of me thinks calling after her and trying again to make conversation would just be an inconvenience to her."
    else:
        n "I wonder if I should try to catch up with her. Would she appreciate that? Part of me thinks calling after her and trying again to make conversation would just be an inconvenience to her."
    n "Another part thinks that she'd be appalled by it. A sliver, though, is sure that on some level she wouldn't mind."
    n "I jog a little to catch up with her. With her headphones in it looks like she didn't hear me coming, but as I come up alongside her she notices me in her peripheral vision and looks in my direction."
    n "I was expecting her reaction to be one of shock, but instead she seems relatively unfazed by my presence."
    n "She even raises her hand slightly in greeting."
    if passednote == True:
        erik "Hey, Annaliese!"
    else:
        erik "Hey!"
    n "She doesn't say anything. Fair enough."
    erik "What have you got next?"
    n "She pulls out her phone and taps a few times before showing me the screen with her timetable open."
    erik "Ah, history. Nice."
    n "She shrugs."
    erik "Not your thing?"
    n "She doesn't have much of a response to this."
    erik "I kind of like it. Learning about how people lived in the past is fascinating."
    n "She pauses for a second, then taps something out in her phone's notes, again showing me the screen when she's done."
    n "{i}prof aschner a shit tho.{/i}"
    erik "Haha, okay, fair enough. He's not the most inspiring."
    n "She taps out something else; {i}and have u heard the crap he listens to while we're working?{/i}"
    erik "Oh I know. 80s Swedish pop music? Why?"
    n "I grin."
    erik "Maybe you should subtly recommend him some headphones that don't leak so badly, huh? It's painful."
    n "She laughs — or, rather, forcefully exhales through her nose — and smiles faintly at the floor."
    if passednote == False:
        n "Without prompt, she taps something else out on her phone and once again shows me the screen."
        n "{i}its annaliese koell, btw.{/i}"
        n "Huh. I completely forgot I hadn't learned her name. Well, that's one mystery solved."
    n "This is decidedly the weirdest way I've ever interacted with someone. Is Annaliese physically mute, or is it purely psychological?"
    n "I think of asking her, and once again that sweet, trilling tone of Katja's floats through my head. Would it be tactful to ask something like that straight up?"
    n "Well, it depends on the person, right? On the impression, I've got on them so far? And in this case..."
    n "I let my gut do the thinking."
    erik "So, Annaliese... can you, uh — "
    n "I realise as soon as I open my mouth that this is a terrible question, but now I'm committed. How can I reword this without looking like an idiot?"
    erik "— speak?"
    n "No, apparently there is no way to reword it without sounding like a complete tool."
    n "She doesn't seem to mind, though."
    n "She nods."
    erik "But you don't?"
    n "She shakes her head, looking a little sheepish."
    erik "Huh. Okay, well, how about this — give me your number. Then we don't have to keep communicating like this. It's kind of awkward."
    n "I'm not sure what drove me to be so forward. If I'm honest, I barely know this girl. Why am I trying so hard to communicate with her?"
    n "I guess I'm done being a bystander. So far, basically everybody I've spoken to in this school has been because I was told to speak to someone by someone else, or because they spoke to me first. I need some license."
    n "This spurt of sudden confidence — it must be something to do with what Ms. Claes said. Even though it's kind of weird, I feel like I'm doing the right thing."
    n "I study Annaliese's face. She still refuses eye contact with me, but I can see she's thinking hard."
    n "Her features are far from inscrutable. When she isn't focused on making herself unnoticed, her face is surprisingly expressive."
    n "Apparently coming to a conclusion, she reaches out and I pass her my phone."
    n "A few taps later, she hands it back. Number acquired."
    n "After a second's pause, I send her a text; {i}Thanks{/i}"
    n "She pulls out her own phone, checks it, smiles and taps out a reply of her own."
    n "{i}good to finally be able to talk to u.{/i}"
    n "Hm. Has she been waiting for this or something?"
    n "I look up at her and — before I can help myself — a laugh escapes my lips at the absurdity of our exchange. Still, if exchanging text messages while standing right next to one another is how Annaliese is, then so be it."
    n "Feeling a little awkward, I decide it best to reply via text myself, as well."
    n "{i}You too.{/i}"
    n "Another silent laugh. She must appreciate me replying in her medium."
    n "As we reach a fork in the corridor, Annaliese and I need to part ways — our next classes are different. I pause for a second, wondering what to say."
    erik "Okay. See you, Annaliese."
    n "She gives me a small wave and heads off."
    n "A few seconds later, my phone buzzes. A text from Anna."
    n "{i}Bye{/i}"
    n "And then a second."
    n "{i}just call me anna btw. annaliese is way too long. and old fashioned as hell.{/i}"
    n "Anna it is, then."
    n "I wonder if she'll ever be able to speak to me."
    n "As Anna rounds a corner out of sight and my mind begins to drift elsewhere, I feel a presence behind me. A foreboding, tense, and somehow non-gender-specific presence."
    n "It's Fran. I can feel it."
    n "Acting on impulse, I whip around and point dramatically at the figure behind me."
    erik "Fran!"
    n "It isn't Fran. The small boy standing behind me, at least a foot shorter than I am, looks terrified. Before I have to take any action myself, though, a hand is placed on gently on the boy's shoulder."
    #fran in?
    fran "Sorry about Erik, chap. He's just been through quite an ordeal. Run along now."
    n "Not needing any further prompting, the boy departs, delighted to get away from me and melt into the crowd. Grinning ear-to-ear, Fran turns to me and chuckles, grinning toothily."
    fran "Oh, oho Erik. Oh, my sweet, precious child. You are persistent, aren't you?"
    n "I can guess what she's talking about, but I'm not going to give her the benefit."
    erik "What are you talking about?"
    fran "Come on, Wilhelm. It's so obvious!"
    erik "Were you listening in on my conversation?"
    n "Fran chuckles again and this time I can definitely see why."
    fran "Haha! What conversation? There was nothing to listen to! Bless you both, though, it was very sweet."
    fran "You're really working hard on winning her over, aren't you? Most people give up in a few minutes, let alone a few days."
    fran "Personally, I can never tell if that's what she wants or not. Plumbing the hidden depths of a selective mute doesn't appeal."
    n "I can see where she's coming from. Communicating with Annaliese wasn't exactly easy."
    erik "No? How come?"
    fran "I just don't have the time for it, sweetie! All strength to her, she's happy to keep doing what she's doing, but talking to her is more of a challenge than I want to take on."
    fran "Still, it should be much easier for you now, right?"
    n "I feel apprehensive about this. What does Fran know?"
    erik "...What are you talking about, Fran?"
    fran "Come on, Erik — I saw you give her your phone! Getting numbers already, and you've been here less than a week? You sly dog, you."
    n "Oh, that."
    n "I didn't even think about getting Annaliese's phone number as... well, getting a girl's number. It was just the simplest way of talking to her. Still, if that's what Fran wants to believe."
    erik "You have to admit, I've got game."
    n "She laughs uproariously."
    n "This time her laugh is much more than a wry chuckle, causing everyone in the hall to turn and look. After a few more seconds, she wipes a few tears from her eyes theatrically and looks back at me."
    fran "...Oh, honey, you weren't being serious, were you?"
    n "I wasn't being serious — but who's to say I {i}couldn't{/i} have been being serious?"
    erik "What are you implying?"
    #>this next line scrolls by super fast -> "cps=*2" sets text speed to double of normal
    fran "{cps=*2}Definitely nothing at all I don't know what you're talking about you definitely have game.{/cps}"
    n "The words pour from her mouth, her grin belying her sincerity."
    fran "Anyway Erik, uh... good for you. Well done."
    erik "Well done?"
    n "Her voice still coy, her expression softens a little and this time she {i}does{/i} sound sincere."
    fran "Your perseverance. It's heartwarming, chap."
    n "Before I can ask her why she decided to say this, she's turned around and calls over her shoulder as she trots away, giggling mischievously."
    fran "See you in class, Wilhelm!"
    #replace 'her' with 'them'?
    n "Ah. I share my next class with her as well. Damn."
    n "For now, though, I'm left on my own once again."
    n "Is the fact that I tried to talk to Annaliese really such a big deal? First Ms Claes and now Fran — who else is going to interrogate me about this?"
    n "All this questioning makes me feel like I'm doing something wrong. It's certainly not helping that constant nagging feeling of forever being an outsider."
    n "But then, why should I let that stop me? I doubt that feeling is going to go away on its own anytime soon and like Ms Claes said, Annaliese must appreciate it. Something good is coming from it, at least. I wonder if she feels as much of an outsider as I do?"
    n "My head now swimming with even more indistinct thoughts and doubts, I head to my next class, still somehow buoyed by Ms Claes' and Fran's encouragement. It might be a bit weird, but it feels like I'm doing the right thing."
    
#-# <end>
#
#--#


########

jump A1_25 # jump A?_??
