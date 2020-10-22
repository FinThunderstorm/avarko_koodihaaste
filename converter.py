def convert(s):
  arabic = 0

  n = len(s)

  if False:
    s = input('Anna roomalainen luku:')
  
  # määritellään roomalaisten numeroiden arvot arabialaisina numeroina
  numeri_romani = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
  }

  esiintyneet = {}

  i = 0
  while i < n-1:


    

    #print('vertailtavat:',s[i],'-',s[i+1])
    
    # Pienempi merkki isomman merkin vasemmalla puolella vähennetään isommasta, oikealla puolella oleva lisätään siihen.
    if numeri_romani[s[i]] > numeri_romani[s[i+1]]:
      #jos merkki on isompi kuin seuraava, niin pohja on s[i]
      #print(s[i],'=',numeri_romani[s[i]])
      arabic += numeri_romani[s[i]]
      i += 1
    elif numeri_romani[s[i]] < numeri_romani[s[i+1]]:
      lisattava = numeri_romani[s[i+1]]-numeri_romani[s[i]]
      #print(s[i+1],'-',s[i],'=',lisattava)
      arabic += lisattava
      i += 2
    elif numeri_romani[s[i]] == numeri_romani[s[i+1]]:
      
      romani = s[i]
      count = 2
      i += 1
      while i<n-1:
        if s[i] == s[i+1]:
          count += 1
        else:
          break
      lisattava = count * numeri_romani[romani]
      #print(lisattava)
      arabic += lisattava
    #print(arabic)
    #if i < n:
      #print('Seuraavana:',s[i],'jäljellä:',s[i:])
  return arabic
  

if __name__ == "__main__":
    #print('->', convert('MCMXCVII')) # 1997
    # 1. lisää M = 1000                -> 1000
    # 2. vähennä M-C = 1000-100 = 900  -> 1900
    # 3. vähennä C-X = 100 - 10 = 90   -> 1990
    # 4. lisää V = 5                   -> 1995
    # 5. lisää I = 1                   -> 1996
    # 6. lisää I = 1                   -> 1997



    print('->', convert('IV')) # 4
    
    
    #print('->', convert('MMMCMXCIX')) # 3999
    #print('->', convert('XXXX')) # ValueError
