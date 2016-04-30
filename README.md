Fortumo SMS API responder
========================
This is a simple api using flask python framework.

The single endpoint respond to a message containing a zordiac sign or date of birth and then respond with
the horoscope prediction for the week.

This is deployed to Heroku.

##### Usage
------------
* https://fortumo.herokuapp.com/?message=06-06-1992
* or
* https://fortumo.herokuapp.com/?message=leo

Either a valid date of birth in the format dd-mm-yyyy can be specified or specify explicitly the sign.

It can be extended to react to the entire payload of the request, something like
* https://fortumo.herokuapp.com/?billing_type=MO&country=NG&currency=NGN&keyword=TXT+HSP&message=aquarius&
  message_id=67b1aa64cc6b317fa65547ca42918827&operator=Starcomms&price=30.0&price_wo_vat=28.57&
  sender=56349893&service_id=977d623be8c913b4863c33a410abfd5a&shortcode=32120
  &sig=e26a8b883036c943f2715279792baeef&status=pending&test=true


