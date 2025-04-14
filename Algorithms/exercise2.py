def get_reg_hours(hours):
    if hours <= 40:
        return hours
    else:
        return hours


print(get_reg_hours(45))
# Output: 40
