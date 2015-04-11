from metamind.api import ClassificationData, ClassificationModel, set_api_key, general_image_classifier

set_api_key("uqXM0XTScBW2y46BI5BSiWpRXLYjEsyEatyYw60zyEpH76KyRf")
classifier = general_image_classifier

jpgs = []    #List of inputs to the classifier, to be populated by video grabs
results = {} #Mapping from input (url? jpg?) to [probability, label]
labels = {}  #Mapping from label to [[inputs][probabilities]]

#Sample data
jpgs.append('http://img.foodnetwork.com/FOOD/2012/12/13/HE_Gift-Cookies-baked_s4x3_lead.jpg')
jpgs.append('http://image.made-in-china.com/2f0j00mMNEsVDarHbj/Combination-Lock-5250-.jpg')
jpgs.append('http://www.psdgraphics.com/file/combination-padlock-icon.jpg')

while (len(jpgs) > 0):
    print "Hi!"
    input = jpgs.pop()
    output = classifier.predict([input], input_type='urls')
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

#Using the classifier on a bunch of URLs, successful
#print classifier.predict(['http://img.foodnetwork.com/FOOD/2012/12/13/HE_Gift-Cookies-baked_s4x3_lead.jpg', 'http://image.made-in-china.com/2f0j00mMNEsVDarHbj/Combination-Lock-5250-.jpg', 'https://kevinberardinelli.files.wordpress.com/2009/12/combo-lock.png'], input_type='urls')

#Using the classifier on jpgs or pngs, which is sometimes BROKEN!!!
#print classifier.predict(['combo-lock.png'], input_type='files')
