class Index(object):
    def __init__(self, store=None):
        if store is None:
            store = dict()
        self.store = store

    def clear(self):
        """Resets the index"""
        self.store.clear()

    def delete(self, event):
        """Deletes any event in the index with a matching host and service.

        Returns the deleted event, if found; None, otherwise.
        """
        return self.store.pop(self._event_key(event), None)

    def expire(self):
        """Removes all expired events from the index.

        Returns a list of events removed from the index.
        """
        raise NotImplementedError()

    def search(self, query):
        """Returns a list of events matching a query AST."""
        raise NotImplementedError()

    def update(self, event):
        """Adds an event to the index"""
        if event.state != 'expired':
            self.store[self._event_key(event)] = event

    def get(self, host, service):
        """Finds an event in the index."""
        event_key = (host, service)
        return self.store.get(event_key)

    def _event_key(self, event):
        return (event.host, event.service)
