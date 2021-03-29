"""Convert BIP39 phrase to succinct hex format and vice versa

May be useful for tools that accept hex format such as:
https://github.com/trezor/python-shamir-mnemonic/

As the wordlist is 2048 words, each word corresponds to the value 0 to 2047
in decimal or 0x000 to 0x7ff in hex. Therefore the word "abandon" can be
encoded more succinctly as '000' rather than:
>>> 'abandon'.encode('utf-8').hex()
'6162616e646f6e'
"""
import sys

WORDLIST = 'english.txt'

def load_wordlist_val_map():
    """BIP39 word => position in wordlist (0-based)"""
    wordlist_val_map = dict()
    with open(WORDLIST) as wordlist:
        word_file = wordlist.readlines()
        position = 0
        for word in word_file:
            word = word.strip()
            wordlist_val_map[word] = position
            position += 1
    assert len(wordlist_val_map) == 2048
    assert wordlist_val_map['abandon'] == 0
    assert wordlist_val_map['zoo'] == 2047
    return wordlist_val_map

def load_val_wordlist_map():
    """Position in wordlist (0-based) => BIP39 word"""
    val_word_map = dict()
    with open(WORDLIST) as wordlist:
        word_file = wordlist.readlines()
        position = 0
        for word in word_file:
            word = word.strip()
            val_word_map[position] = word
            position += 1
    assert len(val_word_map) == 2048
    assert val_word_map[0] == 'abandon'
    assert val_word_map[2047] == 'zoo'
    return val_word_map

def get_hex_chunks(hex_str):
    """From one hex str return it in 3 chars at a time"""
    return [hex_str[i:i+3] for i in range(0, len(hex_str), 3)]

def hex_to_phrase(hex_str):
    """Convert hex representation to BIP39 phrase using english word list"""
    assert len(hex_str) % 3 == 0

    words = []
    val_wordlist_map = load_val_wordlist_map()

    for hex_word in get_hex_chunks(hex_str):
        int_word = int(hex_word, 16)
        word = val_wordlist_map[int_word]
        words.append(word)

    return " ".join(words)

def phrase_to_hex(phrase):
    """Convert BIP39 english word phrase to hex representation"""
    wordlist_val_map = load_wordlist_val_map()
    output = ''
    words = phrase.split(' ')
    for word in words:
        int_val = wordlist_val_map[word]
        hex_val = hex(int_val)[2:].zfill(3)
        output += hex_val

    return output

def _main(argv):
    print(argv[1])
    print("=>")
    try:
        int(argv[1], 16)

        phrase = hex_to_phrase(argv[1])
        print(phrase)

    except ValueError:
        output = phrase_to_hex(argv[1])
        print(output)

if __name__ == '__main__':
    _main(sys.argv)
