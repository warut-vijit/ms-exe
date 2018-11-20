label A1_25:
############

$ persistent.scene_number = "A1_23" # current scene
$ persistent.scene_name = "Grace and Gratitude" # current scene name
$ renpy.save_persistent()

# Backgrounds: Classroom, School Corridor, Cafeteria
# Sprites: Katja
# Music: School Theme (day), Katja Calm Theme

#-# <scene open>
scene classroom1
#Temporary audio stops
stop music fadeout 1.0
stop music2 fadeout 1.0
stop ambience fadeout 1.0
stop ambience2 fadeout 1.0
#--#

#start scene music
play music "music/Be_Green.mp3"


n "There’s a certain {i}je ne sais quoi{/i} about the way the school bell punctuates the end of French class."

n "It’s sort of a relief, for one. The sound liberates me from the droning of the instructor and lets me set aside the prospect of memorising vocabulary for a minute."

n "But right now it brings apprehension, too. It’s lunch again and I’m faced with the ordeal of having a meal in a place that’s still very unfamiliar."

n "I’m not one to depend on consistency, but I still appreciate a stable schedule. Every day at St. Dymphna’s has been an adventure so far. Sure, there’s something nice about improvising each day as it comes, but..."

n "I can’t say I like the idea of my lunches always being adventures. I just want to have a comfortable meal today."

n "It’s all I can do to push myself off my chair and up on my feet. It feels almost more than I can do to lumber toward the classroom door so I can make my way to the cafeteria, but I manage it in time."

scene classroomhall

n "My protesting leg has already delayed me so long that everyone else disappeared down some hall or another."

n "It doesn’t bother me. It’s difficult to feel left behind when I don’t know any of the people who’ve gone ahead. They’re all faces I can’t keep track of, anyway."

n "Maybe I’ll run into one of the few familiar faces at lunch. It’s easiest to eat alone when you don’t know anyone, but I think I’ve made a couple friends and I’d appreciate their company over a meal."

n "Besides, I won’t get better if I hang out on my own all the time. Dr. Faber didn’t prescribe 'sixty minutes of socialisation a day' but I imagine he’d disapprove if I tried to be a loner."

n "Everybody here is dealing with something, and it must make a difference to be surrounded by people you can trust will understand. Most of them, anyway." 

n "Even a complete tease like Fran has that seed of compassion somewhere, I’m sure. If it came down to it, even they would set aside their act and be a decent person. This is just that sort of place."

n "So it’s decided: I’ll try to find someone I know at the cafeteria. Even if it’s Fran. I shouldn’t—don’t want to—get in the habit of eating on my own or waiting for someone to feel sorry for me. This is my initiative to take."

scene cafeteria

n "One good thing about being slow is that by the time I arrive, the worst of the lunch rush is gone. People are either seated or taking their food elsewhere and I can step through the line nice and quick."

n "I guess that’s exactly the kind of optimism I should be adopting here. See the bright side of things."

n "I’ll always be too late to hit rush hour!"

pause 2.0

n "Yeah, I’m laying it on thick."

n "Still, it’s something to keep in mind. This isn’t all bad."

n "Just as I close that thread I reach the front of the food line. Blinking to clear my mind, I get a hearty portion from a pleasant, portly serving lady. I thank her and turn around to survey the tables." 

n "Right. Who do I know?"

n "None of the students seated on the near side seem familiar. I can’t spot Ela’s bushy hair, nor Fran’s perpetual smirk, nor Natalya’s blonde bob." 

n "Maybe they’re obscured somewhere in the crowd, but somehow I doubt it. They’re all quite distinctive in appearance."

n "I weave around chairs and edge to the opposite side of the cafeteria, craning my neck and continuing my survey. There has to be at least one person I know here."

n "For a moment I’m hit with a self-conscious twinge of anxiety; I must look like an idiot, staring in every direction on my own. A black sheep obviously out of place."

n "I have to shake my head to dismiss the thought. I’m just looking for a friend, right? That’s not so strange. Everyone does that. Worries like these get me nowhere."

n "Resuming my search, my eyes reach the far corner of the cafeteria. Last chance."

n "Aha."

