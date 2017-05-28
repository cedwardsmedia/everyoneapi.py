# EveryoneAPI.py v0.1.0-dev

[![Source](https://img.shields.io/badge/source-cedwardsmedia/everyoneapi.py-blue.svg?style=flat-square "Source")](https://www.github.com/cedwardsmedia/everyoneapi.py)
[![Version](https://img.shields.io/badge/version-0.1.0--dev-brightgreen.svg?style=flat-square)]()
[![License](https://img.shields.io/badge/license-BSD-lightgrey.svg?style=flat-square "License")](./LICENSE.md)
[![Gratipay](https://img.shields.io/gratipay/cedwardsmedia.svg?style=flat-square "License")](https://gratipay.com/~cedwardsmedia/)

_EveryoneAPI.py_ is a Python 3 module for querying EveryoneAPI. It is based on [EveryonePHP](https://github.com/cedwardsmedia/everyonephp) and was written to provide a Python class for EveryoneAPI as well as a Python learning project for myself.

In order to use _EveryoneAPI.py_, you must have an [EveryoneAPI account](https://www.everyoneapi.com/sign-up)  with [available funds](https://www.everyoneapi.com/pricing).


## Usage

I have never been a great programmer. As such, I strived to make EveryoneAPI.py as simple to use as possible and I'm always looking to simplify it even more. Let's build a basic EveryoneAPI client using EveryoneAPI.py:

### Step 1: Import the EveryoneAPI module and instantiate the object
```python3
# Import EveryoneAPI
import everyoneapi

# Instantiate EveryoneAPI
api = everyoneapi.EveryoneAPI()
```
Creating a new EveryoneAPI.py object allows us to interact with the class.

### Step 2: Set EveryoneAPI Credentials
```python3
# Set EveryoneAPI Credentials
api.sid = "9e3cef42da225d42bd86feaa80ff47";
api.token = "65f3ef01462c62f7f4ce7d2156ceee";
```
EveryoneAPI.py needs these credentials in order to query EveryoneAPI. Otherwise, the query will fail. How you obtain and store these credentials is completely up to you, just be sure to set them for each instance of EveryoneAPI.py before calling `query()`.

### Step 3: Set EveryoneAPI Data Points
```python3
// Set EveryoneAPI Data Points
data = array("name", "profile", "cnam", "gender", "image", "address", "location", "line_provider", "carrier", "carrier_o", "linetype");
```
Each data point is optional and all data points are returned by default, unless otherwise specified. In the same way EveryoneAPI uses a comma separated list of identifiers, EveryoneAPI.py uses a simple array to specify the data points you wish to retrieve. EveryoneAPI.py passes these identifiers directly to EveryoneAPI so you will use the same identifiers here as you would in a cURL request.

For a full list of available Data Points, check the [EveryoneAPI Docs](https://www.everyoneapi.com/docs#data-points).

### Step 4: Perform EveryoneAPI Query
```python3
// Perform EveryoneAPI query
api.query(phone, data);
```
Only `$phone` is required for this function. The function performs the query against EveryoneAPI and stores the results in a dict, in this example, `api.data`.

### Step 5: Print the Results
```python3
// Print results

// Print first name
print("Name: " + api.results['data']['expanded_name']['first'])

// Print last name
print("Name: " + api.results['data']['expanded_name']['last'])

// Print carrier name
print("Name: " + api.results['data']['carrier']['name'])
```
EveryoneAPI.py converts the JSON response from EveryoneAPI into a dict. This allows us to access the entire response for our application. In the above example, we print the first name, last name, and carrier for the given phone number.

### Optional: Error Checking
```python3
// Check for Error
if (api.error):                     // If there's an error
    print("Error: " + api.error)    // Print it out
    exit(1)                         // Exit with status 1
```
EveryoneAPI.py will assign error messages, if one occurs, to `api.error`. You can use this in an `if` statement, as shown above, to halt your application if something has gone wrong.

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request ^^,

## Credits
Concept and original codebase: Corey Edwards ([@cedwardsmedia](https://www.twitter.com/cedwardsmedia))

Optimization and Debugging: Brian Seymour ([@eBrian](http://bri.io))

## License
_EveryoneAPI.py_ is licensed under the **BSD Simplified License**. See LICENSE for more.

---
**Disclaimer**: _EveryoneAPI.py_ is not endorsed by, sponsored by, or otherwise associated with [OpenCNAM](http://www.opencnam.com), [EveryoneAPI](http://www.everyoneapi.com), or [Telo USA, Inc](http://www.telo.com).
