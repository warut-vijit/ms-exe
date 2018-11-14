
label A1_19:
###############

$ persistent.scene_number = "A1_19" # current scene
$ persistent.scene_name = "Audience to Angels" # current scene name
$ renpy.save_persistent()


# Scene 19 - Audience to Angels
# Scene name: Audience to Angels
# Backgrounds:
# School grounds
# Chapel
# Sprites:
# Katja
# Father Max
# Music:
# School Theme (day)
# Katja Singing Theme
# Katja Calm Theme

#-# <scene open>
scene classroom1
#Temporary audio stops
stop music
stop music2
stop ambience
stop ambience2
#--#

#-# >music: school theme (day)
#--#

n "Two days haven’t been enough to orient me and my afternoon philosophy class does little to help. In other circumstances I might be engaged or, at least, indifferent."
n "As it stands I’m just cynical about it all. Today it’s metaphysics and I can’t for the life of me understand why I should care about \“the underlying ontology of the world\""
n "I’m still struggling to grapple with the reality that I’m at a school for messed-up kids. I don’t have a nicer way to put it, not right now."
n "Maybe that’s on me, but I’m sorry Mr. Kronenberg; as far as I’m concerned Cartesian metaphysics has aged about as well as you have. The ivory tower can lock me out for all I care."
n "Every corner I turn seems to greet me with some mishap or another; just one more awkward experience of trying to be normal at a place that essentially isn’t."
n "If there’s anything I should be learning, it’s how to live with that - how to live with myself and with everyone else. Anything I thought I knew before St. Dymphna’s has long gone out the window and I’m looking for the skills I need to replace."
n "And they’ve put me here to study damn philosophy. Unless a fountain of practical, social wisdom is about to burst from underneath Kronenberg’s magnificent beard, I couldn’t care less."
n "Maybe the day will come when I can sit down and actually engage with whichever dead person it is we’ve moved on to, but that will have to wait. I have more pressing matters at the moment."
n "This is just something to survive for now."
n "Ironic, that."

#-# >clock wipe
scene PitchBlack
with Dissolve(1.5)
scene classroom1
with Dissolve(1.5)
#--#

n "Well, I did it."
n "I survived ninety minutes of philosophy."
n "I’d feel guilty for thinking of it that way if I wasn’t too busy being anxious about everything else. All I can do is put it behind me and look forward."
n "Speaking of, I haven’t given thought to my afternoon plans. My only obligation is to meet with Dr. Faber, and that leaves me with many unblocked hours."

#-# >pause
#This is super messy TODO
$ renpy.pause(1.0)
#--#

n "The meeting."
n "It’s been looming in my head like some ominous spectre I can feel watching me from the corner of the room."
n "On the one hand I realise how silly that is: if anyone’s going to help me it’s the doctor. That’s why I’m here, after all."
n "Looking at it in those terms, I should be eager to see him. If this is going to work out, then every appointment is cause for excitement."

#-#
scene classroomhall
with Dissolve(1.5)
#--#

n "If I can expect to leave our sessions better off than I come into them, what do I have to fear?"
n "But on the other hand, there’s a lot of weight on that {i}if{/i}."
n "Is this really going to work? Even if it does, will it hurt? I’m here because of all the things I’d like to forget, but I know that I’ll only get better if I remember them."

#-#
scene mainbuilding
with Dissolve(1.5)
#--#

n "And then there’s the tiniest voice whispering to me from the distance:"
n "\"Do you even want to get better?\""
n "I can’t afford to listen to it. There’s too much at stake and I have to push ahead."

#-# >school grounds 1 (day)
scene schoolground2
with Dissolve(1.5)
#--#

n "In between my thoughts I’ve found my way to the greenery outside. It’s a natural locus of attraction for all the obvious reasons."
n "Meticulously maintained grass, the gentle breeze, and a sky so clean and clear you could lose yourself in it for hours at a time. It’s hard not to love."
n "St. Dymphna’s is unnerving in many ways, but the scenery almost makes up for it. I could see myself spending more of my time outside than in my own room."
n "And, as I’m sure I’ll be told later, that’s probably better for my own mental health. You aren’t supposed to hole yourself up in a bedroom, as tempting as that’s been as of late."
n "I’m sure I’ll be told many things I’ll have to start keeping track of. A list they give me when I come here so that I won’t need to be here anymore."

