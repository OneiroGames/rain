########################################################
###       Copyright (c) 2019-2022 ONEIRO GAMES       ###
###                 Version: 1.0.0                   ###
###             Description: RAIN MAIN               ###
########################################################

label oneiro_rain:
    scene black with dissolve
    window hide dissolve
    $ renpy.pause(2)
    show text "{size=+10}У каждой истории есть начало и конец.{/size}" at truecenter with dissolve2
    $ renpy.pause(2)
    hide text with dissolve2

    $ renpy.pause(1)
    show text "{size=+10}У каждой истории есть своя канва, синопсис, содержание, ключевые моменты, прологи и эпилоги.{/size}" at truecenter with dissolve2
    $ renpy.pause(2.5)
    hide text with dissolve2

    $ renpy.pause(1)
    show text "{size=+10}И нет такой книги, в которой при каждом новом прочтении не открывались бы вещи,\n на которые раньше не обращал внимания.{/size}" at truecenter with dissolve2
    $ renpy.pause(3.5)
    hide text with dissolve2

    $ renpy.pause(1)
    show text "{size=+10}У каждой истории есть начало и конец. Почти у каждой...{/size}" at truecenter with dissolve2
    $ renpy.pause(2.7)
    hide text with dissolve2

    $ renpy.pause(3)

    play ambience "rain/sounds/ambience/rain2.mp3" fadein 3.5
    play music music_list["lets_be_friends"]
    $ sunset_time()
    $ persistent.sprite_time = 'sunset'

    scene bg ext_island_night with dissolve2
    show un normal pioneer close:
        zoom 1.3
    show rain
    with dspr
    play sound sfx_thunder_rumble fadein 5

    window show dissolve

    me "Дождь, прям как в тот день. Ты его помнишь?"
    "Капельки неба не спеша падали, омывая всё вокруг: траву, землю, деревья, пионеров, озорно играющих на пляже. Вся эта мелодия природы наводила дремоту и спокойствие."

    window hide dspr

    play sound sfx_thunder_crack fadein 2
    show un smile pioneer close:
        zoom 1.45
    with dspr

    window show dspr

    nn "Конечно помню, и никогда не забуду..."

    show un smile pioneer close:
        zoom 1.45
    with dspr

    "От нехватки тепла и близости она нежно прижалась ко мне."
    "Моё дыхание на секунду остановилось, а сердце билось всё чаще. Я приобнял её за талию."
    "В этот дорогой момент хотелось тишины."

    window hide dissolve
    stop music fadeout 3
    stop ambience fadeout 4
    hide window with dissolve
    stop music fadeout 5
    hide un smile pioneer close with dissolve
    scene black with dissolve2
    $ renpy.pause(2.0)

    window show dissolve
    "Да, я тоже никогда не забуду тот день…"
    window hide dissolve

    hide un smile pioneer close
    play ambience "rain/sounds/ambience/rain.mp3" fadein 7
    play music music_list["afterword"] fadein 3
    show text "{size=+20}Годом ранее{/size}" at truecenter with dissolve2
    $ renpy.pause(1.0)
    hide text
    scene bg_city1 with dissolve
    show hard_rain with dspr

    window show dissolve
    "Дождь. Запах сырости. Свинцовые тучи. Люди прячущиеся от непогоды."
    window hide dspr

    scene black with dissolve
    scene bg_city2 with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (25,25)
        ease 0.20pos (0, 0)
        ease 0.20pos (-25,25)
        repeat
    show hard_rain

    window show dspr
    "И я мчащийся домой."
    "Причиной моей спешки был звонок от мамы, а именно звонок о приезде моей подруги, дорогой подруги детства."
    "Я не видел её три года, долгих, скучных, томительных три года…"
    "Она часто уезжала в другие страны потому, что её родители всё не могли найти себе постоянное проживание и работу."
    "Обычно она возвращалась через год после переезда, но в этот раз она пропала надолго. У меня даже не было возможности писать ей."
    "Моя жизнь превратилась в огромную серую тучу, похожую на эту, что сейчас нависла над городом. Я часто не выходил из дома, мой круг общения значительно сузился, а потребности ограничились биологическими."
    window hide dspr

    scene black with dissolve
    scene bg_city4 with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (25,25)
        ease 0.20pos (0, 0)
        ease 0.20pos (-25,25)
        repeat
    show hard_rain with dspr

    window show dspr
    "Для меня она была дороже себя. В детстве мы часто играли вместе, мы были как брат с сестрой. Всегда было желание защитить её и сделать счастливее."
    "Да, она часто уезжала, но я никогда не забывал её, по возможности писал ей письма или звонил."
    "Если бы были такие слова, чтобы охарактеризовать её, то каждое слово вызывало бы неизмеримую любовь и теплоту души."
    "Она всегда была добра ко мне, даже когда я совершал ошибки, и всегда поддерживала меня."
    "Хоть обстоятельства не позволяли нам долго видеться, казалось, что я знаю её вечность."
    window hide dspr

    scene black with dissolve
    scene bg_city3 with dissolve:
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (25,25)
        ease 0.20pos (0, 0)
        ease 0.20pos (-25,25)
        repeat
    show hard_rain with dspr
    stop music fadeout 5

    window show dspr
    "Сердце рвалось от нетерпимости, мысли в моей голове неслись быстрее скорости света. Но вот последний поворот и мой дом…"
    window hide dissolve

    $ renpy.pause(1.0)
    play music music_list["everlasting_summer"]  fadein 5
    scene bg_city3 with dspr

    window show dspr
    "Она стояла с зонтом немного ёжась от прохлады."
    window hide dspr

    show hard_rain with dspr
    show un c cry with dissolve

    window show dspr
    "Я остановился перед ней, пытаясь отдышаться, и не сводил с неё взгляд."
    "Она заметно выросла, стала ещё красивее чем раньше. Её зелёные прекрасные глаза смотрели в мои, они понемногу наливались слезами, горячими слезами радости и разлуки."
    "Я обнял её всем своим мокрым телом, но она лишь приняла в ответ мои объятья с той же силой."
    window hide dspr

    hide un c cry with dspr
    show un c cry:
        zoom 1.3
    with dissolve

    window show dspr
    me "Ты, наконец, приехала..."
    "Прошептал я ей на ухо."
    nn "Да.. и теперь никогда не уеду!"
    window hide dspr

    hide un c cry with dspr
    show un casual cryasmile:
        zoom 1.5
    with dissolve

    window show dspr
    "Сказала она, усиливая свои тёплые объятия."
    me "Теперь мы будем всегда вместе."
    "Уверил я, утирая с её щёк слёзы."
    window hide dissolve

    hide un casual cryasmile with dissolve
    scene black with dissolve
    scene prolog_1 with dissolve2

    stop music fadeout 4
    stop ambience fadeout 4

    window show dissolve
    "Тот день был концом моей прежней жизни. Теперь я живу с улыбкой на лице, зная что с ней всё хорошо, что она счастлива."
    "Её родители решили больше не переезжать, и остаться тут."
    "Моя дорогая всегда будет моей соседкой."
    "Наши родители отправили нас на отдых в лагерь, объясняя это тем, что мы давно не были вместе."
    "Так мы и оказались в 'Совёнке'"
    "Здесь мы стали хоть немного беззаботными и уединенными. Пионеры дружные и весёлые. Вожатая, Ольга Дмитриевна, как и ожидалось, строгая и с характером."
    "Но главное в этом месте - это природа и её умиротворенность. В 'Совёнке', практически, всегда солнце."
    window hide dissolve

    play ambience "rain/sounds/ambience/rain2.mp3" fadein 3.5
    play music music_list["lets_be_friends"] fadein 4

    $ renpy.pause(1.5)

    scene bg ext_island_night with dissolve2
    show un normal pioneer close:
        zoom 1.4
    with dissolve
    show hard_rain
    
    window show dissolve
    "Но сегодня, как и в тот день, льёт дождь. Лёгкие наполняются свежим запахом сырости."
    "Мы сидим с ней на островке, не думая ни о чем, лишь наслаждаясь моментом. Я рядом с любимым мне человеком, для счастья не нужно ничего больше. Я никогда не был так уверен в своих чувствах, но сейчас могу точно сказать: я люблю её."
    "Так не хочется нарушать хрупкую тишину, но я должен…"
    me "В тот день я забыл кое-что сказать тебе."
    nn "И что же?"
    "На некоторое время я погрузился в свои мысли и чувства. Но она не хочет торопить меня, ведь сейчас время для нас не идёт. Я посмотрел в её прекрасные глаза-изумруды, которые ждали моих слов."
    me "Я{w} люблю{w} тебя..."    
    window hide dspr

    hide un normal pioneer
    show un smile pioneer close:
        zoom 1.45

    window show dspr
    "В ответ она прижалась ко мне всем своим горячим телом. Кажется, что сердце сейчас выпрыгнет из груди."
    nn "Я тоже тебя люблю."
    window hide dissolve

    window show dspr
    "Так мы сидели под деревом в жарких объятиях, не обращая внимания на окружающий нас мир. Дождь. Он стал для нас чем-то особым. Дождь стал для нас предвестием доброго предзнаменования..."
    stop ambience fadeout 4
    stop music fadeout 4
    window hide dissolve
    scene black with dissolve2
    $ renpy.pause(2.5, hard = True)
    play music "rain/sounds/music/planya_ch_knopochka_online_piano_cover_by_alina_witch.mp3" fadein 9
    $ renpy.pause(2.5, hard = True)
    show text "{size=+30}Конец.{/size}" at truecenter with dissolve2
    
    $ renpy.pause(2, hard = True)
    
    hide text with dissolve2

    $ renpy.pause(1, hard = True)

    show text "{size=+25}Спасибо за то, что Вы прошли мою модификацию.{/size}" at truecenter with dissolve2
    
    $ renpy.pause(2, hard = True)
    
    hide text with dissolve2

    show text "{size=+25}Если вы хотите меня как-то поблагодарить, то пожалуйста\nпоставьте оценку моему моду в мастерской стима, а также оставьте комментарий с вашей благодарностью.{/size}" at truecenter with dissolve2
    
    $ renpy.pause(8, hard = True)
    
    hide text with dissolve2

    show text "{size=+25}Мой сайт https://dezlow.me{/size}" at truecenter with dissolve2
    $ renpy.pause(2, hard = True)
    hide text with dissolve2

    $ renpy.pause(4, hard = True)

    show text "{size=+65}Спасибо.{/size}" at truecenter with dissolve2
    $ renpy.pause(8, hard = True)
    hide text with dissolve2

    stop music fadeout 4

    $ renpy.pause(6, hard = True)