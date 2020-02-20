from instagram import InstaBot
import config as cf

def main():
    while True:
    a = input('Do you want to login? (y/n): ')
    if a == 'y':
        login = input('input login: \n')
        password = input('input password: \n')
        my_bot = InstaBot(login, password)
        with open('file.txt', 'w') as f:
            f.writelines(my_bot.get_unfollowers())
        break
    elif a == 'n':
        username = input('Input your username: \n')
        my_bot = InstaBot(cf.username, cf.password)
        kek = my_bot.get_unfollowers(False, username)
        print(kek)
        with open('file.txt', 'w') as f:
            for i in kek:
                f.write("%s\n" % i)
        break
    else:
        pass

if __name__ == '__main__':
    main()