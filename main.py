@namespace
class SpriteKind:
    dadu = SpriteKind.create()
    object2 = SpriteKind.create()
    pointer = SpriteKind.create()
    da_bus = SpriteKind.create()
    resort = SpriteKind.create()
    destroykey = SpriteKind.create()
    pointer2 = SpriteKind.create()
    student = SpriteKind.create()
    Kraken = SpriteKind.create()
    p3 = SpriteKind.create()
    p4 = SpriteKind.create()
    P5 = SpriteKind.create()
    P6 = SpriteKind.create()
    p7 = SpriteKind.create()
    p8 = SpriteKind.create()
    p9 = SpriteKind.create()
    p10 = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global pointer3, p92
    sprites.destroy(pointer6)
    sprites.destroy(pointer_4)
    tiles.set_current_tilemap(tilemap("""
        level13
    """))
    pointer3 = sprites.create(img("""
            . . . . . . 7 5 7 . . . . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . 7 5 5 5 5 4 5 5 5 5 7 . . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . .
        """),
        SpriteKind.p4)
    pointer3.set_position(65, 73)
    pointer3 = sprites.create(img("""
            . . . . . . 7 5 7 . . . . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . 7 5 5 5 5 4 5 5 5 5 7 . . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . .
        """),
        SpriteKind.P6)
    pointer3.set_position(100, 73)
    Ayush.set_position(160, 150)
    p92 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . 7 5 5 7 . . . . . . . . . 
                    . . 7 5 5 5 7 7 7 7 7 7 7 7 7 7 
                    . . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 4 5 5 5 4 5 5 5 4 5 5 5 4 
                    7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . 7 5 5 5 7 7 7 7 7 7 7 7 7 7 
                    . . . 7 5 5 7 . . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.p9)
    p92.set_position(80, 80)
