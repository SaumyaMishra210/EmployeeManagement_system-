import random
from calendar import monthrange
from datetime import datetime
from attendance.models import Attendance
from accounts.models import UserProfile  # Adjust import based on your project structure

def generate_random_attendance(user, year, month):
    """
    Generates random attendance data for a given user, year, and month.
    Only generates data if it doesn't already exist for that month.
    Only generates data up to the current date.
    """
    # Check if attendance data for this user, year, and month already exists
    existing_records = Attendance.objects.filter(user=user, date__year=year, date__month=month)

    if existing_records.exists():
        print(f"Attendance data already exists for {user} in {year}-{month}. Fetching existing data.")
        return

    # Get the number of days in the specified month
    days_in_month = monthrange(year, month)[1]

    # Determine today's date and limit it to the end of the current month
    today = datetime.today().date()
    end_date = min(today, datetime(year, month, days_in_month).date())

    attendance_types = ['present', 'absent', 'late', 'early']

    attendance_list = []

    for day in range(1, days_in_month + 1):
        date = datetime(year, month, day).date()

        # Only generate data for days up to today
        if date > end_date:
            break

        # Randomly choose an attendance type for each day
        attendance_type = random.choice(attendance_types)

        # Prepare the attendance record to be saved
        attendance_list.append(
            Attendance(
                user=user,
                date=date,
                attendance_type=attendance_type
            )
        )

    # Bulk create the attendance records to optimize database interaction
    Attendance.objects.bulk_create(attendance_list)

    print(f"Generated random attendance data for {user} in {year}-{month}.")
    # return Attendance.objects.filter(user=user, date__year=year, date__month=month)
