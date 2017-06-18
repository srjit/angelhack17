
def get_weather_alerts():
    with open("weather_msg_summary.txt") as weather_updates:
        updates = weather_updates.read()
    
    updates = list(reversed(updates.split("\n\n--\n\n")))
    return [update for update in updates if update.strip() != ""]
    


foo = get_weather_alerts()    