
label A1_08:
###############

$ persistent.scene_number = "A1_08" # current scene
$ persistent.scene_name = "In Isolation" # current scene name
$ renpy.save_persistent()


# A1_08 - In Isolation
# Scene name: In Isolation
# Kuroe
#-# <Assets: Erik's bedroom, Common Room, School Grounds>
#
#--#

#-# <scene open>
#
#--#
#-# >NEW BEGINNINGS ARISE FROM OLD ENDINGS IN
play music "<from 0.0 to 181.0826 loop 10.1653>music/New Beginnings Arise from Old Endings.mp3" loop
#--#
n "For a few moments, I simply stand there in the silence, watching my parents and siblings make their way to the car park where our family sedan is waiting."
n "I see Hilda throwing one more furtive look in my direction – probably trying to make sure I haven't been abducted by aliens when they weren't looking – and I wave to her in reassurance."
n "She smiles a little and nods, as if in a gesture of encouragement."
n "They finally board the car, and soon enough, it's purring to life, pulling out of the lot and, at last, through the great metal gates of Privatgymnasium St. Dymphna."
n "As I watch it disappear into the streets, a sinking feeling churns in my chest, like a pack of rats."
n "There's this cruel, childish part of me tauntingly coaxing me to charge after them, in a last-ditch effort to turn back, to escape, to perhaps deny everything that's happened so far."
n "A wiser part of me, however, begrudgingly acknowledges the simple fact that there's nothing to return to beyond the gates anymore."
n "I've been pushed off the cliff. I fly or fall now."
erik "\"Ah, this sucks...\""
#-# >bg overcast school grounds
scene mainbuildingfarcloudy
with Dissolve(2)
#--#
n "I throw my head back and look at the sky, staring as thick swaths of cloud lazily, clumsily crawl together in a pool overhead, blotting out the sky with a formless veil of grey."
n "Coupled with the sharp silhouettes of the buildings around me looming over me like hungry eldritch monsters, it makes for a sinister, almost horror movie-like effect."
n "It's not really the kind of atmosphere I need to brighten my mood right now."
n "I put my hands in my pockets and decide to retire to the dormitory building in the meantime."
#-# >bg walkway to dorm
scene outsidemaledormcloudy
with Dissolve(2)
#--#
n "I know I told my parents I was going to take a short stroll to better familiarize myself with the campus's structure, but honestly, I can attend to that at a later date."
n "This school is so big, I've nearly forgotten most of the directions Ela gave us during the tour. The last thing I want is to look like an idiot getting lost so early into my stay."
n "After all, I'm lost enough as is within this gnarly jungle of apprehensions and worries inside my head."
n "I just want some rest. Some time by myself to lie down and let all these things sink in properly. Some time to process what's happened and is happening, and how (and where) to go from there."

