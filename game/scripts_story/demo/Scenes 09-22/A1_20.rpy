label A1_20:

## I am a dummy file here to provide a choice flag for reference in A1_25 and to allow testing.  ##
scene black

stop music fadeout 1.0
stop music2 fadeout 1.0
stop ambience fadeout 1.0
stop ambience2 fadeout 1.0

##

scene schoolground1
with ScDis

n "I leave the chapel and begin my slow walk towards Dr. Faber's office."
 
n "This meeting should be the least of my worries."

n "Considering that I left so early I have no reason to be late to my first appointment."

n "Glancing down at my watch, I confirm to myself that I have plenty of time to spare."

n "I guess it’s pretty good I left early; I don't know how my leg is going to hold up and I'm not too familiar with the route."

n "It’s probably for the best that I don’t take any risks. But..."

n "Maybe it wouldn’t be so bad if I found myself arriving late to the appointment. I don’t think Faber could fault me for that considering what I have to contend with."

n "Should I really stress myself out over making my way there as soon as possible?"

n "Maybe I could come up with some excuse — miss the session entirely."

scene school2
with ScDis

n "From the corner of my eye, I manage to catch the school's directory, which conveniently points me to the school’s main building."

n "There it is, clear as day. Begging to be noticed by the students on campus."

n "How could anyone possibly miss that?"

n "Sigh."

n "All right then Erik."

n "Enough stalling."

n "..."

n ".."

n "{i}Enough stalling.{/i}"

##(SFX - Walking)

n "Unluckily for me, the road to the therapy offices are pretty intuitive."
 
n "Every path connects to the main walkway in some way or another. All you have to do is walk straight and you're bound to end up where you’re supposed to be."

n "I grit my teeth in frustration."
 
n "Pretty straightforward for a person like me working my way to my psychologist's office."

#### Pause beat
## Stop SFX

n "..."
 
n "My psychologist's office."
 
#### Pause beat
 
n "My visit to Dr. Faber is just another confirmation that I belong here."

n "{i}Stop it. {\i}"
 
n "This school is for the mentally-"

n "{i}No.{\i}"

n "For all the people I’ve met at this school, I can’t afford to think like that."

n "No matter what happened I'm still me."

n "I am still Erik Wilhelm."

n "I exhale my held breath in an effort to relieve some of the tension gripping my body." 

n "No."

n "I’m really not the same anymore."

n "Ignoring my problems won't make them go away, and forgetting my situation won't let me get past it either."

n "Well look at that? I’m already making progress in my head! Maybe I don’t need to sit down and talk about my problems after all?"

n "..."
 
n "That train of thought probably won’t win me any favours with Dr. Faber."

#### BG shift — school courtyard, daytime
scene mainbuildingfar
with ScDis
 
n "From here it’s just a straight shot to the main building."

##TODO I think we can have this all in one line.

n "Yet{w} every{w} step{w} makes me realise how much distance there is between the buildings and myself."

##Think that might be it? idk

n "Every foot forward feels like a losing battle, my leg wobbling dangerously underneath me."

n "In this moment my mind and body are moving in opposite directions."

n "As much as this walk sucks, I just need a few more moments, and finally —"

##SFX Door loudly opening
####  BG shift — corridor in the main building, blue
scene faberhallway
with ScDis

n "— I reach the doors to the school offices."

n "As I stumble through the double doors I’m immediately struck by how blue the hallway is."

n "They probably chose blue to be calming and relaxing, but for me it has the opposite effect."

n "The decor starts to make my stomach churn until I’m forced to look down and concentrate on my footsteps."

n "Of course this school would paint the hallways in a forcefully relaxing color."

n "However with my eyes now on the floor I can now clearly make out the imprints of past visitors’ shoes on the hallway carpeting."

n "I’m horrified to find that my feet are falling squarely into them."

n "I force my head up and find that I’m coming close to a junction. On the wall, a conveniently placed non-blue sign directs me to Faber’s office."

n "Of COURSE!"

n "Just what I would expect from this school — it's comically impossible to get lost, no matter how hard a student might try!"

n "If the campus were more complicated, or there were less signs, then you could conveniently get 'lost'?"

n "How great would it be if by the time I reach the office my appointment were over?"

n "\"It’s not my fault Dr. Faber, just an unfortunate set of coincidences causing me to miss every sign on campus.\""

n "\"Perhaps our meeting will just have to be scheduled for a future time.\""

