input.onButtonPressed(Button.B, function () {
    music.stopAllSounds()
})
let Timer = 3
if (Timer == 0) {
    basic.showString("Hello!")
    music.playMelody("E D G F B A C5 B ", 120)
} else {
    Timer += -1
}
