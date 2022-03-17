StreamLink = "https://d1ymi26ma8va5x.cloudfront.net/47af4f688a4d3e34f513_ironmouse_44619847244_1644121175/chunked/index-dvr.m3u8"
# Stream URL is https://www.twitch.tv/videos/1287350698
StreamSections = 94 #How many 30 min sections are in the VOD

'''
Another stream
https://www.twitch.tv/videos/1288758764
https://d1ymi26ma8va5x.cloudfront.net/ad7df46d01d076a6cab0_ironmouse_44606619692_1644025354/chunked/index-muted-FMTK8V9QQ2.m3u8
53
'''

FileName = 'OutputFile'

for i in range(0,StreamSections + 1):
    hour = int(i / 2)
    if hour >= 10:
        hour = str(hour)
    else:
        hour = '0' + str(hour)
    
    minute = (i * 30) % 60
    if minute == 0:
        minute = '00'
    else:
        minute = str(minute)
    TimeStamp = hour + ':' + minute + ':00'
    #print(TimeStamp)
    # Assembles timestemps for every 30 minutes

    if i >= 10:
        FileID = '_' + str(i)
    else:
        FileID = '_0' + str(i)
    # Assembles file ID from i, makes 2 digits long

    FullLine = 'ffmpeg -ss ' + TimeStamp + ' -i ' + StreamLink + ' -frames:v 1 -q:v 2 ' + FileName + FileID + '.jpeg'
    #print(FullLine)

    with open('StreamDownload.bat', 'a') as f:
        f.writelines(FullLine + '\n')

print('Done')
