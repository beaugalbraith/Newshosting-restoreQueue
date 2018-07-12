#!/usr/bin/env python3
import os
import io

def help():
	"""
	The Newshosting app for macOS clears the transfers queue whenever the app is forced to quit. The queued (XML) files remain on disk but they are not repopulated when the app is relaunched. This enumerates those files and adds them to the main queue. The Newshosting app must be closed first, then run this script, then reopen the app. If it doesn't work, try it again. No arguments.
	"""
	print(help.__doc__)

if len(os.sys.argv) > 1:
	help()

def xml(x):
	return True if x.endswith('xml') else False

preamble = '<?xml version="1.0" encoding="UTF-8"?>'
open_queue = '<queue>'
close_queue = '</queue>'
job_open = '<job-ref>'
job_close = '</job-ref>'
queue_buffer = io.StringIO()
home = os.environ['HOME']
# $HOME/Library/Application Support/Newshosting/Newshosting/queue
main_queue_file_directory = os.path.abspath(home) + os.path.sep + "Library" + os.path.sep + "Application Support" + os.path.sep + "Newshosting" + os.path.sep + "Newshosting"
xml_data_directory = main_queue_file_directory + os.path.sep + "queue"

os.chdir(os.path.abspath(home) + os.path.sep + "Library" + os.path.sep + "Application Support" + os.path.sep + "Newshosting" + os.path.sep + "Newshosting" + os.path.sep + "queue")


queue_buffer.write(preamble)
queue_buffer.write(open_queue)
for root, dirs, files in os.walk('.'):
	all_xml = filter(xml, files)
	while all_xml:
		try:
			queue_buffer.write("{}{}{}{}".format(job_open, os.path.abspath(root) + os.path.sep, next(all_xml), job_close))
		except StopIteration:
			break
		except Exception as err:
			print("Unexpected error: ", err)
			raise

queue_buffer.write(close_queue)
os.chdir(os.path.abspath(home) + os.path.sep + "Library" + os.path.sep + "Application Support" + os.path.sep + "Newshosting" + os.path.sep + "Newshosting")

with open((main_queue_file_directory + os.path.sep + 'queue.xml'), 'w+') as fd:
	fd.write(queue_buffer.getvalue())

queue_buffer.close()