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

def get_Transmission(data):
    t = data['transmission']
    return t

def get_Citympg(data):
    make = data['make']
    return make

def get_Model(data):
    model = data['model']
    return model

def get_Make(data):
    make = data['make']
    return make

def get_Highwaympg(data):
    highwaympg = data['highwaympg']
    return highwaympg

def get_Engine(data):
    engine = data['engine']
    return engine

def get_Drivetrain(data):
    drivetrain = data['drivetrain']
    return drivetrain

def get_Year(data):
    year = data['year']
    return year

#print(get_data_by_all("toyota", "camry", "2007"))