#
# Here we step through the world month by month
# Let's just start with makin' babies
#
#

import random
import time
# Our good ol' lists
professionList = [
    'cowherd',
    'dairymaid',
    'farmer',
    'gardener',
    'goatherd',
    'hawker',
    'Herder',
    'horse trainer',
    'plowman',
    'reaper',
    'sheepshearer',
    'shepherd',
    'swineherd',
    'thresher',
    'tillerman',
    'vintner',
    'Woodcutter',
    'woolman',
    'climmer',
    'falconer',
    'forester',
    'fowler',
    'gamekeeper',
    'hawker',
    'hunter',
    'master of hounds',
    'trapper',
    'fisherman',
    'artisan',
    'model',
    'painter',
    'sculptor',
    'composer',
    'playwright',
    'poet',
    'writer',
    'shoemaker',
    'furrier',
    'tailor',
    'jeweler',
    'pastrycook',
    'mason',
    'carpenter',
    'weaver',
    'chandler',
    'cooper',
    'baker',
    'hatmaker',
    'saddler',
    'butcher',
    'blacksmith',
    'roofer',
    'locksmith',
    'ropemaker',
    'tanner',
    'rugmaker',
    'cutler',
    'glover',
    'architect',
    'baker',
    'balancemaker',
    'basketmaker',
    'beekeeper',
    'brewer',
    'bell maker',
    'broom maker',
    'bookbinder',
    'bookprinter',
    'bricker',
    'builder',
    'buttonmaker',
    'cartographer',
    'cartwright',
    'chainmaker',
    'cheesemaker',
    'clockmaker',
    'clothier',
    'compasssmith',
    'disher',
    'dyer',
    'embroiderer',
    'engraver',
    'glassblower',
    'gravedigger',
    'hatmaker',
    'miller',
    'miner',
    'mirrorer',
    'physician',
    'potter',
    'shipwright',
    'spinster',
    'woodcutter',
]
nameListFemale = [
    'Vicenta',
    'Latrice',
    'Corrine',
    'Marcelina',
    'Judith',
    'Marina',
    'Laurie',
    'Yung',
    'Cleotilde',
    'Ming',
    'Ludie',
    'Myrtice',
    'Tegan',
    'Genna',
    'Livia',
    'Maribel',
    'Shelba',
    'Jeanene',
    'Eunice',
    'Meta',
    'Loretta',
    'Jaquelyn',
    'Leda',
    'Alpha',
    'Kathie',
    'Chelsie',
    'Mao',
    'Katia',
    'Mandi',
    'Cleora',
    'Kimberly',
    'Zola',
    'Toi',
    'Margart',
    'Brigette',
    'Samara',
    'Aracelis',
    'Narcisa',
    'Arianna',
    'Jann',
    'Denese',
    'Nettie',
    'Mitsuko',
    'Meri',
    'Sindy',
    'Rae',
    'Polly',
    'Emely',
    'Ghislaine',
    'Olimpia'
]
nameListMale = [
    'Wesley',
    'Chuck',
    'Gus',
    'Lavern',
    'Malcolm',
    'Chance',
    'Elmer',
    'Asa',
    'Kendall',
    'Modesto',
    'Jc',
    'Bob',
    'Leslie',
    'Kristopher',
    'Dion',
    'Stan',
    'Harland',
    'Emmanuel',
    'Deandre',
    'Reginald',
    'Franklin',
    'Charles',
    'Giovanni',
    'Abe',
    'Shelton',
    'Damien',
    'Elliott',
    'Lee',
    'Alec',
    'Douglas',
    'Dale',
    'Hollis',
    'Alden',
    'Ervin',
    'Cyril',
    'Roman',
    'Hubert',
    'Marco',
    'Fredrick',
    'Darwin',
    'Grant',
    'Clarence',
    'Dorsey',
    'Bradford',
    'Ronald',
    'Carrol',
    'Stewart',
    'Elvis',
    'Micah',
    'Mariano'
]
nameListDisease = [
    'Swine Heart',
    'Golden Throat',
    'Jungle Rage',
    'Rock Flu',
    'Running Flu',
    'Tomb Throat',
    'Elephant Plague',
    'Humming Warts',
    'Forest Warts',
    'Immobilizing Stiffness',
    'Pale Hands',
    'Kroad',
    'Cat Scratch Fever',
    'Green Fever',
    'Dying Euphoria',
    'Spirit Migraine',
    'Snake Fever',
    'Explosive Leprosy',
    'Fisherman\'s Scurvy',
    'Dwarf Tongue',
    'Banshee Blight',
    'Devil\'s Lung',
    'Goose Lung'
]
nameListDisaster = [
    'Eternal',
    'Cataclysmic',
    'Almighty',
    'Midnight',
    'Unbound',
    'Veiled',
    'Twin',
    'Swift',
    'Noxious'
]
typeListDisease = [
    'flu',
    'plague',
    'infection'
]
typeListNaturalDisasters = [
    'Hurricane',
    'Tornado',
    'Flood',
    'Tsunami',
    'Volcano',
    'Fire',
    'Earthquake',
    'Sandstorm',
    'Lightning Storm'
]

