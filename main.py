import argparse
from utils.settings import Settings
from objects.database import Database

settings = Settings(".settings")


def set_osu_directory(directory):
	settings["osu_dir"] = directory
	settings.save()


def main():
	parser = argparse.ArgumentParser(description="Creates an osu thumbnail")
	command_group = parser.add_mutually_exclusive_group()
	command_group.add_argument("-od", "--osu_directory", action="store", help="Sets the osu directory")
	command_group.add_argument("link", action="store", help="Creates a thumbnail from the specified link", nargs="?")
	args = parser.parse_args()

	if args.osu_directory is not None:
		set_osu_directory(args.osu_directory)
		return
	if args.link is not None:
		if settings["osu_dir"] is None:
			print("Error: Osu directory is not set!")
			parser.print_help()
		db = Database(settings["osu_dir"] + "osu!.db")
		print("Osu version:", db.version)
		print("Folder count:", db.folder_count)
		print("Account name:", db.account_name)
		# TODO: parse link
		return
	parser.print_help()


main()
