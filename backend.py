import requests

API_KEY="1c685ce4a3fa3846290ae1569a1976ac"

def get_data(place, forecast_days=None, kind=None):
    url=f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_value =8*forecast_days #applying unitary method
    filtered_data=filtered_data[:nr_value]

    return filtered_data

if __name__=="__main__":
    print(get_data(place="mumbai",forecast_days=3,kind="Temprature"))