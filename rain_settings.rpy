# Copyright (c) Oneiro Games. All Rights Reserved.
# Licensed under the GPL License, Version 3.0.

init:
    image rain_particle_large = "rain/images/rain/rain_large.png"
    image rain_particle_large2 = "rain/images/rain/rain_large2.png"
    image rain_particle_normal = "rain/images/rain/rain_normal.png"
    image rain_particle_normal2 = "rain/images/rain/rain_normal2.png"
    image rain_particle_small = "rain/images/rain/rain_small.png"
    image rain_particle_small2 = "rain/images/rain/rain_small2.png"
    image rain:
        truecenter
        xzoom 1.7 yzoom 2.1
        contains:
            SnowBlossom("rain_particle_large", 10, 50, (75, 125), (1600, 1700))
        contains:
            SnowBlossom("rain_particle_normal", 25, 50, (50, 100), (1500, 1600))
        contains:
            SnowBlossom("rain_particle_small", 150, 50, (25, 50), (1400, 1500))
    image hard_rain:
        contains:
            "rain"
        contains:
            "rain"
    image bg_city1 = "rain/images/bg/city1.jpg"
    image bg_city2 = "rain/images/bg/city2.jpg"
    image bg_city3 = "rain/images/bg/city3.jpg"
    image bg_city4 = "rain/images/bg/city4.jpg"
    image un c cry = ConditionSwitch(
    "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    "persistent.sprite_time=='day'", im.MatrixColor( im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cry.png") )
    image un casual cryasmile = ConditionSwitch( "persistent.sprite_time=='sunset'", im.MatrixColor( im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cas.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'", im.MatrixColor( im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cas.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    "persistent.sprite_time=='day'", im.MatrixColor( im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cas.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), "rain/images/sprites/un_body.png",(0,0), "rain/images/sprites/un_casual.png",(0,0), "rain/images/sprites/un_cas.png") )
    define nn = Character(u"***", color="#ffc0cb", what_color="#f1d076")
    $ mods ["oneiro_rain"] = u"Дождь"
    $ config.developer = True
    define nn = Character(u"???", color="#ffc0cb", what_color="#f1d076")
    define audio.sunflower = "rain/sounds/ambience/rain.mp3"
