# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# init:
#     python:
#         renpy.load("questions.rpy")
#         renpy.load("questions_list.rpy") 

# Making Flags;
# default for the variable that will change and 
# define for the variable that will not change
default condition_1  = False
default condition_2 = False

define condition_3 = 1
default player_name = "Player"
# define current_question_idx = 0

# Defining Characters
default p = Character(player_name)
define a = Character("Alex", color="#9BABB8")
define s = Character("Summer", color="#5C8984")
define n = Character("Narrator", color="#5C8000")
# define av  = Character("Trivia Master", color = '#9BABB8')

# define g = Character("General M", color="#5C8000")
# define n = Character("Narrator", color="#5C8000")
# black  = "#0ffff"

# define the image you are going to use
transform exit1:
    "exit.jpeg"
    size(10,230)
    xoffset 190
    yoffset -100
    xpos 190
    ypos 300
    # xalign 0.5

image room:
    "room.png"
    size(1920,1080)
    zoom 1
image Alex_summer_go:
    "Alex_summer_go.png"
    size(1920,1080)
    zoom 1

image b_tempback:
    "bg tempback.jpg"
    size (1920,1080)
    zoom 1
image game_background:
    "game_background.jpg"
    size (1920,1080)
    zoom 1

image back2:
    "bg back2.jpg"
    zoom 0.2

image syl_normal:
    "sylvie green normal.png"
    yoffset -200
    xoffset -250
image logo:
    "images/CyberGrid.png"
    zoom 0.58
image Uvic:
    "images/Uvic_intro.png"
    zoom 0.58
image ECE:
    "splashScreen.png"
    zoom 0.5
image prologue:
    "PROLOGUE.png"
    zoom 1
image once:
    "once.jpg"
    zoom 2.1
    # size()
image cat:
    "cat.jpg"
    zoom 2
image angry_country:
    "angry_country.jpg"
    size(1920,1080)

image Uvic_peacock:
    "Uvic_peacock.jpg"
    # size(360,400)
    xoffset 0
    yoffset -100
    zoom 0.5
image pea:
    "pea.jpg"
    zoom 2.1
image black:
    "black.jpeg"
    zoom 2.1

image military_table:
    "military_table.jpg"
    zoom 2.1
image hacker_table:
    "hacker_table.jpg"
    zoom 2.1
image military_thumbsup:
    "military_thumbsup.jpg"
    zoom 2.1
image month:
    "month.png"
    zoom 2.1
image Alex_in_room_excited:
    "Alex_in_room_excited.jpg"
    zoom 2.2
image Alex_80:
    "Alex_80.jpg"
    zoom 2.1
image Alex_blush:
    "Alex_blush.jpg"
    zoom 2.1
image Alex_room:
    "Alex_room.jpg"
    zoom 2.1
image Alex_room_laptop:
    "Alex_room_laptop.jpg"
    zoom 2.1
image Alex_contract:
    "Alex_contract.jpg"
    zoom 2.1
image test_right:
    "test_right.png"
    size(1920,1080)
    zoom 1
image test_wrong:
    "test_wrong.png"
    size(1920,1080)
    zoom 1
image test_right_2:
    "test_right_2.png"
    size(1920,1080)
    zoom 1
image test_wrong_2:
    "test_wrong_2.png"
    size(1920,1080)
    zoom 1
image Alex_thinking_office:
    "Alex_thinking_office.jpg"
    zoom 2.15
image Alex_Summer_Handshake:
    "Alex_Summer_Handshake.jpg"
    zoom 2.16
image  Alex_hardworking:
    "Alex_hardworking.jpg"
    zoom 2.15
image  Alex_Vacation:
    "Alex_Vacation.jpg"
    zoom 2.15
image Alex_night_office:
    "Alex_night_office.jpg"
    zoom 2.15
image office:
    "office.jpg"
    zoom 2.15
image Alex_completed_shift:
    "Alex_completed_shift.jpg"
    zoom 2.15
image Alex_car:
    "Alex_car.jpg"
    zoom 2.15
image Alex_house:
    "Alex_house.jpg"
    zoom 2.15
image crown:
    "crown.jpg"
    size(1920,1080)
image inbox:
    "inboc.png"
    size(1920,1080)
    zoom 1.5
image phishing_email:
    "phishing_email.jpg"
    size(1920,1080)
image linkdin:
    "linkdin.png"
    size(1920,1080)
image Alex_looking_mail_happy:
    "Alex_looking_mail_happy.jpg"
    size(1920,1080)
image summer_concerned:
    "summer_concerned.jpg"
    size(1920,1080)
image summer_worried_alex:
    "summer_worried_alex.jpg"
    size(1920,1080)
image Alex_running:
    "Alex_running.jpg"
    size(1920,1080)
image summer_angry:
    "summer_angry.jpg"
    size(1920,1080)
image grid:
    "grid.jpg"
    size(1920,1080)
image end:
    "end.png"
    size(1920,1080)
    zoom 1
image Alex_graduate:
    "Alex_graduate.jpg"
    size(1920,1080)
image pre_end:
    "pre_end.png"
    size(1920,1080)
    # sdkfnidsugytftftyyfufuuffufufuyufyfuufyttyttryryy
image light_out:
    "light_out.jpg"
    size(1920,1080)
image light_on:
    "light_on.jpg"
    size(1920,1080)
image summer_meet:
    "summer_meet.jpg"
    size(1980, 1080)
image summer_entry:
    "summer_entry.jpg"
    size(1920,1080)
image companies:
    "companies.jpg"
    size(1920,1080)
image parliament:
    "parliament.jpg"
    size(1920,1080)
image player_summer_meet:
    "player_summer_meet.jpg"
    size(1920,1080)
image player_entry:
    "player_entry.jpg"
    size(1920,1080)
image summer_lead:
    "summer_lead.jpg"
    size(1920,1080)
