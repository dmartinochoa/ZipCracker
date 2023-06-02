import pyzipper

def extract_file(zip, password):
    try:
        zip.extractall(pwd=password.encode())
        return True  # Return True if password is correct
    except RuntimeError as e:
        if 'Bad password' in str(e):
            return False  # Return False if password is incorrect
        raise  # Reraise other runtime errors

def main():
    with pyzipper.AESZipFile('testAES.zip') as zip:
        pass_file = open('wordlist.txt', encoding='utf-8')
        for line in pass_file.readlines():
            password = line.rstrip('\n')
            print('Attempting with: ' + password)
            if extract_file(zip, password):
                print('Password found: ' + password)
                break

        pass_file.close()

if __name__ == '__main__':
    main()
