class ReadOnlyError(Exception):
    def __init__(self, error_info):
        super(ReadOnlyError, self).__init__(error_info)
        self.error_info = error_info

    def __str__(self):
        return self.error_info
