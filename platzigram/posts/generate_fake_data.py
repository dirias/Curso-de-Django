
"""
    Dependencies / Dependencias
    (venv) user@DESKTOP$ pip install Faker 
    Run the code in the Django shell / Correr el código en el shell de Django
    (venv) user@DESKTOP$ python3 manage.py shell
"""
#libraries
from models import User
from faker import Faker

#init
fake = Faker()

for i in range(50):
    user = User()
    full_name = fake.name().split(' ')
    user.first_name = full_name[0]
    user.last_name = full_name[1]
    user.email = f'{user.first_name.replace(" ", "_")}@email.com'
    user.password= f'{user.first_name}1234'
    user.bio = fake.text()
    #print(f'first_name: {user.last_name}, last_name{user.last_name}, email: {user.email}, password: {user.password}')
    user.save()