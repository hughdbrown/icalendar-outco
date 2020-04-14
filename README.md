# icalendar file for Outco
We have events. There is no .ICS file so that we can import into web calendars.

So I made a program that generates most of the calendar.

# Using this program
- Clone the repo
- In a system prompt, cd to the correct directory
- Run the command `./icalendar.py > a.ics`
- Open Chrome
- Open the calendar in Chrome
- In `Other calendars`, press the plus-sign `Add other calendars`
- Select `Import`
- Select `Select file from your computer`
- Navigate to the directory where the repo was cloned to
- Select `a.ics`
- Press `Import` button

# Screen share of import
Here’s what it looks like when you generate the ICS file and import into Chrome:
https://drive.google.com/file/d/1302IbQR_Fptc_TnuwIqvBq0j7ILSTIcK/view

# Disclaimers
- This data is incomplete.
- This data is probably wrong.
- If you want to help with this, please generate a pull request and I’ll see about merging your changes.
- Please change only the `events.json` file.
