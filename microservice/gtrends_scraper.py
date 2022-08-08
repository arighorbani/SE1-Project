# MICROSERVICE MADE BY ARIAN GHORBANI

# gtrends_scraper() documentation:
# PARAMETERS --
# all_keywords: a list of strings representing the different keywords you want to track data for (eg. ["google", "search", "result"])
# timeframe: defaults to "today 5-y", meaning "from 5 years ago to today". The general format is "today #-T", where # is an integer and T can be either 'y' (year), 'm' (month), or 'd' (day)
# geo: defaults to world. Can use capitalized two-letter country abbreviations to specify countries.
# gprop: defaults to web searches. Can be changed to 'images', 'news', 'youtube', or 'froogle' (shopping), each of which represents the type of search
# type: Custom parameter, defaults to "interest_over_time". The possible parameters are "interest_over_time", "get_historical_interest", "interest_by_region", "related_topics", "related_queries", "trending_searches", and "top_charts".

# For more information on this API and how it works specifically, go to https://github.com/GeneralMills/pytrends



from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US')

def gtrends_scraper(all_keywords, cat = 0, timeframe = "today 5-y", geo = "", gprop = "", type = "interest_over_time"):
    #places into "pytrends" all of the data scraped
    pytrends.build_payload(

        all_keywords,

        cat,

        timeframe,

        geo,

        gprop
    )
    match type:
        case "interest_over_time":
            retstr = "INTEREST OVER TIME DATA:\n" + pytrends.interest_over_time().to_string()
            return retstr

        case "get_historical_interest":
            retstr = "HISTORICAL INTEREST DATA:\n" + pytrends.get_historical_interest().to_string()
            return retstr

        case "interest_by_region":
            retstr = "INTEREST BY REGION DATA:\n" + pytrends.get_historical_interest().to_string()
            return retstr

        case "related_topics":
            retstr = "RELATED TOPICS DATA:\n" + pytrends.related_topics().to_string()
            return retstr

        case "related_queries":
            retstr = "RELATED QUERIES DATA:\n" + pytrends.related_queries().to_string()
            return retstr

        case "trending_searches":
            retstr = "TRENDING SEARCHES DATA\n" + pytrends.trending_searches().to_string()
            return retstr

        case "top_charts":
            retstr = "TOP CHARTS DATA\n" + pytrends.top_charts().to_string()
            return retstr
            
        case _:
            retstr = "INTEREST OVER TIME DATA:\n" + pytrends.interest_over_time().to_string()
            return retstr