image summer_alex_blank:
    "summer_alex_blank.jpg"
    size(1920,1080)
image summer_happy:
    "summer_happy.jpg"
    size(1920,1080)
image Knowledge_dustbin:
    "Knowledge_dustbin.png"
    size(1920, 1080)
image Knowledge_phishing:
    "knowledge_phishing.png"
    size(1920,1080)
image scene1:
    "scene1.png"
    size(1920,1080)
    zoom 1

# Defining a Splash Screen
label splashscreen:
    play sound "Logo.mp3" volume 1
    scene logo with Dissolve
    pause 2

    scene Uvic with dissolve
    pause 2

    scene ECE with dissolve
    pause 3
    stop sound
    # show "#fff000"
    return

# The game starts here

label start:
    scene b_tempback
    menu:
        
            n "Do you want to play the prologue? It will tell you about teh background of the story, hwoever its is a bit text heavy ?"
            "sure, why not":
                jump prologue
            "No, stories are boring, I just want to play...":
                jump prologue_skip

label prologue:
    play sound "tense.mp3"
    play sound "Alert.wav"
    scene prologue

# Add screen for Prologue  
    window hide
    scene prologue at center:
        yalign 1.0
        linear 4.0
    $ renpy.pause(4.0, hard=True)
    hide prologue
    stop sound

    scene once
    play music "Tense.mp3"
    n "Once Upon a time ..."
    play sound ["pewpew.mp3"] volume 0.65 fadeout 0.8
    queue sound ["pewpew.mp3"] volume 0.60 fadein 1
    n "In a world divided by two powerful enemies nations ..."
    stop sound
    hide once
    show angry_country
    n "Tensions were at an all time high. Valria sought to expand its dominion and gain control over Astoria ..."
    hide angry_country
    show cat
    # play sound ["meow.mp3"] volume 0.7 fadeout 1.0
    # queue sound ["meow.mp3"] volume 0.55 fadein 1.0
    # queue sound ["meow.mp3"] volume 0.80 fadein 1.0
    n "There cannot be two cat's in a ring, perhaps, meows ..."
    hide cat
    stop sound
    scene pea
    # play sound "peacock.mp3" volume 0.35
    # 
    n "Back in the mystical land of Valeria, it wanted to be the ultimate bully, strutting around like a mischievous peacock."
    hide pea
    hide Uvic_peacock
    stop sound
# 
    scene crown
    n "The sheer delight of envisioning itself as the ruler of the world, unleashing havoc upon poor Asteria!"
    scene military_table
    n "So they Came up with bold operation, Code named: \n                                     'Lunar Blackout' "
    scene hacker_table
    n "The plan involved launching a covert attack on a strategic souteast region of Astoria, Which housed a vital electricity supply network "
    scene military_thumbsup
    n "If successfull, this attack would lead to widespread Blackout and cripple the region's infrastructure "
    # stopping Tense.mp3
    stop music

#  add Screen Coincidently - A month Later...
    # scene black
    window hide
    play sound "Alert.wav"
    scene month at center:
        yalign 1.0
        linear 4.0
    $ renpy.pause(1.5, hard=True)
    stop sound
    hide month

    scene Alex_in_room_excited
    play sound ["<silence 0.6>","woohoo.mp3" ]
    a "Finallyyyy, I got a Co-op, I should celebrate (.. sighs in relief ..)"
    stop sound
    scene Alex_80
    play sound ["<silence 0.59>","male_sighs.mp3"]
    n " It was over  \"eighty\" failed applications that \"Alex\" had gotten an acceptance from Youpower.inc"
    stop sound
    scene Alex_room_laptop
    n " Alex was Excited, and wanted to share, \n... and share he did ... "
#  add linkdin image  ? or a social media image background
    window hide
    scene linkdin at center:
        yalign 1.0
        linear 4.0
    $ renpy.pause(8.0, hard=True)
    hide linkdin

    scene Alex_blush
    n "He posted on the social media page and loved the reaction of his other mates. \nAll the likes and heart's made him blush"
    scene b_tempback
label prologue_choice_1:
    menu:
            n "Is Alex right to do so ? Announcing his success, role and other critical information online ?"
            "yeah, what could go wrong":
                jump prologue_wrong_1
            "Nope, thats wrong...":
                jump prologue_right_1
    return

label prologue_wrong_1:
    # scene test_wrong
    window hide
    scene test_wrong:
        yalign 1.0
        linear 4.0
    $renpy.pause(10.0, hard = True)
    hide test_wrong
    jump continue_1
    return
label prologue_right_1:
    window hide
    scene test_right:
        yalign 1.0
        linear 4.0
    $renpy.pause(10.0, hard = True)
    hide test_right
    jump continue_1
    return
label continue_1:
    scene Alex_thinking_office
    a "(if only I can convert this job to a full-time role.)"
    scene office
    n "Alex meets Summer, his supervisor, for the first time he'll be in the office."
    scene Alex_Summer_Handshake
    s "Hey there, Alex... I hope you have a great time here. You can start working as soon as your onboarding is done."
    scene Alex_contract
    n "There was no information security module that Alex had to go through. It was just some documents he needed to sign."
    scene Alex_hardworking
    n "Works crazy hours, does everything by the book. There is seemingly no time that he slacks off."
    scene Alex_night_office
    n "Days pass by, and everyone is impressed by his efforts."
    #  scene Change
    window hide
    play sound ["<silence 0.35>","Alert.wav"]
    scene black at center:
        yalign 1.0
        linear 4.0
    $ renpy.pause(1.0, hard=True)
    stop sound
    hide black

    scene Alex_completed_shift
    a "Done for the day, just let me look into my office gmail... (there's hardly anything in there...)"
    scene inbox
    a "What's this..."
    scene phishing_email
    n "Alex opens the link."
    scene Alex_looking_mail_happy
    a "Wohooohooo, I knew my plan would work out. Finally, I get all the money I need."
