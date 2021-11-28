def to_slack(message, channel, url, username=None, attachments=None, icon_emoji=None, icon_url=None):
    values = {
         'text': message,
         'channel': channel,
         'username': username,
         'attachments': attachments,
         'icon_emoji': icon_emoji,
         'icon_url': icon_url,
     }
    values = json.dumps(values)
    req = urllib2.Request(url, values)
    urllib2.urlopen(req)
