class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power # this is a value till which wash station can clean your car, meaning bring up the value of clean_mark to this level
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        price_per_car = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                price_per_car.append(self.calculate_washing_price(car))

        return round(sum(price_per_car),1)


    def calculate_washing_price(self, car: Car) -> float:
        # car's comfort class * difference between wash station's clean power and car's clean mark * car wash station rating / car wash station distance to the center of the city, returns number rounded to 1 decimal
        # returns price of one car wash as a float rounded till one decimal
        pass

    def wash_single_car(self, clean_mark: int) -> None:
        # method, that washes a single car, so it should have clean_mark equals wash station's clean_power, if wash_station.clean_power is greater than car.clean_mark
        # The washing cost will depend on car comfort class, car cleanness degree, wash station average rating and wash station distance from the center of the city.
        pass

    def rate_service(self, rating: int) -> None:
        current_total_rating = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        current_total_rating += rating
        self.average_rating = round(current_total_rating / self.count_of_ratings, 1)