n "\"A time when I’m not freaking out at this very moment!\""

n "..."
 
n "What a ridiculous thought."

n "Could I ‘forget’ the way here every time I have an appointment?"
 
n "My eyes are already fixed on another sign directing me to Faber’s office."

n "Hell, at this point I can even see his door."

n "Maybe I could just skip it?"

n "What can they do, scold me?"

n "Kick me out of the school?"

n "I shake my head."

n "What is wrong with you, Erik?"

n "I’m already here, standing conspicuously in the middle of a corridor."

n "I’m just around the corner from another nearby office and close enough to hear the light clicks of a keyboard and rustling papers."

n "I’m not alone."

n "Faber’s door is directly in front of me."

n "All I have to do is walk forward, yet my body feels light-years away."

n "My heart is trembling and I can’t find myself able to commit to any kind of motor function."

n "I don't want to do this."

n "I don't want to be here."

n "You have to do this."

n "I inhale sharply and attempt to calm my racing nerves."

n "One step at a time." 

n "Any distance can be covered one step at a time."

n "I can do this."
 
n "It takes some effort, but I’m able force myself to take the final few motions to Faber’s office."

n "Any cynical thoughts are pushed into the recesses of my mind, and any doors of doubt I try to open kept tightly closed."

n "I knock once." 

n "Silence."

n "Maybe he didn’t hear — ?"

#### SFX, door lightly opening

n "Before I can retreat, the door is opened." 

n "I didn't hear any sound of him approaching the door from the other side."

###show Faber neutral fade from center

n "In the briefest of moments he’s simply there, looking professionally composed as the day I met him during Ela’s tour."

n "Only in this moment he’s smiling."

#show faber smile

drfaber "Hello, Erik."

n "I nod stiffly in acknowledgement, feeling more like a deer in headlights than a student here for a simple counselling appointment."

drfaber "Please, come in. You’re right on time."

n "I trudge into the office..."

##BG Faber's office
scene faberoffice
with ScDis

n "...and am immediately thrown off by what I see."

n "This room isn’t how I imagined a therapist’s office would look."

n "Of course there’s a couch at one end of the room, but the entire office feels unexpectedly civilian."

n "It looks like a normal school office; a cramped space covered in sunlight with various papers and books strewn everywhere."

n "One wall is lined with diplomas, accompanied by an assortment of what seem to be personal photos of Faber in his younger years."

n "The strangest part of the room that I can see is that his desk is pushed to face the far side of the wall."

n "Either his back will be facing me the entire time, or he’ll be directly focused on me during our conversation."

n "I’m not sure how to feel about either scenario."

#faber eyebrows raised

drfaber "Erik?"

n "I stiffen as I direct my attention to Faber, hoping he doesn't notice."

drfaber "Would you like to sit down?"

erik "Yes, please."

#faber neutral

n "Just how tense do I look right now? I can feel it in my shoulders."

n "Strategically I look for other seating arrangements beside the couch and can see that I have a few options."

n "Excluding the chair taken by Faber, there are two others in the room."

n "One of them is a beanbag and the other is an armchair."

n "I decide on the latter and try to make myself comfortable on the creased, aged leather."

n "From here, I await judgement."

#faber smile

drfaber "How are you holding up so far?"

n "I nod mechanically, desperate to try and say something."

erik "F-fine."

n "It’s a good start."

n "He doesn’t question my answer and simply returns a nod."

drfaber "I’m glad you found your way here. I can understand how confusing it might be to find your way around an unfamiliar environment."

n "I fight against the smile I feel forming on my face, shrugging."

erik "There are signs everywhere."

drfaber "So there are. Are you ready to get started?"

n "He patiently waits for my response, though at this point it’s not really like I can say \"Nah I’m good, I just showed up to say hey.\""
 
n "I resign myself to a slow nod."

drfaber "All right, then."

n "He has his chair positioned to directly face me, making it obvious that I have his full attention." 

drfaber "How have you been settling in so far?"
 
n "I can feel my chest sink a little."

n "It’s starting."

n "I think carefully about my choice of words and try responding in a way that doesn’t sound problematic."
 
erik "I've only been here a couple of days, but so far I think I'm doing all right."

erik "I mean nothing seems deliberately nasty or anything, I guess?"

#faber neutral
#1.0 second delay
#faber smile

n "Faber’s smile falters a little and one of his hands reaches up to touch a part of his beard."
 
