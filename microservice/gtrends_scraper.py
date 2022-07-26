from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US')


#SET OF VARIABLES THAT WILL NEED TO BE SENT IN THE SENECA REQUEST; have been set in order to demonstrate microservice as functional
all_keywords = [
    'event management',

    'event planning',

    'event planner'
    ]

cat = '14' #people&society

timeframe = 'today 5-y'

geo = '' #worldwide

gprop = '' #websearch

#places into "pytrends" all of the data scraped
pytrends.build_payload(

    all_keywords,

    cat,

    timeframe,

    geo,

    gprop

    )

print(pytrends.interest_over_time().to_string()) #prints "interest over time" data; EXAMPLE OF WHAT KIND OF DATA WILL BE RECEIVED