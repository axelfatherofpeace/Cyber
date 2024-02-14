
import zipfile  

def ExtractZip(Zip, password):
	try:
		Zip.extractall(pwd=bytes(password, 'utf-8'))
		return password
	except:
		print("Wrong Password")
		return
		
def main():
	Zip = zipfile.ZipFile('Test.zip')
	PassFile = open('Passlist.txt')
	for line in PassFile.readlines():
		password = line.strip('\n')
		guess = ExtractZip(Zip, password)
		if guess:
			print('Password = ' + password)
			break

if __name__ == '__main__':
	main()