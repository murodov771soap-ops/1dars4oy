class Ticket:
    def init(self, movie_name, price, count):
        self.movie_name = movie_name
        self.price = price
        self.count = count

    def total_cost(self):
        return self.price * self.count

    def show_info(self):
        print(f"Film: {self.movie_name}")
        print(f"Umumiy xarajat: {self.total_cost()} so'm")

ticket = Ticket('Avatar', 40000, 3)
print(ticket.total_cost())