drfaber "Were you expecting things to be deliberately nasty?" 

n "Shit."

erik "Uh, well, no but — I don’t know."

erik "New schools typically feel weird, I guess?"

n "I might have worked myself into a corner here."

n "Faber nods."

drfaber "I understand. It can be difficult to adjust to a new school, but I am glad nothing bad has stood out to you."

drfaber "Though I {i}am{\i} surprised."

#faber eyebrows raised

drfaber "I mean, when I came in a few years back I certainly found the school’s {i}food{\i} to be deliberately nasty."

n "... Huh?"

n "His comment throws me off guard."

erik "You... think the food here is nasty?"

#faber big smile

drfaber "I think you might be a little spoiled now. It's much better than it used to be."

drfaber "Though it was hard for me first starting out." 

drfaber "Before my time here I did a little traveling and, I admit, grew a little attached to some of the fancier European cuisines."

n "Before I realise it my body is leaning towards Faber, and I find myself engaged in the conversation."

erik "Where’ve you travelled?"

n "A twinkle of light flashes across Faber’s eyes."

drfaber "Well...where can I start?"

drfaber "I’ve of course toured France’s countryside: from the waters of Saint-Malo all the way down to Toulouse, where I spent a summer. I’ve seen the Atlantic in Porto and the Mediterranean during winter in Venezia."

drfaber "I did enjoy my time in Switzerland quite a bit. Lucerne, Basel-"

erik "That’s — !"

n "I excitedly start to interrupt Faber, but retract immediately once I realize that I’ve rudely interrupted him."

n "He shakes his head with a soft smile."

drfaber "You are not at fault, Erik. What did you want to say?" 

erik "I was just going to say that Basel is where I grew up. My parents live out there now, but it was our whole family's home for a while."

n "Surprising myself, I start talking about my experiences back home."

n "I talk for awhile about growing up and the fun memories I shared with my brother and sisters. Soon enough, I realise I'm smiling without having to force it."

drfaber "I see. Basel is a lovely city to raise a family in. I understand your older siblings moved out not too long ago, correct? "

erik "My brother Gustav moved out a few years ago, and my sisters just recently moved in together in Vienna."

drfaber "Why don't you tell me more about them?"

n "No matter what I say Faber patiently listens and engages in the conversation."

n "This isn’t an interrogation."

#timeskip
scene PitchBlack
with Clockwipe
scene faberoffice
with Clockwipe

n "Towards the end of our session Faber turns to pick up a thick folder from atop his desk."
 
drfaber "Now, before we leave off today, I would like you to go through some extra paperwork so that I can get a better idea of your situation."

#faber eyebrows raised
drfaber "Do you mind?"

n "I shake my head."

#faber neutral

n "The folder he passes me is so thick that I don’t need a clipboard to write my answers down."

n "Thankfully the questions are all multiple choice, so I don’t focus too much on the folder’s weight."

drfaber "Don't overthink your answers, just go with what seems right in the moment."
 
n "He passes me a pen, and with little hesitation I begin to mark down the answers I feel comfortable with."
 
n "I’m surprised by how much more at ease I am even filling out personal medical questions."

## Timeskip
scene PitchBlack
with Clockwipe
scene faberoffice
with Clockwipe
 
n "Minutes later, I put down the pen and pass the papers back."

n "The joints of my fingers are a little sore, but I survived."

n "Dr. Faber flicks through all the papers at an inhuman speed. I’d be surprised if he could actually read any of the documents he’s skimming."

n "It’s only at the very end that he pauses briefly, reading one of the last sections a little more thoroughly, before closing the entire folder and setting it back on his desk."

#Faber smile

drfaber "Everything looks good."

drfaber "I'll go over the details to review for our next appointment, which will be next week at this time."

drfaber "I have your phone number on file, and my contact info was included in the last email I sent you."

drfaber "You'll receive text reminders for next week’s appointment in case you forget."

drfaber "Also..."

n "He reaches yet again back to his desk. Before I can groan at the thought of more paperwork, he passes me over a black hardcover journal."

drfaber "I’d like you to keep a journal to record your thoughts every evening."

drfaber "It doesn’t have to be anything too extensive, just simple remarks about what you've done and how you feel each day."

n "The book looks expensive, though I’m hardly an expert."

n "I flip through all the blank pages, taking in the smell of crisp new paper."

n "It makes me feel like I’d be ruining these pages with the scrawlings of my mundane life rather than contributing to them."