sprites.on_overlap(SpriteKind.player, SpriteKind.p8, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global pointer3
    sprites.destroy(pointer3)
    sprites.destroy(_1p)
    tiles.set_current_tilemap(tilemap("""
        level16
    """))
    pointer3 = sprites.create(img("""
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . . 7 5 5 5 5 5 5 5 5 5 7 . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . . . . 7 5 7 . . . . . . .
        """),
        SpriteKind.p8)
    pointer3.set_position(160, 190)
sprites.on_overlap(SpriteKind.player, SpriteKind.p4, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    global resort_2
    sprites.destroy(p92)
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    resort_2 = sprites.create(img("""
            ................................
                    ......8888888...................
                    .....88f999f8...................
                    .....889f9f98...................
                    .....8899f9998..................
                    .....889f9f9998.................
                    .....88f999fff8.................
                    .....8899999998.................
                    .....8899999998.................
                    ..8888899999998.................
                    ..8999999999998.................
                    ..8999999999998.................
                    ..8999999999998.................
                    ..8888899999998.................
                    ......888888888.................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
        """),
        SpriteKind.resort)
    resort_2.scale = 8
    resort_2.set_position(295, 290)
sprites.on_overlap(SpriteKind.player, SpriteKind.p10, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    global pointer_4, pointer6
    sprites.destroy(pointer3)
    scene.camera_follow_sprite(Ayush)
    tiles.set_current_tilemap(tilemap("""
        level13
    """))
    pointer_4 = sprites.create(img("""
            . . . . . . 7 5 7 . . . . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . 7 5 5 5 5 4 5 5 5 5 7 . . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . .
        """),
        SpriteKind.p4)
    pointer_4.set_position(65, 73)
    pointer6 = sprites.create(img("""
            . . . . . . 7 5 7 . . . . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . 7 5 5 5 5 4 5 5 5 5 7 . . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . .
        """),
        SpriteKind.P6)
    pointer6.set_position(100, 73)
    Ayush.set_position(160, 150)
sprites.on_overlap(SpriteKind.player, SpriteKind.p7, on_on_overlap4)

def on_on_overlap5(sprite5, otherSprite5):
    global da_bus2, MrKraken
    music.play(music.melody_playable(music.zapped),
        music.PlaybackMode.UNTIL_DONE)
    tiles.set_current_tilemap(tilemap("""
        level3
    """))
    da_bus2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . 9 9 . . . . . . 9 9 . . . . 
                    . 9 5 5 5 5 5 5 5 f f f . . . . 
                    2 9 f f f f f f f f f f f 9 . . 
                    . 9 f 5 9 5 9 5 9 5 9 f 5 5 . . 
                    . 9 f 9 5 9 5 9 5 9 5 f 5 5 . . 
                    2 9 f f f f f f f f f f f 9 . . 
                    . 9 5 5 5 5 5 5 5 f f f . . . . 
                    . . 9 9 . . . . . . 9 9 . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.da_bus)
    MrKraken = sprites.create(img("""
            . . . . f f f f 4 4 4 . . . . . 
                    . . . f f f f f f f f f . . . . 
                    . . . f e f e f e f e f . . . . 
                    . . . f e 1 1 e 1 f e f . . . . 
                    . . . . e 1 6 e 6 1 e . . . . . 
                    . . . . e e e d e e e . . . . . 
                    . . . . e e e e e e e . . . . . 
                    . . . . . e e f e e . . . . . . 
                    . . f f d d d d d d d f f . . . 
                    . . f f d d d f d d d f f . . . 
                    . . d . d d d d d d d . d . . . 
                    . . . . d d d f d d d . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . f f f f f . . . . . . 
                    . . . . . f f . f f . . . . . . 
                    . . . . . 8 8 . 8 8 . . . . . .
        """),
        SpriteKind.Kraken)
    MrKraken.scale = 1.8
    da_bus2.scale = 4.7
    da_bus2.set_position(57, 40)
    sprites.destroy(pointer3, effects.none, 500)
    sprites.destroy(Dadu, effects.none, 500)
    sprites.destroy(mom, effects.none, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.pointer, on_on_overlap5)

def on_on_overlap6(sprite6, otherSprite6):
    global Ayush, Student, pointer3
    Ayush = sprites.create(img("""
            ................................................................
                    .............222222222..........................................
                    ............22222222222.........................................
                    ...........222fffffff222........................................
                    ..........22fffffffffff22.......................................
                    .........222fffffffffff222......................................
                    .........22fffffdffdffff22......................................
                    .........22fffddddddddff22......................................
                    .........22fd111ddd111df22......................................
                    .........22dd177ddd771df22......................................
                    .........22dd17fdddf71dd22......................................
                    .........22dd177ddd771dd22......................................
                    .........22ddddddddddddd22......................................
                    .........222ddddddddddd222......................................
                    ..........22ddddddddddd22.......................................
                    ...........2222fffff2222........................................
                    ..........4d222f222f222dd.......................................
                    ..........d4d22fffff22d4d.......................................
                    ..........ddd.2f222f2.ddd.......................................
                    ..............2f222f2...........................................
                    ..............8222228...........................................
                    ..............8686668...........................................
                    ..............8668668...........................................
                    ..............288.882...........................................
                    ............2f222.222f2.........................................
                    ............22f22.22f22.........................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
                    ................................................................
        """),
        SpriteKind.player)
    Ayush.set_position(65, 68)
    controller.move_sprite(Ayush, 50, 50)
    scene.camera_follow_sprite(Ayush)
    sprites.destroy(da_bus2, effects.none, 500)
    sprites.destroy(resort_2, effects.none, 500)
    scene.camera_follow_sprite(Ayush)
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
    Student = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . e e e . . . . . . 
                    . . . . e e e e e e e . . . . . 
                    . . . e e e e e e e e e . . . . 
                    . . . e e e d e d d d e . . . . 
                    . . . . e 1 1 d 1 1 e e . . . . 
                    . . . . d 1 f d f 1 d e . . . . 
                    . . . . d d d d d d d . . . . . 
                    . . . . . d d 2 d d . . . . . . 
                    . . . d 1 1 9 1 9 1 1 d . . . . 
                    . . . d 1 1 1 9 1 1 1 d . . . . 
                    . . . . . 1 1 9 1 1 . . . . . . 
                    . . . . . 8 8 . 8 8 . . . . . . 
                    . . . . . d d . d d . . . . . . 
                    . . . . e e e . e e e . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.student)
    Student.set_position(45, 98)
    Student.scale = 1.6
    scene.camera_follow_sprite(Ayush)
    pointer3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 7 7 7 . . . . 
                    . . . . . . . . . 7 5 5 7 . . . 
                    7 7 7 7 7 7 7 7 7 7 5 5 5 7 . . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 
                    4 5 5 5 4 5 5 5 4 5 5 5 4 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    7 7 7 7 7 7 7 7 7 7 5 5 5 7 . . 
                    . . . . . . . . . 7 5 5 7 . . . 
                    . . . . . . . . . 7 7 7 . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.p3)
    pointer3.set_position(220, 93)
    scene.camera_follow_sprite(Ayush)
    story.print_character_text("Oh, nice. This resort is pretty cool.", "Student")
