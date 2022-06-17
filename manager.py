from hashlib import sha256
from random import randint, choice
from crypt import MemoryCrypter
import sys
import os


class Key:
	""" Generate security key """
	def __init__(self, keytext='key'):
		self.__keytext = keytext
		self.__words = list('qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+1234567890-=|}{][":;?/><.,')

	def gentext(self):
		""" Generate key text """
		for i in range(len(self.__words)):
			self.__keytext += str(choice(self.__words))
		return self.__keytext

	def get_keytext(self):
		""" Get hide var of keytext """
		return self.__keytext

	def get_key(self):
		""" Generate key """
		return sha256(self.__keytext.encode('utf-8')).hexdigest()


def keygen():
	""" simple key generating """
	text = Key('a').gentext()
	key = Key(text)
	return text


def crypter(filename, method, pswd):
	MemoryCrypter(filename, method, pswd, 64 * 1024)


def main():
	print('''
1 - Шифрование файла
2 - Дешифровка файла
		''')
	method = input('>>> ')
	if method == '1':
		file = input('Введите путь к файлу: ')
		method = True
		os.system('clear')
		print(f'''
Путь к файлу: {file}
Выберите пароль:
1 - Создать свой
2 - Генерация пароля
		''')
		pswd_choice = input('>>> ')
		if pswd_choice == '1':
			pswd = input('Пароль: ')
			if len(pswd) < 8:
				print('Внимание! Ваш пароль короткий. Вас могут взломать')
		else:
			print(f'Пароль: {keygen()}')
			pswd = keygen()

		print('В процессе...')
		crypter(file, method, pswd)
		input('Готово!')
	elif method == '2':
		file = input('Введите путь к файлу: ')
		method = False

		pswd = input('Введите пароль от файла: ')
		crypter(file, method, pswd)
		print('Готово!')
	else:
		print('Нету такой функции')
		sys.exit()


if __name__ == '__main__':
	main()
