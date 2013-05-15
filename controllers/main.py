# from brewerydb import *
# BreweryDb.configure("72166c358bc617ab5c18ecf67630a322",["http://api.brewerydb.com/v2/"])
import json
import urllib2
# import requestdir


# use this as an example:
# http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&q=guinness&type=beer

def beerprofile():

    # form=FORM('Brewery Database url:', INPUT(_name='url'), INPUT(_type='submit'))
    # return dict(form=form)

    # print BreweryDb.beers()

    return dict()

def echo():
    query = "q=" + request.vars.name

    pquerystring = "http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&" + query + "&type=beer"

    return pquerystring


def dbquery():
    query = "q=" + request.vars.name
    # make query
    # query = urllib.urlencode(dict(q="blue angel", rpp=5, include_entities=1,
    #                           result_type="mixed"))  
    # make request
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&" + query + "&type=beer")


    # print resp
    # make dictionary (parse json response)
    d = json.load(resp)
    print d
    return d

def locator():
    form = SQLFORM(db.location)
    return dict(form=form)

