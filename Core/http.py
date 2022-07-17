#!/usr/bin/python3

import json

NEWLINE = '\n'

class ResponseBuilder:

    def __init__(self):
        """
        Initialize the parts of a response to nothing.
        """
        self.headers = []
        self.status = None
        self.content = None

    def add_header(self, headerKey, headerValue):
        """ Adds a new header to the response """
        self.headers.append(f"{headerKey}: {headerValue}")

    def set_status(self, statusCode, statusMessage):
        """ Sets the status of the response """
        self.status = f"HTTP/1.1 {statusCode} {statusMessage}"

    def set_content(self, content):
        """ Sets `self.content` to the bytes of the content """
        if isinstance(content, (bytes, bytearray)):
            self.content = content
        else:
            self.content = content.encode("utf-8")

    # TODO Complete the build function
    def build(self):
       
        response = self.status
        response += NEWLINE
        for i in self.headers:
            response += i
        response += NEWLINE
        response += NEWLINE
        response = response.encode("utf-8")
        response += self.content
        
        return response




# TODO: Write the response to a GET request
def get_response(data): 
    json_str= {
    "foodName" : "Groonal"
    }
    sentData = json.dumps(json_str)
    builder = ResponseBuilder()
    builder.set_status("200", "OK")
    builder.set_content(sentData)
    return builder.build()

