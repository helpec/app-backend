""" """

from django.test import TestCase


from ..models import HP_User, Contact, Occurrence


class HP_UserTest(TestCase):
    """ Test module for HP_User model """
    
    def test_create(self):
        
        HP_User.objects.create(
            username="testsilva",
            first_name="Test Silva",
            last_name="Silva",
            email="test@silva.com",
            phone="11 4455223366")
        user = HP_User.objects.all()[0]

        self.assertEqual(
            user.first_name, "Test Silva"
        )
    
        self.assertEqual(
            str(user), "test@silva.com"
        )

    def test_edit(self):
        HP_User.objects.create(
            username="testsilva2",
            first_name="Test Silva2",
            last_name="Silva",
            email="test2@silva.com",
            phone="11 4455223366")
        user = HP_User.objects.all()[0]
        self.assertEqual(
            user.first_name, "Test Silva2"
        )
        user.first_name = "Alterado"
        user.save()
        
        user = HP_User.objects.all()[0]
        self.assertEqual(
            user.first_name, "Alterado"
        )
        

class ContactTest(TestCase):
    """ Test module for Contact model """
    
    @classmethod
    def setUpClass(cls):
        super(ContactTest, cls).setUpClass()
        cls.user = HP_User.objects.create(
            username="user",
            first_name="User Test",
            last_name="Silva",
            email="user@silva.com",
            phone="11 4455223366")

    def test_create(self):
        Contact.objects.create(
            user=self.user,
            name="Mae User",
            phone="11 4455338877"
        )
        contact = Contact.objects.filter(user=self.user)[0]
        self.assertEqual(
            contact.name, "Mae User"
        )

        self.assertIn("user@silva.com - Mae User", str(contact))
    
    
class OccurrenceTest(TestCase):
    """ Test module for Occurrence model """
    
    @classmethod
    def setUpClass(cls):
        super(OccurrenceTest, cls).setUpClass()
        cls.user = HP_User.objects.create(
            username="user2",
            first_name="User Test",
            last_name="Silva",
            email="user@silva.com",
            phone="11 4455223366")

    def test_create(self):
        Occurrence.objects.create(
            user=self.user,
            location="Sao Paulo",
        )
        occurrence = Occurrence.objects.filter(user=self.user)[0]
        self.assertEqual(
            occurrence.location, "Sao Paulo"
        )
    
        self.assertIn("user@silva.com - ", str(occurrence))
    