n "A thick head of strawberry blonde tells me all I need to know. Katja’s there, sitting with a few of her friends. Conveniently, there’s a free spot across from her."

n "I hesitate at the sight of the others—if Katja’s busy talking to them maybe it’s best to leave them alone. I’d hate to force myself into a situation where I’m not welcome."

n "Still, I decided I wouldn’t be eating alone and it looks like Katja’s my only chance at that. I’ll have to trust that she’ll turn me away gently if it’s a problem."

n "I step past the last of the furniture between me and the corner table and stop at the near end." 

n "Noticing me, Katja breaks off from her conversation and looks my way, giving the tray in my hands a glance."

show katja U_P1_E1:
  alpha 0.0 xalign 0.6 yanchor 1.0 ypos 1080+425
  easein 1.0 xalign 0.5 alpha 1.0
with Dissolve (0.25)  

# TODO: ADD KATJA CALM THEME

katja "Hello, Erik."

katja "My intuitions tell me you’re looking for a seat."

erik "I didn’t realize your intuitions looked like a tray of food."

katja "Clearly, you’ve been slacking in your philosophy classes. It’s elementary metaphysics."

katja "That aside, would you care to join us?"

n "She motions to the open spot across from her and I nod, setting my food down and taking the seat."

erik "Thanks. I hope I’m not interrupting anything."

katja "Not at all. We were discussing the choir’s plans for the upcoming Gala. As important as it is, it can wait."

katja "However, introductions are in order. Everyone, this is Erik Wilhelm, a new student in Ms. Claes’ class. Erik—"

n "She begins to motion at each of the others in turn."

katja "—this is Effie, Suraya, and Maria. They’re fellow members of the choir."

"I nod and blink, making a concerted effort to engrave the names and faces into my head. I’m confident I’ll fail, but it seems like common courtesy to try."

"They all smile at me by way of a greeting and we’re thrown into the formulaic exchange of pleasantries. I answer and ask the standard how do you do questions as they come, glancing at Katja all the while."

"By the time we’re done with the extended introductions, I confirm that I’ve completely forgotten their names. I temporarily number them one, two, and three, hoping to be reminded of their identities before it’s obvious I forgot."

"But Katja motions to them before I can say anything, and they resume the conversation on their own. It seems she anticipated my apprehension and decided to make this a one-on-one talk."

"I give her a prayer of thanks for sparing me from the inevitable awkwardness."

"Now she looks back at me with interest. It’s a look of respectful attention, the same one she seems to maintain every time we speak."

"There’s something genuine about it, but also something detached. As though she wants to keep a little distance. I wonder if this is the façade Father Max was talking about."

katja "So, Erik: how have you been?"

n "It’s an innocent question, but I realise I don’t know how to answer it. It’s only been a day since we last talked and yet so much has happened."

n "When someone asks how you are, it’s supposed to be a superficial inquiry. You’re supposed to tell them you’re fine and move on."

n "But when Katja asks how I’ve been, something in her tone prompts me to really consider my answer; how have I been, actually?"

n "The question opens a messy can of worms and I find myself unable to close it. It feels impolite to vent to a new friend, but the words come out before I can stop them. I swallow the food I’ve been munching on and answer."

erik "I’ve been getting by, you know? It’s still a bit overwhelming orienting myself here."

katja "Of course. You’d do best not to push yourself in that respect."

katja "As I mentioned at our first meeting, these things take time. We were all in your shoes, and we’ve all grown into the ones we wear now."

erik "Right, but—"

katja "—those words can sound empty. I know. There’s only so much anyone can say to alleviate the anxiety. In the end, the bulk of it falls squarely in your own hands."

n "I sigh. She’s right, unfortunately, and I have to face the fact that I need to deal with this myself."

katja "This is never to say that you must do it alone. The distinction is important. There are things others can do for you, and there are things you must do for yourself, but those around you can help with the latter."

katja "It’s important to keep that in mind. At St. Dymphna’s, you should never feel lonely."

erik "Right."

erik "That’s actually why I came here, sort of. To this table specifically."

katja "Oh?"

erik "I told myself I couldn’t keep waiting for someone else to come to me and I decided to look for someone I knew at lunch."

