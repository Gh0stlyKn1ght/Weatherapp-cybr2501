#Juan Nevarez
#CYBR250
#9/15/2020
#draft not the final 
import requests #use requests library



def fetch_data(zip=None, city=None, units=None):

    baseUrl = "http://api.openweathermap.org/data/2.5/weather" #url to openweather
    API_Key = "14bf29c16ef6ec7b767c48e0749c43e5" #my  personal api key

 def get_units():
     if units.lower == 'fahrenheit'
        unit == 'Fahrenheit'
    elif:
        units.lower == 'imperial'
    unit = 'Celcius'

    print(f'the temp for {city} is {temp} {units})



    if zip is not None:
        baseUrl += "?zip="+str(zip)+",us"

    else:
        baseUrl += "?q="+str(city)+",us"

    baseUrl += "&appid="+str(API_Key)

    r = requests.get(baseUrl)
    return r

def showResult(resp):


    if resp.status_code == 200:

        data= resp.json()

        print(data['name'])

        print(f"""{data['name']}  forecast:
        Low Temperature {data['main']['temp_min']} High Temperature {data['main']['temp_max']}.
        Wind speed {data['wind']['speed']}.
        Visibility {data['visibility']}.

      

        """)

    else:

        print("Request Failed, Try Again Error Code : ",resp.status_code)

def main():

    while True:

        inp =int(input("Weather Search :\n1. Zip Code\n2. City Name\n3. Exit\n"))

        if inp == 1:

            try:

                queryData=int(input("Enter zip code : "))


                resp= fetch_data(queryData,None)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp == 2:

            try:

                queryData = input("Enter city name : ")

                resp= fetch_data(None,queryData)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp==3:

            break

        else:

            print("Invalid Choice..\n")



if __name__=="__main__":


    main()