# Define our populaces (alive and dead)
# Our large list of objects
populace = []
diseases = []
# List of IDs of alive people
populaceAlive = []
diseasesAlive = []
# List of IDs of dead people
populaceDead = []
diseasesDead = []

# List of diseases! We don't really need to keep track of anything but the names after they die out.


# Create-A-Person


class Person:
    def __init__(self, id, name, gender, age=0, profession='WIP', socialstatus='WIP'):
        self.id = id
        self.name = name
        self.gender = gender
        self.profession = profession
        self.age = age
        self.socialStatus = socialstatus
        self.siblings = []
        self.parents = []
        self.children = []
        self.partner = []
        self.separated = []
        self.infected = []
        self.immune = []
        self.ispregnant = 0
        self.pregnantnum = 0
        self.isalive = True

    def __str__(self):
        return str(self.__dict__)

    def getage(self):
        return self.age/12


class Disease:
    def __init__(self, id, name, lethality, virulence, type):
        self.id = id
        self.name = name
        self.lethality = lethality
        self.virulence = virulence
        self.infectednum = 0
        self.type = type

    def __str__(self):
        return str(self.__dict__)


class Disaster:
    def __init__(self, name, chance, lethality):
        self.name = name
        self.chance = chance
        self.lethality = lethality


# Start the people counter!
peopleCounter = -1
diseaseCounter = -1

# People Stuff

def genid():
    global peopleCounter
    peopleCounter += 1
    return peopleCounter


def gengender():
    genderRatio = random.randint(0,1)
    if genderRatio == 1:
        return 'F'
    else:
        return 'M'


def genname(gender):
    if gender == 'F':
        return nameListFemale[random.randint(0,(len(nameListFemale)-1))]
    elif gender == 'M':
        return nameListMale[random.randint(0,(len(nameListMale)-1))]
    else:
        return 'Neuter'


def createperson():
    gender = gengender()
    name = genname(gender)
    id = genid()
    newperson = Person(id, name, gender)
    return newperson


def firstgen(gensize):
    # We no longer have defined generations, so appending whole generations doesn't make sense
    i = 0
    while i < gensize:
        newperson = createperson()
        populace.append(newperson)
        populaceAlive.append(newperson.id)
        i += 1


def ageup():
    for person in populaceAlive:
        populace[person].age += 1
        if populace[person].ispregnant:
            populace[person].ispregnant += 1
        booup(person)
        havechildren(person)
        getsick(person)
        cull(populace[person])


def booup(spouse):
    for match in populaceAlive:
        person = populace[spouse]
        match = populace[match]
        randbooupchance = random.randint(0, 25)
        # print("old enough?: ", person.getage() > 15 and match.getage()> 15)
        # print("age range?: ", abs(match.getage()-person.getage()) < 8)
        # print("no partners?: ", person.partner == [] and match.partner == [])
        # print("gender match?: ", person.gender != match.gender)
        # print("chance?: ", randbooupchance == 25)
        if noGoT(person, match) and person.getage() > 15 and match.getage() > 15 and abs(match.getage()-person.getage()) < 8 and person.partner == [] and match.partner == [] and person.gender != match.gender and randbooupchance == 25:
            person.partner.append(match.id)
            person.partner.sort()
            match.partner.append(person.id)
            match.partner.sort()


def twinchance():
    if random.randint(0,100):
        return 1
    else:
        return random.randint(2, 3)


def connectsiblings(parent):
    for child in parent.children:
        populace[child].siblings = parent.children.copy()
        populace[child].siblings.remove(child)
        populace[child].siblings.sort()


def noGoT(person, match):
    for sibling in person.siblings:
        if match.id == sibling:
            return False
    for sibling in match.siblings:
        if person.id == sibling:
            return False
    return True


