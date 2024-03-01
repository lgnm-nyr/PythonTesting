#made the inputs into a function
def get_user_input():

    #city options
    city_flight_options = ["berlin", "amsterdam", "london", "paris"]

    #get flight option and make it lowercase to be used in code
    city_flight = input("Enter the city you will be flying to (options: Berlin, Amsterdam, London, Paris): ").lower()

    #code to rechoose if misinput option
    while city_flight not in city_flight_options:
        print("Invalid city. Please choose from the options: Berlin, Amsterdam, London, Paris")
        city_flight = input("Enter the city you will be flying to (options: Berlin, Amsterdam, London, Paris): ").lower()
    
    #input num nights
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))

    #input num of car hire days
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    #return values
    return city_flight, num_nights, rental_days

#function for total hotel stay cost
def hotel_cost(num_nights):
    #cost and calcs
    price_per_night = 100
    total_cost = num_nights * price_per_night
    #return total
    return total_cost

#function for cost of plane tickets
def plane_cost(city_flight):
    
    #Using dictionary because quicker than if/else that hint said (for me)
    flight_costs = {"berlin": 100, 
                    "amsterdam": 200, 
                    "london": 400, 
                    "paris": 75
                    }
    #returns cost
    return flight_costs[city_flight]

#function for car hire cost
def car_rental(rental_days):
    #cost and calcs
    daily_rental_cost = 50
    total_cost = rental_days * daily_rental_cost
    #return total
    return total_cost

#function for total holiday cost, combining all costs
def holiday_cost(hotel_cost, plane_cost, car_rental):
    #calcs
    total_cost = hotel_cost + plane_cost + car_rental
    #return total
    return total_cost

#function to print out all details
def print_details(city_flight, num_nights, rental_days, hotel_cost, plane_cost, car_rental, total_cost):
    print('=' * 100)
    #recapitlaise first letter to look nice :)
    print(f"City: {city_flight.capitalize()}")
    print('-' * 50)
    print(f"Number of Nights: {num_nights}")
    print('-' * 50)
    print(f"Number of Days Renting a Car: {rental_days}")
    print('-' * 50)
    print(f"Total Hotel Cost: £{hotel_cost}")
    print('-' * 50)
    print(f"Total Plane Cost: £{plane_cost}")
    print('-' * 50)
    print(f"Total Car Rental Cost: £{car_rental}")
    print('=' * 50)
    print(f"Total Cost of Entire Holiday: £{total_cost}")
    print('=' * 100)

#main function to call everything in the right order
def main():
    city_flight, num_nights, rental_days = get_user_input()
    hotel_total = hotel_cost(num_nights)
    plane_total = plane_cost(city_flight)
    car_total = car_rental(rental_days)
    total_cost = holiday_cost(hotel_total, plane_total, car_total)
    print_details(city_flight, num_nights, rental_days, hotel_total, plane_total, car_total, total_cost)

#run the program
main()