#-# >school grounds 2 (day)
scene school1
with Dissolve(1.5)
#--#

n "For now I let my legs continue carrying me in an aimless meandering. As much as I have to limit my pace, I’m left with more time to appreciate the view."
n "This isn’t so bad."
n "Most people are still in their classes but there are still a few students lounging about. I find myself taking notes of ingenious study spots underneath trees and convenient slopes to lay down on."
n "Just thinking ahead is helping immensely."

#-# >school grounds 3 (day)
scene schoolground1
with Dissolve(1.5)
#--#

n "Down one of the paths I notice the school chapel, its towering spire reaching into the heavens. It’s framed rather nicely by a set of flowerbeds and exudes a comforting, protective aura."
n "Didn’t Katja mention singing in the chapel? It was a comment almost in passing, but it would be worth stopping by to see if she’s there."
n "I’ve only heard her humming and even that was impressive. I can only imagine what her full singing voice sounds like."
n "In the worst case I’ll get to admire the chapel interior even if she isn’t there. Seems like a win-win."

#-# >chapel entrance (day)
scene chapelentrance
with Dissolve(1.5)
#--#

n "It’s really quite pretty up close. I can’t say I feel a particular religious fervour  - I’ve never had strong feelings in any direction there - but the architecture is admirable in its own right."
n "More than anything it’s {i}imposing{/i}. I suppose the intent is to humble visitors to the house of God. For my part, it’s doing a decent job of that."
n "And… is that a distant sound of singing I hear?"
n "I guess I came at the right time to catch Katja."

#-# >chapel entrance 2 (day)
#--#

n "I step up to the entrance and the voice grows unmistakably into Katja’s soprano. I can’t make out most of the details through the muffling wall between us but even from here I can tell: she’s good."
n "I guess I’m in for a treat. With my breath half held in respect and anticipation I press on the doors and step through."

#-# >chapel atrium (day)
scene chapelinterior
with Dissolve(1.5)
#--#

#-# music: katja singing
#--#

n "It’s even more impressive from the inside. It isn’t exactly huge, like I’d expect from a full-fledged cathedral or a church, but the chapel is clearly designed to evoke awe."
n "My religious indifference does little to subtract from what I feel being in a place made with such weighty emotions in mind. Whatever someone believes, they’d be hard-pressed not to feel respect for this solemn construction."
n "The steep windows illuminate the interior in bright, sharp relief. The ceiling climbs impossibly high and seems to almost disappear into itself. The pews, one after the next, fill themselves with images of worshippers even when there are none to be seen. It’s all so {i}inspired{/i}."
n "And that’s to say nothing of the music. Katja’s voice is bouncing off all the angles inside the hall and it feels like she’s surrounding me, singing from all sides."
n "The acoustics are remarkable and, honestly, disorienting. I find my eyes scanning all the walls even though I know Katja can’t be there. The noise pulls my gaze in every other direction before I finally looking down to the stage at the end of the hall."
n "And there she is."

#-# > cg: katja singing
scene CG08
with Dissolve(1.5)
#--#

n "This Katja is unlike the Katja I’d spoken to these past two days. To say that she’s different would do her an injustice."
n "She {i}transcends{/i} the Katja of yesterday."
n "Her body is flowing with the song and her every movement drips with feeling. As I walk closer I can see that her eyes are closed from concentration - but her lips are turned up into the faintest of smiles."
n "She isn’t just enjoying herself; she’s losing herself to the music."
n "I find myself doing the same with how exceptional her voice is. I can barely break my stare to slip into a pew and I’m immediately looking back at her, entranced."
n "The sounds come like a warm embrace and I can practically feel each word making its way through me."
n "She’s singing in an unfamiliar language, but it doesn’t matter. I can understand everything I need to know from the way she sings it. Katja’s masterful control of intonation is enough to convey the emotion in her words, and I say that hardly knowing what intonation {i}is{/i}."
n "And I can’t believe the same measured, cordial Katja of yesterday is producing so powerful a sound. Whatever she had shown me of herself, it bore no hints of this."
n "But I suppose I shouldn’t be surprised."
n "Anyone who has a passion is completely different when they’re engrossed in it. That’s what makes it a passion."
n "Watching her now, there’s no question that singing is Katja’s passion. It’s only been a couple minutes and I can already tell how important it is to her."
n "If she’d told me yesterday that I’d be having these thoughts now I might not have believed her. I might have thought she was lying or making fun of me. That mild-mannered girl doing something so intense, so emotional?"
n "It seemed impossible then."
n "If you told me now that Katja could get by without singing, though, I’d call you a liar. She’s giving so much of herself to this performance that if you took it from her, you’d take a piece of her with it. Even I can tell that much."
n "I’m more than happy to sit through the rest of this. It’s is just what I need after a third day that didn’t go much better than the last."
n "I close my eyes and lean back, giving all my attention to Katja’s voice."
n "The song rises and falls, it ebbs and flows, and at some point I stop thinking about it. Katja’s reduced it to pure emotion."
n "I can only imagine how much she feels to be able to sing like this."

