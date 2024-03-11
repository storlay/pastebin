from django.contrib.auth.models import Group


def new_users_handler(backend, user, response, *args, **kwargs):
    """Adding a user to a group if they are logged in using social networks"""
    group = Group.objects.filter(name='Social')
    if len(group):
        user.groups.add(group[0])
