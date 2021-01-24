# code designations
letters = {'а': '·-', 'б': '-···', 'в': '·--', 
	'г': '--·', 'д': '-··', 'е': '·', 
	'ж': '···-', 'з': '--··', 'и': '··', 
	'й': '·---', 'к': '-·-', 'л': '·-··', 
	'м': '--', 'н': '-·', 'о': '---', 
	'п': '·--·', 'р': '·-·', 'с': '···', 
	'т': '-', 'у': '··-', 'ф': '··-·', 
	'х': '····', 'ц': '-·-·', 'ч': '---·', 
	'ш': '----', 'щ': '--·-', 'ъ': '·--·-·', 
	'ы': '-·--', 'ь': '-··-', 'э': '···-···', 
	'ю': '··--', 'я': '·-·-'}

# encryption function
def encrypt():
    text = input('Введите текст: ') # enter text
    cypher = ''
    for letter in text:
        if letter != ' ':
        	# searches dictionary and adds a space
    	    cypher += letters[letter] + ' ' 

        else:
            cypher += ' '

    return cypher

# repeating    
while True:
    print(encrypt())