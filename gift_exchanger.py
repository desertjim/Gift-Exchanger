import copy
import sys
import random
import sys
people = ["janice", "henry", "james", "jeff"]
people = ["janice", "henry", "james", "jeff", "ramsey", "drew", "kim"]
dont_match=[("janice", "henry")] 
count = 0

# method prints the 
def printer(giver, sofar):
	print_line(giver, sofar)
	print giver
	sys.exit(0)

# method prints the giver and the recipient to stdout
def print_line(giver, sofar):
	if not sofar.has_key(giver):
		return
	print giver,"->",
	taker = sofar[giver]
	del sofar[giver]
	print_line(taker, sofar)

# method takes the person a list of people that this person can be paired with, 
# a list of don't match people, and the size of the matched list
def build_it(name, people, sofar, dont_match, size):
	if not people and size == len(sofar):
		# if the people dictionary is empty
		# and the size of the original print it
		printer(name, sofar)
		global count 
		count += 1
		if count > 10:
			sys.exit(0)
		return

	for person in people:
		if person == name:
			# don't want to match the person with themself
			continue
		if (name, person) in dont_match or (person, name) in dont_match:
			# don't want to create a pair that is in the don't match list
			continue
		if (person, name) in sofar:
			# don't want a circular match ie Jim buys for Janice and Janice buys for Jim
			continue
		
		deep_copy_people = copy.deepcopy(people) 
		deep_copy_people.remove(person)
		#print "List should be different ", people, deep_copy_people
		deep_copy_sofar = copy.deepcopy(sofar)
		deep_copy_sofar[name] =  person
		#print "List should be different sofar ", sofar, deep_copy_sofar
		build_it(person, deep_copy_people, deep_copy_sofar, dont_match, size)

if __name__ == "__main__":
	build_it(people[random.randint(0, len(people)-1)], people, {}, dont_match, len(people))
