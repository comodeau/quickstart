#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login='',
    password='_',
    like_per_day=900,
    comments_per_day=200,
	tag_list=['l:217631504', 'l:805198877', 'l:234973050', 'l:373987404', 'l:214526970', 'l:1022193652', 'l:370193368', 'l:468037926693284', 'l:35393075', 'l:15781077', 
			  'l:222840553', 'l:216998807', 'l:1201230466639413', 'l:5252788', 'l:135149523949116', 'l:124010504708328', 'l:252376476', 'l:241329752', 'l:402040693527159', 'l:689801919', 'l:406406904', 
			  'l:213252870', 'l:366880595954', 'l:821110451', 'l:630181765', 'l:317991074', 'l:214535316', 'l:366180639', 'l:654746022', 'l:689120548', 'l:c1403046', 
			  'l:c1406768', 'l:250613772', 'l:1022850146', 'l:360198622', 'l:1179433845424407', 'l:269370428', 'l:238353930', 'l:248984193', 'l:526671585', 'l:894006484', 'l:361667448', 
			  'l:234290506', 'l:1034413446', 'l:571484234', 'l:731446490', 'l:c1402344', 'l:238170694', 'l:32855920', 'l:1030081905', 'l:401414433', 'l:218729485', 'l:215992534',
			  'l:c1397756', 'l:220729814', 'l:2519049', 'l:659924363', 'l:548278678', 'l:584843811684773', 'l:238249427', 'l:537183575', 'l:277076546', 'l:552610343', 'l:267609199',
			  'l:254133892', 'l:1031607243', 'l:353266021', 'l:975946665', 'l:370299120', 'l:270018398', 'l:587075819', 'l:314179418', 'l:861554575', 'l:260631774', 'l:236406791',
			  'l:272315651', 'l:761918685', 'l:250485112', 'l:1019412355', 'l:569816968', 'l:273756442', 'l:65469392', 'l:1024567963', 'l:1015708074', 'l:1033416457', 'l:14878145',
			  'l:438643851', 'l:228648650', 'l:257836521', 'l:1090200107709237', 'l:317991074', 'l:1887773974796970', 'l:213388941', 'l:34351812', 'l:503472027', 'l:', 'l:',
			  'l:252350051', 'l:266172054'], 
	tag_blacklist=['sex', 'gay', 'lesb', 'porn', 'fuck'],
    user_blacklist={},
    follow_per_day=400,
    follow_time=24 * 60 * 60,
    unfollow_per_day=440,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    # List of list of words, each of which will be used to generate comment
    # For example: "This shot feels wow!"
    comment_list=["great", "super", "good", "very good", "good", "wow",
                   "WOW", "cool", "GREAT","magnificent", "magical",
                   "very cool", "stylish", "beautiful", "so beautiful",
                   "so stylish", "so professional", "lovely",
                   "so lovely", "very lovely", "glorious","so glorious",
                   "very glorious", "adorable", "excellent", "amazing"],
    # Use unwanted_username_list to block usernames containing a string
    ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
    ### 'free_followers' will be blocked because it contains 'free'
    unwanted_username_list=[
        'sex', 'gay', 'lesb', 'porn', 'fuck'],
    unfollow_whitelist=['example_user_1', 'example_user_2'])
while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