sprites.on_overlap(SpriteKind.da_bus, SpriteKind.resort, on_on_overlap6)

def on_on_overlap7(sprite7, otherSprite7):
    global pointer3, _1p, p92
    tiles.set_current_tilemap(tilemap("""
        level13
    """))
    sprites.destroy(pointer3)
    sprites.destroy(Student)
    pointer3 = sprites.create(img("""
            . . . . . . 7 5 7 . . . . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . 7 5 5 5 5 4 5 5 5 5 7 . . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . .
        """),
        SpriteKind.p4)
    pointer3.set_position(65, 73)
    _1p = sprites.create(img("""
            . . . . . . 7 5 7 . . . . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . 7 5 5 5 5 4 5 5 5 5 7 . . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 4 5 5 5 7 . . . .
        """),
        SpriteKind.P6)
    pointer3.set_position(100, 73)
    p92 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . 7 5 5 7 . . . . . . . . . 
                    . . 7 5 5 5 7 7 7 7 7 7 7 7 7 7 
                    . . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 4 5 5 5 4 5 5 5 4 5 5 5 4 
                    7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . 7 5 5 5 7 7 7 7 7 7 7 7 7 7 
                    . . . 7 5 5 7 . . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.p9)
    p92.set_position(70, 73)
    scene.camera_follow_sprite(Ayush)
sprites.on_overlap(SpriteKind.player, SpriteKind.p3, on_on_overlap7)

def on_on_overlap8(sprite8, otherSprite8):
    global resort_2, pointer3
    story.print_character_text("5", "Mr.Kraken")
    story.print_character_text("6", "Ayush")
    story.print_character_text("7", "Mr.Kraken")
    music.play(music.string_playable("D F G A F G E G ", 192),
        music.PlaybackMode.UNTIL_DONE)
    sprites.destroy(Ayush)
    sprites.destroy(MrKraken)
    scene.camera_follow_sprite(da_bus2)
    da_bus2.set_position(78, 81)
    tiles.set_current_tilemap(tilemap("""
        level4
    """))
    controller.move_sprite(da_bus2, 50, 50)
    resort_2 = sprites.create(img("""
            ................................
                    ......8888888...................
                    .....88f999f8...................
                    .....889f9f98...................
                    .....8899f9998..................
                    .....889f9f9998.................
                    .....88f999fff8.................
                    .....8899999998.................
                    .....8899999998.................
                    ..8888899999998.................
                    ..8999999999998.................
                    ..8999999999998.................
                    ..8999999999998.................
                    ..8888899999998.................
                    ......888888888.................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
                    ................................
        """),
        SpriteKind.resort)
    resort_2.scale = 8
    resort_2.set_position(295, 290)
    pointer3 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . 7 7 7 . . . . 
                    . . . . . . . . . 7 5 5 7 . . . 
                    7 7 7 7 7 7 7 7 7 7 5 5 5 7 . . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 7 . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    7 7 7 7 7 7 7 7 7 7 5 5 5 7 . . 
                    . . . . . . . . . 7 5 5 7 . . . 
                    . . . . . . . . . 7 7 7 . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.p3)
    pointer3.set_position(380, 173)
sprites.on_overlap(SpriteKind.player, SpriteKind.Kraken, on_on_overlap8)

def on_on_overlap9(sprite9, otherSprite9):
    global pointer3
    sprites.destroy(pointer3)
    sprites.destroy(_1p)
    tiles.set_current_tilemap(tilemap("""
        level16
    """))
    pointer3 = sprites.create(img("""
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . . . 7 5 5 5 5 5 5 5 7 . . . . 
                    . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
                    . . 7 5 5 5 5 5 5 5 5 5 7 . . . 
                    . . . 7 7 5 5 5 5 5 7 7 . . . . 
                    . . . . . 7 5 5 5 7 . . . . . . 
                    . . . . . . 7 5 7 . . . . . . .
        """),
        SpriteKind.p7)
    pointer3.set_position(160, 190)
