# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

transform appear:
    on show:
        alpha 0.0
        easein 0.5 alpha 1.0

    on replace:
        alpha 1.0
        easein 0.5 alpha 1.0

    on hide:
        alpha 1.0
        easein 0.25 alpha 0.0

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu1
    use quick_menu2


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window_root"
        xalign 0.5
        yalign 0.5

        at appear

    frame:
        style_group "menu_window"
        xalign .50
        yalign .50

        vbox:
            style "menu"
            spacing 2
            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True

    style.menu_window_root.background = "images/Menus/choicesmenu/ChoiceMenu_Background.png"
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice.size = 35
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.menu_choice_button.idle_background = "/images/Buttons/idle_menubutton.png"
    style.menu_choice_button.hover_background = LiveComposite(
        (250,50),
        (0,0), "/images/Buttons/idle_menubutton.png",
        (150,0), "images/Menus/preferencesmenu/blue_arrow.png"
        )


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window:
        has vbox

        text prompt
        input id "input"

        at appear

    use quick_menu1
    use quick_menu2

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu1
    use quick_menu2

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

label main_menu_reset:

screen main_menu:

  # This ensures that any other menu screen is replaced.
  tag menu

  if (persistent.menu_ui == 6):
    use main_menu_kev
  else:
    # The background of the main menu.
    window:
        style "mm_root"
        at appear

    python:
      # BG stars
      ui.frame(xpos=config.screen_width/2,ypos=config.screen_height/2, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
      ui.imagebutton(im.Scale("images/Menus/mainmenu/MainMenu.png",config.screen_width, config.screen_height, bilinear=True),"images/Menus/mainmenu/MainMenu.png")


    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .5
        yalign .5

        has vbox
        textbutton _("Jan 5, 2016 flowchart test") action None
        textbutton _("Select test UI") action None
        textbutton _("Main Menu") action Jump("kev_ui2")
        textbutton _(" ") action None
        textbutton _("Reset all to new game") action Jump("reset_all")
        textbutton _(" ") action None
        if persistent.show_scene_number:
          textbutton _("scene number on") action Jump("tog_scene_number")
        else:
          textbutton _("scene number off") action Jump("tog_scene_number")
        if persistent.show_girl_totals:
          textbutton _("girl totals on") action Jump("tog_girl_totals")
        else:
          textbutton _("girl totals off") action Jump("tog_girl_totals")
        textbutton _("Set Starting Act") action Jump ("set_act")
        if persistent.skip_menus:
          textbutton _("Use Menus") action Jump("tog_menus")
        else:
          textbutton _("Skip Menus") action Jump("tog_menus")
        textbutton _("Set Girl Totals") action Jump ("set_girls")
        textbutton _(" ") action None
        textbutton _("800 x 450") action Jump("rez_800_450")
        textbutton _("1280 x 720") action Jump("rez_1280_720")
        textbutton _("1600 x 900") action Jump("rez_1600_900")
        textbutton _("1920 x 1080") action Jump("rez_1920_1080")
        textbutton _("2560 x 1440") action Jump("rez_2560_1440")
        textbutton _(" ") action None
        textbutton _("Quit") action Quit(confirm=False)

    # HOW TO ANIMATE MAIN MENU
#  image mmbg composite = LiveComposite(
#    (config.screen_width,config.screen_height),
#   (0,0),"images/Menus/mainmenu/MainMenu.png",
#   (0,0),"images/Menus/mainmenu/shadow.png",
#   (0,0),"images/Menus/mainmenu/dashedline.png")
#
image movie = Movie(size=(config.screen_width, config.screen_height))

init python:
    style.mm_root.background = Frame("images/Menus/mainmenu/MainMenu.png", left=0, top=0, right=None, bottom=None, tile=False)

label main_menu:
    scene movie

    python:
      if persistent.menu_ui == 5:
        renpy.music.play("video/starz4.ogg", channel="movie", loop=True)
      elif persistent.menu_ui == 6:
        #renpy.music.play("video/background720p.webm", channel="movie", loop=True)
        renpy.music.play("music/mainmenumusic.ogg", channel="music", loop=True)
        renpy.music.set_volume(0.8, channel="music")
        #ui.frame("images/Menus/mainmenu/MainMenu.png", xpos=config.screen_width/2,ypos=config.screen_height/2, xanchor='center', yanchor='center', xpadding=0, ypadding=0)
        #style.window.background = Frame("images/Menus/mainmenu/MainMenu.png", left=0, top=0, right=None, bottom=None, tile=False)
    jump main_menu_screen



screen main_menu_kev:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    python:
      if (persistent.k_menu > 2):
        ui.frame(xpos=524*config.screen_width/1200,ypos=154*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar1.png", 40*config.screen_width/1200, 40*config.screen_height/675, bilinear=True),"images/Menus/kstar1.png")
      if (persistent.a_menu > 2):
        ui.frame(xpos=615*config.screen_width/1200,ypos=208*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar2.png", 30*config.screen_width/1200, 26*config.screen_height/675, bilinear=True),"images/Menus/kstar2.png")
      if (persistent.l_menu > 2):
        ui.frame(xpos=752*config.screen_width/1200,ypos=158*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar3.png", 44*config.screen_width/1200, 39*config.screen_height/675, bilinear=True),"images/Menus/kstar3.png")
      if (persistent.j_menu > 2):
        ui.frame(xpos=706*config.screen_width/1200,ypos=42*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar5.png", 22*config.screen_width/1200, 22*config.screen_height/675, bilinear=True),"images/Menus/kstar5.png")
      if (persistent.i_menu > 2):
        ui.frame(xpos=663*config.screen_width/1200,ypos=87*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar5.png", 38*config.screen_width/1200, 38*config.screen_height/675, bilinear=True),"images/Menus/kstar5.png")
      if (persistent.nl_menu > 2):
        ui.frame(xpos=638*config.screen_width/1200,ypos=22*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar6.png", 17*config.screen_width/1200, 17*config.screen_height/675, bilinear=True),"images/Menus/kstar6.png")
      if (persistent.nh_menu > 2):
        ui.frame(xpos=647*config.screen_width/1200,ypos=13*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar6.png", 17*config.screen_width/1200, 17*config.screen_height/675, bilinear=True),"images/Menus/kstar6.png")
      if (persistent.am_menu > 2):
        ui.frame(xpos=752*config.screen_width/1200,ypos=103*config.screen_height/675, xanchor='center', yanchor='center', xpadding=0, ypadding=0, background=None)
        ui.imagebutton(im.Scale("images/Menus/kstar4.png", 27*config.screen_width/1200, 27*config.screen_height/675, bilinear=True),"images/Menus/kstar4.png")

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign .89
        yalign .51


        has vbox
        textbutton _("NEW GAME") action Start()
        # textbutton _("RESUME") action Start("start0")
        # textbutton _("RESUME") action ShowMenu("resume")
        textbutton _("LOAD GAME") action ShowMenu("load")
        textbutton _("SETTINGS") action ShowMenu("preferences")
        textbutton _("EXTRAS") action ShowMenu("extras")
        # textbutton _("SETUI") action Jump("reset_ui")
        # textbutton _("HELP") action Help()
        textbutton _("QUIT") action Quit(confirm=False)



init -2 python:

    # Make all the main menu buttons be the same size.

    style.mm_button.size_group = "mm"
    style.mm_button_text.font = "ui/Fonts/GillSans-LightTrebufied.otf"
    style.mm_button_text.size = 40
    style.mm_button_text.xalign = 0.0
    style.mm_button_text.line_spacing = 23
    style.mm_button_text.color = "#ccccccff"
    style.mm_button_text.hover_color = "#ffffffff"
    style.mm_button.idle_background = "/images/Buttons/idle_menubutton.png"
    style.mm_button.hover_background = LiveComposite(
        (250,50),
        (0,0), "/images/Buttons/idle_menubutton.png",
        (280,-9), "animatedstar"
        )

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"
        at appear

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .50
        yalign .83

        has vbox

        textbutton _("BACK") action Return()
##        textbutton _("Preferences") action ShowMenu("preferences")
##        textbutton _("Save Game") action ShowMenu("save")
##        textbutton _("Load Game") action ShowMenu("load")
##        textbutton _("Main Menu") action MainMenu()
##        textbutton _("Help") action Help()
##        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    style.gm_nav_button_text.font = "ui/Fonts/GillSans-LightTrebufied.otf"
    style.gm_nav_button_text.size = 30
    style.gm_nav_button_text.color = "#ccccff"
    style.gm_nav_button_text.hover_color = "#ffffff"
    style.gm_nav_button.background = "/images/Buttons/idle_menubutton.png"



##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker_save:

    window:
        style "file_picker_save_root"
        at appear


    frame:
        style "file_picker_frame"
        xalign 0.5
        yalign 0.5
        has vbox
        hbox
        $ columns = 3
        $ rows = 3

        # Display a grid of file slots.

        grid columns rows:
            transpose False
            area (0, 0, 0.666, 0.5)
            style_group "file_picker"

            # Display nine file slots (3x3), numbered 1 - 9, 10-18, etc.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i) xpos 30 ypos 18

                    # Format the description, and add it as text.
                    $ description = "{size=+10}%s{/size}{size=+5}\n%s{/size}" % (
                        FileSlotName(i, columns * rows, format="%s%02d"),
                        FileTime(i, format="%d.%m.%Y\n%H.%M", empty=_("Empty")))

                    text description xpos 45 ypos 10

                    key "save_delete" action FileDelete(i)

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            xalign 1.0
            yalign 0.5
            imagebutton idle "images/Menus/save-load/small_left_arrow_30.png" hover "images/Menus/save-load/small_left_arrow_100.png" action FilePagePrevious(max=11,wrap=True)

##            textbutton _("Auto"):
##                action FilePage("auto")

##            textbutton _("Quick"):
##                action FilePage("quick")

            for i in range(1, 12):
                textbutton str(i):
                    action FilePage(i)

            imagebutton idle "images/Menus/save-load/small_right_arrow_30.png" hover "images/Menus/save-load/small_right_arrow_100.png" action FilePageNext(max=11,wrap=True)


screen file_picker_load:

    window:
        style "file_picker_load_root"
        at appear

    frame:
        style "file_picker_frame"
        xalign 0.5
        yalign 0.5
        has vbox
        hbox
        $ columns = 3
        $ rows = 3

        # Display a grid of file slots.

        grid columns rows:
            transpose False
            area (0, 0, 0.666, 0.5)
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i) xpos 30 ypos 18

                    # Format the description, and add it as text.
                    $ description = "{size=+10}%s{/size}{size=+5}\n%s{/size}" % (
                        FileSlotName(i, columns * rows, format="%s%02d"),
                        FileTime(i, format="%d.%m.%Y\n%H.%M", empty=_("Empty")))

                    text description xpos 45 ypos 10

                    key "save_delete" action FileDelete(i)

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"
            xalign 1.0
            yalign 0.5
            imagebutton idle "images/Menus/save-load/small_left_arrow_30.png" hover "images/Menus/save-load/small_left_arrow_100.png" action FilePagePrevious(max=11,wrap=True)

##            textbutton _("Auto"):
##               action FilePage("auto")

##            textbutton _("Quick"):
##                action FilePage("quick")

            for i in range(1, 12):
                textbutton str(i):
                    action FilePage(i)

            imagebutton idle "images/Menus/save-load/small_right_arrow_30.png" hover "images/Menus/save-load/small_right_arrow_100.png" action FilePageNext(max=11,wrap=True)

screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker_save

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker_load

init -2 python:
    style.file_picker_load_root.background = "images/Menus/save-load/load_background.png"
    style.file_picker_save_root.background = "images/Menus/save-load/save_background.png"

    style.file_picker_nav_button_text.font = "ui/Fonts/GillSans-LightTrebufied.otf"
    style.file_picker_nav_button_text.size = 18
    style.file_picker_nav_button_text.hover_color = "#ffffff"
    style.file_picker_nav_button_text.idle_color = "#2e89ff80"
    style.file_picker_nav_button_text.insensitive_color = "#ffffff26"
    style.file_picker_nav_button_text.selected_idle_color = "#2e89ff"

    style.file_picker_nav_button.background = "#00000000"


    style.file_picker_button.idle_background = "images/Menus/save-load/save_frame_30.png"
    style.file_picker_button.hover_background = "images/Menus/save-load/save_frame_100.png"
    style.file_picker_button.insensitive_background = "images/Menus/save-load/save_frame_00.png"
    style.file_picker_text = Style(style.large_button_text)



##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:


    tag menu


    # Include the navigation.
    use navigation

    window:
        style "pref_root"
        at appear

    # Put the navigation columns in a three-wide grid.
    grid 5 1:
        style_group "prefs"
        xfill True
        xalign 0.0 xpos 0.0
        yalign 0.0 ypos 0.25
        spacing 50
        # The left column.

        vbox:
            frame:
                style_group "pref"
                has vbox

        vbox:
            frame:
                style_group "pref"
                has vbox
                label _("Display"):
                    xpos -0.12
                textbutton _("Window") action Preference("display", "any window"):
                    text_align 0.0
                textbutton _("Fullscreen") action Preference("display", "fullscreen"):
                    text_align 0.0

            frame:
                style_group "pref"
                has vbox

                label _("Transitions"):
                    xpos -0.12
                textbutton _("All") action Preference("transitions", "all"):
                    text_align 0.0
                textbutton _("None") action Preference("transitions", "none"):
                    text_align 0.0

            frame:
                style_group "pref"
                has vbox

                label _("Mature Content"):
                    xpos -0.12
                textbutton _("Enabled") action SetField(persistent, "mature", True):
                    text_align 0.0
                textbutton _("Disabled") action SetField(persistent, "mature", False):
                    text_align 0.0


##            frame:
##                style_group "pref"
##                has vbox
##
##                textbutton _("Joystick...") action Preference("joystick")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip"):
                    xpos -0.12
                textbutton _("Seen Messages") action Preference("skip", "seen"):
                    text_align 0.0
                textbutton _("All Messages") action Preference("skip", "all"):
                    text_align 0.0

##            frame:
##                style_group "pref"
##                has vbox
##
##                textbutton _("Begin Skipping") action Skip()
##
            frame:
                style_group "pref"
                has vbox

                label _("After Choices"):
                    xpos -0.12
                textbutton _("Stop Skipping") action Preference("after choices", "stop"):
                    text_align 0.0
                textbutton _("Keep Skipping") action Preference("after choices", "skip"):
                    text_align 0.0


        vbox:
            frame:
                style_group "pref"
                has vbox
                spacing 20
                label _("Text Speed") xpos -0.15
                bar value Preference("text speed")


            frame:
                style_group "pref"
                has vbox
                spacing 20
                label _("Auto-Forward Time") xpos -0.15
                bar value Preference("auto-forward time")

            frame:
                style_group "pref"
                has vbox
                spacing 20
                label _("Music Volume") xpos -0.15
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox
                spacing 20
                label _("Sound Volume") xpos -0.15
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton "Test":
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            frame:
                style_group "pref"
                has vbox
                spacing 20
                label _("")
                if _preferences.mute["music"]:
                    textbutton _("Unmute"):
                        action Preference("all mute", "disable")
                        xpos 0.3
                        ypos -1.9
                else:
                    textbutton _("Mute"):
                        action Preference("all mute", "enable")
                        xpos 0.35
                        ypos -1.9

        vbox:
            frame:
                style_group "pref"
                has vbox
##
##                label _("Voice Volume")
##                bar value Preference("voice volume")
##
##                if config.sample_voice:
##                    textbutton "Test":
##                        action Play("voice", config.sample_voice)
##                        style "soundtest_button"


init -2 python:
    style.pref_root.background = Frame("images/Menus/preferencesmenu/settings_background.png", left=0, top=0, right=None, bottom=None, tile=False)


    style.pref_frame.xfill = False
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xanchor = 0.0
    style.pref_button.xalign = 0.0
    style.pref_button_text.font = "ui/Fonts/GillSans-LightTrebufied.otf"
    style.pref_button_text.size = 30
    style.pref_button_text.xalign = 0.0
    style.pref_button_text.hover_color = "#2e89ff"
    style.pref_button_text.idle_color = "#2e89ff80"
    style.pref_button_text.insensitive_color = "#ffffff26"
    style.pref_button_text.selected_idle_color = "#2e89ffff"
    style.pref_label_text.size = 36

    style.pref_button.background = "/images/Buttons/idle_menubutton.png"
    style.pref_button.selected_background = LiveComposite(
        (300,50),
        (80,0), "/images/Buttons/idle_menubutton.png",
        (-40,12), "images/Menus/preferencesmenu/blue_arrow.png"
        )
    style.pref_slider.xmaximum = 340
    style.pref_slider.xminimum = 340
    style.pref_slider.xalign = 0.0
    style.pref_slider.yalign = 1.0
    style.pref_slider.left_bar = "gui/slider/bar_full.png"
    style.pref_slider.right_bar = "gui/slider/bar_empty.png"
    style.soundtest_button.xalign = 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "yesno_root"
        at appear

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .4
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 27

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 320

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


init -2 python:
    style.yesno_root.background = "images/Menus/yesnomenu/Confirmation_Background.png"
    style.yesno_button.size_group = "yesno"
    style.yesno_label_text.text_align = 0.5
    style.yesno_label_text.size = 36
    style.yesno_button_text.size = 36
    style.yesno_button.background = "/images/Buttons/idle_menubutton.png"
    style.yesno_button.hover_background = LiveComposite(
        (300,50),
        (80,0), "/images/Buttons/idle_menubutton.png",
        (-40,13), "images/Menus/preferencesmenu/blue_arrow.png"
        )

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu1:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.08
        yalign 0.975

##        textbutton _("Q.Save") action QuickSave()
##        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _(" Skip") action Skip()
        textbutton _(" Mute ") action Preference("all mute", "toggle")
        if persistent.show_girl_totals:
          if persistent.am_tot == 0:
            text ("{size=11}{color=#FF0000} Annaliese:[persistent.a_tot] Isolda:[persistent.i_tot] Jeanne:[persistent.j_tot] Lena:[persistent.l_tot] Katja:[persistent.k_tot] Twins:[persistent.nh_tot] {/color}{/size}")
          else:
            text ("{size=11}{color=#FF0000} Annaliese:[persistent.a_tot] Isolda:[persistent.i_tot] Jeanne:[persistent.j_tot] Lena:[persistent.l_tot] Katja:[persistent.k_tot] Twins:[persistent.nh_tot] Anne-Marie:[persistent.am_tot]{/color}{/size}")
        if persistent.show_scene_number:
            text ("{size=11}{color=#FF0000} [persistent.scene_number]{/color}{/size}")


screen quick_menu2:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.92
        yalign 0.975

##        textbutton _("Q.Save") action QuickSave()
##        textbutton _("Q.Load") action QuickLoad()
        textbutton _(" Log") action ShowMenu('log')
        textbutton _(" Save") action ShowMenu('save')
        textbutton _(" Load") action ShowMenu('load')
        textbutton _(" Prefs ") action ShowMenu('preferences')
        if persistent.show_girl_totals:
          if persistent.am_tot == 0:
            text ("{size=11}{color=#FF0000} Annaliese:[persistent.a_tot] Isolda:[persistent.i_tot] Jeanne:[persistent.j_tot] Lena:[persistent.l_tot] Katja:[persistent.k_tot] Twins:[persistent.nh_tot] {/color}{/size}")
          else:
            text ("{size=11}{color=#FF0000} Annaliese:[persistent.a_tot] Isolda:[persistent.i_tot] Jeanne:[persistent.j_tot] Lena:[persistent.l_tot] Katja:[persistent.k_tot] Twins:[persistent.nh_tot] Anne-Marie:[persistent.am_tot]{/color}{/size}")
        if persistent.show_scene_number:
            text ("{size=11}{color=#FF0000} [persistent.scene_number]{/color}{/size}")


init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 24
    style.quick_button_text.idle_color = "#2e89ff80"
    style.quick_button_text.hover_color = "#ffffffff"
    style.quick_button_text.selected_idle_color = "#2e89ff"
    style.quick_button_text.insensitive_color = "ffffff26"

    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False

label reset_all:
  $ persistent.virgin_first = True
  $ persistent.menu_ui = -4
  $ virgin_init_variables()  # Init "first time run" variables
  $ init_variables()         # Init "startup" variables
  jump main_menu_reset

label reset_ui:
  $ persistent.menu_ui = -4
  return False

label set_act:
    $ persistent.start_act = renpy.input("\nEnter scene to start at (example: A1_04a): ")
    jump main_menu_reset

label tog_menus:
    $ persistent.skip_menus = not persistent.skip_menus
    jump main_menu_reset

label set_girls:
    python:
      persistent.a_tot = None
      persistent.i_tot = None
      persistent.j_tot = None
      persistent.l_tot = None
      persistent.k_tot = None
      persistent.nh_tot = None
      persistent.nl_tot = None
      persistent.am_tot = None
      ints_list = []
      girllist = renpy.input("Enter a,i,j,l,k,nh,nl,am as e.g. 1,5,6,1,1,1,-1,5: ")
      if (len(girllist) > 0):
        ints_list = map(int, girllist.strip().split(','))
        if (len(ints_list) > 0):
          persistent.a_tot = ints_list[0]
        if (len(ints_list) > 1):
          persistent.i_tot = ints_list[1]
        if (len(ints_list) > 2):
          persistent.j_tot = ints_list[2]
        if (len(ints_list) > 3):
          persistent.l_tot = ints_list[3]
        if (len(ints_list) > 4):
          persistent.k_tot = ints_list[4]
        if (len(ints_list) > 5):
          persistent.nh_tot = ints_list[5]
        if (len(ints_list) > 6):
          persistent.nl_tot = ints_list[6]
        if (len(ints_list) > 7):
          persistent.am_tot = ints_list[7]

    jump main_menu_reset


label kev_ui2:
    $ persistent.menu_ui = -6
    return False

label tog_scene_number:
    $ persistent.show_scene_number = not persistent.show_scene_number
    $ renpy.call_in_new_context("main_menu")
    return False

label tog_girl_totals:
    $ persistent.show_girl_totals = not persistent.show_girl_totals
    $ renpy.call_in_new_context("main_menu")
    return False

label rez_800_450:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 800
    $ persistent.screen_height = 450
    $ renpy.set_physical_size((800,450))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_1280_720:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 1280
    $ persistent.screen_height = 720
    $ renpy.set_physical_size((1280,720))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_1600_900:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 1600
    $ persistent.screen_height = 900
    $ renpy.set_physical_size((1600,900))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_1920_1080:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 1920
    $ persistent.screen_height = 1080
    $ renpy.set_physical_size((1920,1080))
    $ renpy.call_in_new_context("_save_reload_game")
    return False

label rez_2560_1440:
    $ persistent.menu_ui = -4
    $ persistent.screen_width = 2560
    $ persistent.screen_height = 1440
    $ renpy.set_physical_size((2560,1440))
    $ renpy.call_in_new_context("_save_reload_game")
    return False
#####################################################
## changing confirmation messages
translate None strings:
    old "Are you sure you want to quit?"
    new "Are you sure that you want to quit the game? \n This will lose unsaved progress."


###################################################
## pause menu
screen game_menu:
    tag menu
    window:
        style "gamemenu_root"
        at appear

    # The main menu buttons.
    frame:
        style_group "gamemenu"
        xalign .90
        yalign .50


        has vbox
        spacing 10
        textbutton _("RETURN") action Return()
        textbutton _("LOG") action ShowMenu("log")
        textbutton _("SAVE GAME") action ShowMenu("save")
        textbutton _("LOAD GAME") action ShowMenu("load")
        textbutton _("SETTINGS") action ShowMenu("preferences")
        textbutton _("QUIT") action MainMenu()



init -2 python:

    style.gamemenu_root.background = "images/Menus/pausemenu/PauseMenu_Background.png"

    # Make all the main menu buttons be the same size.

    style.gamemenu_button.size_group = "gamemenu"
    style.gamemenu_button_text.font = "ui/Fonts/GillSans-LightTrebufied.otf"
    style.gamemenu_button_text.size = 40
    style.gamemenu_button_text.xalign = 0.0
    style.gamemenu_button_text.color = "#ccccccff"
    style.gamemenu_button_text.hover_color = "#ffffffff"
    style.gamemenu_button.idle_background = "/images/Buttons/idle_menubutton.png"
    style.gamemenu_button.hover_background = LiveComposite(
        (250,50),
        (0,0), "/images/Buttons/idle_menubutton.png",
        (265,-9), "animatedstar"
        )