erik "What are you going to use this for?"

#faber eyebrows raised

drfaber "Nothing."

#faber smile

drfaber "The journal is for you."

drfaber "If it helps, we'll continue to have you use it."

drfaber "If it doesn’t then you don’t have to write in it, but it's best to start writing out your thoughts now." 

#faber neutral

drfaber "Getting into the habit of writing daily might be more beneficial than you think."

n "I give a reaffirming nod."

drfaber "And Erik?"

erik "Yes, sir?"

n "Faber maintains his smile, but his gaze becomes more intense as he continues."

drfaber "If you need anything from me between appointments, please call."

drfaber "I will always strive to answer the phone, but if I do not then please leave a voicemail and I'll get back to you as soon as possible." 

drfaber "Day or night, it’s my job to be here and help you."

erik "Got it. Thanks." 

n "Faber’s expression warms and he slaps his legs decisively, standing."

drfaber "Great! Well, I look forward to seeing you next week."

n "I blankly stare at him in surprise."

erik "...Huh?"

n "Without realizing it the session is already over, and what should have felt like an hour passed by in only moments."

n "This isn’t how I imagined therapy would be." 
 
erik "That’s it?"

#faber smile

n "Dr. Faber nods, his amused smile telling me this isn’t the first time he’s heard this question."

drfaber "Is there anything on your mind, Erik?"

erik "Well, yeah but... this was a lot more straightforward than I thought it would be."

n "Faber holds his smile."

drfaber "I’m here as a resource for you Erik, the meetings will go however you want them to."

erik "That’s... cool."

n "I don’t really know what else to say, but already I’m physically feeling a lot better."

#faber neutral
drfaber "For now, remember to work on the journal I gave you, and for this week, try to find a few new opportunities to make some good friends here."

drfaber "It’s important to find some safe spaces to settle into with any new school."

drfaber "It will also be a good goal to focus on for our next meeting, don’t you think?"
 
n "I give off a final but very comfortable nod."

n "Taking this as a cue to leave, I stand up from my chair."

n "I can feel the cold air hitting the sweat that had collected on my back, but at this point the sensation is quite refreshing."

erik "Thank you for your time."

#faber smile

drfaber "Any time, Erik."

#faber fade out from center
#door close SFX

scene faberhallway
with ScDis

n "I leave the office and shut the door with an unexpected smile on my face."

n "It’s a simple endeavour to retrace my way out of the building, however this time I pay deliberate attention to avoid walking within the old wear marks on the hallway carpeting."

## BG school road ( daytime )
scene schoolground1
with ScDis
 
n "Now in a much better mood, I decide to take a longer route back to the dorm."

n "Or I would have, but of course I’m predictably stopped short by my leg."

erik "Are you kidding me?"

n "It's only been a few minutes but it’s already beginning to bother me as I work my way down the outdoor path."

n "It looks like I still have some ways to go, as looking around I don't recognize the generic school building and bordering woodland."

n "I could try to push myself to do continue around the building to see if I recognize any obvious landmarks, however —"

n "I stumble, almost face planting the concrete, but thankfully catch myself just in time."

n "Tripping at this point wouldn’t be ideal."

n "I take a momentary glance around and spot a fallen log a short way into the woods beside the main road."

n "It’d be a decent place to sit that isn't in the dirt or sun."

n "But in the woods..."

n "I can already see a fence ominously blocking further entry. However the log is on my side of the fence, so I guess walking that far shouldn’t be a problem."

n "Right?"

n "Cautiously, ignoring a caution along the way sign, I push through some of the side foliage."

## SFX leaves being rustled
## CG treetop canopy
scene forest1
with ScDis

n "...and come out into an almost brand new world under a canopy of trees."

## The sound of a forest, faint 

n "I'm only just a few feet away from the path and already the entire mood has changed."

n "A wash of swaying green leaves and the melody of distant birdsong comes alive before me."

erik "Wow..."
 
n "I make my way towards the log which is only few meters away, continuing to listen in to the sounds of the forest-"
 
##  SFX branch breaking
 
n "I step onto a branch hidden in the soil, which gives way with a resounding {b}crack.{\b}"
 
n "The peaceful ambience of the forest is broken immediately."

## SFX wing fluttering
## CG shift, fluttering wings against a treetop canopy touching the sky
## Music Isolda Theme "Soft"
 
n "The air is soon filled by the sound of fluttering wings."

