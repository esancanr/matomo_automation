import requests

# Global variables
URLMatomo = "<Url Matomo>"
tokenAuth = "<Token Matomo>"

# Variables
siteName = "<Site name>"
siteURL = "<Site link>"
username = "<Username>"
password = "<Password>"
descriptionToken = "<Token Description>"
email = "<Email>"

# Optional
currency = "<Currency>"
timezone = "<Time zone>"

def getData(url, params):
    response = requests.get(url, params)
    data = response.json()
    return data

def createSiteParams (tokenAuth, URLMatomo): 
    params = {
    'module': 'API',
    'method': 'SitesManager.addSite',
    'siteName': siteName,
    'urls': siteURL,
    'format': 'json',
    'token_auth': tokenAuth,
    # Optional
    'currency': currency,
    'timezone': timezone,
}

    data = getData{urlMatomo, params}
    siteId = data['value']
    return siteId

def createUserParams (tokenAuth, URLMatomo, siteId):
    params = {
    'module': 'API',
    'method': 'UsersManager.addUser',
    'userLogin': username,
    'password': password,
    'format': 'json',
    'token_auth': tokenAuth,
    'email': email,
    'initialSite': siteId,
}

    data = getData{urlMatomo, params}
    return username, password

def createTokenParams (tokenAuth, URLMatomo, username, password)
    params= {
    'module': 'API',
    'method': 'UsersManager.createAppSpecificTokenAuth',
    'userLogin': username,
    'passwordConfirmation': password,
    'description': descriptionToken,
    'format': 'json',
    'token_auth': tokenAuth,
}   

    data = getData{urlMatomo, params}
    token = data['value']
    return token

print("site response:", siteId)
print("user response:", username)
print("password response:", password)
print("token response:", token)
