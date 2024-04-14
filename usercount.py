def get_event_date(event):
    return event.date

def current_users(events):
    machines = {}
    for event in events:
        if event not in machines:
            machines[event.machine] = set()
        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users)>0:
            user_list = ",".join(users)
            print("{}: {}".format(machine,user_list))
            