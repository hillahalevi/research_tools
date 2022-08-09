import googlemaps

KEY = "AIzaSyDGd4thbkCx125jfxc0FZ697estekunMbs"
# Requires API key
gmaps = googlemaps.Client(key=KEY)


def check_distance_to_TLV(place, dest='תל אביב'):
    # # Requires cities name
    # origins = [
    #     "Perth, Australia",
    #     "Sydney, Australia",
    #     "Melbourne, Australia",
    #     "Adelaide, Australia",
    #     "Brisbane, Australia",
    #     "Darwin, Australia",
    #     "Hobart, Australia",
    #     "Canberra, Australia",
    # ]
    # destinations = [
    #     "Uluru, Australia",
    #     "Kakadu, Australia",
    #     "Blue Mountains, Australia",
    #     "Bungle Bungles, Australia",
    #     "The Pinnacles, Australia",
    # ]
    # matrix = gmaps.distance_matrix(origins, destinations)
    my_dist = gmaps.distance_matrix(place, dest)['rows'][0]['elements'][0]

    # Printing the result
    return my_dist


if __name__ == '__main__':
    print("")
    file = open('places.txt', mode='r', encoding='utf-8-sig')
    lines = file.readlines()
    file.close()
    inputPlaces = dict(x.split(",") for x in lines)
    clearPlaces = {k: v.strip('\n') for k, v in inputPlaces.items()}
    worthyPlaces = {k: v for k, v in clearPlaces.items() if float(v) > 3000}

    c = {'distance': {'text': '115 km', 'value': 115177}, 'duration': {'text': '1 hour 24 mins', 'value': 5049},
         'status': 'OK'}

    distance = c['distance']['text']
    duration = c['duration']['text']

    for k, v in clearPlaces.items():
        print(k + "," + v)