n "Flocks of birds alarmed by my intrusion launch themselves up and disappear into the sky."

n "I watch as they fly off, but..."
 
##quietly
isoldaunknown "You scared them away..."
 
n "A soft voice calls my attention from the other side of the fallen tree."

## Isolda CG #1 (Neutral)
## Isolda is sitting on a blanket surrounded by a mess of pencils, sketches, her open bag, and black journal. Her gaze is placed slightly away from the audience. 

n "Hobbling to the other end of the fallen log, I find a girl staring longingly into the sky after the now long-gone birds."

n "It turns out what I'd first assumed was moss is actually the head of a St. Dymphna student." 

n "Her hair is pulled out of her face and tied back almost as if it was a second thought."

n "However her uniform is rather ironically neatly pressed and a kind of spotless you would not expect to find under a mess of hair."

n "Or in a forest for that matter."
 
n "It’s hard to pay attention to anything else other than this  girl in front of me."

n "I try and open my mouth to say something, anything, but I’m—"

##show CG Isolda (Upset)

isoldaunknown "Why did you do that?"

n "—cut off as she beats me in starting the conversation." 
 
erik "Oh, I’m sorry! I didn’t think anyone else would be here!"
 
n "She eyes me warily."

n "For a moment..."

n "And then a while..."

n "The silence begins to stretch so far between us that soon my pre-Faber internal anxiety is starting to return."

n "Should I just leave, or...?"

n "It doesn’t even seem like she wants to look at me, although that’s not too surprising considering that I am a random stranger in her eyes."

n "\"Try to find a new opportunities to make some good friends…\""

n "Faber’s voice rings out in my mind."

n "So... I clear my throat."
 
erik "I'm Erik Wilhelm."

n "I extend my hand towards hers."

erik "I'm actually a new transfer student."

n "She glances briefly at my uniform, then looks away just as quickly."

n "She nods, perhaps in acknowledgement of my words, although the reaction appears more mechanical than any kind of natural response."

n "Was this how I came across to Dr. Faber earlier?"

n "The quiet stillness quickly returns between the two of us, leaving only the accompaniment of light rustling of leaves."

n "You screwed up, Erik."

n "I slowly retract my hand."

n "My emotional high from Dr. Faber’s meeting slowly begins to spill away into empty hollowness."

erik "I’m sorry for bothering you."

n "I’m ready to turn around and leave. However, as if compelled by my sudden departure, the girl mumbles out a barely-audible whisper."

#smalltext TODO
isoldaunknown "I'm supposed to introduce myself..."

##show CG Isolda (Neutral)
 
n "She squares her shoulders, though still neglects to make eye contact with me, and calls out her own introduction with a voice much louder than before."
 
isolda "I'm Isolda, Isolda Gaillard. I've been here for 2 years and 1 month."
 
n "I nod back, but in the spirit of making friends I feel a little confused at this point."

n "I have no idea how to continue this conversation."
 
isolda "It’s nice to meet you."

n "That’s a start."

erik "Oh— right, it’s nice to meet you too!"

n "I try to play my absent mindedness as a joke, chuckling."

isolda "Why are you laughing?"

n "The hollow laughter catches in my throat, and I answer with resignation."

erik "I don’t know."

n "She nods, as if indicating that to be a perfectly acceptable answer."

isolda "You’re really weird."

n "I work hard to stifle another laugh."

erik "Yeah, I mean, I feel pretty weird right now."

##SFX Heartbeat

n "My leg is now screaming at me, leaving me close to collapsing."

#isolda arms crossed

erik "To tell you the truth, I’m a little tired and was looking for a place to rest."

n "I motion to the fallen log she's occupying."

erik "Can I sit down?"

n "At this point I’m not even sure if I could make it back to the main road if she said no."

n "My butt meeting the ground seems to be an inevitability, whether elevated on a log or not."

isolda "Probably."

n "I’ll take it."

n "It’s not a definitive yes, but I can already feel my legs buckling underneath me."

#Isolda CG removed, forest BG appears. 

n "I wobble dangerously before perching on the end of the log, just a little away from where Isolda’s sitting."

n "Exhaustion overtakes me."

n "I don’t know whether it’s because I’m relying far too much on one leg for support, or if it’s that I had mentally exhausted myself throughout Faber’s meeting."

n "Still, in a few moments gratifying relief courses throughout my body, and I throw my head back with a satisfied sigh."

