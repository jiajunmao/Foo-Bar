def answer(s):
    decrypt = "";
    for i in range(0, len(s)):
        ascii = ord(s[i]);
        if (ascii <= 122 and ascii >= 97):
            decrypt += chr(97 + 122 - ascii);
        else:
            decrypt += chr(ascii);

    return decrypt;
