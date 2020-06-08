from django.test import TestCase
from .models import *

# Create your tests here.
class ProfileTestCase(TestCase):
    
    def setUp(self):
        self.new_user = User(username='deadpool', password='password')
        self.new_profile = Profile(contact_email='scarscoobydoo@gmail.com', contact_number='0798734442', bio='Just a mere bio', profile_pic='/path/example.png', owner=self.new_user)
        
    def tearDown(self):
        Profile.objects.all().delete()
        
    def create_profile(self, contact_email='scarscoobydoo@gmail.com', contact_number=236, bio='Just a mere bio', profile_pic='/path/example.png'):
        return Profile.objects.create(contact_email=contact_email, contact_number=contact_number, bio=bio, profile_pic=profile_pic)
    
    def test_profile_creation(self):
        profile = self.create_profile()
        self.assertTrue(isinstance(profile, Profile))
        self.assertEqual(profile.__str__(), profile.contact_email)
        
    def test_save_profile(self):
        self.new_user.save()
        self.new_profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        self.new_user.save()
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.filter(id=1).delete()
        
    def test_update_profile(self):
        self.new_user.save()
        self.new_profile.save_profile()
        self.new_profile.update_profile(contact_email='scarscoobydoo@gmail.com', contact_number=247, bio='Just a bio update', profile_pic='/path/example2.png')
        self.assertTrue(self.new_profile.contact_email == 'scarscoobydoo@gmail.com')
        self.assertTrue(self.new_profile.contact_number == 247)
        self.assertTrue(self.new_profile.bio == 'Just a bio update')
        self.assertTrue(self.new_profile.profile_pic == '/path/example2.png')
        
    def test_get_profile_by_id(self):
        self.new_user.save()
        self.new_profile.save_profile()
        self.new_profile.get_profile_by_id(self.new_profile.id)
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)
        

class ProjectTestCase(TestCase):
    
    def setUp(self):
        self.new_user = User(username='deadpool', password='password')
        self.new_project = Project(title='Just a title', description='Just a mere description', link='https://example.com/', owner=self.new_user)
        
        
    def create_project(self, title='Just a title', description='Just a mere description', link='https://example.com/', landing_page='/path/example.png'):
        return Project.objects.create(title=title, description=description, link=link, landing_page=landing_page)
    
    def tearDown(self):
        Project.objects.all().delete()
        
    def test_project_creation(self):
        project = self.create_project()
        self.assertTrue(isinstance(project, Project))
        self.assertEqual(project.__str__(), project.title)
        
    def test_save_project(self): 
        self.new_user.save()
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)
        
    def test_delete_project(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_project.delete_project()
        project = Project.objects.filter(id=1).delete()
        
    def test_update_project(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_project.update_project(link='Just a link update', description='Just a description update', title='Just a title update', landing_page='/path/example2.png')
        self.assertTrue(self.new_project.link == 'Just a link update')
        self.assertTrue(self.new_project.description == 'Just a description update')
        self.assertTrue(self.new_project.title == 'Just a title update')
        self.assertTrue(self.new_project.landing_page == '/path/example2.png')
        
    def test_get_project_by_id(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_project.get_project_by_id(self.new_project.id)
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)
        
    
    
class RateTestCase(TestCase):
    
    def setUp(self):
        self.new_user = User(username='deadpool', password='password')
        self.new_project = Project(title='Just a title', description='Just a mere description', link='https://example.com/', owner=self.new_user)
        self.new_rate = Rate(usability=2, design=4, content=6, owner=self.new_user)
        
    def create_rate(self, title='Just a title', description='Just a mere description', link='https://example.com/', landing_page='/path/example.png'):
        return Rate.objects.create(design=2, usability=5, content=6)
    
    def tearDown(self):
        Rate.objects.all().delete()
        
    def test_rate_creation(self):
        rate = self.create_rate()
        self.assertTrue(isinstance(rate, Rate))
        self.assertEqual(rate.__str__(), rate.design)
        
    def test_save_rate(self): 
        self.new_user.save()
        self.new_project.save_project()
        self.new_rate.save_rate()
        rates = Rate.objects.all()
        self.assertTrue(len(rates)>0)
        
    def test_delete_rate(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_rate.save_rate()
        self.new_rate.delete_rate()
        rate = Rate.objects.filter(id=1).delete()
        
    def test_update_rate(self):
        self.new_user.save()
        self.new_project.save_project()
        self.new_rate.save_rate()
        self.new_rate.update_rate(content=10, design=10, usability=10)
        self.assertTrue(self.new_rate.content == 10)
        self.assertTrue(self.new_rate.usability == 10)
        self.assertTrue(self.new_rate.design == 10)
    