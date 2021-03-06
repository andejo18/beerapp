# from brewerydb import *
# BreweryDb.configure("72166c358bc617ab5c18ecf67630a322",["http://api.brewerydb.com/v2/"])
import json
import urllib2



# use this as an example:
# http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&q=guinness&type=beer

def beerprofile():

    # form=FORM('Brewery Database url:', INPUT(_name='url'), INPUT(_type='submit'))
    # return dict(form=form)

    # print BreweryDb.beers()

    return dict(results="make a search, already!")

def echo():
    query = "q=" + request.vars.name

    pquerystring = "http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&" + query + "&type=beer"

    return pquerystring



def dbquery():
    # initialize information about the beer
    import gluon.contrib.simplejson

    query = "q=" + request.vars.name
    # make query
    # query = urllib.urlencode(dict(q="blue angel", rpp=5, include_entities=1,
    #                           result_type="mixed"))  
    # make request
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&" + query + "&type=beer")

    # make dictionary (parse json response)
    d = json.load(resp)
    print
    return d


def dumper():
    names = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    import gluon.contrib.simplejson
    return gluon.contrib.simplejson.dumps(names)


def locator():
    reference=urllib2.urlopen("https://maps.googleapis.com/maps/api/place/details/json?reference=CoQBegAAAKTLGPNK5WrDyrG5aEPkn6vkAyrf_nERYb58fP70u5Xjl6kCCtgQVO39pMVG3KTS1VLaAUho0NzFyPkgWQGowBvY-b3UQymN3BN2nCSgOpJ__VBkHkBaZF7CxgE5Om6xhx1h20pP1p1L2XspyMEpM-G2TSHf2x3_cWRGHuSly0oQEhAN-d2NuwCr-d52HSRXGkgRGhQATBnAoQ2YHItcgODyL_iTGYLLjA&sensor=true&key=AIzaSyDcTWUD6SC5iapjaIIbMoXoMzn_cyQl-6U")
    mydict= json.load(reference)
    return dict(mydict = mydict)

