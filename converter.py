# Aloitettu 14:22

def checkValidity(s):
    valid = False
    numeri_romani = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    }
    n = len(s)
    
    loop_validity = True

    chars = {}

    for i in range(n):
        #check for over 3 same chars in a row
        if s[i] not in chars:
            chars = {}
            chars[s[i]] = 0
        chars[s[i]] += 1
        if chars[s[i]] > 3:
            loop_validity = False
        
        #check for unvalid format
        if i < n-1:
          if numeri_romani[s[i+1]] // numeri_romani[s[i]] > 10:
            loop_validity = False

        #check not valid chars
        if s[i] not in numeri_romani:
            loop_validity = False
            break
    
    if n > 0 and loop_validity == True:
        return True
    else:
        return False


def convert():
    arabic = 0
    numeri_romani = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
    }
    
    isValid = False
    while isValid == False:
        s = input('Anna roomalainen luku: ')
        n = len(s)
        if checkValidity(s) == True:
          isValid = True
        else:
          print('Syöttämäsi roomalainen luku oli virheellinen. Tarkasta syöte.')


    if n == 1:
        arabic += numeri_romani[s[0]]
    else:
        i = 0
        while i < n-1:
            if numeri_romani[s[i]] > numeri_romani[s[i+1]]:
                arabic += numeri_romani[s[i]]
                i += 1
            elif numeri_romani[s[i]] < numeri_romani[s[i+1]]:
                to_add = numeri_romani[s[i+1]]-numeri_romani[s[i]]
                arabic += to_add
                i += 2
            elif numeri_romani[s[i]] == numeri_romani[s[i+1]]:  
                romani = s[i]
                count = 2
                i += 1
                while i<n-1:
                    if s[i] == s[i+1]:
                        count += 1
                        i += 1
                    else:
                        i += 1
                        break
                to_add = count * numeri_romani[romani]
                arabic += to_add
    print(arabic)
  

if __name__ == "__main__":
    convert()

# Kuinka tekisin globaalisti skaalautuvan ratkaisun?
# 
# Vastaus: Tekisin ReactJS -frontend + Node.js -backendin päälle verkkopalvelun, jolla tarkastettaisiin luvut.
