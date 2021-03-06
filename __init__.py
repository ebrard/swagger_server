#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder



app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'This is a sample server Petstore server.  You can find out more about     Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).      For this sample, you can use the api key &#x60;special-key&#x60; to test the authorization     filters.'})
#    app.run(port=8080)
