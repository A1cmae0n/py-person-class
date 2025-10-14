class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # store people by {name: person_object}
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        spouse = "husband" if "husband" in person.keys() else "wife"
        name = person["name"]
        spouse_name = person[spouse]
        if spouse_name:
            if spouse == "husband":
                Person.people[name].husband = Person.people[spouse_name]
            else:
                Person.people[name].wife = Person.people[spouse_name]

    return people_list
