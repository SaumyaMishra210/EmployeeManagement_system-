# context_processors.py
def is_hr_context(request):
    """
    Returns a context dictionary with is_HR value,
    indicating whether the logged-in user is an HR.
    """
    is_HR = False
    if request.user.is_authenticated:
        # Replace 'hr' with the actual role or condition to check if the user is HR.
        is_HR = request.user.groups.filter(name='HR').exists()  # Update as per your logic

    return {'is_HR': is_HR}
