import json
import urllib2


def discover():
    styles = ["Light","Medium","Heavy"]



    return dict(title="hi there",stylelist = styles)

def discovery():

    # this is the actual one ... passing the list in
    # would be possibly laborious 

    return dict()

def dbquery():
    # take the id attribute of the class tiertwo element and 
    # query the brewery db api with it. 

    # TODO - get the query from the page

    # myqurr = 

    qstr = ""
    # query = urllib.urlencode(dict(q=))

    # query the api:
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&" + "q=" + qstr + "&type=beer")