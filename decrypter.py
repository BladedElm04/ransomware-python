import os
import pyaes

## abrir o arquivo criptografado
## open the crypto file

file_name = 'test.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## chave de descriptografia
## decrypted key

key = b'ransomwarepython'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
## remove the crypted file

os.remove(file_name)

## criar um novo arquivo descriptografado
## create a new decrypted file

new_file = 'test.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
