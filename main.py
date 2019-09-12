import Encryptor
import Decryptor
import time

def main():

    e = Encryptor.EncryptorA("Cryptography using armstrong number")
    d = Decryptor.DecryptorA("Cryptography using armstrong number")

    print(time.time())
    flag = e.encrypt("e:\\photo.jpg", "e:\\tmp.jpg")#("e:\\b.mp4", "e:\\b99.mp4")
    print(time.time())

    if flag == 3:
        flag = d.decrypt("e:\\tmp.jpg", "e:\\new.jpg")#("e:\\b99.mp4", "e:\\bAgain.mp4")
        print(time.time())
        if flag == 3:
            print("DONE")


main()
