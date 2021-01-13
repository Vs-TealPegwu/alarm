input.onButtonPressed(Button.B, function () {
    music.stopAllSounds()
})
let Timer = 3
if (Timer == 0) {
    music.playMelody("E D G F B A C5 B ", 120)
} else if (Timer != 0) {
    Timer += -1
} else {
    Timer += -1
}