n "I’m not sure whether Isolda is still eyeing me warily or not, so without looking directly at her I try to make an attempt to engage in small talk." 

erik "So, you come here often?"

isolda "Yes."

#isolda arms crossed, eyes down

n "Her curt reply draws my attention, and by looking over I see that she is now standing."

n "Her eyes are fixed hard on the blanket that she’s standing on, and following her gaze I’m embarrassed that it has taken me this long to realise the pages of sketches littered all around her."

n "They’re comprised of differently shaped and shaded local birds, and they look quite good."

erik "Did you draw all these?"

n "She answers me without looking up."

isolda "Yes."

n "I’m still unsure whether I should back out of this conversation or not."

n "Once more, perhaps, to see if any kind of discussion is possible?"

erik "Would you mind if I looked at them up close?"

#isolda arms crossed, angry

n "She tenses up immediately." 

isolda "Yes."

n "Fair enough."

#move isolda down, show standing straight, eyes down 

n "However, as I resign myself to ending our talk, she bends down and reaches for a black journal placed next to her." 

n "She picks it up with the utmost grace and care; her fingertips grazing the outer edges as if the entire journal were priceless to her."

#isolda up

n "Despite her previous response she holds the book out towards me..."

n "...and waits for me to take it."

erik "I don’t understand."

#isolda standing default

isolda "I’m handing it to you."

n "She sounds annoyed now, so rather than argue the point I accept the book —"

#isolda standing wide-eyed

isolda "Ah —!"

n "I scoot over and reach my hands out to take it, but before I can she violently jerks the journal back."

n "It takes her a moment, but she quickly collects herself and extends the book towards me again."

n "Only this time, she’s holding it with just with her fingertips."

#isolda standing neutral

n "It’s almost as if she’s afraid to have any contact with me."

n "I decide not to push the issue and accept the book once more."
 
## Drawing of a sketched bird CG
## TODO CG09
show CG09:
  alpha 0.0
  easein 1.0 alpha 1.0
  yalign 0.0
  ease  20.0 yalign 1.0

## Music amplifies, an extension of Isolda’s theme building into something more concrete than the ambient sounds before. What once was a light ambient piano as remnants of an Isolda Theme is now overtaken by more concrete instruments. I have envisioned Isolda’s theme comprising a collection of strings in this moment. 

n "The book is just like the journal Dr. Faber had given to me earlier, but after opening and flipping through the pages I see that it’s filled with pictures instead of words."

n "Every page is covered in drawings varying from simple pencil outlines to intricately shaded creatures; from sketches the size of her thumb to full pages depicting a single forested backdrop."

n "It's as if the there were another world trapped within the pages."

n "Up close they’re... {i}really{\i} good." 
 
n "I finish on a picture of an owl sheltering in the fork of a tree, its head tilted to one side as if eyeing me suspiciously. I’m quickly reminded of the girl in front of me."

n "Satisfied, I hand the book back to her."

hide CG09
with ScDis

#end CG

#isolda standing puzzled

n "Isolda accepts it with her fingertips, still looking as if she’s making some effort not to touch my hands."

n "I try not to pay much mind to it, but rather focus on what I had just seen from her journal."
 
erik "These drawings are amazing."

#isolda standing neutral
 
n "She simply nods, looking as if what I said was a dry fact rather than praise for her work."

isolda "I've got a lot more back at my room. Jeanne likes them as well."

n "Jeanne? I wonder if that’s the same girl from my gym class..."
 
n "Isolda pauses, looks up at me from where she's collected her drawing implements, and starts putting both of them back into her bag."
 
isolda "They're really nothing special though.  I just draw what's in front of me."

erik "You’re a very talented artist."

#isolda standing puzzled
 
n "She looks momentarily puzzled as she glances down at the sketch pads in front of her, and then up at a few of the trees in front of her."
 
isolda "There are plenty of people who —"
 
##  SFX alarm on phone.
 
n "I hear an alarm go off from in her bag."

#isolda standing eyes down

n "It takes her a moment fumbling through pockets, but soon enough she pulls out a phone and taps it to stop the alarm."
 
isolda  "Five o'clock..."
 
n "She seems to have forgotten I'm there as she fumbles around and gathers up her materials."
 
n "She hastily returns the sketch books to her bag, along with the blanket and other materials, before standing back up."

#isolda standing arms crossed

isolda "I have to get back to the dorm,  Jeanne will be waiting for me to come to dinner."

n "With only that as a goodbye, she starts picking her way through the woods and back towards the school."