#-# >pause
#This is super messy TODO
$ renpy.pause(1.0)
#--#

n "I don’t know how long to expect the song to last and, quite frankly, I’d be happy resting here for a full half hour listening to it. It’s only another two or three minutes before Katja’s voice fades out from the final note, though."

#-#
scene chapelinterior
with Dissolve(1.5)
#--#

#-# >music: katja calm
#--#

n "I open my eyes and find her looking at me with a hesitant sort of expression."

#-# > KATJA IN, Katja_Uniform_P5_E10.png, center
show katja U_P5_E10:
  xalign 0.35 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.55 alpha 1.0
#--#

katja "Erik. I didn’t expect to see you here."
n "I did come unannounced, to be fair. Still, I can’t tell from her tone whether that’s a good or bad thing."
erik "You mentioned this yesterday. It seemed like the friendly thing to do."
n "Maybe I’m laying it on a bit thick; I decided somewhat on a whim but in retrospect I’m glad I did. Sometimes it doesn’t pay to be honest."

#-# >Katja_Uniform_P1_E3a.png
show katja U_P1_E3a
with Dissolve(0.5)
#--#

katja "I see. Stepping up to the plate with your best gentlemanly behaviour. I might be able to put the lunchtime incident behind us at last."
n "I chuckle at this: there’s the Katja I know. It’s comforting, in a way, to see for myself that the two Katja’s are one and the same. If she’d spoken to me with the same composure as she had while singing I might have gone home worried that Katja had an identical twin."
erik "Of course. That was definitely my intention."

#-# >Katja_Uniform_P1_E2b.png
show katja U_P1_E2b
with Dissolve(0.5)
#--#

katja "Consider yourself provisionally forgiven, then."
n "She’s really pushing her luck with this, but I’m in a good mood. Besides, I should humour her as payment for the song. It seems only fair."
erik "I’m provisionally relieved to hear that."

#-# >Katja_Uniform_P1_E12.png
#show katja U_P1_E12
#with Dissolve(0.5)
#does not exist TODO
#--#

n "Now she giggles, and I realise I’d never seen her laugh. It feels almost like a scandalous invasion of privacy, as cordial as she’s been."
n "The moment is gone as quickly as it came, and Katja’s face returns to its usual measured smile."

#-# >Katja_Uniform_P1_E2a.png
show katja U_P1_E2a
with Dissolve(0.5)
#--#

katja "In any case, I’m obliged to ask: what did you think?"
erik "Of the singing?"

#-# >Katja_Uniform_P1_E3a.png
show katja U_P1_E3a
with Dissolve(0.5)
#--#

katja "Well, Erik, I’m not asking about the weather."
n "She got me there."
n "But how do I answer that question? Katja is an incredible singer and I’m not sure how to even put it into words."
erik "I thought it was amazing. Like, really, really good."
erik "I don’t think I’ve ever watched someone sing that well."

#-# >Katja_Uniform_P1_E8a.png
show katja U_P1_E8a
with Dissolve(0.5)
#--#

n "Katja’s smile widens and… she seems to blush a little? Surely with skill like hers, she’s used to all sorts of compliments."

#-# >Katja_Uniform_P1_E2b.png
show katja U_P1_E2b
with Dissolve(0.5)
#--#

katja "That’s very kind of you. I hope you know there’s no need to exaggerate on my account."
erik "Well, you’re right. I don’t need to exaggerate because you’re just that good. How long have you been singing?"

#-# >Katja_Uniform_P1_E3a.png
show katja U_P1_E3a
with Dissolve(0.5)
#--#

