import requests

def get_data_by_make(make):
    api_url = 'https://api.api-ninjas.com/v1/cars?make=' + make + '&limit=20'
    response = requests.get(api_url, headers={'X-Api-Key': 'satQ5cAvuZnDLaHo6QNHhA==be21RIxCh11f66As'})
    data = response.json()
    return data

def get_data_by_model(model):
    api_url = 'https://api.api-ninjas.com/v1/cars?model=' + model + '&limit=20'
    response = requests.get(api_url, headers={'X-Api-Key': 'satQ5cAvuZnDLaHo6QNHhA==be21RIxCh11f66As'})
    data = response.json()
    return data

def get_data_by_year(year):
    api_url = 'https://api.api-ninjas.com/v1/cars?year=' + year + '&limit=20'
    response = requests.get(api_url, headers={'X-Api-Key': 'satQ5cAvuZnDLaHo6QNHhA==be21RIxCh11f66As'})
    data = response.json()
    return data

def get_data_by_all(typeList):
    api_url = 'https://api.api-ninjas.com/v1/cars?make=' + typeList[0] + '&model=' + typeList[1] + '&year=' + typeList[2] + '&limit=20'
    response = requests.get(api_url, headers={'X-Api-Key': 'satQ5cAvuZnDLaHo6QNHhA==be21RIxCh11f66As'})
    data = response.json()
    return data

def getInput():
    spec = input("Do you want to search make, model, year, or all?")
    if spec == 'make':
        make = input('Enter make:')
        return make
    elif spec == 'model':
        model = input('Enter model')
        return model
    elif spec == 'year':
        year = input('Enter year:')
        return year
    elif spec == 'all':
        make = input('Enter make:')
        model = input('Enter model')
        year = input('Enter year:')
        return [make, model, year]

def getTransmission(data):
    t = data['transmission']
    return t 

def getCitympg(data):
    make = data['make']
    return make 

def getModel(data):
    model = data['model']
    return model

def getMake(data):
    make = data['make']
    return make 
