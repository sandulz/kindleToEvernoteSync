import os
import time

username = "alexander.close2"
document = open("/Users/"+username+"/Dropbox/kindle-clippings.txt","r") 
 
data = "".join(document.readlines())
notes = []
try:
    clippings = data.split('==========')
    for clip in clippings:

        if "Bookmark" in clip:
            print 'Skipping bookmark'
            continue

        clipping = clip.split('Added on ')

        title = clipping[0].split('\r\n- ')[0].replace('\r\n','')
        date = clipping[1].split('\r\n')[0]
        location = clipping[0].split('\r\n- ')[1].replace('\r\n','')
        text = clipping[1].split('\r\n\r\n')[1]
        note = {'title': title, 'date': date, 'location': location, 'text': text}
        notes.append(note)
        #print note
    
except:
    print 'Unable parse clipping'

# - TODO:
# - new notes route to notebook "Inbox" by default, good for review and filing
# - currently throwing an error but completing task - look into error 
def MakeEvernoteNote(note):
    cmd = '''
    osascript<<END
        tell application "Evernote"
            set note_title to "''' + unicode(note['title'], errors="ignore") +  '''"
            set note_plain_text to "''' + unicode(note['text'].strip(), errors="ignore") + '''"
            set note_full_contents to "''' + unicode(note['text'], errors="ignore") + "\n" '''"
            set tag_name to "kindle-note"
            set note_search_term to note_title
            set found_notes to find notes note_search_term
            set num_notes_found to count found_notes

            if num_notes_found is greater than 0 then
                set this_note to item 1 in found_notes
                set this_note_text to (HTML content of item 1 of found_notes)
                if note_plain_text is not in this_note_text then
                    tell this_note to append text note_full_contents
                end if
            else
                set clip to create note title note_title with text note_full_contents
                if (not (tag named tag_name exists)) then
                    make tag with properties {name:tag_name}
                end if
                assign tag tag_name to clip
            end if
        end tell
    END'''

    os.system(cmd)

for note in notes:
    time.sleep(1)
    MakeEvernoteNote(note)