katja "Oh, longer than I can remember. If someone told me I was born holding a high C, I might just believe it."
erik "You know, I just might, too."

#-# >Katja_Uniform_P1_E2a.png
show katja U_P1_E2a
with Dissolve(0.5)
#--#

katja "Naturally."
katja "Whenever it was that I in fact started, it’s long become part of who I am. I’m not sure I’d be Katja if I didn’t sing."
erik "From just that one song I think you’re right. It shows in your performance."

#-# >Katja_Uniform_P4_E13.png
#show katja U_P4_E13
#with Dissolve(0.5)
#Does not exist TODO
#--#

katja "You’re being rather generous with your praise. If you wanted to hear another song you can just ask, you know."
n "Easy there, Katja. Your pride is showing."
n "Not that she’s wrong. I wouldn’t mind hearing her sing more, and she’s earnt the praise well. I decide I still owe it to her to play along."
erik "Well…"
n "She interrupts me before I can finish the thought."

#-# >Katja_Uniform_P1_E3b.png
show katja U_P1_E3b
with Dissolve(0.5)
#--#

katja "Unfortunately that was the last song in my set, and I really shouldn’t strain my voice too much. Like any muscle it’s prone to injury."
n "Aha, I have been led on."
erik "Of course. That’s my loss."

#-# >Katja_Uniform_P1_E2b.png
show katja U_P1_E2b
with Dissolve(0.5)
#--#

katja "Indeed, such a pity."

#-# >Katja_Uniform_P5_E5.png
show katja U_P5_E5
with Dissolve(0.5)
#--#

n "She pauses before her next sentence."

#-# >Katja_Uniform_P5_E8a.png
show katja U_P1_E8a
with Dissolve(0.5)
#--#

katja "I’m glad you decided to come, though. I don’t usually have an audience and it helps, now and again."
n "I hadn’t thought about it before but she makes an interesting point. There wasn’t a single soul in the chapel watching when I came in - or rather, none that still had a body."
n "It’s a bit surprising. I know I’d come by once in a while if I knew someone like Katja was practicing. It’s basically a free performance."
n "It must get distracting, though. There’s a reason an audience only helps “now and again” and I’d expect Katja to choose her practice times around the more quiet parts of the day. It was good luck that I ended up here during one of her practices."
erik "I’m glad to be of help. I have my gentleman’s reputation to uphold, after all."

#-# >Katja_Uniform_P5_E3a.png
show katja U_P5_E3a
with Dissolve(0.5)
#--#

katja "I think you can only uphold things that actually exist, Erik."
erik "Ouch. There goes my gentleman’s honour."

#-# >Katja_Uniform_P5_E3b.png
show katja U_P5_E3b
with Dissolve(0.5)
#--#

katja "Same answer."
n "You know, I think I’ve paid for my attendance at this point. Katja’s just messing with me now."
erik "Are you always this polite to your fans?  I think I’m beginning to see why your practices are sold out."

#-# >Katja_Uniform_P1_E10.png
show katja U_P1_E10
with Dissolve(0.5)
#--#

katja "Oh, so you’re a ‘fan’, now? A bit premature after one song, don’t you think?"
n "I’ve been outplayed. It might not be too late to gather the scattered ashes of my ego."
erik "What can I say? I have a refined palate and eye for talent."

#-# >Katja_Uniform_P1_E8b.png
show katja U_P1_E8b
with Dissolve(0.5)
#--#

katja "I’d ask you to get your vision checked but that degree of self-deprecation is something even I’m not willing to employ for the sake of a joke."
erik "Good. I win."
n "Her eyebrows shoot up."

#-# >Katja_Uniform_P1_E10.png
show katja U_P1_E10
with Dissolve(0.5)
#--#

katja "I didn’t realise we were having a competition."
erik "You started it!"

#-# >Katja_Uniform_P1_E2b.png
show katja U_P1_E2b
with Dissolve(0.5)
#--#

katja "Ah, there’s your knightly chivalry. I’m glad to see it’s alive and well."
n "Grinning at me, she slips her phone from her pocket and glances at the display."

#-# >Katja_Uniform_P1_E2a.png
show katja U_P1_E2a
with Dissolve(0.5)
#--#

