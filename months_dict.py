
month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(month_conversions["Feb"])
print(month_conversions.get("Mar"))
print(month_conversions.get("Blah"))
print(month_conversions.get("Blah", "None of value"))
print(month_conversions.keys())
print(month_conversions.values())
