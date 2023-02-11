month = {'01': 'January',
         '02': 'February',
         '03': 'March',
         '04': 'April',
         '05': 'May',
         '06': 'June',
         '07': 'July',
         '08': 'August',
         '09': 'September',
         '10': 'October',
         '11': 'November',
         '12': 'December'}
status = {True: "rented", False: "not rented"}


class DVD:

    def __init__(self, name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.dvd_id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls,dvd_id: int, name: str, date: str, age_restriction: int):
        day, creation_month, creation_year = date.split(".")
        return cls(name, dvd_id, creation_year, month[creation_month], age_restriction)

    def __repr__(self):
        return f"{self.dvd_id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {status[self.is_rented]}"