erik "It took a while, but I managed to spot you here in the corner."

erik "So, in a way, I guess this is me taking your advice before it was given and trying not to be alone."

katja "Lonely. Not alone."

katja "Regardless, I’m very happy to hear that, and I’m glad I’ve managed to be of assistance."

erik "When you put it that way it sounds so sterile."

katja "My apologies. It’s an occupational hazard."

erik "Occupational hazard? Of what occupation?"

katja "Being me."

n  "She says this with a giggle, and I’m reminded how rare it is to see her break the cover of formality. This must be another piece of what Father Max was alluding to: the reality underneath the façade." 

n "Maybe I’ll see more of this true layer of Katja in the days and weeks to come. Getting her to laugh is definitely satisfying. It feels like a sign that I’m doing something right in my interactions with the people here."

n "If the ever-cordial Katja is comfortable enough with me to let out a giggle, then maybe I’m not so awkward as I thought."

katja "How was the rest of your Wednesday evening, by the way?"

erik "Ah, well… it was eventful."

katja "Eventful?"

katja "A good or a bad kind of eventful?"

erik "A bit of both, I think. There were many events."

n "She raises an eyebrow and I feel her eye bore into me, not with any malice but with a healthy dose of sarcasm."

katja "Would you like to discuss any of these events, or shall I continue to prompt you and advance this conversation in sentence-length episodes?"

n "That’s a pretty blunt way to put it, but I can tell that beneath the teasing she’s got a point. I have to decide for myself what I want to talk about."

erik "I had my first appointment with Dr. Faber, for one."

katja "I see. That would be enough to make any day eventful on its own. The first appointment can be a significant milestone for the students here."

erik "It was, in a way. I had my own expectations and to be honest, he defied them — I was pleasantly surprised."

erik "I came in cynical about the whole thing but I left genuinely feeling a little better and hopeful, you know? I didn’t think it would affect me so quickly."

erik "The idea of therapy seemed dark and mysterious to me and I’m starting to realise that may have been wrong."

katja "It may have, but you wouldn’t be the first to have the idea. I fear popular representations have painted therapy in a rather bad light."

katja "Every year an appreciable proportion of the incoming class has the same concerns and finds them allayed soon enough."

katja "I’m glad you had a good first experience with Dr. Faber. I expect it’ll help to be able to look forward to your sessions."

erik "Absolutely. I’d be lying if I said I wasn’t anxious before the first one, but now I can feel relaxed about it."

katja "I think you’ll find that that alone helps with the treatment tremendously."

erik "I hope so."

katja "I’d count on it."

katja "So, that was the first of multiple events. Shall I ask about the next?"

n "I still feel guilty unloading my worries on Katja, but she seems happy to talk about them. I’m also feeling better for having started this conversation; Katja has a good sense for what to say." 

n "I guess I don’t have any reason to stop now."

erik "You remember how when we first met, you asked me about my sandwich?"

katja "Yes."

erik "You called it ‘protocol’ and explained how it was useful for gauging individual students."


## TODO: check which choice Erik made in A1_20
# [if wrong Isolda choice in A1_20]
## ref flag : A1_20_bad 

# erik "I’ve been trying to do something similar since then and I’m discovering it’s hard to nail down."

# erik "On my way back from the appointment I ran into someone and... I’m not sure I handled it the best."

# erik "I thought I was doing alright, I tried to be friendly, but I ended up tripping over myself and making things awkward."

# erik "With how different everyone is I don’t know how to improvise the one-size-fits-all approach you used on me and when I try I mess it up."

# katja "I wouldn’t rush to make that comparison. It’s only your fourth day, after all."

# erik "Right, but when will I get better at this?"

# n "Katja pauses and gives me a look, her brows pressed together like she’s giving my question genuine consideration." 

# katja "You said you tried to be friendly."

# erik "I did. Not pushy but still, friendly. I thought I’d try to make conversation."

# katja "I see."

# n "She lets out a sympathetic sigh."

# katja "Unfortunately, Erik, not being pushy isn’t always enough. Noble as it is, if you’re aiming for a general-purpose approach you’ll need to set aside being ‘friendly’ at all."

