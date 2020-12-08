# Day 7 Handy Haversacks

class Bag:
    def __init__(self, color):
        self.color = color
        self.contained = {}
        self.contained_by = []


def get_bags():
    bags = {}
    with open("../assets/bagcriteria.txt", 'r') as f:
        for line in f.readlines():
            line = (line[:-2].split(" contain "))
            contained_bags = line[1].split(", ")

            bag = Bag(line[0])
            for contained_bag in contained_bags:
                if contained_bag == "no other bags":
                    bag.contained = {}
                elif int(contained_bag[0]) == 1:
                    bag.contained[contained_bag[2:] + "s"] = int(contained_bag[0])
                else:
                    bag.contained[contained_bag[2:]] = int(contained_bag[0])

            bags[bag.color] = bag

    return bags


def link_bags(bags):
    for bag in bags.values():
        for contained in bag.contained:
            bags[contained].contained_by.append(bag.color)

    return bags


def part1(desired_bag="shiny gold bags"):
    bags = link_bags(get_bags())
    bag = bags[desired_bag]
    potential_containers = recursive_find(bags, bag, set())
    print(len(potential_containers))


def part2(desired_bag="shiny gold bags"):
    bags = link_bags(get_bags())
    bag = bags[desired_bag]
    tally = 0
    a = recursive_add(bags, bag)
    print(a)


def recursive_add(bags, bag):
    num_contained_bags = 0

    for contained_bag in bag.contained:
        if bag.contained == {}:
            return 0

        num_contained_bags += bag.contained[contained_bag] * (
                    1 + recursive_add(bags, bags[contained_bag]))

    return num_contained_bags


def recursive_find(bags, bag, potential_containers):
    if bag.contained_by == []:
        return potential_containers
    else:
        potential_containers = potential_containers | set(bag.contained_by)
        for container in bag.contained_by:
            potential_containers = recursive_find(bags, bags[container], potential_containers)
    return potential_containers


part1()
part2()