#  fill Later
    scene black
    # play sound ["<silence 0.59>","tsck.mp3"]
    n "Oh boy, here we go... Alex starts dreaming of his new life..."
    stop sound
    play sound["<silence 0.2>","car.mp3"]
    scene Alex_car
    n "should I buy the car in red or blue ?..."
    stop sound
    play sound ["<silence 0.59>","doorbell.mp3"]
    scene Alex_house
    n "I might get that house that i wanted..."
    stop sound

    play sound ["<silence 0.59>","vacation.mp3"] 
    scene Alex_Vacation
    n "Europe bagpacking, a dream not so distant "
    stop sound
    a "Let me pack up and go home now. It's almost time... (should I thank Summer?)"
    jump prologue_choice_2
label prologue_choice_2:
    scene b_tempback
    menu:
        n "should Alex have click the link in the email... without verifying ? "
        "Yeah, he got to know about his full-time offer through this":

            jump prologue_wrong_2
        "Nope, thats wrong...":
            jump prologue_right_2
        
    return

label prologue_wrong_2:
    scene test_wrong_2
    window hide
    scene test_wrong_2:
        yalign 1.0
        linear 4.0
    $renpy.pause(10.0, hard = True)
    hide test_wrong_2    
    jump continue_2
    return
#  add phishing email
label prologue_right_2:
    show test_right_2
    window hide
    scene test_right_2:
        yalign 1.0
        linear 4.0
    $renpy.pause(10.0, hard = True)
    hide test_right_2
    jump continue_2
    return
label continue_2:
    scene Alex_thinking_office
    n "As Alex was in the predicament to go to Summer or not (to thank her)..."
    scene grid
    n "suddenly ... something weird started to happen to the electricity grid"
    scene Alex_graduate
    a "This was not taught to me in ECE 488."
    scene Alex_running
    n "Alex rushes to summer, to get all the help he needs.."
    scene Alex_80
    a "I hope they don't kick me out, it took me 80 applications to get this role."
    scene summer_concerned
    s "Hey, are you alright ?"
    scene summer_worried_alex
    a "I think you need to see this ..."
    scene black with dissolve

    scene light_out
    # add jugnu sounds....
    n " ... ... ... the grid's out "
    scene summer_angry with dissolve
    s "What did you do ? If this has anything to do with you ... I wont be recommending you for our full-time position ..."
    #  add screen here, summer in a meeting, concerned
    scene summer_meet
    n "As soon as Summer got to know of the story, she set out and incident response team ..."
    #  add screen here lightup on the island
    scene light_on
    n "with significant efforts the team is able to get the electricity back ... "
    #  add screen blank faces in office.... sumer and alex looking at each other.
    scene summer_alex_blank
    a "Sorrryyyyy"
    #  Add screen Blank, scene change 
    window hide
    scene black:
        yalign 1.0
        linear 4.0
    $renpy.pause(1.5, hard = True)
    hide black
    scene parliament
    n "the Asterian parliament was furious, and they wanted answers moreover a plan so that this never happens again."
    scene summer_lead
    n "They hired summer,  as she so gracefully handled the attack on the south - east region, a few months back"
    scene companies
    n "The govt has identified a few companies more probable of going under an attack" 
    scene summer_entry
    n "Summer was tasked to go into each company to shadow and observe their securtiy protcols"
    scene player_entry
    n "it is there where she meets you "
    jump prologue_skip
    return

label prologue_skip:
    scene player_summer_meet
    s "Hi i am Summer, I'll be overlooking you daily operations for sometime... I hope it'll be fun."
    $ player_name = renpy.input("Psst, introduce yourself, don't keep her waiting")
    $ p = player_name
    scene summer_happy
    p "I am [player_name], glad to meet you ..."
    scene scene1
    s "Mistakes happen, but it's what we learn from them that counts." 
    s"Time to inspect our organization's child branches, ensuring top-notch information security practices."
    s "Let's kick off with the first office. Ready to make a difference? Let's go!"
    scene Alex_summer_go
    p "Sure, Lets find how our firm is doing ..."
    jump Map
    return
################################################################################################################
transform custom: 
    size(1920, 1080)
    zoom 1
transform exit_game:
    size(150,100)
    zoom 1
    xpos 2400
    ypos 1000
init:
    $ hotspotclick = True

screen map_screen:
    imagemap:
        ground "images/Map/abc.png" at custom
        add "exit.jpeg" at exit_game
        hotspot (715, 217, 964, 435) action If(hotspotclick,[Jump('iot_start'),SetVariable('hotspotclick',False)])
        hotspot (1887, 340, 2193, 624) action If(hotspotclick,[Jump('Card_Game'),SetVariable('hotspotclick',False)])
        hotspot (202, 441, 567, 659)  action If(hotspotclick,[Jump('pre_desk'),SetVariable('hotspotclick',False)])
        hotspot (882, 750, 1204, 983) action If(hotspotclick,[Jump('dustbin'),SetVariable('hotspotclick',False)])
        hotspot (2102,1100,2647,1226) action If(hotspotclick,[Jump('end_game_label'),SetVariable('hotspotclick',False)])
        
label Map:
    $hotspotclick = True
    play sound "MainMusic.mp3"
    window hide
    show screen map_screen
    $renpy.pause()  
    stop sound
    return

################################################################################################################
################################################################################################################

