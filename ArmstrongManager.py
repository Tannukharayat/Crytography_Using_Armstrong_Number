class ArmstrongManagerA:
    armstrongNumber = [153, 370, 371, 407] 
    baseTable = [1234, 1243, 1324, 1342, 1423, 1432, 2134, 2143, 2314, 2341, 2413, 2431, 3124, 3142, 3214, 3241, 3412, 3421, 4123, 4132, 4213, 4231, 4312, 4321] #permutation list

    @classmethod
    def _convertKeyToNumber_(cls, key):
        total = 0
        i = 0
        keyLen = len(key)

        while i < keyLen:
            total += ord(key[i]) 
            i += 1

        return total


    @classmethod
    def _generatePermuatationKey_(cls, num):

        permutation = cls.baseTable[num % len(cls.baseTable)]

        xorKey = ''
	while permutation > 0:
            digit = permutation % 10 -1
            xorKey = str(cls.armstrongNumber[digit]) + xorKey
            permutation = permutation// 10 

        xorKey = xorKey + str(num)

        return  xorKey

    @classmethod
    def generateXORKey(cls, key):

        num = cls._convertKeyToNumber_(key)
        xorKey = cls._generatePermuatationKey_(num)
        return  xorKey