# katja "You can be cordial and pleasant without being friendly, and given that some people are less than comfortable with friendliness, that is what I’d suggest."

# katja "You can try to be more forward if you’re sure the person would welcome it, but otherwise it’s best to maintain an appreciable distance between them and yourself."

# n "I’m reminded of my first two encounters with Annaliese, the disasters that they were. In retrospect I realized I was pushing too hard, but I didn’t think that meant I should avoid being friendly altogether."

# n "Given yesterday’s events, though, maybe Katja’s right. I have to be more careful. I can’t assume everybody wants to have a conversation and I can’t force it on them."

# katja "For that matter, the same advice goes for people you’re already friends with."

# katja "Sometimes our friends just need a little solitude and in those moments it’s important to respect that."

# erik "I think I get it. But how do I know if someone’s receptive, then?"

# katja "That, alas, is a matter of practice. You’ll pick it up."

# n "I sigh."

# erik: "Alright."

# [else]

erik "I’ve been trying to do something similar myself and I think I might be getting the hang of it."

erik "I ran into someone on my way back from the appointment yesterday and I want to say I did alright."

erik "It was a bit awkward but I was able to talk to the person without making too much a fool of myself."

katja "That’s certainly progress from our first meeting."

katja "But, speaking seriously, I’m pleased to hear that."

erik "Yeah. I guess I’m learning how to gauge people better."

n "My run-in with Isolda definitely went better than the first two times I tried to talk to Annaliese. Sometimes you have t0 know when not to try and engage someone."

n "These are the little lessons I have to learn along the way." 

erik "Before I came here I thought I could get by trying to make conversation with everyone I met, but I’m beginning to understand it’s not so simple."

erik "Sometimes people don’t want to jump right into a talk."

n "Katja tilts her head almost like she’s surprised at my comments."

katja "That’s very insightful of you."

erik "Well, there’s some brain behind all this brawn, you know."

katja "Of that there was never any doubt. It doesn’t have much to hide behind, after all."

erik "Sometimes I wonder why I even try."

katja "Your valiance is endearing."

katja "And yes, you’re correct: there’s more to people than just making conversation. That isn’t an idiosyncrasy of St. Dymphna’s, but something you’ll find wherever you go."

katja "The only reason you’ve been able to get by without that realization so far is that you’ve had enough open people to work with."

katja "When you’re used to receptiveness it’s easy to dismiss those less willing to engage with a stranger as abnormal outliers."

katja "For better or for worse, with the type of school St. Dymphna’s is we have a greater concentration of people who would rather not strike up conversation with someone they’ve only just met."

katja "It’s good you’ve figured this out so soon."

erik "Well, it’s like you said: this takes time, but I’m making progress."

erik "I can’t spend my whole time here playing catch-up to your social skills."

katja "And at this rate, I’m confident you won’t have to."

# [return]

n "The discussion reminds me of the most recent development in my social life. I’m on a roll and I decide to press through, even if I’m just dumping everything that’s been on my mind."

# [if bad Annaliese choice in 1_24]

### check against flag shouldertap=true 

# erik "On that subject, I guess sometimes you just have to give up on someone."

# n "Katja seems to perk up at this comment. She gives me an inquisitive look, and I think I see a hint of concern mixed into it."

# katja "Do you think so?"

# erik "I just mean that sometimes you run into a person who doesn’t want to make friends at all and at that point, there’s no good reason to try."

# katja "There is something to that, to be sure. You’re right that it’s sometimes best to leave a person well enough alone."

# katja "I’d hesitate to call that ‘giving up’, however."

# katja "It’s one thing to acknowledge that a particular person isn’t going to engage with you the way you might want. It’s another to conceptualise that as a resignation."

# katja "The first involves accepting the other person for who they are and moving on from that; the second frames the exchange as a failure and puts the responsibility for that on the person you’ve ‘given up’ on."

# n "Katja’s response surprises me. I’m sure she knows nothing of how my latest 'interaction' with Annaliese went, but she’s still managed to hit the nail on the head."

# n "The whole experience felt like a failure to me, and I realise I was blaming her."

