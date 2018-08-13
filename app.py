from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import random
import threading

app = Flask(__name__)
socketio = SocketIO(app, logger = True, async_mode="threading")

class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=5):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            
            newLottery()
            
            time.sleep(self.interval)

marksix = []

def newLottery():
    global marksix

    marksix = []
    for x in range(6):
        marksix.append(random.randint(1,49))

    print("new lottery is: " +  str(marksix))
    socketio.emit('new_marksix', {"arr": marksix}, broadcast=True)
    return marksix

@app.route('/')
def hello():
    return render_template("index.html")    

if __name__ == '__main__':
    test = ThreadingExample()
    socketio.run(app)    
        
