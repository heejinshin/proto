# 생성된 Person 클래스를 이용하여 객체를 만들고, 값을 지정한 후 이를 파일로 저장하는 예제
import address_pb2

person = address_pb2.Person()
person.name = 'Terry'
person.age = 42
person.email = 'terry@mycompany.com'

try:
 f = open('myaddress','wb')
 f.write(person.SerializeToString())
 f.close()
 print('file is wriiten')

except IOError:

 print('file creation error')
 print(person.name)
 print(person.age)
 print(person.email)


from google.protobuf.json_format import MessageToJson
jsonObj = MessageToJson(person)
print(jsonObj)