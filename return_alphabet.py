def return_alphabet(i,a = None):
    list_upcase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    list_downcase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if a == 'A':
        return list_upcase[i]
    else:
        return list_downcase[i]
    