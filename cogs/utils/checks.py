def is_event(message):
    """Check if a message contains event data"""
    embed = message.embeds[0]
    return (message.channel.name == 'upcoming-events'
            and 'fields' in embed
            and 'name' in embed['fields'][0]
            and 'name' in embed['fields'][1]
            and 'name' in embed['fields'][2]
            and embed['fields'][0].get("name") == "Time"
            and embed['fields'][1].get("name") == "Accepted"
            and embed['fields'][2].get("name") == "Declined")