# n "It was frustrating trying to communicate with Annaliese and failing over and over again. How can I reduce that situation to 'accepting' that we’re different and moving on from it?"

# n "Every time I tried with her it felt like poking at an uncooperative brick wall. There wasn’t a single crack to break through and the futility of it got to me."

# n "It’s not even like I did it without thinking. I knew I couldn’t expect a normal greeting to work so I tried a more sensitive strategy—even if I took it too far by literally asking her about sandwiches."

# n "To have all that effort fall flat seems like the definition of a failure, and I can’t see how that’s my fault."

# n "That doesn’t stop Katja’s words from digging at me."

# n "A brick wall can’t help being what it is. If anything, it might be frustrating having people throw themselves at you all the time."

# n "I don’t know if I can just 'accept' that Annaliese doesn’t want to be talked to, but maybe I should accept that it’s not on her that I couldn’t get a conversation going. For all I know, she might feel the same way about me."

# erik "I didn’t think of it that way but I take your point. Putting it in terms of ‘giving up’ was a bit unfair."

# katja "More than that, it closes a door which may still be open."

# katja "I’m not telling you this to prompt you into reconsidering whatever interaction it is you’re alluding to, but as advice for the future. We rely so much on the open doors we find. It’s reckless to close them prematurely."

# n "At this point it just feels like Katja is lecturing me. I want to feel indignant at this, but I’m struggling to justify it."

# n "She’s being a bit presumptuous, but her advice is solid. And, to be fair, I chose to complain to her. I guess I’ll just have to take what she has to say."

# erik "That makes sense."

# [else]

erik "I actually think I’ve had a bit of a breakthrough on that front today."

katja "A breakthrough?"

erik "Yeah. There’s someone in my class I’d been trying to talk to for a few days. Nothing I tried was working; they just wouldn’t say a word to me."

n "Katja nods and gives me a knowing look. I’m not going to bother identifying Annaliese to her but I expect word gets around about someone so quiet. It wouldn’t be difficult to guess who I’m talking about."

erik "But then this morning I switched to more indirect form of communication and it actually worked."

erik "I was on the verge of accepting, as you said, that we weren’t going to have any sort of conversation, but all it took was a little shift in my thinking."

erik "My old book of social tricks won’t always work here but I think I’m giving it a good update."

katja "That sounds like a lesson well learnt."

katja "As much as opening moves like my sandwich inquiry are catered to work with a wide audience, a change of tactics is sometimes in order."

katja "Learning to act with that kind of flexibility will get you far here."

erik "It was satisfying, to say the least. I’m taking it as a sign that maybe my time here will actually work out."

katja "It will pass more easily if you’re not shooting yourself in the foot quite so often, yes."

# [return]

n "At this point I notice I’ve gone through most of my meal and made the conversation into an impromptu therapy session. I should probably fix that before the entire lunch break is gone."

n "I glance at number one, two, and three, and they seem to be engaged in standard classmate small talk. Wanting something a little more substantial, I think back to the conversation I interrupted when I first arrived."

erik "Anyway, you said you had planning to do for the Gala?"

n "Katja blinks at the sudden gear shift, but catches on quickly enough with a smirk."

katja "You aren’t obliged to humour me, you know."

erik "It isn’t an obligation, I’m really curious—and besides, what kind of gentleman would I be if I spent the whole lunch talking about myself?"

katja "Not too different a kind from the others I’ve met, suffice it to say."

katja "But yes, the choir has a performance planned for the Gala. There are details to be worked out about our roles and we’ll be spending much more time in practice…"

katja "I expect it’ll keep me quite busy the next ten days."

erik "When are you performing? Sunday?"

katja "That’s right, per the obvious religious associations."

katja "It’s one of the most ambitious events we have every year and the coordination it takes is substantial. We have to arrange multiple solos and the length gets exhausting."

katja "At the same time it’s something we’ve always been proud of. Most of the school turns up to watch, and given the withdrawn tendencies some of them have, that’s saying something."

n "Now she pauses and looks off to one side, pensive. Her expression clouds into troubled thought, like she’s considering something and isn’t sure how to judge it."

