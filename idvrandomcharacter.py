import random

# Character data
characters = {
    "survivor": ["Doctor", "Lawyer", "Gardener", "Lucky Guy", "Magician", "Explorer", "Mercenary", "Coordinator", "Mechanic", "Forward", "The Mind's Eye", "Priestess", "Perfumer", "Cowboy", "Female Dancer", "Seer", "Embalmer", "Prospector", "Enchantress", "Wildling", "Acrobat", "First Officer", "Barmaid", "Postman", "Grave Keeper", "Prisoner", "Entomologist", "Painter", "Batter", "Toy Merchant", "Patient", "Psychologist", "Novelist", "Little Girl", "Weeping Clown", "Professor", "Antiquarian", "Composer", "Journalist", "Aeroplanist", "Cheerleader", "Puppeteer", "Fire Investigator", "Faro Lady"],
    "hunter": ["Hell Ember", "Smiley Face", "Gamekeeper", "The Ripper", "Soul Weaver", "Geisha", "Wu Chang", "Photographer", "Mad Eyes", "The Feaster", "Dream Witch", "Axe Boy", "Evil Reptilian", "Bloody Queen", "Guard 1  26", "Disciple", "Violinist", "Sculptor", "Undead", "Breaking Wheel", "Naiad", "Wax Artist", "Nightmare", "Clerk", "Hermit", "Night Watch", "Opera Singer", "Fool’s Gold", "The Shadow"]
}

def select_random_character(faction):
  """Selects a random character from the given faction."""
  if faction.lower() in characters:
    return random.choice(characters[faction.lower()])
  else:
    return "Invalid faction"

# Get user input
faction = input("Which faction would you like to choose between type \"survivor\" or \"hunter\"? ")

# Select and print random character
random_character = select_random_character(faction)
print(f"Your randomly selected IDV {faction} is: {random_character}")