n "By the time I'm back on my feet, she's already put some distance between us."

n "She isn’t walking to the main road though, instead cutting directly through the trees on a horizontal path to what I assume to be the direction of the dorms."

n "I’m sure there are a number of different rules against that, but at this point I’m inclined to take the shortcut with her."

n "Would it be weird to follow her?"

n "We’re both heading back to campus, so there’s nothing strange about it, right?"
 
## SFX, leaf litter crunching underfoot
 
n "We walk in silence, aside from the crunching of fallen branches and leaf litter."
 
n "Isolda doesn’t look back, her destination set."
 
n "Ultimately the distance is a short one and it takes only moments to reach the end of the treeline."

n "I can already see Isolda walking through a muddy clearing by the dormitories."

n "Just as I start to work my way around —"

scene PitchBlack
with Dissolve (0.1)

erik "Shit!"

n "— I feel my leg fold underneath me."

scene forest1
with ScDis

n "I fall against the mud, expertly missing dry grass by mere centimetres."

n "I’m now very sore, though the feeling in my leg means I can still move at least."

n "It takes a bit of coercion rubbing my side, but..."

n "I’m tentatively able to lever myself back to a sitting position, trying to keep the mud dripping on only one side of my body."

#show Isolda standing puzzled
 
n "As I look up, I’m surprised to see a nervous Isolda staring at my leg." 

n "I hadn’t even noticed her approach, but there she is, standing in the middle of the mudpit I just fell into." 

erik "Hey..."

n "I wipe the mud off of my hands and test out my leg a little."

n "I can probably get up without help and hopefully not embarrass myself further."

n "That said, with Isolda here, I wouldn't mind a hand..."
 
## and here is the big choice ##

menu:
    "Reach a hand out and ask for help":
        jump A1_20a
    "I'm fine!":
        $ ig_tot += 1
        $ A1_20_bad = True
        jump A1_20b


label A1_20a:
##LABEL

## Reach a hand up and beg for help ##
## Nul points for those keeping score ##
## Set flag A1_20_bad (temporary name) ##

n "I smile, and I reach a hand up to Isolda."
 
erik "Could you help me out here?"

erik "This doesn’t tend to happen."

#isolda standing straight angry

n "She eyes my hand with hostility before coldly replying."

isolda "No."

n "..."

#isolda standing straight eyes down

n "Rather than the usual reaction I expected she simply stands there and watches me, her arms staying firm by her sides."

n "Her eyes still aren’t trained on me, but rather some nearby foliage."

erik "...Please?"

isolda "I said no."

n "I’m still on the ground and Isolda is still standing there."

n "At this point I could just push myself off the ground, but I can't help feeling frustrated with her."

erik "Well, why not?"

n "I’m growing a little more agitated and the annoyance in my voice is beginning to slip out."

n "It might be a little unfair, but is it that hard to help someone out when they’ve fallen down?"

#isolda standing angry

isolda "Because I don’t want to."

n "Her voice is firm and steady, conveying similar annoyance."

erik "Right. That makes sense..."

n "It actually takes me a lot longer than anticipated to push myself off the ground, but eventually I manage to work my way back onto my feet."

n "I almost lose my balance again, but I’m still standing vertically in the end."

n "I can’t help but grimace at the mud that’s now collected on my clothes. While it isn’t Isolda’s fault I still direct some of my frustration to her."

erik "Thanks for the help." 

n "I mumble sarcastically, probably a lot more harshly than necessary."

#isolda standing neutral

isolda "You’re welcome."

n "I try and prepare myself to combat her own sarcastic remark, however her soft and confused tone takes me by surprise."

n "I don’t think she’s jabbing back at me. It’s sincere."

n "In fact, as I look up her entire body seems to be tensing inward with her eyes flicking consistently to my leg."

n "It looks like she’s worried but..."

n "I remember back to when she flinched away from me when I was accepting her sketchbook."

n "If she was that uncomfortable with another person touching her then that would mean —"

n "I suddenly realize that I’m the one at fault in this situation."

n "I’ve been oblivious this entire time to just how much I’ve been intruding on her space."

erik "I..."

#isolda standing, eyes down

isolda "I need to go." 

n "She turns in the direction of the dorm buildings."

n "I try again to think of the words for an apology, but I can’t really seem to find them."

n "I wasn’t trying to be rude in my misunderstanding, in fact I was hoping to gain some kind of friendliness out of this exchange."