init python:
    import random
    def corkGunTransform(t, st, at):
        global cork_gun_pos
        global cork_gun_size

        mousepos = renpy.get_mouse_pos()

        if mousepos[0] - cork_gun_size[0] / 2 <= config.screen_width - cork_gun_size[0] and mousepos[0] >= cork_gun_size[0] / 2:
            cork_gun_pos = (int(mousepos[0] - cork_gun_size[0] / 2), cork_gun_opos[1])

        t.xpos = cork_gun_pos[0]
        cork_gun_pos = (cork_gun_pos[0], cork_gun_opos[1] + int((mousepos[1] - config.screen_height / 2) / 7))

        t.ypos = cork_gun_pos[1]

        return 0

    def setupTargets():
        emails = ['images/Phishing1.png', 'images/NonPhishing1.png', 'images/Phishing2.png', 'images/NonPhishing2.png','images/Phishing3.png', 'images/NonPhishing3.png', 'images/Phishing4.png', 'images/NonPhishing4.png', 'images/Phishing5.png', 'images/NonPhishing5.png','images/Phishing6.png', 'images/NonPhishing6.png']
        target_start_x = 100
        target_row_1_y = 105
        target_row_2_y = 285
        target_row_3_y = 460
        target_spacing = 250
        target_down_time = (0.0, 1.0)
        target_up_time = 10.0


        current_column = 0
        for i in range(2):
            if i == 0:
                k = random.randint(0,11)
                path = emails[k]
                target_transform = Transform(child = path, zoom = target_row_1_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 1
                target_sprites[-1].down_time = random.uniform(target_down_time[0], target_down_time[1])
                target_sprites[-1].x = target_start_x + (target_sizes["top"][0] * i) + (target_spacing * i)
                target_sprites[-1].y = target_row_1_y
                target_sprites[-1].phishing = k%2

            elif i == 1:
                k = random.randint(0,11)
                path = emails[k]
                target_transform = Transform(child = path, zoom = target_row_1_zoom)
                target_sprites.append(target_SM.create(target_transform))
                target_sprites[-1].row = 1
                target_sprites[-1].down_time = random.uniform(target_down_time[0], target_down_time[1])
                target_sprites[-1].x = target_start_x + (target_sizes["top"][0] * i) + (target_spacing * i)
                target_sprites[-1].y = target_row_1_y
                target_sprites[-1].phishing = k%2
            
            target_sprites[-1].idle_animation_direction = "up"
            target_sprites[-1].current_frame = 5
            target_sprites[-1].animation_time = 0.0
            target_sprites[-1].hit = False
            target_sprites[-1].up_time = target_up_time


            

    def targetUpdate(st):
        for li, target in enumerate(target_sprites):
            if target.hit == True:
            #     k = random.randint(0,5)
            #     path = emails[k]
            #     if target.row == 1:
            #         target.animation_time = 0
            #         target.hit = False
            #         target.phishing = k%2
            #         t = Transform(child = path, zoom = target_row_1_zoom)
            #     #target.current_frame = 2
            #     target.set_child(t)
                if target.current_frame == 1:
                    i = Image("images/envelope.png")
                    if target.row == 1:
                        target.animation_time = 0
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 2
                    target.set_child(t)
                elif target.current_frame == 2:
                    i = Image("images/envelope.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 3
                    target.set_child(t)
                elif target.current_frame == 3 and target.animation_time >= 0.1:
                    i = Image("images/envelope.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 4
                    target.set_child(t)
                elif target.current_frame == 4 and target.animation_time >= 0.12:
                    i = Image("images/envelope.png")
                    if target.row == 1:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 2:
                        t = Transform(child = i, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = i, zoom = target_row_3_zoom)
                    target.current_frame = 5
                    target.set_child(t)
                elif target.current_frame == 5 and target.animation_time >= 0.13:
                    k = random.randint(0,11)
                    path = emails[k]
                    target.phishing = k%2
                    if target.row == 1:
                        t = Transform(child = path, zoom = target_row_1_zoom)
                    elif target.row == 2:
                        t = Transform(child = path, zoom = target_row_2_zoom)
                    elif target.row == 3:
                        t = Transform(child = path, zoom = target_row_3_zoom)
                    target.current_frame = 1
                    target.animation_time = 0
                    target.hit = False
                    target.set_child(t)
            else:
                if target.idle_animation_direction == "up":
                    if target.animation_time >= target.down_time:
                        if target.current_frame == 5:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 3
                            target.set_child(t)
                        elif target.current_frame == 3 and target.animation_time >= target.down_time + 0.1:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 2
                            target.set_child(t)
                        elif target.current_frame == 2 and target.animation_time >= target.down_time + 0.12:
                            k = random.randint(0,11)
                            path = emails[k]
                            target.phishing = k%2
                            if target.row == 1:
                                t = Transform(child = path, zoom = target_row_1_zoom)
                            elif target.row == 2:
                                t = Transform(child = path, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = path, zoom = target_row_3_zoom)
                            target.current_frame = 1
                            target.idle_animation_direction = "down"
                            target.animation_time = 0
                            target.set_child(t)
                elif target.idle_animation_direction == "down":
                    if target.animation_time >= target.up_time:
                        if target.current_frame == 1:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 2
                            target.set_child(t)
                        elif target.current_frame == 2:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 3
                            target.set_child(t)
                        elif target.current_frame == 3 and target.animation_time >= target.up_time + 0.1:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 4
                            target.set_child(t)
                        elif target.current_frame == 4 and target.animation_time >= target.up_time + 0.12:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 5
                            target.set_child(t)
                        elif target.current_frame == 5 and target.animation_time >= target.up_time + 0.13:
                            i = Image("images/envelope.png")
                            if target.row == 1:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 2:
                                t = Transform(child = i, zoom = target_row_2_zoom)
                            elif target.row == 3:
                                t = Transform(child = i, zoom = target_row_3_zoom)
                            target.current_frame = 5
                            target.idle_animation_direction = "up"
                            target.animation_time = 0
                            target.hit = False
                            target.set_child(t)

            target.animation_time += 0.01

        return 0

    def corkEvents(event, x, y, st):
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1 and y < config.screen_height - 140:
                cork_sprites.append(cork_SM.create(cork_transform))
                cork_sprites[-1].original_size = (110 / 2, 138 / 2)
                cork_sprites[-1].x = cork_gun_pos[0] + cork_sprites[-1].original_size[0]
                cork_sprites[-1].y = cork_gun_pos[1]
                cork_sprites[-1].original_pos = (cork_sprites[-1].x, cork_sprites[-1].y)
                cork_sprites[-1].zoom = 0.5
                cork_sprites[-1].move_to_pos = (cork_gun_pos[0], y)
                cork_SM.redraw(0)

    def corkUpdate(st):
        global score
        for cork in cork_sprites:
            if cork.y > cork.move_to_pos[1]:
                cork.y -= abs(cork.move_to_pos[1] - cork.original_pos[1]) / 15
                t = Transform(child = cork_image)
                cork.zoom -= 0.023
                cork.x += 1.2
                cork.original_size = (cork.original_size[0] * cork.zoom, cork.original_size[1] * cork.zoom)
                t.zoom = cork.zoom
                t.update()
                cork.set_child(t)
            else:
                for i, target in enumerate(target_sprites):
                    if target.row == 1:
                        if target.current_frame == 1 and target.x <= (cork.x - cork.original_size[0] / 2) <= (target.x + target_sizes["top"][0]) and target.y <= (cork.y - cork.original_size[1] / 2) <= (target.y + target_sizes["top"][1]) - 30:
                            target.hit = True
                            if target.phishing == 0:
                                score += 10
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) - 1:
                            cork.destroy()
                            cork_sprites.remove(cork)
                    elif target.row == 2:
                        if target.current_frame == 1 and target.x <= (cork.x - cork.original_size[0] / 2) <= (target.x + target_sizes["middle"][0]) and target.y <= (cork.y - cork.original_size[1] / 2) <= (target.y + target_sizes["middle"][1]):
                            target.hit = True
                            score += 10
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) - 1:
                            cork.destroy()
                            cork_sprites.remove(cork)
                    elif target.row == 3:
                        if target.current_frame == 1 and target.x <= (cork.x - cork.original_size[0] / 2) <= (target.x + target_sizes["bottom"][0]) and target.y <= (cork.y - cork.original_size[1] / 2) <= (target.y + target_sizes["bottom"][1]):
                            target.hit = True
                            score += 15
                            target_SM.redraw(0)
                            cork.destroy()
                            cork_sprites.remove(cork)
                            renpy.restart_interaction()
                            break
                        elif i == len(target_sprites) - 1:
                            cork.destroy()
                            cork_sprites.remove(cork)

        return 0

    def prepareShootingGallery():
        global countdown_time
        global score

        countdown_time = inital_countdown_time
        score = 0

        for target in target_sprites:
            target.hit = False
            target.idle_animation_direction = "up"
            target.animation_time = 0.0
            target.current_frame = 5
            path = Image('images/envelope.png')
            t = Transform(child = path, zoom = target_row_2_zoom)
            target.set_child(t)

transform extra_size:
    size (1920,1080)
    zoom 1

transform half_size:
    zoom 0.5

transform full_size:
    zoom 1


transform spotlights:
    zoom 0.5
    blend "add"
    alpha 0.5

screen scene_1:
    image 'images/game_background.jpg' at extra_size
    imagebutton idle Solid("#FFFFFF00") hover "images/scene-1-sg-button.png" align (0.7, 0.3) at half_size action Show("shooting_gallery")

screen shooting_gallery:
    on "show" action [Function(prepareShootingGallery), SetVariable("default_mouse", "targetgame"), SetVariable("shooting_gallery", True)]
    image "images/inbox_bg.png" at extra_size
    add target_SM
    add cork_gun_transform
    add cork_SM
    image "images/score-background.png" pos (10, 0) at half_size
    text "Score: [score]" color "#FFFFFF" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] size 25 pos(55, 40) anchor(0.0, 0.0)
    text "Time: {:.0f}".format(countdown_time) color "#FFFFFF" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] size 25 pos(210, 40) anchor(0.0, 0.0)

    timer 1.0 action If(countdown_time > 0, true = SetVariable("countdown_time", countdown_time - 1.0), false = Show("time_is_up")) repeat If(countdown_time > 0, true = True, false = False)

