#kindleToEvernoteSync

## Backup Kindle Highlights/Notes & Add to Evernote


1) Using Automator, Mac will detect the Kindle has been plugged in and download the file 

	~/documents/My Clippings.txt

to 
	
	~/Users/"+username+"/Dropbox/kindle-clippings.txt 

and replace the file if one is already present.

2) kindle_to_evernote_sync.py will run, which copies the files into the users evernote account.

File changes (new highlights) will be added to previously made Evernote notes - appending those notes

New notes route to notebook "Inbox" by default, to be reviewed and filing into any other notebook within Evernote



###If for some reason the automator file .wflow isn't working, can navagate to the local file and run:
	
	python kindle_to_evernote_sync.py


Resourses:
[@vindia](https://github.com/vindia/kindle-2-evernote)
[this gist](https://gist.github.com/1071682) by jplattel and [this workflow](http://evansims.com/1380/a-perfect-instapaper-sync-for-kindle/) by Evan Sims 
