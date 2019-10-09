from morse_code import MORSE_CODE


def decodeMorse(morseCode):
    return ' '.join(
            ''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word
            in morseCode.strip().split('   '))


if __name__ == '__main__':
    print(decodeMorse(".... . -.--   .--- ..- -.. ."))
    print(decodeMorse(".   ."))
    print(decodeMorse("... --- ..."))
    print(decodeMorse("...   ---   ..."))
    print(decodeMorse("   .   . "))
    print(decodeMorse(
            "      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... "
            ".-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- "
            ". .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  "))
