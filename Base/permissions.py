# Check if the user is in the HR group
def is_HR(user):
    return user.groups.filter(name='HR').exists()or user.is_superuser
def is_Employee(user):
    return user.groups.filter(name='Employee').exists()

def is_Admin(user):
    return user.groups.filter(name = 'Admin').exists()