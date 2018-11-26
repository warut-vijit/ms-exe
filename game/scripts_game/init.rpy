

label __virgin_init_variables:
  python:
    # First-time init, or
    # reinit entire game if persistent.virgin_first == True
    if (persistent.virgin_first == None or persistent.virgin_first == True):
        # Reset start of game flag
        persistent.started = 0
        persistent.start_act = "A1_01"
        persistent.skip_menus = False
        # TEMP select UI and/or screen rez
        if (persistent.menu_ui != 6 and not (persistent.menu_ui < 0)):
          persistent.menu_ui = 0
          persistent.show_scene_number = False
          persistent.show_girl_totals = False
          persistent.screen_width = 0
          persistent.screen_height = 0
  return


label __init_variables:
  # Declare characters used by this game.
  python:
    ig_tot = 0
    jl_tot = 0
    lf_tot = 0
    kb_tot = 0
    ak_tot = 0
    nv_tot = 0
    ir_tot = 0
  return
