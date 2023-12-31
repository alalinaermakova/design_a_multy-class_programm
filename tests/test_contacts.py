from lib.contacts import Contacts

"""
Given a name and phone number as a string
We see name reflected in name and tel property
"""

def test_contacts_name_entry():
    contact = Contacts("Alina", "0777777777")
    assert contact.name == "Alina"

"""
Given a name and phone number as a string
We see phone num reflected in name and tel property
"""

def test_contacts_phone_entry():
    contact = Contacts("Alina", "0777777777")
    assert contact.tel == "0777777777"

"""
Given a name and phone number as a string
We see in #format info is reflected as a one string
"""

def test_contacts_phone_entry():
    contact = Contacts("Alina", "88890000000")
    assert contact.format() == "Alina's tel: 88890000000"