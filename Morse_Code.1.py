from MorseCodePy import encode
#from MorseCodePy import chart
# gamitin mo tong code na toh chart(dot='·') para makita yung chart for conversion

while True:
    message = input("\nInput a message: ")
    converted = encode(message, language='english')
    print(converted)
        
# download mo yung module:  https://pypi.org/project/MorseCodePy/