sprites.on_overlap(SpriteKind.player, SpriteKind.P6, on_on_overlap9)

def on_on_overlap10(sprite10, otherSprite10):
    global p92
    sprites.destroy(pointer3)
    tiles.set_current_tilemap(tilemap("""
        level11
    """))
    p92 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . 7 5 5 7 . . . . . . . . . 
                    . . 7 5 5 5 7 7 7 7 7 7 7 7 7 7 
                    . . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 4 5 5 5 4 5 5 5 4 5 5 5 4 
                    7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . 7 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    . . 7 5 5 5 7 7 7 7 7 7 7 7 7 7 
                    . . . 7 5 5 7 . . . . . . . . . 
                    . . . . 7 7 7 . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.p10)
    scene.camera_follow_sprite(Ayush)
    p92.set_position(30, 70)
sprites.on_overlap(SpriteKind.player, SpriteKind.p9, on_on_overlap10)

Student: Sprite = None
MrKraken: Sprite = None
da_bus2: Sprite = None
resort_2: Sprite = None
_1p: Sprite = None
p92: Sprite = None
pointer_4: Sprite = None
pointer6: Sprite = None
pointer3: Sprite = None
mom: Sprite = None
Dadu: Sprite = None
Ayush: Sprite = None
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99d99bbbbbcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99ddbdd66168bcccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999ddbbbd66888111ccccccb99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966ddbbbb6688811818ccccccbbc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdd69dddbbb66618881888818818cccccbe9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddd96dd6b6dbd68888888888888888cccccc99fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbd9666666dbb668886888888cccccccccccccc9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb99666966d68866888888cccccccccccccccccc69ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666888888888ccccbbbcc8bcccccccccc9fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999666666666888888888cbbcbe8bbbcbcccccbbcccb9ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff9bbb999666666666688888888bccb888888bbbbb88888bcccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffdbbb999669666666866888868bbbbb8888888ccc888b88bbc8cccffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffdbbb9d99ddd666668868888688bbcb888888888bc888bcc8bc886c9fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffbbbbbbddd966666888688888888888888b88888888888cc8ccc886c9ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffdbbbbbbdd6966666666868888888888bbdbbebb8888888888bcc8c86c9fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff9bbdbddd6666666666888688868888ddddddddde8888888888bccbbccccfffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff9dbb9dd666666666668868888888bddddddbdbbddcccccd88b8ebccbbbbc9ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffdd99999666666666668868888888bdddddbbbbbdbbbccccccb8bbbccc8bbb9fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9dd99996696966666666668888bbbdddddbbbddbbbbbbbbbcccc8bcccbb8bbcfffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9d999996666966666668688888bbdddbbbbdbbbbbbbbbbbcccccc8bbccc88bc9ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff99999999666996696668868868bbdddddbbbdbbbbbbbbbbbbcbccc88bcccc88c6ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff999996696669666966d8868666bddbbbddbbdbbbbbbbbbbbbcccccc88bbccc8869fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999996699669666666d6688668bddbbdbbbbbbbbbbbbbbbbbccccccc88bcccc866fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9dd999669966666666666688668bdddbbbbbbbbbbbbbbbbbbbccccccc888bbccc669ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff999999669d69666666666688868bddbbbdbbbbbbbbbbbbbbbbcccccccc888bbcc869ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999996ddd69666666688888868ddbddbbbbbbbbbbbbbbbbbbccccccccc888888866ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999999969ddd6669666688688888bbbbbbbbbbbbbbbbbbbbbbbbccbccccc8888888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99999966ddddd669666688888888bbbbbbbbbbbbbbbbbbbbbbbcbccccccccc88888869fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff999bb99666dddd6666666668886888bbbbbbbbbbbbbbbbbbbbbbcccccccccccc8888889fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbb966696666666666888886888bbbbbbbbbbbbbbbbbbbbbbcbccccccccccc888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbdbb666969666666668888868888bbbbbbbbbbbbbbbbbbbbccbccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99dbbbbb6696966666666668886868888bbbbeb888bbbbbbbbbcccccccccccccc8888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbe6969666666666888888888888888888888bbbbbbbbccccccccccccc88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccbc66966666666688888688888888888d888ebbbbbbbcccccccccccbb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbcc69996666688668886888888dd88dbbd88bbbbbbbccccccccccceb88888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbbccc999966668868888888888ddddbbbbd88cbbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9ebbbbcccccccc9966666688888888888888ddbbbb888bbbbbbbbccccccccc8888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbccccccccc666666888866888888888dddddbdd88bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffbbbbbbcccccccccc6666688888888888888888d8888888bbbbbbccccccccc88888888bb9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbccbbccccccb666688868888888888888888888888bbbbbccccccccc888888888b9ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9dbbbbbbbbcccccbb66666688888888888888888888888bbbbccccccccccc88888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbcccccccb666666688888888888888888888888bbbbcccccccccc888888888869ffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff9bbbbbbbccccccbb666666688888888888888888888888bbbbcccccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffff99bbbbbbbbccccb6666668888888888888888888888888bbbbcbcccccccc88888888886fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcbbccccb6666668888888888888888888888888bbbbbccccccccc888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff99dbbbcccccccc6666668688688888888888888888888bbbbccccccccc8888cc888869fffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff999bbbbbccccbc6666666688688888888888888888888bbbbcccccccc88888dd88886ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffff969bbbbbbcccc69666666668688868888888888888888bbbbccccccc88888bd888886ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff99bbbbcccccc696bb668888888868888888888888888bbbcccccccc8888bbd888869ffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffff9999bbbcccc9666dbbb8888888888888888888888888ccbcccccccc8888bc888886fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff699bbbbccc966966bbb8888888888888888888888888bbbbccccc88888bcc88869fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9999bbcccc666666dbbdd88888888688888888888888bbcccccc88888888888669fffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffff9699dbcccc66666666bb6d8888888688888888888888bbcccccc8888888888869ffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff9696bbbcc66666666dbbd6886868888888888888888bbcbccc8888888888d669ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff999ebbccc666666666dbb8868888688888888888888bbbccc8888888889b69fffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff969ccbcc66996666666bbb868888888888888888888bbbc888888888888b6ffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff96ccccc966966666666bb8688666888888888888888b8888888888888699ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff99ccbc996666666666dbb6888668888888888888888888888888888869fffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff969ccb9666666666666dbb88866888888888888888888888888888869ffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff969ccc6696666666666dd8888668888888888888888888888888866fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff969cc9669666966d66dd8888868888888888888888888bb8888669fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff96ccc66699669dddd888868888888888888888888888be888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff96c66669966666dd88886666668888888888888888dd888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff96966669966ddd686886868888888888888888888d888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff969666696666666688686888888888888888888888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff9966966966666666886888888888888886888888669fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9699996666666888888888888888888118888699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff969996666668888881188888888881888669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff996999666688881818888888881886669ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9961161186618811188886116699ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff99161111611118111666699fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff9999661166669999ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff999999999fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
scene.set_background_color(1)
story.print_character_text("123", "DADU ")
tiles.set_current_tilemap(tilemap("""
    level2
"""))
Ayush = sprites.create(img("""
        ................................................................
            .............222222222..........................................
            ............22222222222.........................................
            ...........222fffffff222........................................
            ..........22fffffffffff22.......................................
            .........222fffffffffff222......................................
            .........22fffffdffdffff22......................................
            .........22fffddddddddff22......................................
            .........22fd111ddd111df22......................................
            .........22dd177ddd771df22......................................
            .........22dd17fdddf71dd22......................................
            .........22dd177ddd771dd22......................................
            .........22ddddddddddddd22......................................
            .........222ddddddddddd222......................................
            ..........22ddddddddddd22.......................................
            ...........2222fffff2222........................................
            ..........4d222f222f222dd.......................................
            ..........d4d22fffff22d4d.......................................
            ..........ddd.2f222f2.ddd.......................................
            ..............2f222f2...........................................
            ..............8222228...........................................
            ..............8686668...........................................
            ..............8668668...........................................
            ..............288.882...........................................
            ............2f222.222f2.........................................
            ............22f22.22f22.........................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
    """),
    SpriteKind.player)
