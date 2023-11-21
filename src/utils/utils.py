import os
import time


def stand_by( milliseconds : int | float ) -> None:
    return time.sleep( milliseconds )


def clear() -> None:
    '''
        nt = Windows operational system
        posix = Linux operational system
    '''

    operational_system = os.name

    if operational_system == 'nt':
        return os.system('cls')
    elif operational_system == 'posix':
        return os.system('clear')
    else:
        print('Ops! The operational system is not supported...')
        pass