katja "As much as I’m enjoying this honourable exchange, I have to get going."
katja "I arrange my practice sets in between other obligations and one of those is about to begin."
n "Other obligations? I open my mouth to ask and only just stop myself in time. That degree of curiosity is hardly warranted after our third meeting, and it’s especially tactless with the types of obligations students here might have."
n "Still, I am curious. What are all the things people do here in their free time? I might need to ask Katja at some point."
n "For now, she’s gathering her belongings from the corner of the stage. As she slings her bag over her shoulder she looks back at me and smiles."

#-# >Katja_Uniform_P1_E3a.png
show katja U_P1_E3a
with Dissolve(0.5)
#--#

katja "I did mean it, by the way."
erik "Mean what?"

#-# >Katja_Uniform_P1_E8a.png
show katja U_P1_E8a
with Dissolve(0.5)
#--#

katja "I appreciate you coming, especially since I never asked you to. It’s a kind gesture."
n "She’s still on about that? I didn’t think it was such a big deal, but I can see how it might get lonely practicing on your own all the time."
erik "It’s nothing, really. It was my pleasure."

#-# >Katja_Uniform_P1_E2b.png
show katja U_P1_E2b
with Dissolve(0.5)
#--#

katja "It might feel like ‘nothing’ to you, but you’ll find in time that not everyone is so forthcoming as you appear to be. So I’m grateful, even if it’s for nothing."
n "That’s an unhelpfully ambiguous sentence. Is it a warning? A bit of life advice, or just an offhand comment? How exactly are people not so forthcoming? I bookmark it for later."
erik "Ah… I see. You’re welcome."
n "Ready to go, she gives me one last smile."

#-# >Katja_Uniform_P1_E8b.png
show katja U_P1_E8b
with Dissolve(0.5)
#--#

katja "I look forward to seeing you around more. Let me know if you need help with anything. I try to make people feel welcome."
erik "Thanks. I’ll see you later."

#-# >KATJA OUT
show katja U_P1_E8b:
  easein 1.0 xalign 0.35 alpha 0.0
#--#

n "With that, she’s off. Her shoes tapping on the ground and echoing around the hall remind me of the performance I’d just seen and I think again of the stark dichotomy between singing Katja and chatting Katja. I guess I’ll grow used to it in time."
n "I still have some time before my appointment with Dr. Faber so I decide to give the chapel a more thorough look. Distracted as I was with Katja earlier, it’s only now that I notice some of the details."
n "The windows aren’t just impressively tall: they’re also filled with intricate stained-glass artwork. Here and there I can recognise the images as representing Biblical figures, but even those that look unfamiliar are rather beautiful."
n "I’m reminded of all the nursery rhymes and childhood hymns. They were surprisingly effective at teaching me what I never had the interest to learn by reading."
n "I suppose that’s what they call an \"oral tradition\"."
n "I also realise that behind the stage, obscured somewhat by shadows, a gargantuan array of pipes reach up most of the way to the ceiling. A chapel is incomplete without a pipe organ, but I didn’t see it until now."
n "It occurs to me that Katja sings as part of a choir. Do they ever use instrumental accompaniment? More to the point, does Katja ever sing over the organ?"
n "She’s already impressive, but the thought of her voice over the brassy, booming pipes gives me goosebumps. I’d pay to see that."
n "Through my thoughts I hear footsteps approaching from an inside chamber at the side of the hall. Just as I’ve turned to look, a heavy door swings open with a creak and a congenial-looking elderly man steps through. "
n "From his attire it’s clear he’s some sort of priest. Like the organ, I should have expected his presence, but the thought never occurred to me."
n "He smiles at me across the pews and makes his way toward me."
oldpriest "I see you’ve met Ms. Böhm!"
n "His voice meanders around the hall with a comforting depth. It isn’t loud, but it’s stronger than I’d guessed from his narrow frame, and deeper too."
n "I can imagine what it would be like to listen to his sermons - reassuring, even if you’re not sure you understand his meaning."
erik "Ah, yeah… we’ve spoken a few times."

#-# >FATHER MAX IN, FatherMax_P1_E1.png, center
#--#

n "As he reaches me I can make out some of his features more clearly. His pensive gray eyes observe me without a hint of judgment, and his wrinkles show the age of someone who’s spent most of his life smiling. Gentle is how I’d describe him, in a word."
n "He gives me a once-over himself and offers another smile, which I do my best to return."
oldpriest "I’m Father Maximillian Steinhoff, rector of St. Dympnha’s. That is a fine mouthful, however, and you should feel free to call me Father Max."

