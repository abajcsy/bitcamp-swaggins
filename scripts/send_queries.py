from metamind.api import ClassificationData, ClassificationModel, set_api_key, general_image_classifier

set_api_key("uqXM0XTScBW2y46BI5BSiWpRXLYjEsyEatyYw60zyEpH76KyRf")
classifier = general_image_classifier

jpgs = []    #List of inputs to the classifier, to be populated by video grabs
results = {} #Mapping from input (url? jpg?) to [probability, label]
labels = {}  #Mapping from label to [[inputs][probabilities]]

#Sample data
jpgs.append('../resources/hamburger.jpg')
jpgs.append('../resources/lock.jpg')
jpgs.append('../resources/fire.jpg')

#Get base64 encoding, which allows an image to work as a URL
def toBase64 (jpg):
    with open(jpg, "rb") as f:
        data = f.read()
        data_string = data.encode("base64")
        return data_string

def loop ():
    while (len(jpgs) > 0):
        print "Hi!"
        input = jpgs.pop()
        base64 = toBase64(input)
        output = classifier.predict(['data:image/lock.jpg;base64,'+ base64], input_type='urls')
        probability = output[0].get(u'probability')
        label = output[0].get(u'label')
        results[input] = [probability, label]
        if labels.has_key(label):
            labels[label][0].append(input)
            labels[label][1].append(probability)
        else:
            labels[label] = [[input],[probability]]
        print 'Results[',input,']: ', results[input]
        print 'Labels[',label,']: ', labels[label]

loop() #MAKE IT GO!

#Using the classifier on a bunch of URLs, successful
#print classifier.predict(['http://img.foodnetwork.com/FOOD/2012/12/13/HE_Gift-Cookies-baked_s4x3_lead.jpg'], input_type='urls')

#Using the classifier on jpgs or pngs, which is BROKEN!!! Must call toBase64
#print classifier.predict(['combo-lock.png'], input_type='files')