Dadu = sprites.create(img("""
        ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ................................................................
            ...............111111...ddddddddddd.....11......................
            ..............11111111.ddddddddddddd.11111......................
            ............1111111111ddddddddddddddd111111111..................
            ...........11111111111ddddddddddddddd111111111..................
            ...........111111111ddddddddddddddddddd111111111................
            ...........111111111ddddddddddddddddddd111111111................
            ...........111111111ddddddddddddddddddd1111111111...............
            ..........111111111dd11111ddddddd11111dd111111111...............
            ..........111111111dd11111ddddddd11111dd111111111...............
            ..........111111111dd11111ddddddd11111dd111111111...............
            ..........111111111dd11666ddddddd66611dd111111111...............
            ..........11111111ddd11666ddddddd66611dd111111111...............
            ............111111ddd11666ddddddd66611ddd11111111...............
            ............111111ddd1166fdddddddf6611ddd1111111................
            .............11111ddd1166fdd444ddf6611ddd111111.................
            ..............1111dddddddddd444dddddddddd1111...................
            .................ddddddddddd444ddddddddddd......................
            .................ddddddddd4444444ddddddddd......................
            ..................dddddddd4444444dddddddd.......................
            ...................ddddddd4444444ddddddd........................
            ...................ddddddddddddddddddddd........................
            ....................ddddddddddddddddddd.........................
            .....................ddddddddddddddddd..........................
            .................11111.dddddddddddd1111.........................
            ................11111111ddddddddddd111111.......................
            ...............111111111111111111111111111111...................
            .............11111111111111111111111111111111...................
            ............111111111111111111111111111111111...................
            ...........1111111111111111111111111111111111...................
            ...........1111111111111111111111111111111111...................
            ...........1d11111111111111111111111111111111...................
            ..........dddd11111111111111111111111111dd111...................
            ..........ddddddd1111111111111111111111dddd.....................
            ........eedddddddee.111111111111111111ddddd.....................
            ........eedddddddee..1111111111111111ddddd......................
            ..........ddddddd....111111111111111.ddddd......................
            ...........ddddd....881111111111111188.dd.......................
            ............eedd...866111111111111168888........................
            ............ee....8866666666666666668868........................
            ............ee...88666666666666996666888........................
            ............ee...86669966666666966666688........................
            ............ee...86666996666666996666688........................
            ............ee...86666696668886699666888........................
            ............ee...88666696668.86966666868........................
            ............ee....8866996668.86666668868........................
            ............ee.....86666688..88886886668........................
            ............ee....e888888.......e866668e........................
            ............ee..ee.......e......e88888.ee.......................
            ............ee..e.......e.......e.......e.......................
            ............ee..eeeeeeeee.......eeeeeeeee.......................
            ................................................................
            ................................................................
    """),
    SpriteKind.dadu)
