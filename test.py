from datetime import datetime
import time


def tingy():
    start = datetime.now()

    time.sleep(5)
    end = datetime.now()
    return {"string", (end - start)}


print(tingy())
