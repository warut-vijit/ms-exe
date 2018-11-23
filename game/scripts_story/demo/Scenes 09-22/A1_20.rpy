label A1_20:

## I am a dummy file here to provide a choice flag for reference in A1_25 and to allow testing.  ##
scene black
n "So, it's all a bit lonely in here, and it's all dark."

n "The only way either of us is getting out of here is to make a choice."

n "A choice so momentous that it will change your life forever."

n "Can you live with that responsibility?"

## and here is the big choice ##

menu:
    "Reach a hand out and beg for help":
        jump A1_20a
    "I'm a free independent mental patient, and I don't need no woman!":
        $ persistent.ig_tot += 1
        $ A1_20_bad = True
        jump A1_20b


label A1_20a:


## Reach a hand up and beg for help ##
## Nul points for those keeping score ##
## Set flag A1_20_bad (temporary name) ##
n "You've gone and done it now."
n "You've dishonoured your ancestors by begging for help - and you don't even know why."
n "Just... commit suddoku or something."
jump A1_20_end

label A1_20b:
## I'm a free independent mental patient, and I don't need no woman! ##
## +1 Isolda

n "Well, at least you're determined to help yourself escape whatever fine mess you've managed to get yourself into."
n "Better luck next time..."

jump A1_20_end



label A1_20_end:

jump A1_21
