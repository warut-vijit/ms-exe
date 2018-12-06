label A1_20:

## I am a dummy file here to provide a choice flag for reference in A1_25 and to allow testing.  ##
scene black

stop music fadeout 1.0
stop music2 fadeout 1.0
stop ambience fadeout 1.0
stop ambience2 fadeout 1.0

n "PLACEHOLDER SCENE"

n "This scene is not yet complete, but has a choice that future scenes rely on."

n "As such, a dummy scene has been placed in it's stead until the scene is complete."

show irene U_P1_E2:
  xalign 0.3 yanchor 1.0 ypos 1080+425 alpha 0.0
  easein 1.0 xalign 0.5 alpha 1.0
show irene U_P1_E2 alpha 1.0

irene "Hey guys! What's going on in this sce..."

show irene U_P1_E4
with SDis

irene "Oh..."

$ renpy.pause(5.0)

show irene U_P1_E2
with SDis

irene "I'll come back at a better time!"

show irene U_P1_E2:
  xalign 0.5 yanchor 1.0 ypos 1080+425 alpha 1.0
  easein 1.0 xalign 0.7 alpha 0.0
show irene U_P1_E2 alpha 1.0

## and here is the big choice ##

menu:
    "Reach a hand out and ask for help":
        jump A1_20a
    "I'm fine!":
        $ ig_tot += 1
        $ A1_20_bad = True
        jump A1_20b


label A1_20a:


## Reach a hand up and beg for help ##
## Nul points for those keeping score ##
## Set flag A1_20_bad (temporary name) ##
n "Your response has been noted for use in future scenes."
jump A1_20_end

label A1_20b:
## I'm a free independent mental patient, and I don't need no woman! ##
## +1 Isolda

n "Your response has been noted for use in future scenes."

jump A1_20_end



label A1_20_end:

jump A1_21
