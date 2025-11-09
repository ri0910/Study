import json

# serialization
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert Python object to JSON string
# dumps stand for string
parsedjson1 =json.dumps(person, indent=4)
print(parsedjson1)
parsedjson = json.dumps(person, indent=4, separators=('; ', '= '))
print(parsedjson)


sortedJson = json.dumps(person, indent=4, sort_keys=True)
print(sortedJson)

# dump stand for file
with open('person.json', 'w') as file:
  json.dump(person, file, indent=4)
  

# Deserialization
person = json.loads(parsedjson1)
print(person)

with open('person.json', 'r') as file:
  person = json.load(file)
  print(person)

class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
user = User('Max', 27)

def encode_user(o):
  if isinstance(o, User):
    return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
  else:
    raise TypeError('Object of type User is not Json serializable')
  
userJson = json.dumps(user,default=encode_user, indent=4)
print(userJson)

from json import JSONEncoder

class UserEncode(JSONEncoder):
  
  def default(self,o):
    if isinstance(o, User):
      return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
      raise TypeError('Object of type User is not Json serializable')
    
userJson = UserEncode().encode(user)
print(userJson)

def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'], age=dct['age'])
  return dct

user = json.loads(userJson, object_hook=decode_user)
print(user)
print(type(user))
print(user.name)