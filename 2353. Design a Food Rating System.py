import heapq

class FoodRating:
    def __init__(self, food, cuisine, rating):
        self.food = food
        self.cuisine = cuisine
        self.rating = rating

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_to_food = {}
        self.food_map = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            if cuisine not in self.cuisine_to_food:
                self.cuisine_to_food[cuisine] = []

            food_rating = FoodRating(food, cuisine, rating)
            heapq.heappush(self.cuisine_to_food[cuisine], (-rating, food))
            self.food_map[food] = food_rating

    def changeRating(self, food: str, newRating: int) -> None:
        food_rating = self.food_map[food]
        new_food_rating = FoodRating(food, food_rating.cuisine, newRating)
        self.food_map[food] = new_food_rating
        heapq.heappush(self.cuisine_to_food[new_food_rating.cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        while True:
            rating, food = heapq.heappop(self.cuisine_to_food[cuisine])
            if self.food_map[food].rating == -rating:
                heapq.heappush(self.cuisine_to_food[cuisine], (rating, food))
                return food
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
