__author__ = 'gabriel'

from flask import Flask,jsonify,request
from flask_restful import Resource, Api
from sign import SignParser

app = Flask(__name__)
api = Api(app)
sp = SignParser()

'''
Request Anatomy
---------------
"/?billing_type=MO&country=NG&currency=NGN&keyword=TXT+HSP&message=aquarius&message_id=67b1aa64cc6b317fa65547ca42918827&
operator=Starcomms&price=30.0&price_wo_vat=28.57&sender=56349893&service_id=977d623be8c913b4863c33a410abfd5a&shortcode=32120
&sig=e26a8b883036c943f2715279792baeef&status=pending&test=true"
'''

class Horoscope(Resource):
    def get(self):
        msg = request.args['message']

        if(SignParser.isValidDob(msg)):
            weekDetails = dict(sp.weekHoroscope(sp.getSignFromDob(msg)))

        elif sp.isSign(msg):
            weekDetails = dict(sp.weekHoroscope(msg))
        else:
            return 'INVALID Sign or Date of Birth, message should be in the format HSP 18-02-1988 or HSP leo'

        return weekDetails['horoscope']

api.add_resource(Horoscope, '/')

if __name__ == '__main__':
    app.run(debug=False)