# International morse code (sample)
Morse = {
    # Letters
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    # Numbers
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    # Punctuation
    "&": ".-...",
    "'": ".----.",
    "@": ".--.-.",
    ")": "-.--.-",
    "(": "-.--.",
    ":": "---...",
    ",": "--..--",
    "=": "-...-",
    "!": "-.-.--",
    ".": ".-.-.-",
    "-": "-....-",
    "+": ".-.-.",
    '"': ".-..-.",
    "?": "..--..",
    "/": "-..-.",
}


def translate_text(text):
    """
    Translates text to morse code
    Accepts:
        text(str): String to translate
    Returns:
        str: A translated string of morse code
    """

    if text == "":
        return "Please provide a valid text"

    morse_code = ""
    words = text.split(" ")

    for word in words:
        w = []
        for char in word:
            if char.lower() in Morse:
                w.append(Morse[char.lower()])

        morse_code += " ".join(w)
        morse_code += "  "

    return morse_code.rstrip()


def translate_morse(morse_code):
    """
    Translates morse code to english.
        Accepts:
            morse (str): A string of morse code to translate
        Returns:
            str: A translated string of text
    """
    if morse_code == "":
        return "Please provide a valid morse code."

    text = ""

    words = morse_code.split("   ")

    for morse_word in words:
        chars = morse_word.split(" ")
        for char in chars:
            for k, v in Morse.items():
                if char == v:
                    text += k
            text += " "

    return text.rstrip()


if __name__ == "__main__":
    text = "This string has been translated to morse code." 

    # Translate text to morse code
    morse = translate_text(text)

    # Translate morse code to text
    translated_text = translate_morse(morse)

    print(morse)
    print(translated_text)

