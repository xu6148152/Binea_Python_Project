#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def test_character_code():
    s = 'cafe'
    print(len(s))
    b = s.encode('utf8')
    print(b)
    print(len(b))


def test_bytes_bytearray():
    cafe = bytes('cafe', encoding='utf_8')
    print(cafe)
    print(cafe[0])
    print(cafe[:1])

    cafe_arr = bytearray(cafe)
    print(cafe_arr)


def test_encoder_decoder():
    for codec in ['latin_1', 'utf_8', 'utf_16']:
        print(codec, 'El Nino'.encode(codec), sep='\t')


if __name__ == '__main__':
    test_encoder_decoder()
