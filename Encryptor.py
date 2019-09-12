import os
import ArmstrongManager
import ColorManager

class EncryptorA:

    def __init__(self, k):
        self.key = k
        self.XorKey = ArmstrongManager.ArmstrongManagerA.generateXORKey(self.key)
        self.cMgr = ColorManager.ColorManagerA(self.XorKey)

    def encrypt(self, srcFile, trgtFile):
        status = 0
        fhSrc = None
        fhTrgt = None
        try:
            if os.path.exists(srcFile):
                fhSrc = open(srcFile, "rb")
                fhTrgt = open(trgtFile, "wb")
                flag = True
                i = 0
                cFlag = 1

                length = len(self.XorKey)
                encoded = bytearray()

                while flag:
                    buff = fhSrc.read(2048)

                    if buff: 

                        for abyte in buff:
                            enc1 = abyte ^ int(self.XorKey[i])
                            i += 1
                            i %= length

                            enc2 = self.cMgr.colorEncode(cFlag, enc1)
                            cFlag = cFlag % 3 +1

                            encoded.append(enc2)


                        fhTrgt.write(encoded)
                        encoded.clear()
                    else:
                        flag = False

                status = 3

            else:
                status = 0 

        except IOError :
                status = 1 
        except:
                status = 2
        finally:
            if fhSrc is not  None:
                fhSrc.close()
            if fhTrgt is not  None:
                fhTrgt.close()

            return  status 


