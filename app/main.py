class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    instances_people = []

    for person in people:
        instance = Person(person["name"], person["age"])

        if person.get("wife") is not None:
            instance.wife = person["wife"]

        if person.get("husband") is not None:
            instance.husband = person["husband"]

        instances_people.append(instance)
        Person.people[instance.name] = instance

    for instance in instances_people:
        if hasattr(instance, "wife"):
            instance.wife = Person.people.get(instance.wife)

        if hasattr(instance, "husband"):
            instance.husband = Person.people.get(instance.husband)

    return instances_people
