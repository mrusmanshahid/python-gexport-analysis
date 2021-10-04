
class Common:

    def __init__(self):
        pass
    
    # method to return response to the user with response message and status code to define the response is empty.
    def response_empty(self, obj):
        return {"status": 204, "response_message":"No data found", "response_code":"NO_CONTENT", "data": obj }
    
    # method to return error to the user with response message and status code to define what went wrong.
    def response_error(self, obj):
        return  {"status": 500, "response_message":obj, "response_code":"ERROR", "data": [] }

    # method to return data wrapped in general response dictionary for user to process easily.
    def response(self, obj):
        return {"status": 200, "response_message":"Success", "response_code":"SUCCESS", "data": obj }
    
    # method to validate if object, string, or array is empty.
    def validate_empty(self, obj):
        return obj == [] or obj == {} or obj == ""
