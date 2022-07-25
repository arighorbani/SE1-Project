from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US')

all_keywords = [

    'event management',

    'event planning',

    'event planner'

    ]

cat = '14' #people&society

timeframes = [

    'today 5-y',

    'today 12-m',

    'today 3-m',

    'today 1-m'

    ]

geo = '' #worldwide

gprop = '' #websearch

pytrends.build_payload(

    all_keywords,

    cat,

    timeframes[0],

    geo,

    gprop

    )


keywords = []
def check_trends():

    pytrends.build_payload(

        keywords,

        cat,

        timeframes[0],

        geo,

        gprop

        )

    data = pytrends.interest_over_time()

for keyword in all_keywords:

    keywords.append(keyword)

    check_trends()

    keywords.pop()