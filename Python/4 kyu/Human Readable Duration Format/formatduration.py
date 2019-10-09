from __future__ import print_function


def format_duration(seconds):
    
    if seconds == 0:
        duration = "now"
        print(duration)
        return duration
    
    duration = []
    duration_text = ''
    
    years = seconds // (365*24*60*60)
    days = (seconds % (365*24*60*60)) // (24*60*60)
    hours = ((seconds % (365*24*60*60)) % (24*60*60)) // (60*60)
    mins = (((seconds % (365*24*60*60)) % (24*60*60)) % (60*60)) // 60
    secs = (((seconds % (365*24*60*60)) % (24*60*60)) % (60*60)) % 60
    
    def segment(amount, time_segment):
        text = ''
        if amount > 0:
            text += ' '.join([str(amount), time_segment])
            if amount > 1:
                text += 's'
        return text
    
    duration.append(segment(years, 'year'))
    duration.append(segment(days, 'day'))
    duration.append(segment(hours, 'hour'))
    duration.append(segment(mins, 'minute'))
    duration.append(segment(secs, 'second'))
    
    duration = list(filter(None, duration))
    
    if len(duration) == 1:
        duration_text += duration[0]
    else:
        comma = False
        for text in duration[0:-1]:
            if comma:
                duration_text += ', '
            duration_text += text
            comma = True
        duration_text += ' and ' + duration[-1]
        
    print(duration_text)
    return duration_text


if __name__ == '__main__':
    format_duration(0)
    format_duration(1)
    format_duration(62)
    format_duration(120)
    format_duration(3600)
    format_duration(3662)
    format_duration(15731080)
    format_duration(132030240)
    format_duration(205851834)
