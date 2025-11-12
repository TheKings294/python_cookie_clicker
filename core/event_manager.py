from utils.observable import Observable


class EventManager(Observable):
    listener_list: dict = {}

    def __init__(self):
        pass

    def subscribe(self, event_type, listener):
        if event_type not in self.listener_list:
            self.listener_list[event_type] = []
        if listener in self.listener_list[event_type]:
            self.listener_list[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type in self.listener_list:
            if listener in self.listener_list[event_type]:
                self.listener_list[event_type].remove(listener)

    def notify(self, event_type, data):
        if event_type not in self.listener_list:
            print(f"[No listeners] for event '{event_type}'")
            return
        for listener in self.listener_list[event_type]:
            listener(data)
