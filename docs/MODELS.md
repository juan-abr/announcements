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


Announcement model
    title (char field)
    description(text field)
    publication  date (pub_date) (Date Field) (day event is published) (for newsletter)
    recurring (boolean field) (True or False) (If recurring, repeat event each week)

    event date (date field) (day of the event) (True if blank)

        
Event model
    announcement (one to one field) (Announcement)
    event_date (date field)





<!-- 2020    2021
Jan     Jan
Feb     Feb
Mar     Mar
etc     etc


ArchiveIndexView
March 13, 2021 - Tournament
March 20, 2021 - Youth Class
March 22, 2021 - Breaking Presentation

February 12, 2021 - Tournament


ArchiveYearView



Home Page
=================

March:
Tournament
Youth Class
Breaking Presentation -->