#-# >FatherMax_P1_E3.png
#--#

fathermax "I assume you are the new arrival, Erik Wilhelm? I’ve not seen you yet."
n "As Father Max says this he extends a hand and I shake it and nod, putting these new pieces together. Of course we’d have a Father at the chapel, that much makes sense. But if he’s a rector…"
erik "...you’re in charge around here? Not the principal?"

#-# >FatherMax_P2_E1.png
#--#

n "Now he grins."
fathermax "Ah, yes, in practice he is the principal principal. My responsibilities tend toward the ecumenical and it serves the school best for me to leave him to his duties. He performs them admirably.”"
n "A sinecure. I see. For a clergyman to lead the school is still a bit of a surprise; I’ve hardly been doused in religious rhetoric since arriving here. That said, the connection isn’t hard to make."
erik "I guess with a name like St. Dymphna’s I should have guessed this was a religious institution."
n "He holds up a hand as though he’s asking for my patience."

#-# >FatherMax_P1_E2.png
#--#

fathermax "Strictly speaking, Erik, you are correct: this is a religious institution."

#-# >FatherMax_1_E1.png
#--#

fathermax "That said, I wouldn’t worry yourself about any implications of that term."
fathermax "Once upon a time this was a Jesuit monastery and on paper it’s still the property of the order… but that is purely theoretical."
fathermax "The legal status is neither reflected in school policy nor priority. We have religious services for those who would attend, but you’re not obligated to them."
n "I want to say that that’s a relief, but I realise that might be rude."
erik "I understand. Thank you for the clarification."

#-# >FatherMax_P2_E2.png
#--#

n "Father Max gives me a nod."
fathermax "I’m here to help however I might. You’re welcome to contact me if I can ever be of assistance - and that offer isn’t restricted to religious circumstances."
erik "I will."
n "Now he looks down the hall at the entrance through which Katja had left just now."

#-# >FatherMax_P2_E3.png
#--#

fathermax "Katja doesn’t usually have visitors during her practices, you know."
erik "Yeah, she told me."
erik "We were talking yesterday and she mentioned that she sings here often, so I thought I’d stop by after class."

#-# >FatherMax_P2_E4.png
#--#

fathermax "I’m glad you did. I don’t think enough people appreciate that girl’s talent."
erik "There’s a lot to appreciate, that’s for sure."

#-# >FatherMax_P2_E3.png
#--#

n "I think he raised his eyebrows a little at that, but if there was any movement he carries on unperturbed."
fathermax "Indeed. She’s practicing for the Gala in two weeks. I’d strongly recommend you attend."
n "That’s right. The school festival. It would make sense for Katja to perform then; that would be something to see."
erik "I’ll be sure to."
n "I hesitate. Something Father Max said weighs on my mind and I contemplate addressing it for a moment."
n "It couldn’t hurt to ask, I decide. The very worst case is that I get no answer."
erik "If I might ask…"
fathermax "Hm?"
erik "You mentioned religious service for those who want to attend."
erik "Is Katja one of those people?"
n "Now his eyebrows definitely shoot up, but he returns to his standard, pleasant expression soon enough."

#-# >FatherMax_P2_E1.png
#--#

fathermax "While that isn’t protected information, Erik, it would not quite be appropriate for me to divulge."
erik "Right. I’m sorry."

#-# >FatherMax_P1_E1.png
#--#

fathermax "That said, Katja’s singing brings her here often."
fathermax "And it seems to have brought you here, too. I'm glad to see you're finding friends."
n "Are Katja and I really friends? I realise I don’t know what the boundaries of the word are. I’d be reluctant to apply it to us already, but if she said it were so I don’t think I’d object."
n "I guess we’re friends-ish. Friend-adjacent. Approximately friends."
erik "Something like that."

#-# >FatherMax_P1_E2.png
#--#

fathermax "Then permit me to offer you some advice, to your mutual benefit."
n "Oh? Where could he be going with this?"

#-# >FatherMax_P1_E1.png
#--#

fathermax "I'm sure that with the nature of this school, you've found yourself thinking perhaps more than usual about your social interactions."
erik "Well…"
n "He's not wrong. But it's a bit embarrassing to admit, since those thoughts are usually of a more judgmental sort."