def havechildren(spouse):
    for match in populace[spouse].partner:
        person = populace[spouse]
        partner = populace[match]
        if 40 > person.getage() > 18 and 40 > partner.getage() > 18 and not person.ispregnant and not partner.ispregnant and random.randint(0, 20) == 20 and random.randint(0, len(partner.children)+1) == 0:
            if person.gender == 'F':
                person.ispregnant = 1
                person.pregnantnum = twinchance()
            if partner.gender == 'F':
                partner.ispregnant = 1
                partner.pregnantnum = twinchance()
        if person.ispregnant > 9:
            i = 0
            while i < person.pregnantnum:
                newperson = createperson()
                person.children.append(newperson.id)
                partner.children.append(newperson.id)
                newperson.parents.append(person.id)
                newperson.parents.append(partner.id)
                populace.append(newperson)
                populaceAlive.append(newperson.id)
                connectsiblings(person)
                i += 1
            person.ispregnant = 0
            person.pregnantnum = 0
        if partner.ispregnant > 9:
            i = 0
            while i < partner.pregnantnum:
                newperson = createperson()
                person.children.append(newperson.id)
                partner.children.append(newperson.id)
                newperson.parents.append(person.id)
                newperson.parents.append(partner.id)
                populace.append(newperson)
                populaceAlive.append(newperson.id)
                connectsiblings(partner)
                i += 1
            partner.ispregnant = 0
            partner.pregnantnum = 0


def die(character):
    for spouse in character.partner:
        populace[spouse].separated.append(character.id)
        populace[spouse].partner.remove(character.id)
    for disease in character.infected:
        diseases[disease].infectednum -= 1
    populaceAlive.remove(character.id)
    populaceDead.append(character.id)
    character.isalive = False


def cull(person):
    # Old Age
    age = person.getage()
    if 80 > age > 50 and random.randint(0, (round((abs(-age+90)*1.5) ** 0.5))*200) == 0:
        print('Died: ', age, 'Name: ', person.name)
        die(person)
    elif age >= 80 and random.randint(0, round(95-age)*5) == 0:
        print('Died: ', age, 'Name: ', person.name)
        die(person)
    # Child Death
    if 1 >= age > .01 and random.randint(0, round(age*3000)) == 0:
        print('Died: ', age, 'Name: ', person.name)
        die(person)
    #

# End People Stuff

# Disease Stuff
def diseaseid():
    global diseaseCounter
    diseaseCounter += 1
    return diseaseCounter


def diseasename():
    return nameListDisease[random.randint(0, (len(nameListDisease)-1))]


def culldisease(disease):
    if diseases[disease].infectednum <= 0:
        diseases[disease].infectednum = 0
        if diseases[disease].type == 'plague':
            diseasesAlive.remove(disease)
            diseasesDead.append(disease)


def createdisease():
    id = diseaseid()
    name = diseasename()
    lethality = random.randint(50, 800)
    virulence = random.randint(20, 500)
    type = typeListDisease[random.randint(0, len(typeListDisease)-1)]
    newdisease = Disease(id, name, lethality, virulence, type)
    return newdisease


def spawndiseases():
    if random.randint(0, 100*len(diseasesAlive)) == 0:
        newdisease = createdisease()
        # patient zero
        populace[random.randint(0, (len(populace) - 1))].infected.append(newdisease.id)
        newdisease.infectednum += 1
        print(newdisease)
        diseases.append(newdisease)
        diseasesAlive.append(newdisease.id)


def getsick(person):
    for disease in diseasesAlive:
        culldisease(disease)
        if disease not in populace[person].infected and disease not in populace[person].immune and random.randint(0, round(diseases[disease].virulence/(diseases[disease].infectednum+1))) == 0:
            populace[person].infected.append(disease)
            # print(populace[person].name + " got sick from", diseases[disease].name)
            diseases[disease].infectednum += 1
        diseaseoutcome(person)


def diseaseoutcome(person):
    for disease in populace[person].infected:
        if random.randint(0, diseases[disease].lethality) == 0:
            print('Death by', diseases[disease].name + ': ', populace[person].getage(), 'Name: ', populace[person].name)
            die(populace[person])

        else:
            if diseases[disease].infectednum > 0:
                diseases[disease].infectednum -= 1
            populace[person].infected.remove(disease)
            if diseases[disease].type == 'plague':
                populace[person].immune.append(disease)

# End Disease Stuff
# Disasters
# init disasters

def disasters():
    # When disaster strikes, Everyone is affected equally so no need to iterate
    # Decide if a disaster happens
    if random.randint(0, 2) == 0:
        # Generate this new disaster



# End Disaster Stuff


def runworld(years, genonesize):
    firstgen(genonesize)
    i = 0
    while i < years * 12:
        # start = time.time()
        ageup()
        spawndiseases()
        # print("year: ", round(i/12, 2))
        # end = time.time()
        # print("Time: ", round(end-start, 2), "Seconds")
        i += 1


# Let's start with making our first generation
runworld(100, 20)

f = open("output.txt", "w")
f.write("")
f.close()
f = open("output.txt", "a")


for people in populace:
    for attr, value in people.__dict__.items():
        if str(attr) != "id":
            f.write("    ")
        f.write(str(attr) + ": " + str(value) + "\n")
    f.write("\n")
age = 0
for dead in populaceDead:
    age = age + populace[dead].getage()

print("Average Death Age: ", age/len(populaceDead))
print(len(populaceAlive))

