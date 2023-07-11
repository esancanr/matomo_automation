# **Matomo site, user and token creation automation**

This repository contains code to automate the creation of user, site, token in Matomo Analytics.

To execute this code using python, it's necessary to download the **'request'** library.

Run this line of code in the terminal to install the request library:
```
pip install requests
```
For this to work you must have the url that matomo gives you and the authentication token which you can get in the matomo analytics settings.

## **Important**
If you want to create the site with multifactor authentication (MFA) enabled you must disable it, because creating the site with MFA enabled will give you an error which does not allow you to get the site ID.