#-# >FatherMax_P1_E2.png
#--#

fathermax "It's quite alright, Erik. That was not an accusation. It's natural to tread more carefully in a place like this. Wise, even."
erik "Right."

#-# >FatherMax_P1_E3.png
#--#

fathermax "In fact, I bring it up only to give my recommendations on the very same matter."
fathermax "You will of course be aware that, unfortunately, those with mental conditions of all sorts have to contend with a great deal of stigma. It can be overwhelming."
n "I shift a little at this. Until very recently I was responsible for some of that stigma. Even now, it's hard not to be on edge around some of my classmates."
n "If Father Max noticed my unease, he didn't respond to it."
fathermax "Given this, many of the students here have had to learn to put up appearances. It does not do to show your true self to every stranger when many of them have treated you poorly for it."
n "I'm reminded of the panic attack I had during Ela's tour. The way everyone just looked at me, and of how uncomfortable it was."
erik "Yeah. I get that."

#-# >FatherMax_P1_E4.png
#--#

fathermax "I expect you will also understand that as part of this facade, students often find that they need to effect a more stoic demeanour than they actually feel."
n "And now I'm reminded of how, right after the attack, I tried to put on a calm face for everyone else's sake."
erik "Yeah."

#-# >FatherMax_P1_E3.png
#--#

fathermax "You should not be surprised, then, if you find that people here appear to change as you grow close to them. Of course, they aren't changing; they're merely showing more of themselves to you. And you, in turn, will show more of yourself to them."
fathermax "More thoughts, more feelings, more sensitivities."
fathermax "What I want to suggest to you is that as these days come to pass, you'll find yourself treading as carefully as before. You'll still need to think before you speak."

#-# >FatherMax_P1_E1.png
#--#

fathermax "But where with strangers, you may not see the obstacles in your path, with friends, you'll know that the step you're taking is the right one. That is, if you've paid attention."
fathermax "And that is my advice to you, Erik: pay attention to the friends you make. They will need you as you will need them. When the time comes, you will know how to be there for them, if you've paid attention."
n "This sounds a bit much. I'm not socially inept—I know to listen to my friends. It's hard not to feel condescended to at Father Max's words."
n "But I guess guidance like this is exactly how a school of maladjusted kids is able to stay afloat. The little reminders to steer you in the right direction."
n "We all have our own triggers and preferences we have to keep in mind. Father Max is doing me a favour by putting that front and center in my head."
erik "I’ll keep that in mind, I appreciate it."

#-# >FatherMax_P1_E2.png
#--#

fathermax "Very good. As a rule you’ll find that advice useful for anyone, but in Katja’s case exceptionally so."

#-# >FatherMax_P1_E1.png
#--#

fathermax "This isn’t a warning, to be clear. I’ve just seen what careless ‘friends’ can do to a student. Everyone here deserves a brighter future than that."
n "Aha. There's the hint. However grandiose the Father's words may have been, he's saying them for Katja's sake specifically. He can't be obvious about it, but this isn't just generic teacher advice."
n "I feel like I understand his intentions better now. He's just looking out for his best singer. It's good that Katja's found someone she can rely on like that."
n "I might want to think about doing the same, in time. We’re nothing without our supports."
erik "Of course. I like to think I’m a decent friend, Father."
fathermax "I’m sure you are."
fathermax "For my part, I must be off."
n "He grins in good humour."

#-# >FatherMax_P2_E2.png
#--#

fathermax "I’ve got a rather large pile of church paperwork to get through. I only stepped away to give you my welcome."

#-# >FatherMax_P1_E1.png
#--#

fathermax "So, welcome to St. Dymphna’s. I hope to see you around."
n "I wave as he turns back toward the side room."
erik "I’ll be around."

#-# >father max out
#--#

n "I’m left once again with my thoughts and I realise I’ve lost track of the time. I check my phone: it’s getting close to my appointment with Dr. Faber. "
n "I’ll probably be fine, but just in case I get lost along the way, I decide to head there now. Better to arrive early with time to spare than be late to my very first meeting."
n "I take one final look around the chapel hall as I exit. I can still almost hear the faintest echoes of Katja’s voice."

#-# <end>
#
#--#


########

jump A1_20 # jump A?_??
