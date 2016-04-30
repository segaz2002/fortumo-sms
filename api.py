__author__ = 'gabriel'

from flask import Flask,jsonify,request
from flask_restful import Resource, Api
from sign import SignParser

app = Flask(__name__)
api = Api(app)
sp = SignParser()


class Horoscope(Resource):
    def get(self):
        args = request.args
        #print(args)
        msg =  args['message']

        if(SignParser.isValidDob(msg)):
            weekDetails = dict(sp.weekHoroscope(sp.getSignFromDob(msg)))

        elif sp.isSign(msg):
            weekDetails = dict(sp.weekHoroscope(msg))
        else:
            return jsonify(message = 'Invalid keyword, message should be in the format HSP 18-02-1988 or HSP leo')

        return weekDetails['horoscope']
         #jsonify(#week=weekDetails['week'],
                   #sunsign=weekDetails['sunsign'],
                   #horoscope=weekDetails['horoscope'])

#api.add_resource(Horoscope, '/<string:message>')
api.add_resource(Horoscope, '/')

if __name__ == '__main__':
    app.run(debug=True)