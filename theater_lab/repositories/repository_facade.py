from .director_repository import DirectorRepository
from .theater_repository import TheaterRepository
from .hall_repository import HallRepository
from .actor_repository import ActorRepository
from .play_repository import PlayRepository
from .role_repository import RoleRepository
from .buyer_repository import BuyerRepository
from .seat_repository import SeatRepository
from .schedule_repository import ScheduleRepository
from .ticket_repository import TicketRepository

class RepositoryFacade:
    def __init__(self):
        # Ініціалізуємо всі репозиторії
        self.director_repo = DirectorRepository()
        self.theater_repo = TheaterRepository()
        self.hall_repo = HallRepository()
        self.actor_repo = ActorRepository()
        self.play_repo = PlayRepository()
        self.role_repo = RoleRepository()
        self.buyer_repo = BuyerRepository()
        self.seat_repo = SeatRepository()
        self.schedule_repo = ScheduleRepository()
        self.ticket_repo = TicketRepository()

    def get_all_directors(self):
        return self.director_repo.get_all()

    def get_director_by_id(self, director_id):
        return self.director_repo.get_by_id(director_id)

    def create_director(self, first_name, last_name, date_of_birth=None):
        return self.director_repo.create(first_name, last_name, date_of_birth)

    def get_all_theaters(self):
        return self.theater_repo.get_all()

    def get_theater_by_id(self, theater_id):
        return self.theater_repo.get_by_id(theater_id)

    def create_theater(self, name, address, number_of_halls):
        return self.theater_repo.create(name, address, number_of_halls)

    def get_all_halls(self):
        return self.hall_repo.get_all()

    def get_hall_by_id(self, hall_id):
        return self.hall_repo.get_by_id(hall_id)

    def create_hall(self, name, number_of_seats, theatre):
        return self.hall_repo.create(name, number_of_seats, theatre)

    def get_all_actors(self):
        return self.actor_repo.get_all()

    def get_actor_by_id(self, actor_id):
        return self.actor_repo.get_by_id(actor_id)

    def create_actor(self, first_name, last_name, date_of_birth=None):
        return self.actor_repo.create(first_name, last_name, date_of_birth)

    def get_all_plays(self):
        return self.play_repo.get_all()

    def get_play_by_id(self, play_id):
        return self.play_repo.get_by_id(play_id)

    def create_play(self, title, genre, duration, premiere_date, director=None):
        return self.play_repo.create(title, genre, duration, premiere_date, director)

    def get_all_roles(self):
        return self.role_repo.get_all()

    def get_role_by_id(self, role_id):
        return self.role_repo.get_by_id(role_id)

    def create_role(self, role_name, actor, play):
        return self.role_repo.create(role_name, actor, play)

    def get_all_buyers(self):
        return self.buyer_repo.get_all()

    def get_buyer_by_id(self, buyer_id):
        return self.buyer_repo.get_by_id(buyer_id)

    def create_buyer(self, first_name, last_name, email):
        return self.buyer_repo.create(first_name, last_name, email)

    def get_all_seats(self):
        return self.seat_repo.get_all()

    def get_seat_by_id(self, seat_id):
        return self.seat_repo.get_by_id(seat_id)

    def create_seat(self, seat_number, hall):
        return self.seat_repo.create(seat_number, hall)

    def get_all_schedules(self):
        return self.schedule_repo.get_all()

    def get_schedule_by_id(self, schedule_id):
        return self.schedule_repo.get_by_id(schedule_id)

    def create_schedule(self, date, time, play, hall):
        return self.schedule_repo.create(date, time, play, hall)

    def get_all_tickets(self):
        return self.ticket_repo.get_all()

    def get_ticket_by_id(self, ticket_id):
        return self.ticket_repo.get_by_id(ticket_id)

    def create_ticket(self, ticket_number, seat, buyer, price, schedule):
        return self.ticket_repo.create(ticket_number, seat, buyer, price, schedule)
