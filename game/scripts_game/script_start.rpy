

# The game starts here.

    # Adding about button to main menu
    #$ config.main_menu.insert(3, ('About', _intra_jumps("about", "main_game_transition"), "True"))


init python:
    import time
    # Function to set main menu "stars" correctly
    # Call with girl's define and a parameter, meaning:
    # (0) means hidden path, (1) means not hidden
    # 'meet' = have met the girl (2)
    # 'path' = have opened her path to Act 2 (3)
    # 'good' = have gotten her good ending (4)
    # '100%' = have gotten all of her endings (5)
    # Do NOT have 'meet' part of Anne-Marie's hidden path
    def menu_chibi(girl,mode):
      # global a_menu,i_menu,j_menu,l_menu,k_menu,nl_menu,nh_menu,am_menu
      if (mode == 'meet'):
        if (girl == 1):
          girl = 2
      elif (mode == 'path'):
        if (girl == 2):
          girl = 3
      elif (mode == 'good' or mode == '100%'):
        if (girl == 3 or girl == 4):
          if (persistent.am_menu == 0):
            persistent.am_menu = 1
          # Since the last 'good' hasn't copied yet,
          # check for all 4s or 5s except one 3
          # This will change Anne-Marie to 'meet'
          if (persistent.am_menu == 1 and girl == 3 and persistent.i_menu>2 and persistent.j_menu>2 and persistent.l_menu>2 and persistent.k_menu>2 and persistent.a_menu>2 and persistent.nl_menu>2 and persistent.nh_menu>2):
            tot = 0
            if (persistent.i_menu==3): tot += 1
            if (persistent.j_menu==3): tot += 1
            if (persistent.l_menu==3): tot += 1
            if (persistent.k_menu==3): tot += 1
            if (persistent.a_menu==3): tot += 1
            if (persistent.nl_menu==3): tot += 1
            if (persistent.nh_menu==3): tot += 1
            if (tot == 1):
              persistent.am_menu = 2
          if (mode == 'good' and girl < 5):
            girl = 4
          else:
            girl = 5
      else:
        renpy.error("MS: unknown chibi menu mode: %s" % mode)

      return girl



#  layout.imagemap_main_menu("images/Menus/menu1.jpg", "images/Menus/starnames.png", [
#    (550, 1, 680 ,130, "Start Game"),
#    (111, 313, 392, 378, "Load Game"),
#    (48, 432, 237, 529, "Preferences"),
#    (48,529,237,576, "Quit"),
#    (48, 435, 237, 482, "Help"),
#    ])


# About box
#label about:
#    python hide:
#        renpy.transition(config.intra_transition)
#        ui.window(style=style.gm_root)
#        ui.frame(ymargin=10, xmargin=10, style=style.menu_frame)
#        ui.side(['t', 'c', 'r', 'b'], spacing=2)
#
#        # Here you put the title of your VN
#        layout.label("My visual novel", None)
#
#        vp = ui.viewport(mousewheel=True)
#
#        # This is where the text will go. You can use all the usual tags.
#        ui.text("This is my first visual novel, be gentle, thank you.. :)")
#        ui.bar(adjustment=vp.yadjustment, style='vscrollbar')
#
#        layout.button(u"Return to menu", None, clicked=ui.jumps("main_menu_screen"))
#        ui.close()
#        ui.interact()
#    return

label splashscreen:
  image white = Solid("#fff")
  scene black
  $ renpy.pause(1)
  $ renpy.movie_cutscene("video/Somnova_Intro.webm")
  show movie
  play movie "video/Somnova_Intro.webm" fadeout 3.0
  scene white
  stop movie
  show text "{color=#000}{b}{i}This game deals with potentially sensitive themes, including fictional depictions of psychological issues and trauma.\n\nThis demo does not represent quality of the final product.\n\n\n\n{/i}{/b}{/color}" at center
  $ renpy.pause(5)
  scene black
  with Dissolve(1.0)
  $ renpy.pause(1)
  $ persistent.loaded = False

  return

label start:
  if (persistent.menu_ui < 0):
    $ persistent.menu_ui = -persistent.menu_ui
    return

  $ persistent.i_tot = 0
  $ persistent.j_tot = 0
  $ persistent.l_tot = 0
  $ persistent.k_tot = 0
  $ persistent.a_tot = 0
  $ persistent.nl_tot = 0
  $ persistent.nh_tot = 0
  $ persistent.am_tot = 0

label start0:

  $ renpy.music.play("video/SkyLoop2.webm", channel="movie", loop=True)
  show PitchBlack:
  with Dissolve (3.0)
  stop movie

  if (persistent.menu_ui < 0):
    $ persistent.menu_ui = -persistent.menu_ui
    return

  # Debug info
  $ persistent.scene_number = "startup" # current scene

  $ virgin_init_variables()  # Init "first time run" variables
  $ init_variables()         # Init "startup" variables

  transform spin:
    xanchor 0.5 yanchor 0.5
    xpos 0.95 ypos 0.9
    rotate 0
    linear 4.0 rotate 360
    repeat

  transform spin1:
    xanchor 0.5 yanchor 0.5
    rotate 0
    linear 8.0 rotate 360
    repeat

  image animatedstar = At("images/Buttons/button_star.png", spin1)
  image ctcstar = At("images/Buttons/button_star.png", spin)

##define pause menu
  $ _game_menu_screen = "game_menu"

