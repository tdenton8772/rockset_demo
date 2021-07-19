from rockset import Client, ParamDict
import json

def popularity(year):
    rs = Client(api_key='qrSyXTfbYvxevJ15iLc5AgV6U6DYhkkUq2xWRDXoTdwd472b1lGmOU1yvFdeloY4',
              api_server='https://api.rs2.usw2.rockset.com')

    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
        'popularity',
        version='7f22390063895c2e',
        workspace='commons')

    params = ParamDict()
    params['year'] = year
    results = qlambda.execute(parameters=params)
    return results['results']


def revenue(year):
    rs = Client(api_key='qrSyXTfbYvxevJ15iLc5AgV6U6DYhkkUq2xWRDXoTdwd472b1lGmOU1yvFdeloY4',
              api_server='https://api.rs2.usw2.rockset.com')

    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
        'revenue',
        version='d461808689453a0e',
        workspace='commons')

    params = ParamDict()
    params['year'] = year
    results = qlambda.execute(parameters=params)
    return results['results']

def genres(year):
    rs = Client(api_key='qrSyXTfbYvxevJ15iLc5AgV6U6DYhkkUq2xWRDXoTdwd472b1lGmOU1yvFdeloY4',
              api_server='https://api.rs2.usw2.rockset.com')

    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
        'genres',
        version='c83a14419222b1f7',
        workspace='commons')

    params = ParamDict()
    params['year'] = year
    results = qlambda.execute(parameters=params)
    return results['results']

def production_companies(year):
    rs = Client(api_key='qrSyXTfbYvxevJ15iLc5AgV6U6DYhkkUq2xWRDXoTdwd472b1lGmOU1yvFdeloY4',
              api_server='https://api.rs2.usw2.rockset.com')

    # retrieve Query Lambda
    qlambda = rs.QueryLambda.retrieve(
        'production_companies',
        version='f845d826feafea71',
        workspace='commons')

    params = ParamDict()
    params['year'] = year
    results = qlambda.execute(parameters=params)
    return results['results']

def main(year):
    pop = popularity(year)
    rev = revenue(year)
    gen = genres(year)
    prod = production_companies(year)
    return (pop, rev, gen, prod)


if __name__ == "__main__":
    popularity, revenue, genre, production_companies = main("1997")
    print(popularity)
