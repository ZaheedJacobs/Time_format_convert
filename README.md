# Time_format_convert

The user will be asked to type in a time in a 24-hour format. The input string should have the following structure:
- "yyyy-mm-dd hh-mm"

If the input string does not match this structure, the user will be asked again for input.

After taking the string in the proper format, the program will convert it into a time in 12-hour format. An example of input/output will look like this:
- "Enter the date and time (yyyy-mm-dd hh:mm):"
- 2003-02-20 06:20
- "06:20am on 20th February '3"

What the program does is it takes the input string and splits it up into 3 substrings, each of which represents the year, month and day respectively.

Then it checks the month_nums list for the number of the user-specified month, in order to set the month number into the full name of the month.

Afterwards, it checks the day substring, converted into an integer, to find the correct day suffix (st, nd, rd or th) and adds it to the substring.

Next is the hour portion, set to an integer, to find the time suffix (am if it's between 0 and 12, and pm if it's between 12 and 24) and the hour is changed into 12-hour format (-12 hours if hour >= 13, +12 hours if hour == 0).

After all that is done, the output time string in 12-hour format is put together and returned to the main function.
