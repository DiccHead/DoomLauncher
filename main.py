import eel
import os
import platform


def launch():
	current_dir = os.listdir()
	arch = platform.architecture()
	global engine
	if "engine" not in current_dir:
		print("Can't find engine dir, making new.")
		os.mkdir("engine")
		print("Succes")
	else:
		print('Engine dir located')

	if "gzdoom" not in os.listdir("engine"):
		print("Can't find gzdoom dir, making new.")
		os.mkdir("engine/gzdoom")
		print("Succes")
	else:
		print("Gzdoom dir located")

	if "lzdoom" not in os.listdir("engine"):
		print("Can't find lzdoom dir, making new.")
		os.mkdir("engine/lzdoom")
		print("Succes")
	else:
		print("Lzdoom dir located")

	if "iwads" not in current_dir:
		print("Can't find iwads dir, making new.")
		os.mkdir("iwads")
		print("Succes")
	else:
		print('Iwads dir located')

	if "mods" not in current_dir:
		print("Can't find mods dir, making new.")
		os.mkdir("mods")
		print("Succes")
	else:
		print('Mods dir located')

	if "64bit" in arch:
		engine = "engine/gzdoom/gzdoom.exe"
		print("Engine set to Gzdoom")
	if "32bit" in arch:
		engine = "engine/lzdoom/lzdoom"
		print("Engine set to Lzdoom")


def norm_path(str):
	result = str.replace("\\", r"\✪")
	result = result.replace("✪", "")
	return result


def eel_onready():
	print("Onready performed!")

def gen_mod_list(x):
	mod_list = 0
	for element in x:
		if mod_list == 0:
			mod_list = " -file " + mod_dir + '/' + element
		else:
			mod_list = mod_list + " -file " + mod_dir + '/' + element
	return mod_list

launch()


iwad_dir = "iwads"
mod_dir = "mods"
brightmaps_s = ""
lights_s = ""
additional = ""
if len(os.listdir(iwad_dir)) != 0:
	current_iwad = os.listdir(iwad_dir)[0]
mods = os.listdir(mod_dir)
active_mods = 0


eel.init('web/')
eel.print_mods(mods)


@eel.expose
def iwad_changed(x):
	global current_iwad
	current_iwad = x
	print("iwad is " + x)

@eel.expose
def mods_changed(x):
	x.remove('')
	global active_mods
	active_mods = gen_mod_list(x)
	print(active_mods)


@eel.expose
def open_explorer():
	os.system('explorer /n,' + norm_path(os.getcwd()))


@eel.expose
def brightmaps(x):
	global brightmaps_s
	if x == True:
		brightmaps_s = " -file " + engine + "/brightmaps.pk3 "
		print(brightmaps_s)
	if x == False:
		brightmaps_s = ""
		print(brightmaps_s)


@eel.expose
def lights(x):
	global lights_s
	if x == True:
		lights_s = " -file " + engine + "/lights.pk3 "
		print(lights_s)
	if x == False:
		lights_s = ""
		print(lights_s)


@eel.expose
def engine_change(x):
	global engine
	if x == "GZDoom":
		engine = "engine/gzdoom/gzdoom.exe"
	if x == "LZDoom":
		engine = "engine/lzdoom/lzdoom.exe"


@eel.expose
def rip_and_tear(x):
	if x != 0 or x != []:
		x.remove('')
		global active_mods
		active_mods = gen_mod_list(x)
		print(active_mods)

	if active_mods == 0:
		os.system('start ' + engine + " -iwad " + iwad_dir + '/' + current_iwad + brightmaps_s + lights_s)
		print('start ' + engine + " -iwad " + iwad_dir + '/' + current_iwad + brightmaps_s + lights_s)
	else:
		os.system('start ' + engine + " -iwad " + iwad_dir + '/' + current_iwad + brightmaps_s + lights_s + active_mods)
		print('start ' + engine + " -iwad " + iwad_dir + '/' + current_iwad + brightmaps_s + lights_s + active_mods)


eel_onready()

eel.print_iwads(os.listdir(iwad_dir))

if __name__ == "__main__":
	eel.start('index.html', size=(840,620))
