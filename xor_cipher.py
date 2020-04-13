from itertools import cycle
import sys
import os
import platform

class cipher():
	def launch():
		if 'Windows' in platform.platform():
			os.system('cls')
		elif 'Linux' in platform.platform():
			os.system('clear')
		else:
			pass
		
		banner = '''	▄▄▄        ██████  ██░ ██  ██▓ ▄▄▄      
	▒████▄    ▒██    ▒ ▓██░ ██▒▓██▒▒████▄    
	▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██▒▒██  ▀█▄  
	░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██░░██▄▄▄▄██ 
	 ▓█   ▓██▒▒██████▒▒░▓█▒░██▓░██░ ▓█   ▓██▒
	 ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓   ▒▒   ▓▒█░
	   ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░  ▒   ▒▒ ░
	  ░   ▒   ░  ░  ░   ░  ░░ ░ ▒ ░  ░   ▒   
   	   ░  ░      ░   ░  ░  ░ ░        ░  ░
 
 
                   \033[31m{ By AskaD }\033[00m
              [=] \033[34mAuthor\033[00m  : AskaD    [=]
                 { \033[34mGithub\033[00m : 3x1t1um }  

                 		  *BETA'''
		print(banner)
		print()
		print('	'+'='*38)
		print()
		cipher.check()

	def tostrings(data):
		return ''.join([chr(int(x, 2)) for x in data])

	def check():
		if len(sys.argv) <= 3:
			cipher.help()
		
		else:
			if sys.argv[1] == '--crypt' or sys.argv[1] == '-c':
				text = [sys.argv[i] for i in range(3, len(sys.argv))]
				print('key : '+sys.argv[2])
				print('text : '+' '.join(text))
				print()
				cipher.xored(sys.argv[2],' '.join(text))
			
			elif sys.argv[1] == '--decrypt' or sys.argv[1] == '-d':
				text = [sys.argv[i] for i in range(3, len(sys.argv))]
				print('key : '+sys.argv[2])
				print('text : '+' '.join(text))
				print()
				cipher.xored(sys.argv[2],cipher.tostrings(text))
			
			else:
				print('		 \033[31m[ * ] Error Argument \033[00m')
				cipher.help()
	
	def xored(key, data):
		rep = tuple(zip(data, cycle(key)))
		final = []
		
		for (x,y) in rep:
			final.append(cipher.compare(format(ord(x),'b').zfill(8), format(ord(y),'b').zfill(8)))

		print('Xored ( Base 2)  :\n'+' '.join(final))
		print()
		
		if sys.argv[1] == '--decrypt' or sys.argv[1] == '-d':
			print('Xored ( ASCII) :\n'+cipher.tostrings(final))

	
	def compare(target, key):
		payload = []
		
		for i in range(0,8):
			if int(target[i]) - int(key[i]) == 0:
				payload.append('0')
			else:
				payload.append('1')

		return ''.join(payload)

	
	def help():
		print()
		print(r'		    \* HELP PAGE */')
		print()
		print(f'		 |=	{sys.argv[0]} --decrypt <key> <text encoded with bin> ')
		print(f' \033[34mDecrypt Command\033[00m |')
		print(f'		 |=	{sys.argv[0]} -d <key> <text encoded with bin>')
		print()
		print(f'		 |=	{sys.argv[0]} --crypt <key> <text> ')
		print(f' \033[34mCrypt Command\033[00m   |')
		print(f'		 |=	{sys.argv[0]} -c <key> <text>')
		print()
		print()
		print('	'+'='*38)
		print()
		print()

if __name__ == '__main__':
	run = cipher.launch()
