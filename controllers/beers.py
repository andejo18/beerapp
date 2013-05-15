import json
import urllib2

response.title = "Choose Your Destiny(Beer)!"
response.subtitle = "...Or not, It's cool."




def discover():
    styles = ["Light","Medium","Heavy"]
    return dict(title="hi there",stylelist = styles)

def discovery():

    # this is the actual one ... passing the list in
    # would be possibly laborious 

    return dict(respd="")

def datquery():
    # take the id attribute of the class tiertwo element and 
    # query the brewery db api with it. 

    # TODO - get the query from the page

    # myqurr = 
    beerlist = []

    # print response.vars.name

    qstr = "coors light"
    # query = urllib.urlencode(dict(q=))
    print "tits"
    # query the api:
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/search/?key=72166c358bc617ab5c18ecf67630a322&" + "q=" + qstr + "&type=beer")

    # make dictionary of the response. 
    respd = json.load(resp)
    
    beerdict = respd.items()[3][1]
    
    for abeer in beerdict:
        # print abeer.get('name')
        beerlist.append(abeer.get('name'))
        # if abeer.get('style'):

            # print abeer['style']
    #get description
    for abeer in beerdict:
        pass





    # NAME FILTER
    for bname in beerlist:
        if bname.lower() == qstr.lower():
            print bname


    # resultnamelist 
    # print type(resplist[3][0]) #type unicode - "data"
    # print type(resplist[3][1]) #type list
    # # print resplist[3][1]

    # print type(resplist[3][1][0]) # type dict - I think it's the 

    # for anitem in resplist[3][1][0]: 
    #     # anitem being the beer object
    #     print anitem
        
    # print resplist[3][1][0]['status']

    return beerlist


def categories():
    # Data
    # List of category dictionaries 
    catdictlist = []
    #list of categories
    catestlist = []


    resp = urllib2.urlopen("http://api.brewerydb.com/v2/categories/?key=72166c358bc617ab5c18ecf67630a322&")

    # make dictionary of the response. 
    respd = json.load(resp)

    print "\n"

    print respd
    # Make list of category dicts
    catdictlist = respd.items()[2][1]


    return dict(res=catdictlist)

def styles():
    #note to self - the styles are connected to the categories in
    # this db.

    # Data
    # List of style dictionaries 
    styledictlist = []
    #list of style
    stylelist = []
    # make the request
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/styles/?key=72166c358bc617ab5c18ecf67630a322&")
    # make dictionary of the response. 
    respd = json.load(resp)

    print "\n"



    # Make list of category dicts
    styledictlist = respd.items()[2][1]
    # print "Style: " + styledictlist[0]['name']
    #How to get the cat name of the style at
    # print "Style's category: " + styledictlist[0]['category']['name']

    # for astyle in styledictlist:
    #     if astyle['id'] == 25:
    #         print astyle['name']
    # for astyle in styledictlist:
    #     stylelist.append(astyle['name'])
    #     print astyle['name']


    return dict(sdict=styledictlist)



def beerlistings():
    #pass in the style id and get the beer with the parameter of styleId of
    # the style passed in.
    # Data

    # GIVEN THE STYLE ID OF "American-Style Pale Ale":
    styleid = "25"

    # List of style dictionaries 
    beerdictlist = []
    #list of style
    beerlist = []
    # make the request
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/beers/?key=72166c358bc617ab5c18ecf67630a322&styleId=" + styleid)
    # make dictionary of the response. 
    respdi = json.load(resp).items()

    print "\n"
    beerdictlist = respdi[3][1]

    # total results vvvvv
    # print beerdictlist[2]

    print beerdictlist[2]['name']

    abeer = beerdictlist[0]




    # Make list of category dicts
    # beerdictlist = respd.items()[2][1]
    # print "Beer: " + beerdictlist[0]['name']
    #How to get the cat name of the style at
    # print "Style's category: " + beerdictlist[0]['category']['name']

    # for astyle in styledictlist:
    #     stylelist.append(astyle['name'])
    #     print astyle['name']


    return dict(bdict=beerdictlist, beerstyle="American-Style Pale Ale")


def beerprofile():
        #pass in the Beer id and get the beer with the parameter
    # Data

    # GIVEN THE Beer ID OF "8-Bit Pale Ale":
    beerId = "odItSS"

    beername = "8-Bit Pale Ale"

    
    # make the request
    resp = urllib2.urlopen("http://api.brewerydb.com/v2/beer/" + beerId + "?key=72166c358bc617ab5c18ecf67630a322&withBreweries=Y")
    # make dictionary of the response. 
    respdi = json.load(resp).items()

    print "\n"
    profdict = respdi[2][1]


    return dict(beerd=profdict,beertitle=beername)

def printer():
    print request.vars.z

    print "I hart fart"

