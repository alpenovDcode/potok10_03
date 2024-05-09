# a = "Привет мир"
# cod = a.encode('utf 8')
# print(cod)

# b = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82 \xd0\xbc\xd0\xb8\xd1\x80'
# a1 = b.decode('utf 8')
# print(a1)
#
# bytes_array = bytes()
# print(bytes_array)

# `ISO-8859-1`

# original = "Привет, мир!"
#
# text_cp1251 = original.encode('cp1251')
# print(text_cp1251)
# print(text_cp1251.decode('cp1251'))

multi_char = "𐍈"
print(len(multi_char))  # Выводит 1, потому что это один Unicode символ
encoded_multi_char = multi_char.encode('utf-8')
print(encoded_multi_char)  # Выводит 4, потому что символ кодируется 4 байтами в UTF-8