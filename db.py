import pymongo
import sys
import base64
import gridfs
import os
try:
    client = pymongo.MongoClient('mongodb+srv://pttsbyk:TqKnNhWREBkkdYOu@cluster0.idlutxe.mongodb.net/?retryWrites=true&w=majority')
except pymongo.errors.ConfigurationError:
    print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
    sys.exit(1)

db = client.bbreeds

birdInfo = db["birdInfo"]

def addBirdInfo(document):

    # document = [{"name":"Alexandrine Parakeet"},
    #             {"name":"Plum-headed Parakeet"},
    #             {"name":"Derbyan Parakeet"},
    #             {"name":"Moustached Parakeet"}]
    document = [{"name":"", "price":0,"images":[]}]

    try:
        result = birdInfo.insert_many(document)
    except pymongo.errors.OperationFailure:
        print("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
        # sys.exit(1)
        return {'status':False}
    else:
        inserted_count = len(result.inserted_ids)
        text = "%x new types have been added." %(inserted_count)
        return {'text':text,'status':True}
    
def getAllBird():

    myCursor = birdInfo.find()

    if myCursor:
        result = list(myCursor)
        return result
    else:
        return ""

def getAllMainBreeds():

    myCursor = birdInfo.find()

    if myCursor:
        result = list(myCursor)
        return result
    else:
        return ""
    
# def getBirdInfo(bird_id):

#     myCursor = birdInfo.find()

#     if myCursor:
#         result = list(myCursor)
#         return result
#     else:
#         return ""

# addBirdInfo("")

# try:
#     document = {"name":"unnamed-1", "price":0,"images":[]}
#     fs = gridfs.GridFS(db, "birdInfo")

#     image_files = ["static/images/S__7864344_0_6_11zon.jpg","static/images/S__7864346_0_7_11zon.jpg"]

#     for file in image_files:
#         if os.path.exists(file):
#             with open(file, 'rb') as f:
#                 image_data = f.read()
            
#             # Store each image as an object within the 'images' array
#             # image_object = image_data
            
#             # Append the image object to the 'images' array
#             document['images'].append(image_data)
#         else:
#             raise FileNotFoundError(f"File not found: {file}")
#     # Insert the document into the MongoDB collection
#     birdInfo.insert_one(document)
#     print("Images stored successfully.")
# except Exception as e:
#     print(f"An error occurred: {e}")

try:
    document = [{"name":"unnamed-1", "price":0,"images":[]},
                {"name":"unnamed-2", "price":0,"images":[]},
                {"name":"unnamed-3", "price":0,"images":[]},
                {"name":"unnamed-4", "price":0,"images":[]},
                {"name":"unnamed-5", "price":0,"images":[]},
                {"name":"unnamed-6", "price":0,"images":[]},
                {"name":"unnamed-7", "price":0,"images":[]},
                {"name":"unnamed-8", "price":0,"images":[]},
                {"name":"unnamed-9", "price":0,"images":[]},
                {"name":"unnamed-10", "price":0,"images":[]},
                {"name":"unnamed-11", "price":0,"images":[]},
                {"name":"unnamed-12", "price":0,"images":[]},]
    fs = gridfs.GridFS(db, "birdInfo")

# change imagessssssssssssssssssssssssss
    image_files = [["static/images/S__7864344_0_6_11zon.jpg","static/images/S__7864346_0_7_11zon.jpg"], #body: green, head: black
                   ["static/images/S__7864350_0_10_11zon.jpg"], #body: yellow, wings: green, head: high
                   ["static/images/S__7864353_0_12_11zon.jpg"], #small bule black eyes
                   ["static/images/S__7864354_0_13_11zon.jpg"], #pure white body, pink-whote mouth
                   ["static/images/S__7864355_0_14_11zon.jpg","static/images/S__7864357_0_41_11zon.jpg", "static/images/S__7864359_0_16_11zon.jpg"], #body: yellow head orange
                   ["static/images/S__7864360_0_17_11zon.jpg","static/images/S__7864362_0_18_11zon.jpg"], #body green, mouth: yellow-orange, in-wing: blue, out-wing: green
                   ["static/images/S__7864370_0_44_11zon.jpg","static/images/S__7864346_0_7_11zon.jpg", "static/images/S__7864388_0_36_11zon.jpg"], #body yellow, head: orange-yellow
                   ["static/images/S__7864371_0_24_11zon.jpg","static/images/S__7864372_0_25_11zon.jpg"], #body: dark green, head: interporate yelow and orange
                   ["static/images/S__7864373_0_26_11zon.jpg","static/images/S__7864386_0_35_11zon.jpg", "static/images/S__7864392_0_38_11zon.jpg", "static/images/S__7864392_0_38_11zon.jpg","static/images/S__7864394_0_4_11zon.jpg", "static/images/S__7864395_0_5_11zon.jpg"], #body white, black mouth
                   ["static/images/S__7864380_0_30_11zon.jpg"], # body/head: orange-yellow, tail: green
                   ["static/images/S__7864382_0_32_11zon.jpg"], # body:green, head: green-blue-yellow
                   ["static/images/S__7864384_0_33_11zon.jpg", "static/images/S__7864385_0_34_11zon.jpg"], #body: yellow, under neck: yellow
                   ]
    i = 0
    for doc in document:
        for file in image_files[i]:
            if os.path.exists(file):
                with open(file, 'rb') as f:
                    image_data = base64.b64encode(f.read()).decode('utf-8')
                    # print(base64.b64encode(image_data))
                    # print(base64.b64encode(image_data).decode('utf-8'))
                # Store each image as an object within the 'images' array
                # image_object = image_data
                
                # Append the image object to the 'images' array
                doc['images'].append(image_data)
            else:
                raise FileNotFoundError(f"File not found: {file}")
        i+=1
    # print(len(document[0]["images"]))
    # Insert the document into the MongoDB collection
    # birdInfo.insert_many(document)
    print("Images stored successfully.")
except Exception as e:
    print(f"An error occurred: {e}")