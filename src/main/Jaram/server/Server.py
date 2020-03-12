import os

status = 'deactived'

class start:
    if status == 'activated':
        print('Server Is Already Running.')
        pass
    else:
        status = 'activated'
        pass
    pass

class stop:
    status = 'deactived'
    pass