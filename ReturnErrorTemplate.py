# Return Error Template

# You can add the utils submodule to your project to use the returnError module. Although here's a copy of it, for reference:

# Return Error
# A Library to return an HTTP response containing an error message and HTTP status 500

import json
import azure.functions as func

def returnError (msg=''):
    return func.HttpResponse(json.dumps(dict({"Response" : msg})), status_code=500)


# Now here's a usage example, in two parts:

# Part One: __init__.py
# When you let Azure create __init__ for you, it tries to package your function's return into an HTTP response. But instead, you're going to package and return the HTTP response yourself.
    if data:
        # load the json into a dict
        return func.HttpResponse(json.dumps(compareDocs(json.loads(data))))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a data in the query string or in the request body for a personalized response.",
             status_code=200
        )

# so 
return func.HttpResponse(json.dumps(compareDocs(json.loads(data))))
# ==becomes=>
return Upsert(json.loads(data))



# Part Two: The Function
# Subpart A: Try and try again!
try:
    with open(os.path.join(dataPath, 'corpusQueue.pkl'), 'rb') as f:
        corpusQueue = pickle.load(f)
except FileNotFoundError:
    corpusQueue = []
except Exception as exc:
    return returnError(str(exc))
# Here you'll want to return the result of returnError where you fail and want to catch-all.



# But where you do eventually succeed, return that HTTP response that you took out of __init__:
return func.HttpResponse(json.dumps(list([msg, data])), status_code=200)