screen time_is_up:
    modal True

    frame:
        xfill True
        yalign 0.5
        background "#FFFFFF80"
        padding (15, 15)
        text "Time is up!" color "#000000" align(0.5, 0.5) size 40

    timer 3.0 action [Hide("time_is_up"), Show("final_score")]

screen final_score:
    zorder 2
    modal True

    frame:
        background "#000000BF"
        xfill True
        yfill True
        padding(0, 0)

        frame:
            align(0.5, 0.5)
            xysize(int(1485 / 2), int(912 / 2))
            background None
            padding(0, 0)
            image "images/final-score-background.png" align(0.5, 0.5) at half_size
            text "Your score: [score]" outlines [(absolute(1), "#00000050", absolute(1), absolute(1))] color "#FFBF5F" size 40 align(0.5, 0.5)
            imagebutton auto "images/play-again-button-%s.png" align(0.20, 0.7) action [Hide("final_score"), Hide("shooting_gallery"), Function(prepareShootingGallery), Show("shooting_gallery")] at half_size
            imagebutton auto "images/quit-button-%s.png" align(0.55, 0.7) action [Hide("final_score"), Hide("shooting_gallery"), Jump('Desktop_Knowledge'), SetVariable("default_mouse", None), SetVariable("shooting_gallery", False)] at half_size

define config.mouse = {}
define config.mouse["targetgame"] = [("images/target-pointer.png", 17, 10)]
define shooting_gallery = False

