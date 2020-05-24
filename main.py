import argparse
from utils.settings import Settings
from objects.database import Database

settings = Settings(".settings")


def set_osu_directory(directory):
	settings["osu_dir"] = directory
	settings.save()


def get_background_file(path):
	with open(path) as file:
		while file.readable():
			line = file.readline()
			if line.startswith("0,0,"):
				return line.split(",")[2].strip("\"")

	return None


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

		link_arguments = args.link.split("/")
		beatmap_id = int(link_arguments[-1])
		beatmap_set_id = int(link_arguments[-2].split("#")[0])
		print("Beatmap id:", beatmap_id, "Beatmap set id:", beatmap_set_id)

		db = Database(settings["osu_dir"] + "osu.db", beatmap_set_id, beatmap_id)
		print("Osu version:", db.version)
		print("Folder count:", db.folder_count)
		print("Account name:", db.account_name)

		current_beatmap = db.search_result

		if current_beatmap == 0:
			print("Beatmap not found!")
			return

		print(current_beatmap.song_title)
		background_image = get_background_file(settings["osu_dir"] + "Songs/" + current_beatmap.folder_name + "/" + current_beatmap.file_name)
		print(background_image)
		return
	parser.print_help()


main()
