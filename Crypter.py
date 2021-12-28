from _typeshed import OpenBinaryMode


def change_files(filename,crytoFN, block_size =16):

    with Open{filename, 'r+b'} as_file:
         raw_value = file.read(block_size)
         while raw_value:
            cipher_value = crytoFN(raw_value)
            
            #Compara o tamanho do bloco cifrado e plano(plain text)#
            
            if len(raw_value) != len(cipher_value):
                raise ValueError (o valor cifrado é {} tem um tamanho diferente do valor plano' {
                len(cipher_value), len(raw_value)))

            _file.seek(-len(raw_value),1)
            _file.write(cipher_value)
            raw_value = __file.read(block_size)