label pre_desk:
    play sound "MainMusic.mp3"
    $hotspotclick = False
    image phishhing_before_scene:
        "phishhing_before_scene.jpeg"
        size(1920,1080)
        zoom 1
    screen predesk:
        frame:
            add "phishhing_before_scene.jpeg"
    show screen predesk
    s "Alright, it's time to put your phishing knowledge to the test! "
    s "Let's see how well you can defend against those sneaky phishing emails."
    p "I'm ready to show off my skills! "
    p "Bring on the challenge and let's keep those phishers at bay! "
    $renpy.pause()
    hide screen predesk
    jump Desktop
    return
label Desktop:
    $hotspotclick = False
    # Corkgun variables
    $cork_gun_image = Image("images/cork-gun.png")
    $cork_gun_size = (int(330 / 2), int(384 / 2))
    $cork_gun_pos = (0, 0)
    $cork_gun_opos = (int((config.screen_width / 2) - (cork_gun_size[0] / 2)), config.screen_height - cork_gun_size[1] + 60)
    $cork_gun_transform = Transform(child = cork_gun_image, zoom = 0.5, pos = (cork_gun_opos[0], cork_gun_opos[1]), function = corkGunTransform)
    $cork_image = Image("images/cork.png")
    $cork_transform = Transform(child = cork_image, zoom = 0.5)
    $cork_sprites = []
    $cork_SM = SpriteManager(update = corkUpdate, event = corkEvents)

    # Target variables
    $target_SM = SpriteManager(update = targetUpdate)
    $target_row_1_zoom = 1
    $target_row_2_zoom = 1
    $target_row_3_zoom = 1
    $target_sizes = {"top" : (750 * target_row_1_zoom, 500 * target_row_1_zoom), "middle" : (376 * target_row_2_zoom, 455 * target_row_2_zoom), "bottom" : (376 * target_row_3_zoom, 455 * target_row_3_zoom)}
    $target_sprites = []
    $setupTargets()
    #Emails list
    $emails = ['images/Phishing1.png', 'images/NonPhishing1.png', 'images/Phishing2.png', 'images/NonPhishing2.png','images/Phishing3.png', 'images/NonPhishing3.png', 'images/Phishing4.png', 'images/NonPhishing4.png', 'images/Phishing5.png', 'images/NonPhishing5.png','images/Phishing6.png', 'images/NonPhishing6.png']

    # Other variables
    $score = 0
    $inital_countdown_time = 60
    $countdown_time = inital_countdown_time
    call screen scene_1
    s "..."
    jump Desktop_Knowledge
    return


label Desktop_Knowledge:
    hide screen scene_1
    # screen summer_screen:
    #     frame:
    #         xalign 0.5
    #         yalign 0.5
    #         add "summer_happy.jpg"

    # show summer_screen
    # $renpy.pause()
    # s "I hope you upskilled yourself, and won't fall for any more phishing emails."
    # s "But still know this..."

    screen Desktop_tip:
        frame:
            # Define the layout and style of the screen
            xalign 0.5
            yalign 0.5
            add "Knowledge_phishing.png"  # Assuming "Knowledge_phishing" is the image name

    show screen Desktop_tip
    $ renpy.pause()
    # hide summer screen
    hide screen Desktop_tip
    stop sound
    jump Map
    return




################################################################################################################
################################################################################################################
#################################################################################################################


init python:
    def setup_puzzle():
        # Setup the puzzle by placing each piece of the puzzle in a random location to the right of the screen.
        # We do that by setting a start and end coordinate that we can pick random values from.
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            rand_rot = renpy.random.choice((0, 90, 180, 270))
            initial_piece_coordinates.append(rand_loc) # Add the random locations to a list so we can use them to place each piece.
            initial_piece_rotations.append(rand_rot) # Add the random rotations to a list so we can use them to rotate each piece.

    def rotate_piece(piece):
        if initial_piece_rotations[piece] == 270:
            initial_piece_rotations[piece] = 0
        else:
            initial_piece_rotations[piece] += 90

    def piece_drop(dropped_on, dragged_piece):
        # Function that runs when a piece has been dropped.
        # Below, we check if the dragged piece is dropped on a droppable piece of the same kind and snap it to its location.
        global finished_pieces

        if dragged_piece[0].drag_name == dropped_on.drag_name and dragged_piece[0].child.rotate == 0:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y) # Snap the piece to the dropped location.
            dragged_piece[0].draggable = False # Dropped piece in the correct place should no longer be able to be dragged.
            finished_pieces += 1

            if finished_pieces == page_pieces:
                # All pieces have been placed. We continue with the normal flow of the visual novel.
                renpy.jump("reassemble_complete")



screen reassemble_puzzle:
    # scene b_tempback
    frame:
        background "puzzle-frame.png"
        xysize full_page_size
        anchor(0.5, 0.5)
        pos(650, 535)

    draggroup:
        # Group of draggable pieces, and the spots they can be dragged to.
        # Paper pieces
        for i in range(page_pieces):
            drag:
                drag_name i
                drag_raise True
                anchor(0.5, 0.5)
                pos initial_piece_coordinates[i]
                focus_mask True
                alternate Function(rotate_piece, i)
                image "Pieces/piece-%s.png" % (i + 1) rotate initial_piece_rotations[i] rotate_pad False anchor(0.5, 0.5)

        # Snappable spots to drag to.
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "Pieces/piece-%s.png" % (i + 1) alpha 0.0 # Have the alpha at a higher value when first placing the pieces to make sure it looks correct.

default page_pieces = 12 # Amount of pieces for this puzzle.
default draggable_pieces = []
default full_page_size = (711, 996)
default piece_coordinates = [(451, 149), (719, 139), (868, 238), (421, 399), (658, 318), (700, 488), (796, 538), (453, 718), (776, 773), (464, 925), (743, 958), (921, 888)] # The correct coordinates for each piece.
default initial_piece_coordinates = [] # Will be filled with random initial locations of the pieces.
default initial_piece_rotations = [] # Will be filled with random initial rotation of the pieces.
default finished_pieces = 0 # Keeps track of the amount of pieces that have been placed correctly.

