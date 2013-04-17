import sublime, sublime_plugin
import subprocess, os, sys

class GotoFolderCommand(sublime_plugin.ApplicationCommand):
	def __init__(self):
		self.app_path_mac = None
		self.folder_list = None
		self.cache = False

	def get_sublime_path(self):
		if sublime.platform() == 'osx':
			if not self.app_path_mac:
				from ctypes import cdll, byref, Structure, c_int, c_char_p, c_void_p
				from ctypes.util import find_library
				Foundation = cdll.LoadLibrary(find_library('Foundation'))
				CFBundleGetMainBundle = Foundation.CFBundleGetMainBundle
				CFBundleGetMainBundle.restype = c_void_p
				bundle = CFBundleGetMainBundle()
				CFBundleCopyBundleURL = Foundation.CFBundleCopyBundleURL
				CFBundleCopyBundleURL.argtypes = [c_void_p]
				CFBundleCopyBundleURL.restype = c_void_p
				url = CFBundleCopyBundleURL(bundle)
				CFURLCopyFileSystemPath = Foundation.CFURLCopyFileSystemPath
				CFURLCopyFileSystemPath.argtypes = [c_void_p, c_int]
				CFURLCopyFileSystemPath.restype = c_void_p
				path = CFURLCopyFileSystemPath(url, c_int(0))
				CFStringGetCStringPtr = Foundation.CFStringGetCStringPtr
				CFStringGetCStringPtr.argtypes = [c_void_p, c_int]
				CFStringGetCStringPtr.restype = c_char_p
				self.app_path_mac = CFStringGetCStringPtr(path, 0)
				CFRelease = Foundation.CFRelease
				CFRelease.argtypes = [c_void_p]
				CFRelease(path)
				CFRelease(url)
			return self.app_path_mac.decode() + '/Contents/SharedSupport/bin/subl'
		elif sublime.platform() == 'linux':
			return open('/proc/self/cmdline').read().split(chr(0))[0]
		else:
			return sys.executable

	def sublime_command_line(self, args):
		args.insert(0, self.get_sublime_path())
		return subprocess.Popen(args)

	def run(self):
		if not sublime.active_window():
			sublime.run_command("new_window")
			self.use_active_window = True
		else:
			self.use_active_window = False
		if not self.cache or not self.folder_list:
			settings = sublime.load_settings('GotoFolder.sublime-settings')
			self.cache = settings.get("cache", False);
			root_folders = settings.get("root_folders", [{'folder': sublime.packages_path(), 'alias': 'Plugin'}])
			self.folder_list = [];
			self.folder_info = [];
			folder_count = 0;
			for root in root_folders:
				if 'alias' not in root:
					root['alias'] = ""
				else:
					root['alias'] += ":"
				try:
					for f in os.listdir(root['folder']):
						if f.startswith(".") or (os.path.isfile(root['folder']+"/"+f) and not f.endswith(".sublime-project")):
							continue
						self.folder_list.append([root['alias']+f])
						a = [root['folder']+"/"+f]
						if 'extra' in root:
							a += root['extra']
						self.folder_info.append(a)
						folder_count+=1
				except Exception as e:
					print(e, ". Check GotoFolder.sublime-settings file")
			#print "GotoFolder Plugin:", folder_count, "folders added to the list"
		sublime.active_window().show_quick_panel(self.folder_list, self.on_select)

	def on_select(self, idx):
		if idx < 0:
			return
		# disabled due to lack of sublime.focus_window API
		#if self.find_and_focus_folder(folder_list[idx][1]): return
		args = ["-n"] + self.folder_info[idx]
		if self.use_active_window:
			args[0] = "-a"
		self.sublime_command_line(args)

	def find_and_focus_folder(self, folder):
		for w in sublime.windows():
			for f in w.folders():
				if f == folder:
					sublime.focus_window(w)
					#sublime.set_timeout(partial(ctypes.windll.user32.SetForegroundWindow, window.hwnd(), 0), 500)
					return True
		return False


