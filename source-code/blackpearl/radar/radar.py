from flask import Flask, render_template, request
import json, serial, time
import random, string

ser = serial.Serial('/dev/ttyACM1', 9600)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

# handle radar
@app.route('/radar', methods=['POST'])
def handle_radar():
    if request.method == 'POST':
        distance = requestDistance();
        if ':' in distance:
            distance = distance.strip('\r\n')
            distance = distance.split(':')
        
        # parse data to list
        d = 0; pos = 0
        if len(distance) > 1:
            d = distance[0]
            pos = distance[1]
            if d.isdigit() and pos.isdigit():
                d = int(d)
                pos = int(pos)
            else:
                d = 0
                pos = 0
        print d,":",pos
        object_id = generateId()
        print object_id
        return json.dumps({'distance':d, 'pos':pos, 'id': object_id})
            
def requestDistance():
    request = '1'
    ser.write(request)
    while True:
        try:
            time.sleep(0.025)
            distance = ser.readline()
            return distance
        except:
            pass
    time.sleep(0.025)

def generateId():
    object_id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(5))
    return object_id
    
if __name__ == '__main__':
	app.run(host="10.0.0.4", port=9000, debug=True, threaded=True)