transform fill:
    size (1920,1080)

    
label dustbin:
    play sound "MainMusic.mp3"
    $hotspotclick = False
    screen paper:
        frame:
            add "paper.jpeg" at fill
    
    show screen paper

    $setup_puzzle()
    call screen reassemble_puzzle
    # jump Map
    
    jump dustbin_Knowledge
    return

label reassemble_complete:
    screen room:
        frame:
            add "room.png" zoom 1

    show screen room

    s "I did it!"
    s "Now let's see what it says ... it seems the information is important ... "
    jump dustbin_Knowledge
    # jump Map
    return

label dustbin_Knowledge:
    screen dust_tip:
        frame:
            # Define the layout and style of the screen
            xalign 0.5
            yalign 0.5
            add "Knowledge_dustbin.png"  # Assuming "Knowledge_phishing" is the image name

    show screen dust_tip
    $ renpy.pause()
    # hide summer screen
    hide screen dust_tip
    hide screen room
    hide screen paper
    stop sound
    jump Map
    return
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################



init python:
    def randomize_cards():
        # Function to create cards.
        global cards
        cards = []

        for i in range(int(card_amount)):
            # Fill the cards list with 2 cards (a pair) in each iteration of the loop.
            # The loop iterates card_amount / card_rows times to create the resulting amount of cards.
            # This creates a a nested list that looks like this example: cards = [["card-5", "deselected", "visible"], ["card-2", "deselected", "visible"] ...]
            # 1: name of the card, 2: if the card is selected or deselected, 3: if the card is visible or invisible.
            cards.append(["card-%s" % (i+1), "deselected", "visible", i+1])
            #cards.append(["card-%s" % rand_card_num, "deselected", "visible"])
        # Shuffle the filled list so that each card ends up in a random location instead of right next to each other.
        renpy.random.shuffle(cards)

    def select_card(card_index):
        # Function to select a card that was clicked on.
        global selected_cards
        global match_found

        # Select the card the user clicked on.
        cards[card_index][1] = "selected"
        selected_cards.append(card_index)

        if len(selected_cards) == 2:
            if (cards[selected_cards[0]][3] == (cards[selected_cards[1]][3]+1)) and cards[selected_cards[0]][3] % 2 == 0:
                    # Two matching pairs of cards has been selected.
                    match_found = True
            if (cards[selected_cards[1]][3] == (cards[selected_cards[0]][3]+1)) and cards[selected_cards[1]][3] % 2 == 0:
                    # Two matching pairs of cards has been selected.
                    match_found = True

    def deselect_cards():
        # Function to deselect cards after 2 have been selected that doesn't match.
        global selected_cards

        if len(selected_cards) == 2:
            for card in cards:
                if card[1] == "selected":
                    card[1] = "deselected"
        selected_cards = []

    def hide_matches():
        # Function to hide matching cards.
        global selected_cards
        global match_found
        global hidden_cards

        cards[selected_cards[0]][2] = "hidden" # First card
        cards[selected_cards[1]][2] = "hidden" # Second card
        hidden_cards += 2
        deselect_cards()
        match_found = False

    def reset_memory_game():
        # Function to reset mini-game.
        global match_found
        global hidden_cards

        match_found = False
        hidden_cards = 0
        randomize_cards() # create new cards

transform card_fadein:
    alpha 0.0
    easein 0.5 alpha 1.0

screen memory_mini_game:
    image "card_background.png" zoom 1
    grid int(card_amount / card_rows) card_rows:
        align(0.9, 0.5)
        spacing 5
        for i, card in enumerate(cards):
            if card[1] == "deselected" and card[2] == "visible":
                # This card isn't selected, and it hasn't been matched to another card yet, so we show the back of the card.
                # We set it to be sensitive/clickable only if the player hasn't clicked on 2 cards yet. This is to prevent the player from clicking more cards while they wait for the result.
                imagebutton idle "card-back.png" sensitive If(len(selected_cards) != 2, True, False) action Function(select_card, card_index = i) at card_fadein
            elif card[1] == "selected" and card[2] == "visible":
                # This card has been selected and it's visible, so we flip it to show its image.
                image "%s.png" % card[0] at card_fadein
            else:
                # This card is hidden because it was matched with another card.
                # We use a "null" displayable here to emulate an emptpy space due to that we're using a grid. If not, the cards that comes after will shift to fill the empty gap.
                null

    # If there's a matching pair visible on the screen, we want to make them invisible. If there are two non-matching cards instead, we flip them over again.
    # We do this with timers to make sure the player has time to observe the cards to see what they are.
    if match_found:
        timer 1.0 action Function(hide_matches) repeat True # Hides the cards 1.0 second after a match has been found.
    elif len(selected_cards) == 2:
        timer 1.0 action Function(deselect_cards) repeat True # Flips the cards back over 1.0 second after no match was found.
    elif hidden_cards == card_amount:
        # All cards have been matched. We reset the game after 0.5 seconds so the player can play again after the game finished.
        timer 1 action Jump('Knowledge_card_game') repeat False


default card_amount = 12 # The amount of cards you want to show.
default card_rows = 3 # How many rows these cards should be placed on.
default cards = [] # Holds the name of the cards and their properties.
default selected_cards = [] # Holds the index positions of the cards selected in the cards list.
default hidden_cards = 0 # Amount of cards that have been hidden from matches.
default match_found = False # If a match has been found.

