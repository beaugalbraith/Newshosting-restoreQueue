# Newshosting-restoreQueue
`
	"""
	The Newshosting app for macOS clears the transfers queue whenever the app is forced to quit. The queued (XML) files remain on disk but they are not repopulated when the app is relaunched. This enumerates those files and adds them to the main queue. The Newshosting app must be closed first, then run this script, then reopen the app. If it doesn't work, try it again. No arguments.
	"""
`