n "Instead it looks like I’ve pissed someone off this soon in the semester."

erik "Right... I better head back to my dorm and change."

n "Isolda nods, still facing away from me."

#isolda standing neutral

isolda "That'd be a good idea. Before you get too cold, or get mud within any important places."

n "..."

n "That was an odd way of saying that."
 
n "Without waiting another moment Isolda walks off towards the main part of campus, though after only a few paces stops in place."
 
n "She turns back towards me."

#isolda standing arms crossed.

isolda "Are you sure you're all right?"

n "Her words reach me but her eyes don’t, and even her arms are now in a hard folded position."

n "Is she actually concerned or just asking out of an annoyed obligation at this point?"

n "I could understand if it were the latter. I haven't earned any sympathy from her."
 
erik "I'll be fine."

#isolda standing neutral

isolda "Well then, goodbye."

#exit isolda center to left

n "Before I can say anything else she turns back around and eventually disappears amongst the many St. Dymphna buildings in front of us."

n "With that, I make my way back to my own dorm."

n "Slowly."

## //scene
##JUMP
jump A1_20_end

##LABEL
label A1_20b:
## +1 Isolda

n "I stretch my bad leg out, rubbing the muscles in my thigh, and roll over so I can get my good leg under myself."

n "I take a moment,{w} gathering myself,{w} and then push myself up to my feet."

n "I stumble as I put weight on my bad leg, but I manage to right myself."

erik "Good as new."
 
n "I look down at myself, seeing all the dirt collected on my new uniform, and can’t help but smile a little at the situation."
 
erik "Well, a little worse for wear."

isolda "Are you all right?"

n "I look back and see Isolda holding an expression of concern towards me."

erik "I survived." 

#isolda standing smile

isolda "That’s good."

n "She once again nods, but I am a little surprised to see that she’s smiling now." 

n "It’s a smile so genuine that it hurts."

n "I need to... think of something to say."

erik "I..."

#isolda standing neutral

isolda "I need to go now. I don’t want to keep Jeanne waiting."

n "Just like that she turns away from me and faces in the direction of the school dorm buildings."

#isolda move center to left of center

n "She starts to walk away but I want to stop her."

erik "Isolda!"

#isolda move back to center
#isolda standing puzzled

n "She stops and turns back to me, albeit a little confused."

n "She doesn’t say anything, and she doesn’t even really look at me, but I know she’s waiting for me to say something." 

erik "Can I see you again? It might seem weird to say, but I’m trying to meet some new people."

#isolda touching nose eyes down

n "A minor look of confusion crosses her face, though I hardly feel as if I’ve said anything perplexing." 

#isolda standing neutral eyes down

isolda "..."

#isolda standing neutral

isolda "Probably."

#isolda standing eyes down

n "She begins to turn away again, but..."

n "I suddenly realize something important." 

erik "No, I mean..."

n "She stops, and I force the words caught in my throat to come out."

erik "I’d like to be your friend. Is that all right?"

n "She is a little taken aback by my comment, and takes a long pause."

n "I wait."

#wait 5 seconds
#isolda standing smile

isolda "I wouldn’t mind."

#isolda standing neutral 

isolda "But I really need to go."

erik "Of course!" 

erik "I should head back to my dorm room and change as well."

n "Isolda nods, her body slowly tilting to face away from me."

n "I figure at this point it’s hardly a malicious gesture."

n "It’s simply a part of who she is. Kind of different than the first time I met her."

#isolda standing hands on hips, smiling

isolda "That'd be a good idea, before you get too cold, or get mud inside anything important."

n "It’s an interesting comment, but nonetheless I can’t help but crack a big grin."

erik "Right, no one would want that."

#isolda standing smile

isolda "Not even the mud I imagine."

#isolda standing neutral

isolda "Well then, goodbye Erik."

#isolda move from center to center left
#stop

#isolda smile

isolda "For now."

#isolda exit from center left

n "She turns and finally, after a moment of pause, she walks away for good."

n "She doesn’t look back."

n "Just like that I’m left covered in mud alone, but with a big smile on my face."

n "It felt good to hear her say my name."

n "With a newfound energy, one even greater than my experience with Dr. Faber, I turn towards the other direction and make the trip back to my own dorm."

n "I hardly even notice my leg."

##JUMP
jump A1_20_end



label A1_20_end:
scene PitchBlack
with Clockwipe

jump A1_21
