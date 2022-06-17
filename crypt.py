import io
import os
import pyAesCrypt


def MemoryCrypter(path, is_encrypted, password, buffersize):
	sequence_bytes = io.BytesIO()

	with open(path, 'rb') as f:
		file_content = io.BytesIO(f.read())

	with open(path, 'wb') as f:
		if is_encrypted:
			pyAesCrypt.encryptStream(
				file_content,
				sequence_bytes,
				password,
				buffersize
			)
		else:
			try:
				pyAesCrypt.decryptStream(
					file_content,
					sequence_bytes,
					password,
					buffersize,
					len(file_content.getvalue())
				)
			except Exception as ex:
				print('Произошла ошибка:', ex)
		f.write(sequence_bytes.getvalue())

# Examples
# MemoryCrypter(файл, шифровка - True, дешифровка - False, пароль, размер буффера)
# MemoryCrypter('data.txt', False, 'test', 64 * 1024)
