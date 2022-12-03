## Test Cases - Registration Page

| Feature | Description | Steps To Execute | Test Data / Input | Expected Results |
| ---- | ---- | ---- | ---- | ---- |
| User Interface| Check all the text boxes, buttons, etc. | 1. Click on buttons, and text boxes | N/a | Ui should be perfect |
| Required fields | Check the required fields by not filling any data | 1. Do not enter any value in the field. <br> 2. Click on the Register button. | N/a | It redirects to an error page |
| Required fields | Check user should Register by filling all the required fields | 1. Enter valid values in the required fields. <br> 2. Click the Register button. | N/a | 1. Users should be registered successfully. |
| Email validation | • Check the Email text field that has an Email address without @ symbol. • Check the Email text field that has @ symbol written in words. • Check the Email text field that has a missing dot in the email address. | 1. Enter Invalid Emails <br> 2. Click on the Register Button. | 1.testemail.com <br> 2.testatemail.com <br> 3.test@emailcom | It should show the validation message for a valid email (If we do not write '.' the validiation message  is not displayed.)|
| Email validation| Check all the valid emails | 1. Enter valid Emails <br> 2. Click on the Register Button. | 1.test.email@email.com <br> 2.test@email.com | It should not show any validation message |
| Password Validation| Check if password field is empty | Enter nothing | N/a | Successful registration |