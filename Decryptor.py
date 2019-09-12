import os
import ArmstrongManager
import ColorManager

class DecryptorA:

    def __init__(self, k):
        
        self.key = k
        self.XorKey = ArmstrongManager.ArmstrongManagerA.generateXORKey(self.key)
        self.cMgr = ColorManager.ColorManagerA(self.XorKey)

    def decrypt(self, encodedFile, orgiginalFile):
        status = 0
        fhSrc = None
        fhTrgt = None
        try:
            if os.path.exists(encodedFile):
               
                fhEncoded = open(encodedFile, "rb")

                fhOriginal = open(orgiginalFile, "wb")

                flag = True
                i = 0
                cFlag = 1

                length = len(self.XorKey)
                decoded = bytearray()

                while flag:
                    buff = fhEncoded.read(2048)

                    if buff: 

                        for abyte in buff:
                            dec2 = self.cMgr.colorDecode(cFlag, abyte)
                            cFlag = cFlag % 3 + 1

                            dec1 = dec2 ^ int(self.XorKey[i])
                            i += 1
                            i %= length


                            decoded.append(dec1)


                        fhOriginal.write(decoded)
                        decoded.clear()
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
            if fhEncoded is not  None:
                fhEncoded.close()
            if fhOriginal is not  None:
                fhOriginal.close()

            return  status 


