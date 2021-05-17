Installation
-----

- git clone https://github.com/k0inwork/test_PDU
- cd test_PDU
- cd website1
- pip install -r requirements.txt
- python3 manage.py runserver

Functionality
-----

Backend http://127.0.0.1:8000/admin - manage PDUs (admin site) (also used to login/logout users)

Only user - admin/admin

Frontend http://127.0.0.1:8000/site/pdus
____


Shows list of PDUs and their positions on the map

"Play" button moves center of the map to the PDU

"Stop" button disables the PDU
