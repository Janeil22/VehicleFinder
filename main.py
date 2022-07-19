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

def get_data_by_all(make, model, year):
    api_url = 'https://api.api-ninjas.com/v1/cars?make=' + make + '&model=' + model + '&year=' + year + '&limit=20'
    response = requests.get(api_url, headers={'X-Api-Key': 'satQ5cAvuZnDLaHo6QNHhA==be21RIxCh11f66As'})
    data = response.json()
    return data

def getInput():
    spec = input("Do you want to search make, model, year, or all?")
    if spec == 'make':
        make = input('Enter make:')
        x = [spec, make]
        return x
    elif spec == 'model':
        make = input('Enter make:')
        x = [spec, make]
        return x

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
