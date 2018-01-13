
label A1_13:
###############

$ persistent.scene_number = "A1_13" # current scene
$ persistent.scene_name = "Morgellon's Disease" # current scene name
$ renpy.save_persistent()


# 
# Kosherbacon + that swampie guy
# Scene name: Morgellon's Disease
# 
# Bgs:
# school hallway, dorm
# 
# Sprites:
# 
# Special Effects:
# fade to white
# 
# Music:
# Be Green (Afternoon)
# 
#-# <Scene opens>
#
#--#

#-# <school hallway (afternoon)>
scene classroomhall
with Dissolve(2)
#--#

n "I'm a little relieved to have all that school photo business taken care of. My first day of class wasn't unpleasant but I feel like it's taken forever and I'm happy to get it over with."

n "Seeing that this was the first day of class, I've got to ask myself, can I survive like this?"

n "I..."

n "Well..."

#-# >A Windmill in the Mirror in
stop music fadeout 5.0
play music "music/A Windmill in the Mirror.mp3" loop
#--#

n "I have no idea, but it's not like I have any choice."

n "Oh well. Home was a spotty mess of trial and error with good ideas built up and bad ones filtered out to get me on my feet."

n "Now that I know how to stand I can learn how to walk here, build a routine and pan out a rhythm I can follow 'til the end of my days."

n "Wake up. Go to school. Go to club meetings. Eat. Do homework. Go to sleep."

n "I imagine there's going to be some therapy shoehorned in at inopportune moments, but inconvenience is the spice of life."

n "Am I really prepared to be another cog in the machine though? Just a boring, grey person working a desk job I hate?"

n "Yeah, right."

n "These are my formative years, I'll be damned if I let myself get imprinted with a whole lot of boring."

n "Fran probably knows how to have a good time. I'm not so sure of Lena, though. If I get desperate I could try hanging out with my sisters, but I doubt that'd do wonders for my sex life."

n "See, this is what happens when I'm left alone allowed to think to myself. I haven't really had any alone-time, what with the doctors, family and classes. Five minutes of me alone with myself and I start resenting everything."

#-# <Erik's room (afternoon)>
scene erikdorm
with Dissolve(2)
#--#

n "When I get back to my room, I decide to start my homework \"whenever,\" which is sometime between 17:30 and the second coming of Jesus."

n "It's unhealthy to let myself get run ragged without having some downtime when I need it. A great philosopher once said \"There's never enough time to do all the nothing you want.\""

n "I throw myself into my chair, fire up my laptop, and stare blankly at the start-up screen, as though I need booting up as much as the machine does."

n "Who am I again? I knew who I was last year, where I belonged. I'm light years away from home in a strange land filled with strange people. I just want to go back to holing up in my room goofing off on the computer once in awhile."

n "Lena was right about amnesia being versatile. It surely would have made adjusting to a new life a lot easier."

n "I absent-mindedly click around the screen before opening up a web-browser. The bookmarks menu is full of landmarks from a past life and I'm pretty sure most of them are dead links now. I don't think I've used this machine much at all in nearly a year."

n "Spending quality time with myself has me testing the school server's bandwidth limits and content filters. A little escapism never hurt anyone."

n "..."

#-# <fade to dorm (afternoon)>
scene erikdorm
with Dissolve(2)
#--#

#-# >Erik's Homework in
stop music fadeout 5.0
play music "music/Erik's Homework.mp3" loop
#--#

n "Introspectives can get messy. What's happening in the outside world?"

n "A cursory search of \"Privatgymnasium St. Dymphna\" drew out a sanitized webpage alongside perfectly forgettable social media profiles of alumni organizations, and online catalogues."

n "I've seen this website before, but I never really took in any of the information here."

n "It's nice and polite, like having the world's best bowl of oatmeal for breakfast. Nothing worth getting excited over."

n "There's a small \"news\" section that seems to be updated every month with success stories, inspirational quotes and school news."

n "Just under a small goodbye written for a retiring teacher is an announcement that catches my attention."

n "{i}\"Get ready for this year's Dymphnatag!\"{/i}"

n "I click on the included link and find myself on another part of the school website, this page detailing some sort of festival the school holds each year."

n "It's surprising, honestly. I kind of expected the outside world to want nothing to do with... us. But it looks like investors, therapists from other facilities and family members are encouraged to come to this event"

n "I didn't expect that a student body from a school for the impaired would be able to organise a whole Gala."

n "Perhaps my sisters would be able to come? I'm sure the two of them would love to see more of the school."

n "Enough goofing off. Maybe there's something school-related I can do online, like sign up for class mailing lists or register for grade-tracking accounts."

n "I should be able to do stuff like that without any assistance, since I signed up for a school e-mail account when I enrolled."

n "Oh yeah, e-mail. I should probably check mine."

#-# <end>
stop music2 fadeout (5.0)
#--#

########

jump A1_14 # jump A?_??
