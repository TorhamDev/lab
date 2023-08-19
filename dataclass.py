from dataclasses import dataclass, field


def generate_license():
    return "34234245-0rewe-rwert"


@dataclass
class Car:
    name: str
    model: str
    max_speed: int
    car_license: str = field(default_factory=generate_license)

    def increse_speed(self):
        self.max_speed += 1


tesla = Car(name="tesla", model="12", max_speed=300)


print(tesla)

tesla.increse_speed()

print(tesla)
