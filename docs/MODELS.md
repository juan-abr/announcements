Year
    Year

    defs
    Months(Property)

Month
    Year (Foreign Key)
    Month of Year

    defs
    Events(Property) (Order by date)


Event
    Month (Foreign Key)
    Class (boolean)
    Event Date (Date Field)


== New ==


Event
    title (char field)
    description (text field)
    publication date (pub_date) (Date Field) (day event is published)
    event date (date field) (day of the event)
    recurring (boolean field) (True or False) (If recurring, repeat event each week)

