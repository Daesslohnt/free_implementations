from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Person:
    sort_index: int = field(init=False, repr=False)
    name: str
    job: str
    age: int
    strength: int = 100

    def __post_init__(self):
        object.__setattr__(self, 'sort_index', self.strength)


person1 = Person("Gerald", "Witcher", 40, 120)
person2 = Person("Yenifer", "Sorceress", 37)
person3 = Person("Yenifer", "Sorceress", 37)

#person3.age = 100 it is illegal because of frozen

print(id(person3))
print(id(person2))
print(person1)

print(person1 > person2)