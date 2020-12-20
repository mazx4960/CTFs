import datetime
from urllib.parse import quote
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
CATEGORIES = [
	"Reverse",
	"Forensics",
	"Programming",
	"Miscellaneous",
	"Web",
	"Binary Exploitation",
	"Cryptography",
	"Hardware",
	"Cloud",
	"Emulations"
]
EVENT_TEMPLATE_FILE = os.path.join(BASE_DIR, 'templates', 'event_template.md')
CHALLENGE_TEMPLATE_FILE = os.path.join(BASE_DIR, 'templates', 'challenge_template.md')
CAT_HEADER = r"### [{}]({}/)"
CHALL_BULLETS = r"- [x] [{}]({}/{})"


def get_year():
	return datetime.datetime.now().year


def create_dir(dir_path):
	if os.path.exists(dir_path):
		print('\n[*] Directory already exists:', dir_path)
		print('[*] Skipping...\n')
		return 
		
	print('[*] Directory created:', dir_path)
	os.mkdir(dir_path)


def create_readme(dir_path, template_file, mappings):
	read_path = os.path.join(dir_path, "README.md")

	if os.path.exists(read_path):
		print('\n[*] README already exists:', read_path)
		if input('[*] Continue? [n] ') != 'y':
			return

	with open(template_file, 'r') as f:
		template = f.read().format(**mappings)

	with open(read_path, 'w') as f:
		print('[*] README created:', read_path)
		f.write(template)


def display_menu(options):
	print('')
	for ind, option in enumerate(options):
		print(f'[{ind + 1}] {option}')
	print()


def init_chall_files(categories):
	challenge_dict = {}
	for cat in solved_cats:
		challenge_dict.setdefault(cat, [])
		print("Enter the challenge names for the {} category".format(cat))
		print("Type done when done")
		name = input('')
		while name != 'done':
			challenge_dict[cat].append(name)
			name = input('')

	for cat in solved_cats:
	challenges += CAT_HEADER.format(cat, quote(cat)) + '\n'
	for name in challenge_dict[cat]:
		chall_dir = os.path.join(event_dir, cat, name)
		create_dir(chall_dir)
		create_readme(chall_dir, CHALLENGE_TEMPLATE_FILE, {'title': name})
		challenges += CHALL_BULLETS.format(name, quote(cat), quote(name)) + '\n'

	return challenges


def main():
	year = get_year()
	year_dir = os.path.join(BASE_DIR, str(year))
	create_dir(year_dir)

	event = input("Enter the event name: ")
	event_dir = os.path.join(year_dir, event)
	create_dir(event_dir)
	
	display_menu(CATEGORIES)
	solved_cats = list(map(lambda x: CATEGORIES[int(x) - 1], input("Enter the category index separated by commas: ").split(',')))

	for cat in solved_cats:
		cat_dir = os.path.join(event_dir, cat)
		create_dir(cat_dir)

	init_chals = input("Would you like to initialise challenges? [n] ").lower() == 'y'
	if init_chals:
		challenges = init_chall_files(solved_cats)
	else:
		challenges = '\n\n'.join([CAT_HEADER.format(cat, quote(cat)) for cat in solved_cats])

	mappings = {
		'event': event,
		'challenges': challenges
	}
	create_readme(event_dir, EVENT_TEMPLATE_FILE, mappings)


if __name__ == '__main__':
	main()
