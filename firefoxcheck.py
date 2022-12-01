import os
import json


dictionary = {
        "policies": {
            "Certificates": {
            "ImportEnterpriseRoots": True
            }
        }
                }

if os.path.exists("/Applications/Firefox.app/"):
    print("Firefox is installed")

    path = "/Applications/Firefox.app/Contents/Resources/distribution"
    try:
        os.makedirs(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        print("Directory already exists. Will try appending policis.json if it exists")

        if os.path.exists("/Applications/Firefox.app/Contents/Resources/distribution/policies.json"):
            print("Policies.json exists and was appended")
            json_object = json.dumps(dictionary, indent=4)
            with open("/Applications/Firefox.app/Contents/Resources/distribution/policies.json", "a") as outfile:
                outfile.write(json_object)

        else:
            print("policies.json does not exist. Will create a policies.json file")
            json_object = json.dumps(dictionary, indent=4)
            with open("/Applications/Firefox.app/Contents/Resources/distribution/policies.json", "w") as outfile:
                outfile.write(json_object)


    else:
        print ("Successfully created the directory %s " % path)
        #dictionary = {
        #"policies": {
         #   "Certificates": {
          #  "ImportEnterpriseRoots": True
           # }
        #}
        #        }
        print("Creaint policies.json file")
        json_object = json.dumps(dictionary, indent=4)
        with open("/Applications/Firefox.app/Contents/Resources/distribution/policies.json", "w") as outfile:
            outfile.write(json_object)



else:
    print("Firefox does not exist")