##define characters

  #narrator
  define n = Character(' ', ctc="ctcstar", ctc_position="fixed")

  #main
  define erik = Character('Erik', color="#FFCC99", ctc="ctcstar", ctc_position="fixed")
  define him = Character('Him', color="#FFCC99", ctc="ctcstar", ctc_position="fixed")
  define me = Character('Me', color="#FFCC99", ctc="ctcstar", ctc_position="fixed")
  define isolda = Character('Isolda', color="#5ABF90", ctc="ctcstar", ctc_position="fixed")
  define jeanne = Character('Jeanne', color="#ED0202", ctc="ctcstar", ctc_position="fixed")
  define lena = Character('Lena', color="#808000", ctc="ctcstar", ctc_position="fixed")
  define mysteriouslady = Character('Mysterious Lady', color="#FE8A8A", ctc="ctcstar", ctc_position="fixed")
  define mysteriouslylady = Character('Mysterious Lady', color="#FE8A8A", ctc="ctcstar", ctc_position="fixed")
  define humminggirl = Character('Humming Girl', color="#FE8A8A", ctc="ctcstar", ctc_position="fixed")
  define katja = Character('Katja', color="#FE8A8A", ctc="ctcstar", ctc_position="fixed")
  define annaliese = Character('Annaliese', color="#22374c", ctc="ctcstar", ctc_position="fixed")
  define natalya = Character('Natalya', color="#FF8A00", ctc="ctcstar", ctc_position="fixed")
  define natasha = Character('Natasha', color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define sofiya = Character('Sofiya', color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define femalevoice = Character("Girl's Voice", color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define annemarie = Character('Anne-Marie', color="#964820", ctc="ctcstar", ctc_position="fixed")

  #Side
  define drfaber = Character('Dr. Faber', color="#BF8000", ctc="ctcstar", ctc_position="fixed")
  define faber = Character('Dr. Faber', color="#BF8000", ctc="ctcstar", ctc_position="fixed")
  define principalben = Character('Principal Ben', color="#", ctc="ctcstar", ctc_position="fixed")
  define oldpriest = Character('Old Priest', color="#E6E6E6", ctc="ctcstar", ctc_position="fixed")
  define fathermax = Character('Father Max', color="#E6E6E6", ctc="ctcstar", ctc_position="fixed")
  define hertha = Character('Ms. Wieck', color="#E949DA", ctc="ctcstar", ctc_position="fixed")
  define wieck = Character('Ms. Wieck', color="#E949DA", ctc="ctcstar", ctc_position="fixed")
  define mswieck = Character('Ms. Wieck', color="#E949DA", ctc="ctcstar", ctc_position="fixed")
  define edna = Character('Ms. Claes', color="#D90936", ctc="ctcstar", ctc_position="fixed")
  define claes = Character('Ms. Claes', color="#D90936", ctc="ctcstar", ctc_position="fixed")
  define msclaes = Character('Ms. Claes', color="#D90936", ctc="ctcstar", ctc_position="fixed")
  define ela = Character('Ela', color="#987889", ctc="ctcstar", ctc_position="fixed")
  define köhler = Character('Mr. Köhler', color="#CF6040", ctc="ctcstar", ctc_position="fixed")
  define karin = Character('Karin', color="#00FF00", ctc="ctcstar", ctc_position="fixed")
  define alfons = Character('Alfons', color="#", ctc="ctcstar", ctc_position="fixed")
  define fran = Character('Fran', color="#703D6F", ctc="ctcstar", ctc_position="fixed")
  define suspiciousperson = Character('Suspicious Person', color="#703D6F", ctc="ctcstar", ctc_position="fixed")

  #Family Related
  #Erik
  define mark = Character('Mark', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define father = Character('Father', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define dad = Character('Father', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define johanna = Character('Johanna', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define mother = Character('Mother', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define mom = Character('Mother', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define mum = Character('Mother', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define gustav = Character('Gustav', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define hilda = Character('Brunhilde', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define beatrice = Character('Beatrice', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define girl = Character('Girl', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")

  #Lena
  define gunther = Character('Gunther', color="#007FFF", ctc="ctcstar", ctc_position="fixed")
  define flora = Character('Flora', color="#E48400", ctc="ctcstar", ctc_position="fixed")

  #Jeanne
  define adrienne = Character ('Adrienne', color="#2020DE", ctc="ctcstar", ctc_position="fixed")
  define gaston = Character ('Gaston', color="#2E0D20", ctc="ctcstar", ctc_position="fixed")

  #Other
  define unknownqqq = Character('Unknown', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define unknown = Character('Unknown', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define Unknown = Character('Unknown', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define voice = Character('Voice', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define Voice = Character('Voice', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define man = Character('Man', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define woman = Character('Woman', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define bosworth = Character('Bosworth', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define guard = Character('Guard', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define fritz = Character('Fritz', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define teacher = Character('Teacher', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define student = Character('Student', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define nurse = Character('Nurse', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define stranger = Character('Stranger', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define nell = Character('Nell', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define eleanor = Character('Eleanor', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define boy = Character('Boy', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define yvonne = Character('Yvonne', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define allen = Character('Allen', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define irene = Character('Irene', color="#906D9F", ctc="ctcstar", ctc_position="fixed")
  define inconspicuousshrub = Character('Inconspicuous Shrub', color="#906D9F", ctc="ctcstar", ctc_position="fixed")
  define maskedgirl = Character('Masked Girl', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define brunettegirl = Character('Brunette Girl', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  #Undefined
  define todo = Character('TODO', color="#ff8300", ctc="ctcstar", ctc_position="fixed")

  #spelling errors
  define hilde = Character('Brunhilde', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define nataha = Character('Natasha', color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define natsha = Character('Natasha', color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define natahsa = Character('Natasha', color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define anna = Character('Annaliese', color="#22374c", ctc="ctcstar", ctc_position="fixed")
  define beatice = Character('Beatrice', color="#9d9d9d", ctc="ctcstar", ctc_position="fixed")
  define mysterious = Character('Mysterious Lady', color="#FE8A8A", ctc="ctcstar", ctc_position="fixed")

  define bg = Character('BG', color="#FABE28", ctc="ctcstar", ctc_position="fixed")
  define music = Character('MUSIC', color="#FABE28", ctc="ctcstar", ctc_position="fixed")

  #backgrounds
  image mountainRange =            "backgrounds/MountainRange.png"
  image bg car_interior = im.Scale("backgrounds/car_interior.jpg", 1280, 720, bilinear=False)

  image bg black="#000000"
  scene bg black
  with fade

  image BosworthOffice =    im.Scale("backgrounds/BosworthOffice_Under.png", 1920, 1080, bilinear=True)
  image BosworthOfficeFG =  im.Scale("backgrounds/BosworthOffice_Over.png", 1920, 1080, bilinear=True)
  image SisAptMorning =     im.Scale("backgrounds/SistersAppartment_ErikRoom_Morning_NOPAN.png", 1920, 1080, bilinear=True)
  image SisAptNight =       im.Scale("backgrounds/SistersAppartment_ErikRoom_Night_NOPAN.png", 1920, 1080, bilinear=True)
  image SisAptMain =        im.Scale("backgrounds/SisterApartment_DiningRoom_NOPAN.png", 1920, 1080, bilinear=True)
  image SisAptOutside =              "backgrounds/Vienna_OutsideApartment.png"
  image dormhall =          im.Scale("backgrounds/School_DormCorridor_NOPAN.png", 1920, 1080, bilinear=True)
  image outsidemaledorm =            "backgrounds/School_MaleDormsOut.png"
  image outsidemaledormcloudy =      "backgrounds/School_MaleDormsOut_Cloudy.png"
  image outsidefemaledorm =          "backgrounds/School_Generic2.jpg"
#  image inabush =                   "backgrounds/hedge.jpg"
  image mainbuilding =               "backgrounds/School_MainBuildEntrance.png"
  image mainbuildingclose =          "backgrounds/School_MainBuildingClose.png"
  image mainbuildingfar =            "backgrounds/School_MainBuildingFar.png"
  image mainbuildingfarcloudy =      "backgrounds/School_MainBuildingFar_Cloudy.png"
  image mainGateOverview =           "backgrounds/School_GateOverview.png"
  image mainGate =          im.Scale("backgrounds/School_Gate_NOPAN.png", 1920, 1080, bilinear=True)
#  image entrance1 =                 "backgrounds/School_MainBuildEntrance.png"
  image classroomhall =              "backgrounds/School_Corridor1.png"
  image classroomhall2 =             "backgrounds/School_Corridor2.png"
#  image hallway3 =                  "backgrounds/School_Corridor2.png"
  image school1 =                    "backgrounds/School_Generic1.png"
  image school2 =                    "backgrounds/School_Generic2.png"
  image chapel =                     "backgrounds/School_Generic3.png"
  image mainlobby =                  "backgrounds/School_MainHall.png"
  image classroom1 =        im.Scale("backgrounds/School_Classroom1_NOPAN.png", 1920, 1080, bilinear=True)
  image relaxroom =                  "backgrounds/School_Relaxroom_NOPAN.png"
  image clubroom1 =         im.Scale("backgrounds/School_Clubroom_NOPAN.png", 1920, 1080, bilinear=True)
  image cafeteriaoutside =           "backgrounds/School_CafeteriaOutside.png"
  image cafeteria =                  "backgrounds/School_Cafeteria.png"
  image ViennaStreet1 =              "backgrounds/Vienna_1.png"
  image ViennaStreet2 =              "backgrounds/Vienna_2.png"
  image ViennaStreet3 =              "backgrounds/Vienna_3.png"
  image ViennaStreet4 =              "backgrounds/Vienna_4.png"
  image ViennaCafe =                 "backgrounds/Vienna_Cafe.png"
  image erikdorm =          im.Scale("backgrounds/School_ErikRoom_NOPAN.png", 1920, 1080, bilinear=False)
  image erikdormcloudy =    im.Scale("backgrounds/School_ErikRoom_Cloudy_NOPAN.png", 1920, 1080, bilinear=False)
  image dormhallnight =     im.Scale("backgrounds/School_DormCorridor_Night_NOPAN.png", 1920, 1080, bilinear=True)
  image outsidemaledormnight =       "backgrounds/School_MaleDormsOut_Night.png"
  image schoolnight1=                "backgrounds/School_Grounds1_Night.png"
  image schoolnight2=                "backgrounds/School_Grounds2_Night.png"
  image erikdormnight =     im.Scale("backgrounds/School_ErikRoom_Night_NOPAN.png", 1920, 1080, bilinear=False)
  image mainbuildingnight =          "backgrounds/School_MainBuildingFar_Night.png"
  image schoolground1=               "backgrounds/School_Grounds1.png"
  image schoolground2=               "backgrounds/School_Grounds2.png"

  #CG
  image CGW1 = im.Scale("images/CG/CG_W1.png", 1920, 1080, bilinear=True)
  image CGW2 = im.Scale("images/CG/CG_W2.png", 1920, 1080, bilinear=True)
  image CGW3 = im.Scale("images/CG/CG_W3.png", 1920, 1080, bilinear=True)
  image CG01 = im.Scale("images/CG/CG_01.png", 1920, 1080, bilinear=True)
  image CG02 = im.Scale("images/CG/CG_02.png", 1920, 1080, bilinear=True)
  image CG03E1 = im.Scale("images/CG/CG_03_E1.png", 1920, 1080, bilinear=True)
  image CG03E2 = im.Scale("images/CG/CG_03_E2.png", 1920, 1080, bilinear=True)
  image CG03E3 = im.Scale("images/CG/CG_03_E3.png", 1920, 1080, bilinear=True)
  image CG03E4 = im.Scale("images/CG/CG_03_E4.png", 1920, 1080, bilinear=True)
  image CG03E5 = im.Scale("images/CG/CG_03_E5.png", 1920, 1080, bilinear=True)
  image CG04 = "images/CG/CG_04.png"
  image CG05 = im.Scale("images/CG/CG_05demo.png", 1920, 1080, bilinear=True)
  image CG05E1 = im.Scale("images/CG/CG_05_E1.png", 1920, 1080, bilinear=True)
  image CG05E2 = im.Scale("images/CG/CG_05_E2.png", 1920, 1080, bilinear=True)
  image CG05E3 = im.Scale("images/CG/CG_05_E3.png", 1920, 1080, bilinear=True)
  image CG06E1 = im.Scale("images/CG/CG_06_E1.png", 1920, 1080, bilinear=True)
  image CG06E2 = im.Scale("images/CG/CG_06_E2.png", 1920, 1080, bilinear=True)
  image CG07 = im.Scale("images/CG/CG_07.png", 1920, 1080, bilinear=True)
  image CGErik = im.Scale("images/CG/CG_Erik.png", 1920, 1080, bilinear=True)
  image EriksPhone = im.Scale("images/CG/EriksPhone.png", 1920, 1080, bilinear=True)
  image CGui = im.Scale("ui/TextboxFade.png", 1920, 1080, bilinear=True)
  #Sprites

  image PitchBlack = Solid("#000")
  image PitchWhite = Solid("#FFF")
  image LensFlare1 = im.Scale("Transitions/lensflareoverlay.png", 1920, 1080, bilinear=False)

  #main characters

  image ela P1_E1 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E1.png", 0.70, bilinear=True)
  image ela P1_E2 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E2.png", 0.70, bilinear=True)
  image ela P1_E3 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E3.png", 0.70, bilinear=True)
  image ela P1_E4 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E4.png", 0.70, bilinear=True)
  image ela P1_E5 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E5.png", 0.70, bilinear=True)
  image ela P1_E6 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E6.png", 0.70, bilinear=True)
  image ela P1_E7 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E7.png", 0.70, bilinear=True)
  image ela P1_E8 = im.FactorScale("images/Sprites/Main Characters/Ela/Ela_P1_E8.png", 0.70, bilinear=True)

  image irene U_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Irene/Uniform/Irene_Uniform_P1_E1.png", 0.63, bilinear=True)
  image irene U_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Irene/Uniform/Irene_Uniform_P1_E2.png", 0.63, bilinear=True)
  image irene U_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Irene/Uniform/Irene_Uniform_P1_E3.png", 0.63, bilinear=True)
  image irene U_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Irene/Uniform/Irene_Uniform_P1_E4.png", 0.63, bilinear=True)
  image irene U_FALLING = im.FactorScale("images/Sprites/Main Characters/Irene/Uniform/Irene_Uniform_P1_E2.png", 0.63, bilinear=True)
  image irene HD_P1_E1 = im.FactorScale("images/Sprites/HD/IreneHD_E1.png", 0.63, bilinear=True)
  image irene HD_P1_E2 = im.FactorScale("images/Sprites/HD/IreneHD_E2.png", 0.63, bilinear=True)
  image irene HD_P1_E4 = im.FactorScale("images/Sprites/HD/IreneHD_E4.png", 0.63, bilinear=True)

  image isolda U_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E1.png", 0.66, bilinear=True)
  image isolda U_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E2.png", 0.66, bilinear=True)
  image isolda U_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E3.png", 0.66, bilinear=True)
  image isolda U_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E4.png", 0.66, bilinear=True)
  image isolda U_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E5.png", 0.66, bilinear=True)
  image isolda U_P1_E6 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E6.png", 0.66, bilinear=True)
  image isolda U_P1_E7 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E7.png", 0.66, bilinear=True)
  image isolda U_P1_E8 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P1_E8.png", 0.66, bilinear=True)
  image isolda U_P2_E1 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P2_E1.png", 0.66, bilinear=True)
  image isolda U_P2_E2 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P2_E2.png", 0.66, bilinear=True)
  image isolda U_P2_E6 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P2_E6.png", 0.66, bilinear=True)
  image isolda U_P2_E7 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P2_E7.png", 0.66, bilinear=True)
  image isolda U_P2_E8 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P2_E8.png", 0.66, bilinear=True)
  image isolda U_P3_E1 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E1.png", 0.66, bilinear=True)
  image isolda U_P3_E2 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E2.png", 0.66, bilinear=True)
  image isolda U_P3_E3 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E3.png", 0.66, bilinear=True)
  image isolda U_P3_E4 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E4.png", 0.66, bilinear=True)
  image isolda U_P3_E5 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E5.png", 0.66, bilinear=True)
  image isolda U_P3_E6 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E6.png", 0.66, bilinear=True)
  image isolda U_P3_E7 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E7.png", 0.66, bilinear=True)
  image isolda U_P3_E8 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P3_E8.png", 0.66, bilinear=True)
  image isolda U_P4_E1 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P4_E1.png", 0.66, bilinear=True)
  image isolda U_P4_E2 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P4_E2.png", 0.66, bilinear=True)
  image isolda U_P4_E3 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P4_E3.png", 0.66, bilinear=True)
  image isolda U_P4_E6 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P4_E6.png", 0.66, bilinear=True)
  image isolda U_P5_E1 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P5_E1.png", 0.66, bilinear=True)
  image isolda U_P5_E4 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P5_E4.png", 0.66, bilinear=True)
  image isolda U_P5_E5 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P5_E5.png", 0.66, bilinear=True)
  image isolda U_P5_E6 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P5_E6.png", 0.66, bilinear=True)
  image isolda U_P5_E8 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P5_E8.png", 0.66, bilinear=True)
  image isolda U_P6_E4 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P6_E4.png", 0.66, bilinear=True)
  image isolda U_P6_E5 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P6_E5.png", 0.66, bilinear=True)
  image isolda U_P6_E6 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P6_E6.png", 0.66, bilinear=True)
  image isolda U_P6_E8 = im.FactorScale("images/Sprites/Main Characters/Isolda/Uniform/Isolda_Uniform_P6_E8.png", 0.66, bilinear=True)

  image katja U_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E1.png", 0.69, bilinear=True)
  image katja U_P1_E2a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E2a.png", 0.69, bilinear=True)
  image katja U_P1_E2b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E2b.png", 0.69, bilinear=True)
  image katja U_P1_E3a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E3a.png", 0.69, bilinear=True)
  image katja U_P1_E3b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E3b.png", 0.69, bilinear=True)
  image katja U_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E4.png", 0.69, bilinear=True)
  image katja U_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E5.png", 0.69, bilinear=True)
  image katja U_P1_E6 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E6.png", 0.69, bilinear=True)
  image katja U_P1_E7a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E7a.png", 0.69, bilinear=True)
  image katja U_P1_E7b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E7b.png", 0.69, bilinear=True)
  image katja U_P1_E8a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E8a.png", 0.69, bilinear=True)
  image katja U_P1_E8b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E8b.png", 0.69, bilinear=True)
  image katja U_P1_E9 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E9.png", 0.69, bilinear=True)
  image katja U_P1_E10 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P1_E10.png", 0.69, bilinear=True)
  image katja U_P2_E1a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E1a.png", 0.69, bilinear=True)
  image katja U_P2_E1b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E1b.png", 0.69, bilinear=True)
  image katja U_P2_E2 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E2.png", 0.69, bilinear=True)
  image katja U_P2_E6 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E6.png", 0.69, bilinear=True)
  image katja U_P2_E7 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E7.png", 0.69, bilinear=True)
  image katja U_P2_E8 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E8.png", 0.69, bilinear=True)
  image katja U_P2_E9 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P2_E9.png", 0.69, bilinear=True)
  image katja U_P4_E1 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E1.png", 0.69, bilinear=True)
  image katja U_P4_E2 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E2.png", 0.69, bilinear=True)
  image katja U_P4_E5 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E5.png", 0.69, bilinear=True)
  image katja U_P4_E6 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E6.png", 0.69, bilinear=True)
  image katja U_P4_E7 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E7.png", 0.69, bilinear=True)
  image katja U_P4_E8 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E8.png", 0.69, bilinear=True)
  image katja U_P4_E9 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E9.png", 0.69, bilinear=True)
  image katja U_P4_E10 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P4_E10.png", 0.69, bilinear=True)
  image katja U_P5_E1 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E1.png", 0.69, bilinear=True)
  image katja U_P5_E2a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E2a.png", 0.69, bilinear=True)
  image katja U_P5_E2b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E2b.png", 0.69, bilinear=True)
  image katja U_P5_E3a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E3a.png", 0.69, bilinear=True)
  image katja U_P5_E3b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E3b.png", 0.69, bilinear=True)
  image katja U_P5_E4 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E4.png", 0.69, bilinear=True)
  image katja U_P5_E5 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E5.png", 0.69, bilinear=True)
  image katja U_P5_E6 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E6.png", 0.69, bilinear=True)
  image katja U_P5_E7a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E7a.png", 0.69, bilinear=True)
  image katja U_P5_E7b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E7b.png", 0.69, bilinear=True)
  image katja U_P5_E8a = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E8a.png", 0.69, bilinear=True)
  image katja U_P5_E8b = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E8b.png", 0.69, bilinear=True)
  image katja U_P5_E9 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E9.png", 0.69, bilinear=True)
  image katja U_P5_E10 = im.FactorScale("images/Sprites/Main Characters/Katja/Uniform/Katja_uniform_P5_E10.png", 0.69, bilinear=True)

  image lena U_M_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E1.png", 0.72, bilinear=True)
  image lena U_M_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E2.png", 0.72, bilinear=True)
  image lena U_M_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E3.png", 0.72, bilinear=True)
  image lena U_M_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E4.png", 0.72, bilinear=True)
  image lena U_M_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E5.png", 0.72, bilinear=True)
  image lena U_M_P1_E6 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E6.png", 0.72, bilinear=True)
  image lena U_M_P1_E7 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E7.png", 0.72, bilinear=True)
  image lena U_M_P1_E8 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P1_E8.png", 0.72, bilinear=True)
  image lena U_M_P2_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P2_E1.png", 0.72, bilinear=True)
  image lena U_M_P2_E2 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P2_E2.png", 0.72, bilinear=True)
  image lena U_M_P2_E4 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P2_E4.png", 0.72, bilinear=True)
  image lena U_M_P3_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E1.png", 0.72, bilinear=True)
  image lena U_M_P3_E2 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E2.png", 0.72, bilinear=True)
  image lena U_M_P3_E3 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E3.png", 0.72, bilinear=True)
  image lena U_M_P3_E4 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E4.png", 0.72, bilinear=True)
  image lena U_M_P3_E5 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E5.png", 0.72, bilinear=True)
  image lena U_M_P3_E6 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E6.png", 0.72, bilinear=True)
  image lena U_M_P3_E7 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E7.png", 0.72, bilinear=True)
  image lena U_M_P3_E8 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P3_E8.png", 0.72, bilinear=True)
  image lena U_M_P4_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P4_E1.png", 0.72, bilinear=True)
  image lena U_M_P4_E2 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P4_E2.png", 0.72, bilinear=True)
  image lena U_M_P4_E4 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P4_E4.png", 0.72, bilinear=True)
  image lena U_M_P5_E8 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P5_E8.png", 0.72, bilinear=True)
  image lena U_M_P6_E5 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P6_E5.png", 0.72, bilinear=True)
  image lena U_M_P7_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformMask_P7_E1.png", 0.72, bilinear=True)
  image lena U_N_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E1.png", 0.72, bilinear=True)
  image lena U_N_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E2.png", 0.72, bilinear=True)
  image lena U_N_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E3.png", 0.72, bilinear=True)
  image lena U_N_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E4.png", 0.72, bilinear=True)
  image lena U_N_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E5.png", 0.72, bilinear=True)
  image lena U_N_P1_E6 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E6.png", 0.72, bilinear=True)
  image lena U_N_P1_E7 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E7.png", 0.72, bilinear=True)
  image lena U_N_P1_E8 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P1_E8.png", 0.72, bilinear=True)
  image lena U_N_P3_E1 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E1.png", 0.72, bilinear=True)
  image lena U_N_P3_E2 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E2.png", 0.72, bilinear=True)
  image lena U_N_P3_E3 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E3.png", 0.72, bilinear=True)
  image lena U_N_P3_E4 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E4.png", 0.72, bilinear=True)
  image lena U_N_P3_E5 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E5.png", 0.72, bilinear=True)
  image lena U_N_P3_E6 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E6.png", 0.72, bilinear=True)
  image lena U_N_P3_E7 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E7.png", 0.72, bilinear=True)
  image lena U_N_P3_E8 = im.FactorScale("images/Sprites/Main Characters/Lena/Uniform/Lena_uniformNomask_P3_E8.png", 0.72, bilinear=True)
  image lena HD_P3_E2 = im.FactorScale("images/Sprites/HD/LenaHD_P3_E2.png", 0.72, bilinear=True)
  image lena HD_P3_E4 = im.FactorScale("images/Sprites/HD/LenaHD_P3_E4.png", 0.72, bilinear=True)

  image anna U_B_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P1_E1.png", 0.65, bilinear=True)
  image anna U_B_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P1_E2.png", 0.65, bilinear=True)
  image anna U_B_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P1_E3.png", 0.65, bilinear=True)
  image anna U_B_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P1_E4.png", 0.65, bilinear=True)
  image anna U_B_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P1_E5.png", 0.65, bilinear=True)
  image anna U_B_P2_E1 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P2_E1.png", 0.65, bilinear=True)
  image anna U_B_P2_E3 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P2_E3.png", 0.65, bilinear=True)
  image anna U_B_P2_E4 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P2_E4.png", 0.65, bilinear=True)
  image anna U_B_P2_E6 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P2_E6.png", 0.65, bilinear=True)
  image anna U_B_P2_E7 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P2_E7.png", 0.65, bilinear=True)
  image anna U_B_P2_E8 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformBuds_P2_E8.png", 0.65, bilinear=True)
  image anna U_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P1_E1.png", 0.65, bilinear=True)
  image anna U_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P1_E2.png", 0.65, bilinear=True)
  image anna U_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P1_E3.png", 0.65, bilinear=True)
  image anna U_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P1_E4.png", 0.65, bilinear=True)
  image anna U_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P1_E5.png", 0.65, bilinear=True)
  image anna U_P2_E1 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P2_E1.png", 0.65, bilinear=True)
  image anna U_P2_E3 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P2_E3.png", 0.65, bilinear=True)
  image anna U_P2_E4 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P2_E4.png", 0.65, bilinear=True)
  image anna U_P2_E6 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P2_E6.png", 0.65, bilinear=True)
  image anna U_P2_E7 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P2_E7.png", 0.65, bilinear=True)
  image anna U_P2_E8 = im.FactorScale("images/Sprites/Main Characters/Annaliese/Annaliese_UniformNobuds_P2_E8.png", 0.65, bilinear=True)

  image natalya U_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E1.png", 0.68, bilinear=True)
  image natalya U_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E2.png", 0.68, bilinear=True)
  image natalya U_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E3.png", 0.68, bilinear=True)
  image natalya U_P1_E4 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E4.png", 0.68, bilinear=True)
  image natalya U_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E5.png", 0.68, bilinear=True)
  image natalya U_P1_E6 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E6.png", 0.68, bilinear=True)
  image natalya U_P1_E7a = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E7a.png", 0.68, bilinear=True)
  image natalya U_P1_E7b = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E7b.png", 0.68, bilinear=True)
  image natalya U_P1_E8 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E8.png", 0.68, bilinear=True)
  image natalya U_P1_E9 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E9.png", 0.68, bilinear=True)
  image natalya U_P1_E10 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P1_E10.png", 0.68, bilinear=True)
  image natalya U_P2_E1 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E1.png", 0.68, bilinear=True)
  image natalya U_P2_E2 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E2.png", 0.68, bilinear=True)
  image natalya U_P2_E3 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E3.png", 0.68, bilinear=True)
  image natalya U_P2_E4 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E4.png", 0.68, bilinear=True)
  image natalya U_P2_E5 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E5.png", 0.68, bilinear=True)
  image natalya U_P2_E6 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E6.png", 0.68, bilinear=True)
  image natalya U_P2_E7a = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E7a.png", 0.68, bilinear=True)
  image natalya U_P2_E7b = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E7b.png", 0.68, bilinear=True)
  image natalya U_P2_E8 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E8.png", 0.68, bilinear=True)
  image natalya U_P2_E9 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E9.png", 0.68, bilinear=True)
  image natalya U_P2_E10 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P2_E10.png", 0.68, bilinear=True)
  image natalya U_P3_E1 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E1.png", 0.68, bilinear=True)
  image natalya U_P3_E2 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E2.png", 0.68, bilinear=True)
  image natalya U_P3_E3 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E3.png", 0.68, bilinear=True)
  image natalya U_P3_E4 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E4.png", 0.68, bilinear=True)
  image natalya U_P3_E5 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E5.png", 0.68, bilinear=True)
  image natalya U_P3_E6 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E6.png", 0.68, bilinear=True)
  image natalya U_P3_E7a = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E7a.png", 0.68, bilinear=True)
  image natalya U_P3_E7b = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E7b.png", 0.68, bilinear=True)
  image natalya U_P3_E8 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E8.png", 0.68, bilinear=True)
  image natalya U_P3_E9 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E9.png", 0.68, bilinear=True)
  image natalya U_P3_E10 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P3_E10.png", 0.68, bilinear=True)
  image natalya U_P4_E1 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E1.png", 0.68, bilinear=True)
  image natalya U_P4_E2 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E2.png", 0.68, bilinear=True)
  image natalya U_P4_E3 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E3.png", 0.68, bilinear=True)
  image natalya U_P4_E4 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E4.png", 0.68, bilinear=True)
  image natalya U_P4_E5 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E5.png", 0.68, bilinear=True)
  image natalya U_P4_E6 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E6.png", 0.68, bilinear=True)
  image natalya U_P4_E7a = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E7a.png", 0.68, bilinear=True)
  image natalya U_P4_E7b = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E7b.png", 0.68, bilinear=True)
  image natalya U_P4_E8 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E8.png", 0.68, bilinear=True)
  image natalya U_P4_E9 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E9.png", 0.68, bilinear=True)
  image natalya U_P4_E10 = im.FactorScale("images/Sprites/Main Characters/Natalya/Uniform/Natalya_Uniform_P4_E10.png", 0.68, bilinear=True)

  image sofiya C_P1_E1 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E1.png", 0.64, bilinear=True)
  image sofiya C_P1_E2 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E2.png", 0.64, bilinear=True)
  image sofiya C_P1_E3 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E3.png", 0.64, bilinear=True)
  image sofiya C_P1_E4a = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E4a.png", 0.64, bilinear=True)
  image sofiya C_P1_E4b = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E4b.png", 0.64, bilinear=True)
  image sofiya C_P1_E5 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E5.png", 0.64, bilinear=True)
  image sofiya C_P1_E6 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E6.png", 0.64, bilinear=True)
  image sofiya C_P1_E7 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E7.png", 0.64, bilinear=True)
  image sofiya C_P1_E8 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E8.png", 0.64, bilinear=True)
  image sofiya C_P1_E9 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P1_E9.png", 0.64, bilinear=True)
  image sofiya C_P2_E1 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E1.png", 0.64, bilinear=True)
  image sofiya C_P2_E2 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E2.png", 0.64, bilinear=True)
  image sofiya C_P2_E3 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E3.png", 0.64, bilinear=True)
  image sofiya C_P2_E4a = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E4a.png", 0.64, bilinear=True)
  image sofiya C_P2_E4b = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E4b.png", 0.64, bilinear=True)
  image sofiya C_P2_E5 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E5.png", 0.64, bilinear=True)
  image sofiya C_P2_E6 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E6.png", 0.64, bilinear=True)
  image sofiya C_P2_E7 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E7.png", 0.64, bilinear=True)
  image sofiya C_P2_E8 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E8.png", 0.64, bilinear=True)
  image sofiya C_P2_E9 = im.FactorScale("images/Sprites/Main Characters/Sofiya/Sofiya_Casual_P2_E9.png", 0.64, bilinear=True)

  #side characters

  image beatrice P1_E1 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E1.png", 0.68, bilinear=True)
  image beatrice P1_E2 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E2.png", 0.68, bilinear=True)
  image beatrice HDP1_E2 = im.FactorScale("images/Sprites/Side Characters/Beatrice/BeatriceHD_P1_E2.png", 0.68, bilinear=True)
  image beatrice P1_E3 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E3.png", 0.68, bilinear=True)
  image beatrice HDP1_E3 = im.FactorScale("images/Sprites/Side Characters/Beatrice/BeatriceHD_P1_E3.png", 0.68, bilinear=True)
  image beatrice P1_E4 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E4.png", 0.68, bilinear=True)
  image beatrice P1_E5 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E5.png", 0.68, bilinear=True)
  image beatrice P1_E6 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E6.png", 0.68, bilinear=True)
  image beatrice P1_E7 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E7.png", 0.68, bilinear=True)
  image beatrice P1_E8 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P1_E8.png", 0.68, bilinear=True)
  image beatrice P2_E1 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E1.png", 0.68, bilinear=True)
  image beatrice P2_E2 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E2.png", 0.68, bilinear=True)
  image beatrice P2_E3 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E3.png", 0.68, bilinear=True)
  image beatrice P2_E4 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E4.png", 0.68, bilinear=True)
  image beatrice P2_E5 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E5.png", 0.68, bilinear=True)
  image beatrice P2_E6 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E6.png", 0.68, bilinear=True)
  image beatrice P2_E7 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E7.png", 0.68, bilinear=True)
  image beatrice P2_E8 = im.FactorScale("images/Sprites/Side Characters/Beatrice/Beatrice_P2_E8.png", 0.68, bilinear=True)

  image hilda P1_E1 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P1_E1.png", 0.77, bilinear=True)
  image hilda P1_E2 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P1_E2.png", 0.77, bilinear=True)
  image hilda P1_E4 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P1_E4.png", 0.77, bilinear=True)
  image hilda P1_E5 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P1_E5.png", 0.77, bilinear=True)
  image hilda P2_E1 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E1.png", 0.77, bilinear=True)
  image hilda P2_E2 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E2.png", 0.77, bilinear=True)
  image hilda P2_E3 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E3.png", 0.77, bilinear=True)
  image hilda P2_E4 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E4.png", 0.77, bilinear=True)
  image hilda P2_E5 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E5.png", 0.77, bilinear=True)
  image hilda P2_E6 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P2_E6.png", 0.77, bilinear=True)
  image hilda P3_E1 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P3_E1.png", 0.77, bilinear=True)
  image hilda P3_E2 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P3_E2.png", 0.77, bilinear=True)
  image hilda P3_E3 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P3_E3.png", 0.77, bilinear=True)
  image hilda P3_E4 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P3_E4.png", 0.77, bilinear=True)
  image hilda P3_E5 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P3_E5.png", 0.77, bilinear=True)
  image hilda P3_E6 = im.FactorScale("images/Sprites/Side Characters/Brunhilde/Brunhilde_P3_E6.png", 0.77, bilinear=True)

  image faber P1_E1 = im.FactorScale("images/Sprites/Side Characters/Dr. Faber/Faber_P1_E1.png", 0.73, bilinear=True)
  image faber P1_E2 = im.FactorScale("images/Sprites/Side Characters/Dr. Faber/Faber_P1_E2.png", 0.73, bilinear=True)

  image claes P1_E1 = im.FactorScale("images/Sprites/Side Characters/Edna Klaes/Edna_P1_E1.png", 0.73, bilinear=True)
  image claes P1_E2 = im.FactorScale("images/Sprites/Side Characters/Edna Klaes/Edna_P1_E2.png", 0.73, bilinear=True)
  image claes P1_E3 = im.FactorScale("images/Sprites/Side Characters/Edna Klaes/Edna_P1_E3.png", 0.73, bilinear=True)
  image claes P1_E4 = im.FactorScale("images/Sprites/Side Characters/Edna Klaes/Edna_P1_E4.png", 0.73, bilinear=True)
  image claes P1_E5 = im.FactorScale("images/Sprites/Side Characters/Edna Klaes/Edna_P1_E5.png", 0.73, bilinear=True)

  image fathermax P1_E1 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P1_E1", 0.666, bilinear=True)
  image fathermax P1_E2 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P1_E2", 0.666, bilinear=True)
  image fathermax P1_E3 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P1_E3", 0.666, bilinear=True)
  image fathermax P1_E4 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P1_E4", 0.666, bilinear=True)
  image fathermax P2_E1 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P2_E1", 0.666, bilinear=True)
  image fathermax P2_E2 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P2_E2", 0.666, bilinear=True)
  image fathermax P2_E3 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P2_E3", 0.666, bilinear=True)
  image fathermax P2_E4 = im.FactorScale("images/Sprites/Side Characters/Father Max/FatherMax_P2_E4", 0.666, bilinear=True)

  image fritz P1_E2 = im.FactorScale("images/Sprites/Side Characters/Fritz/Fritz_P1_E2", 0.666, bilinear=True)
  image fritz P1_E4 = im.FactorScale("images/Sprites/Side Characters/Fritz/Fritz_P1_E4", 0.666, bilinear=True)

  image dad P1_E1 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P1_E1.png", 0.76, bilinear=True)
  image dad P1_E2 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P1_E2.png", 0.76, bilinear=True)
  image dad P1_E4 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P1_E4.png", 0.76, bilinear=True)
  image dad P1_E5 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P1_E5.png", 0.76, bilinear=True)
  image dad P1_E7 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P1_E7.png", 0.76, bilinear=True)
  image dad P1_E9 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P1_E9.png", 0.76, bilinear=True)
  image dad P2_E1 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P2_E1.png", 0.76, bilinear=True)
  image dad P2_E2 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P2_E2.png", 0.76, bilinear=True)
  image dad P2_E4 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P2_E4.png", 0.76, bilinear=True)
  image dad P2_E5 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P2_E5.png", 0.76, bilinear=True)
  image dad P2_E7 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P2_E7.png", 0.76, bilinear=True)
  image dad P2_E9 = im.FactorScale("images/Sprites/Side Characters/Mr.Wilhelm/MrWilhelm_P2_E9.png", 0.76, bilinear=True)

  image mum P1_E1 = im.FactorScale("images/Sprites/Side Characters/Mrs.Wilhelm/MamaWilhelm_P1_E1.png", 0.76, bilinear=True)
  image mum P1_E2 = im.FactorScale("images/Sprites/Side Characters/Mrs.Wilhelm/MamaWilhelm_P1_E2.png", 0.76, bilinear=True)
  image mum P1_E4 = im.FactorScale("images/Sprites/Side Characters/Mrs.Wilhelm/MamaWilhelm_P1_E4.png", 0.76, bilinear=True)
  image mum P1_E5 = im.FactorScale("images/Sprites/Side Characters/Mrs.Wilhelm/MamaWilhelm_P1_E5.png", 0.76, bilinear=True)
  image mum P1_E7 = im.FactorScale("images/Sprites/Side Characters/Mrs.Wilhelm/MamaWilhelm_P1_E7.png", 0.76, bilinear=True)
  image mum P1_E8 = im.FactorScale("images/Sprites/Side Characters/Mrs.Wilhelm/MamaWilhelm_P1_E8.png", 0.76, bilinear=True)

  image bosworth P1_E2 = im.FactorScale("images/Sprites/Side Characters/Principal Bosworth/Bosworth_P1_E2.png", 0.75, bilinear=True)
  image bosworth P1_E4 = im.FactorScale("images/Sprites/Side Characters/Principal Bosworth/Bosworth_P1_E4.png", 0.75, bilinear=True)

  image fran P1_E1 = im.FactorScale("images/Sprites/Side Characters/Fran/Fran_Uniform_P1_E1.png", 0.68, bilinear=True)
  image fran P1_E2 = im.FactorScale("images/Sprites/Side Characters/Fran/Fran_Uniform_P1_E2.png", 0.68, bilinear=True)
  image fran P1_E3 = im.FactorScale("images/Sprites/Side Characters/Fran/Fran_Uniform_P1_E3.png", 0.68, bilinear=True)
  image fran P1_E4 = im.FactorScale("images/Sprites/Side Characters/Fran/Fran_Uniform_P1_E4.png", 0.68, bilinear=True)
  image fran P1_E5 = im.FactorScale("images/Sprites/Side Characters/Fran/Fran_Uniform_P1_E5.png", 0.68, bilinear=True)

  image hertha U_P1_E1 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E1.png", 0.72, bilinear=True)
  image hertha U_P1_E2 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E2.png", 0.72, bilinear=True)
  image hertha U_P1_E3 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E3.png", 0.72, bilinear=True)
  image hertha U_P1_E4 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E4.png", 0.72, bilinear=True)
  image hertha U_P1_E5 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E5.png", 0.72, bilinear=True)
  image hertha U_P1_E6 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E6.png", 0.72, bilinear=True)
  image hertha U_P1_E7 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P1_E7.png", 0.72, bilinear=True)
  image hertha U_P2_E2 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P2_E2.png", 0.72, bilinear=True)
  image hertha U_P2_E3 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P2_E3.png", 0.72, bilinear=True)
  image hertha U_P2_E4 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P2_E4.png", 0.72, bilinear=True)
  image hertha U_P2_E5 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P2_E5.png", 0.72, bilinear=True)
  image hertha U_P2_E6 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P2_E6.png", 0.72, bilinear=True)
  image hertha U_P2_E7 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P2_E7.png", 0.72, bilinear=True)
  image hertha U_P3_E1 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P3_E1.png", 0.72, bilinear=True)
  image hertha U_P3_E2 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P3_E2.png", 0.72, bilinear=True)
  image hertha U_P3_E7 = im.FactorScale("images/Sprites/Side Characters/Hertha/Hertha_Uniform_P3_E7.png", 0.72, bilinear=True)

  $ renpy.music.set_volume(0.75, 0, "music")
  $ renpy.music.set_volume(0.75, 0, "music2")
  $ renpy.music.set_volume(0.75, 0, "sound")
  $ renpy.music.set_volume(0.75, 0, "ambience")
  $ renpy.music.set_volume(0.75, 0, "ambience2")
  $ config.default_music_volume = 0.75
  $ config.default_sfx_volume = 0.75

  # flag that game has been started
  $ persistent.started = 1

  # Girl influence totals
  if (persistent.i_tot == None):
    $ persistent.i_tot = 0
  if (persistent.j_tot == None):
    $ persistent.j_tot = 0
  if (persistent.l_tot == None):
    $ persistent.l_tot = 0
  if (persistent.k_tot == None):
    $ persistent.k_tot = 0
  if (persistent.a_tot == None):
    $ persistent.a_tot = 0
  if (persistent.nl_tot == None):
    $ persistent.nl_tot = 0
  if (persistent.nh_tot == None):
    $ persistent.nh_tot = 0
  if (persistent.am_tot == None):
    $ persistent.am_tot = 0
  $ j_help = 0

  # Girl whose path you are on, 1..x, up to 9, "0"=on no path
  # yes, use a string
  $ persistent.girlpath = "0"

  python:
    if (persistent.start_act == None or persistent.start_act == ""):
      persistent.start_act = "A1_01"

  # Act 1 misc flags
  $ club_flag = 0        # Default is to not have been to the club
  $ scene_a1_30_flag = 1 # This needs to be set as default in case the question is skipped

  # image movie = Movie(size=(1024, 768))
  stop movie

  # Debug info
  $ persistent.scene_number = "no scene" # current scene

  jump expression persistent.start_act.upper()[:3] + persistent.start_act.lower()[3:]

