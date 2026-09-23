HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
Python version tested:

Team members and concrete contributions
---------------------------------------
We randomised which tasks each member gets.

Name: Isac
Contribution:
Task number 7
Task number 9

Name: Edvin
Contribution: 
Task number 4: consolidate_data
Task number 5: check_van_cap

Name: Gustav
Contribution:
Task number 1: menu
Task number 2: validate_reference
Task number 8: Make the console resilient

Name (if applicable): Zaid
Contribution:
Task number 3
Task number 6

Design notes
------------
Main function boundaries:

How input validation is organized: 
Gustav went over tasks 2, 3, 5 and 7 to add conditions to which values are accepted
If not accepted then user is prompted again to reenter values. 
Inputing letters instead of numbers may break code in some instances.

How shared calculations are reused:

Known limitations
-----------------
Write "None known" or describe each known limitation.
1. check_van_cap - User input lacks any sanity checks, assumes correct input.
UPDATED - Now rejects negative numbers but anything that isnt numbers breaks code. 
2. weekly_report - Not inputting numbers while still being 7 objects breaks code.
3. task-3 - Not inputting numbers breaks code.