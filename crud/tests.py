import pytest
from django.urls import reverse
from .models import Member

@pytest.mark.django_db
def test_create_member(client):
    response = client.post('/crud/create', {
        'firstname': 'John',
        'lastname': 'Doe'
    })
    assert response.status_code == 302
    assert Member.objects.count() == 1
    member = Member.objects.first()
    assert member.firstname == 'John'
    assert member.lastname == 'Doe'

@pytest.mark.django_db
def test_update_member(client):
    member = Member.objects.create(firstname='Old', lastname='Name')
    response = client.post(f'/crud/edit/update/{member.id}', {
        'firstname': 'New',
        'lastname': 'Name'
    })
    assert response.status_code == 302
    member.refresh_from_db()
    assert member.firstname == 'New'

@pytest.mark.django_db
def test_delete_member(client):
    member = Member.objects.create(firstname='Delete', lastname='Me')
    response = client.post(f'/crud/delete/{member.id}')
    assert response.status_code == 302
    assert Member.objects.count() == 0
