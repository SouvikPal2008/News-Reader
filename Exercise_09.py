# Akhbar Padhke Sunao



def speak(Paragraph):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(Paragraph)

if __name__ == '__main__':
    def news(API_Key):
        from requests import get
        from json import loads

        print("Please Enter Any KeyWord Regarding Which You Want To Know News")
        print("It Can Be Your City, Your Wanted News Genre etc.")
        newskeyword = input("Enter Here : ")

        print("Enter Your Country Code")
        print("Refer To These Sites Please")
        print(f"https://newsapi.org/docs/endpoints/top-headlines#:~:text=HTTP%20header.-,country,param.,-category",
              f"https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes")
        countryinput = input("Enter Here : ")
        API_URL = f"https://newsapi.org/v2/top-headlines?q={newskeyword}&country={countryinput}&apiKey={API_Key}"
        getnews = get(API_URL)
        dictfile = getnews.content
        jsonfile = loads(dictfile)
        # print(jsonfile)
        i = 0
        rangenum = int(jsonfile['totalResults'])
        while True:
            if (rangenum >= i+1):
                speak(f"News Number {i + 1}")
                articles = jsonfile['articles']
                thelist = [thelist['title'] for thelist in articles]
                titles = thelist[i]
                print(f"News Number {i + 1}")
                print(f"{titles} \n")
                speak(titles)
                description = [description['description'] for description in articles]
                descriptionfun = description[i]
                print(f"{descriptionfun} \n")
                speak(descriptionfun)
                i = i + 1
            else:
                print("No News Found")
                speak("No News Found")
                break


    API_Key = input("Enter The API Key")
    news(API_Key)


