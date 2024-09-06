# Check if the user is in the HR group
def is_HR(user):
    return user.groups.filter(name='HR').exists()
