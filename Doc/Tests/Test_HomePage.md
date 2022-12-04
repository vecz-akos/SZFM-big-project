## Test Cases - Home page

| Feature | Description | Steps To Execute | Expected Results |
| ---- | ---- | ---- | ---- |
| Category missing | User get an error message, if admin dont fill minimum one category. | Go to a link localhost/home | User get error message |
| Data Upload | Admin can upload categories and samples | 1. Go to a link localhost/admin <br> 2. Log in | Load admin page and admin can fill data |
| Sample missing | User load the home page and see if the category is dont fill | Go to a link localhost/home | User see the empty message |
| Sample not missing | User load the home page and see the sample at the bottom of the categories | Go to a link localhost/home | User see the fill categories with samples |
| Menu bar check | Check user name and all button | Check Menu bar | User should use Home and Recommended, Log-Out button |
| Open Menu bar | The menu bar can be opened with the arrow | 1. Click the arrow on the Menu bar | More data is displayed in the menu bar |
| Category Page | Load Category Page | Click on one of the categories card | User can see the Category Page |
| Recommended Page | Load Recommended Page | Click Recommended button on the Menu bar | User can see the Recommended Page |
| Log Out | The User exits his account | Click Log Out button at the bottom of the menu bar | User can logout his account |
| User name check | The User name display at the top of the Menu bar | 1. Click the arrow on the Menu bar <br> 2. Check name at the top of the Menu bar | User name matches |