label Card_Game:
    play music "MainMusic.mpeg"
    $ hotspotclick = False
    $randomize_cards() # Create cards.

    screen cardGame:
        frame:
            add "Alex_summer_go.png" size(1920,1080)

    show screen cardGame
    $renpy.pause()

    s "Alright, Player, buckle up for a thrilling ride through the world of information security."
    s"We're about to embark on a flip card adventure like no other. "
    s "Get ready to show off your cyber-savvy skills!"
    p "Summer, you never fail to amaze me with your crazy ideas!"
    p "I'm all in for this wild ride. "
    p "Let's flip those cards and prove that I've got the brains and the bytes to conquer any digital challenge!"
    hide screen cardGame

    call screen memory_mini_game

    jump Knowledge_card_game
    return

label Knowledge_card_game:
    screen card_tip_1:
        frame:
            # Define the layout and style of the screen
            xalign 0.5
            yalign 0.5
            add "Knowledge_cards_1.png"  # Assuming "Knowledge_phishing" is the image name
    screen card_tip_2:
        frame:
            # Define the layout and style of the screen
            xalign 0.5
            yalign 0.5
            add "Knowledge_cards_2.png"  # Assuming "Knowledge_phishing
    screen card_tip_3:
        frame:
            # Define the layout and style of the screen
            xalign 0.5
            yalign 0.5
            add "Knowledge_cards_3.png"  # Assuming "Knowledge_phishing
    show screen card_tip_1
    $ renpy.pause()
    show screen card_tip_2
    $renpy.pause()
    show screen card_tip_3
    $renpy.pause()
    # hide summer screen
    hide screen card_tip_1
    hide screen card_tip_2
    hide screen card_tip_3
    stop music 
    jump Map
    return
#################################################################################################################
#################################################################################################################
#################################################################################################################
#################################################################################################################

# This file contains the script that runs the game. 

screen iot_game:
    add "images/backgrounds/bg.png" zoom 1.6
    # add '"bg tempback.jpg"' zoom 3
    

# The game starts here.
label iot_start:
    play sound "MainMusic.mp3"
    $hotspotclick = False
    # Initialize the setup. 
    call make_question_list from _call_make_question_list

    # scene background 
    
    show screen iot_game

    # Introduce the game. 
    av "Welcome to trivia!"
    av "Pick the answer choice you think is correct."
    av "After you've made your choice, the correct answer will come up."
    av "Try to score as many points as possible!"
    av "Good luck!"
    jump begin_game


# Show the current question. 
label begin_game:
    # Initializing setup on each turn for testing purposes.
    # Can be commented out in the final game. 
    call make_question_list from _call_make_question_list_1

    # call make_question_list from  question_list.rpy
    # If the player has run out of questions, end the game. 
    if current_question_idx >= len(question_list):
        jump finished

    # Otherwise, get the next question. 
    $ current_question = question_list[current_question_idx]

    # Introduce the question. 
    # Note that Python indexing starts at 0, which is why we need to add 1. 
    $ adjusted_idx = current_question_idx + 1
    av "Here's question [adjusted_idx]."

    # ------------------------
    style new_style:
        font 'gui/fonts/family.otf'
        size 56
        color "#FF0000"
        xalign 0.5
        yalign 0.5
        xpos 1000
        ypos 70

    style explain_style:
        font 'gui/fonts/family.otf'
        size 62
        color "#F28123"
        xalign 0.5
        yalign 0.5
        xpos 1000
        ypos 400

    

    style answer_style:
        font 'gui/fonts/family.otf'
        size 52
        color "#B22222"
        xalign 0.5
        yalign 0.5
        xpos 1000
        ypos 700

    screen question_text_screen:
        vbox:
            text "[current_question.question]" style "new_style"

    show screen question_text_screen
    pause



    # ------------------------
    # Show the text for the current question. 
    # show text [current_question.question] at slide_up_center
    # pause 5
    play sound pop


# Show a menu displaying all four answer choices. 
menu:
    "[current_question.a1]":
        $ player_response = current_question.a1
        call start_after from _call_start_after

    "[current_question.a2]":
        $ player_response = current_question.a2
        call start_after from _call_start_after_1

    "[current_question.a3]":
        $ player_response = current_question.a3
        call start_after from _call_start_after_2

    "[current_question.a4]":
        $ player_response = current_question.a4
        call start_after from _call_start_after_3


# Process the player's response. 
label start_after:

    # Hide the question and show the correct response. 
    
    screen question_text_screen:
        vbox:
            text "[current_question.question]" style "new_style"

    show screen question_text_screen
    pause

    # show text [current_question.question] at flip
    # pause 0.5
    hide text [current_question.question]

    screen explain:
        vbox:
            text "[current_question.explain]" style "explain_style"

    show screen explain
    $renpy.pause()
    hide screen explain
    # show text [current_question.explain] at unflip

    # If the player responds correctly:
    if (player_response == current_question.correct):
        play sound ding
        pause
        av "You got it right! Great job!"
        $ score += current_question.point_value

    # If the player responds incorrectly:
    else:
        play sound dizzy
        pause
        av "Wrong Answer!!! Correct Answer: [current_question.correct]"

    # Display the current score and start again. 
    av "Your current score is [score]."

    # Increment the question counter. 
    $ current_question_idx += 1

    # Hide the current correct answer. 
    # screen answer:
    #     vbox:
    #         text "[current_question.correct]" style "answer_style"

    # show screen answer
    pause 1
    hide screen answer
    # show text [current_question.correct] at flip
    # pause 0.5
    hide text [current_question.correct]
    hide explain
    jump begin_game


# Finish the game.
label finished:
    av "Congratulations! Your final score is [score]."
    hide screen question_text_screen
    hide screen answer
    hide screen explain
    jump iot_end
    stop sound
    call Map
    return


label iot_end:

    # Hide the dialogue window.
    window hide
    # Direct the player back to the main menu. 
    hide screen iot_game
    jump Map
    return


label end_game_label:
    $hotspotclick =  False
    screen end_game:
        frame:
            add "end.png"
    
    show screen end_game
    $renpy.pause()
    hide screen end_game
    return

    # new