controller.move_sprite(Ayush, 50, 50)
scene.camera_follow_sprite(Ayush)
mom = sprites.create(img("""
        . . . . f f f 1 f f f f . . . . 
            . . f f f f 1 f f f 1 1 f . . . 
            . . f f 1 f f f f f f f 1 . . . 
            . f f 1 f f f d f d d f f f . . 
            . f f f f d d d d d d d f f . . 
            . f f f f 1 1 d d 1 1 1 f f . . 
            . f f d 1 1 5 d d 5 1 1 d . . . 
            . f f d 1 1 5 d d 5 1 1 d . . . 
            . f f d d d d d d d d d d . . . 
            . f f d d d 4 d d d d d d . . . 
            . f f . d d d 4 4 d d . . . . . 
            . f f . a a d d d a a . . . . . 
            . f f f a a a a a a a a d . . . 
            . f f f d a a a a a a d d . . . 
            . . f f . 8 8 8 8 8 . . . . . . 
            . . . . . e d . d e . . . . . .
    """),
    SpriteKind.player)
mom.scale = 1.5
mom.set_position(126, 30)
pointer3 = sprites.create(img("""
        . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . . . 7 5 5 5 5 5 5 5 7 . . . . 
            . 7 7 7 5 5 5 5 5 5 5 7 7 7 . . 
            . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
            . 7 5 5 5 5 5 5 5 5 5 5 5 7 . . 
            . . 7 5 5 5 5 5 5 5 5 5 7 . . . 
            . . . 7 7 5 5 5 5 5 7 7 . . . . 
            . . . . . 7 5 5 5 7 . . . . . . 
            . . . . . . 7 5 7 . . . . . . .
    """),
    SpriteKind.pointer)
pointer3.set_position(160, 200)
Dadu.scale = 0.6
Dadu.set_position(36, 41)
story.print_character_text("YOWAI MO SON", "Mom")