n "It’s a bit surprising; Katja usually cruises through a conversation with ease. I wouldn’t have expected her to freeze up like this."

n "I wait for her to work it through and after a moment, she looks back at me and speaks."

katja "I like to think that it gives everyone a bit of hope for the year. The concept can be so foreign to a lot of us here, and I want to make it familiar."

katja "Preparing for the Gala invariably puts us under intense pressure, but I feel it’s worth it. As a performance it’s a spectacle to watch, but more than that I want it to lift everyone’s spirits."

katja "If I—if we—manage to do that, then I can take the heat of the preceding weeks."

katja "A little hope can be enough to save someone."

n "For a second I just look at her, not sure how to respond. The sincerity of what she said takes me off guard and I realise she hasn’t been in the habit of revealing her feelings like this."

n "At the same time I notice that she’s looking at me expectantly. That’s fair enough—some acknowledgment is required on my part."

erik "I’ve obviously never been to one of these but I can see how important it would be."

erik "And you’re right. A little hope can go a long way when someone is at their lowest."

n "I don’t need to make it clear that I’m speaking from experience. I think we can all speak to it the same."

erik "If you put that much effort into it I think there’s a good chance it’s having the intended effect. I know I’m looking forward to seeing it."

n "Katja lights up at that last sentence."

katja "Oh, excellent! I’m eager to know what you think of it, when the time comes."

katja "For now I just have to focus on our practices."

erik "If they’re anything like what I saw you do yesterday, I’m sure you’ll be fine."

katja "Thank you."

katja "I do want to thank you again for coming to watch, and actually…"

katja "I also wanted to more formally invite you to see my practices, whenever you’d like."

katja "I often practice on my own, as you saw yesterday. Having someone I know there is helpful."

katja "Even during group sessions I appreciate having an audience, particularly one who can give their thoughts unsullied by musical formalism."

n "More chances to see Katja sing? Her invitation is practically a free season pass to the movies and I’m very tempted."

n "As I acclimatise to St. Dymphna’s I expect my schedule will fill up and it might be difficult to find time for that. Still, setting aside half an hour now and again to sit in on Katja’s practices is not too shabby an idea for leisure."


# TODO: MENU CHOICE AND POINTS
menu:
    "Yeah, that would be great!":
        jump great
    "Sure, I'd like to visit when I can!":
        jump visit

label great:
# Katja +1

erik "Yeah, definitely, that would be great!"

erik "I could use something to unwind, and I’d enjoy being at your practice sessions."

erik "Just let me know when and I’ll make some time to drop by."

n "Katja gives me a wide smile and inclines her head in a gentle bow."

katja "Thank you, Erik. I’ll keep you informed."

katja "In the meantime, we might want to finish up here. Our break is nearing its close."

n "I check my phone—she’s right. We’ve used up all but ten minutes of our lunch."

n "I’d say it was time well spent."

n "I stack my empty plates on the tray and stand up with the elegance of an arthritic man, but that can’t be helped. Katja collects her own things and waves goodbye to her friends before giving me one last smile."

katja "It’s been a pleasant conversation. I look forward to seeing you around at our sessions."

erik "Sure, count on it. I’ll see you later."

#-# >Katja out
show Katja U_P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#

n "And with that we make our way back to our classes."

jump resume_25

label visit:

erik "Sure, I'd like to hear you sing again! I'll try to come when I can."

n "Katja offers a slight smile in response."

katja "Thank you. I’ll let you know about our sessions."

katja "For now, it would appear we’ve run out of time to talk."

n "I give my phone a quick glance and notice that we only have ten minutes of lunch left."

n "The time went by more quickly than I expected, but I feel like I’ve managed to have a productive conversation with Katja." 

n "As I’m collecting my plates Katja waves goodbye to her friends and gets up."

katja "Thank you for your company, Erik. Perhaps I’ll be seeing you soon."

erik "Yeah, I’ll see you later."

#-# >Katja out
show Katja U_P1_E1:
  easein 1.0 xalign 0.9 alpha 0.0
#--#

n "She heads off, and I’m left to my thoughts on my way to my afternoon classes."

jump resume_25

label resume_25:

jump A1_26
