## Test Cases - Login Page

| Feature | Description | Steps To Execute | Expected Results |
| ---- | ---- | ---- | ---- |
| User Interface| Check all the text boxes, buttons, etc. | 1. Check Page | • UI should be perfect • Text boxes and buttons should be aligned |
| Required Fields | Check the required fields by not filling in any data. | 1. Enter an invalid username <br> 2. Enter the correct password <br> 3. Click on Login Button | User should not log in and should show proper error message |
| User Login | Check When passing a correct username and invalid password | 1. Enter a valid username <br> 2. Enter an incorrect password <br> 3. Click on Login Button | User should not log in and should show proper error message |
| User Interface | Check Keeping Password | 1. Enter a valid username <br> 2. Do not enter a password <br> 3. Click on Login Button | User should not log in and should show proper error message |
| User Login | Check when pass correct email and password | 1. Enter a valid username <br> 2. Enter a valid password <br> 3. Click on Login Button | User should log in |
| User Login | Check if the password is entered in encrypted | 1. Enter a valid username <br> 2. Enter password <br> 3. Click on Login Button | Password is entered in encrypted form |
| Signup Option for new users | Check whether the signup link for the new user is working | Click Signup link | Clicking the signup link takes the user to the signup side successfully |
| Required Fields | Verify if blank spaces are passed in required fields. | 1. Go to the Site. <br> 2. Passed blank spaces in required fields. <br> 3. Click on the Login button | Those Blank spaces should trim and the Validation error message for required fields should visible. |