#-# >Fade to outside male dorms
#todo no walkway yet scene outsidemaledormcloudy
#with Dissolve(2)
#--#
n "I'm glad to remember just enough to reach the boy's dorm without much trouble. Finally reaching it, I tarry a bit on the steps to take in the sight of the titanic building before me."
n "This thing's been here for at least a century by the looks of it, standing proud and stately, wearing an air of stern, aloof majesty certainly accumulated over its evidently long, storied existence."
n "It doesn't look like something people actually live in – really, it'd probably be at home in a fantasy movie or a history documentary. Even the very doors look imposing and intimidating."
n "All that said, however, I guess I'd better get used to it sometime soon. For this year, at the very least, it's going to be my home."
n "My hand alights on the door handle. With a big gulp to calm the last pangs of hesitancy in my mind, I give it a decisive twist and step inside."
#-# >Dorm Interior
scene dormhall
with Dissolve(2)
stop ambience fadeout 2.0
#--#
n "... I somehow expected the place to be a lot noisier."
n "Before I entered, I briefly entertained a mental image of a shrieking group of kids wreaking ungodly havoc on each other and on the room while a flock of orderlies try to defuse the situation, in vain."
n "In reality, all that welcomes me inside is deafening, awkward silence."
n "A small flock of boys are sitting on the floor and the couch, some of them merely giving me a curious glance that lasted for all of a second before they returned to whatever they were doing prior."
n "Some are playing cards, some board games, while a few others are simply immersed in their phones and music players or staring at the TV with rapt attention."
n "How... normal. Relatively speaking, of course."
n "I wonder if I should say hi to them. I'm sort of hoping to acquaint myself with my new community, but can I manage it without committing some horrendous gaffe?"
n "Can I manage it without one of them suddenly slashing my jugular with a box cutter?"
n "... God damn it, Erik. Get a hold of yourself."
n "In the end, all I do is give them a stiff nod in salutation and quickly flee to where my dormitory room is before I find an opportunity to pull myself into further embarrassment."
n "I scan the room doors I pass along the corridor."
#-# >bg corridor
scene dormhall
with Dissolve(2)
#--#
n "If nothing else, the place is really well-kept, its walls supernaturally pristine, each polished, varnished door looking like juxtaposed copy-pastes of each other."
n "The corridor is also pretty much devoid of any signs of life, barring the occasional teacher or patrolling guard or loitering student, none of whom give me so much as a second glance."
n "The only person here who seems to have paid any attention to my arrival is this guy in room 90 who followed me with his eye from his slightly open door, but the less said about that, the better."
#-# >Music fades out
stop music fadeout 3.0
#--#
n "Room 97... 98... 99... 100... ah, there we go. Room 101."
#-# >bg Erik dorm room, kinda dark
scene erikdormcloudy
with Dissolve(2)
#--#
#-# >muted past in
stop music fadeout 5.0
play music "music/Muted Past.mp3" loop
#--#
n "Stepping inside, the door swings shut behind me."
n "I feel like I should have some sort of responsibility at this point, but looking around the room I can't think of anything I need to do."
n "Everything has already been put away – even the clothes from my suitcase."
n "I slump down onto my neatly-made bed and sweep the room with a glance."
n "My room. For all intents and purposes, my home, at least for the time being. It feels weird, almost like meeting a new person, in a sense."
n "My gaze lands on some papers on the bedside table. For lack of anything better to do I pick some up and riffle through them."
n "They aren't anything very interesting."
n "A leaflet that I've already seen. It was mailed to us along with everything else a while ago."
n "Under that, a quaint newsletter that looks as though it's put together by the students."
n "Nothing too surprising here either, though there are a few pages dedicated to advertising the school's apparently numerous clubs that catch my attention."
n "Cooking, knitting, music, track, gaming. Potholing. Bomb construction."
n "Okay, there actually weren't anything like those last two. Still, it sounds like there's plenty of interesting stuff to do. Maybe I'll check some of them out at some point."
n "Might as well make the most out of my time here, though I doubt I'll be running on the track team any time soon."
n "A schedule of upcoming events is next, followed by a map of the grounds."
n "Finally, to my surprise, a personal timetable with all my classes. I'd expected that I would've had to pick that up in homeroom tomorrow or something. They must really look after you here."
#-# >MUTED PAST FADE OUT
stop music fadeout 5.0
#--#
n "All it does is remind me of what kind of place I've just landed myself in."
#-# >UNKNOWN PAST FADE IN
play music "music/Unknown Past.mp3" loop
#--#
n "During the tour of the school, Ela certainly made sure to give us the best first impression of the school."
n "She highlighted the beautiful architecture, the scenery, the wonderful experiences I'll be having here and what a godsend this place is for people of our kind."
n "She really sounded like an incredibly skilled saleswoman."
n "She must've had lots of experience with this kind of thing, then, reassuring parents their little darling babies will be fine and everything's wonderful and good within St. Dymphna's."
n "Of course, even if she boasted of five-star hotel amenities in the school, that does exactly squat to hide the truth of what this school is, in the end."
n "It's a glorified scrap heap for damaged, defective people."
n "I know she did her best to reassure me that that's not the case, but it's no mean feat to shake off these lingering apprehensions and doubts from my mind."
n "Still, in spite of all that, I do want to believe in what she said. I want to – I need to – at least give this new chance a shot."
n "In the months following that incident in the mountains, I felt like my life began to slow down to a crawl until it finally stopped moving."
n "Days and nights came and went, months passed, and seasons turned, but I lagged behind, trapped helplessly in this strange, dreary limbo, unmoving, unchanging."
n "The accident may not have been fatal, and it may not have even injured me grievously, but it still snatched so much away from me, stripped away a part of who I used to be."
n "And I know that if I don't keep pushing forward, if I throw this one last chance away, I might never be able to regain the things I've lost."
#-# >RAIN NOISE IN
play ambience "music/effects/softrain.ogg" fadein 2.0 loop
#--#
n "Thunder rumbles in the distance, and the first drops of rain descend, pitter-pattering on the window and tracing narrow streaks of water as they cascade down the glass pane."
#-# >Fade to black
scene PitchBlack
with Dissolve(3)
#--#
n "The quiet white noise of the subsequent rainshower feels a bit melancholy, but soothing, like a lullaby without words. I sink into the softness of the bed and close my eyes."
n "Tomorrow, my new life will begin in earnest."
n "My mind wanders down a million different routes of thought thinking of what could happen and how things would turn out, but really, the most I can do at this point is guess."
n "The decisions I'll make... the paths I'll take... only they can give the answers to that."
#-# <end scene>
stop ambience fadeout 0.5
stop music fadeout 5.0
#--#

########

jump A1_09 # jump A?_??
