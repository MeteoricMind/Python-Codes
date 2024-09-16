book= {}
book['Tom'] = {
    'name': 'Tom',
    'address' : 'red streat',
    'phone' : 68926783
}
book['bob'] = {
    'name' : 'bob',
    'address' : 'green streat',
    'phone' : 45678909
}

import json
s = json.dumps(book)
print(s)