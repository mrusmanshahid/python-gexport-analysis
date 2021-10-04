
class Common:

    def __init__(self):
        pass

    def response_empty(self, obj):
        return {"status": 204, "response_message":"No data found", "response_code":"NO_CONTENT", "data": obj }
    
    def response_error(self, obj):
        return  {"status": 500, "response_message":"Error", "response_code":"ERROR", "data": obj }

    def response(self, obj):
        if obj == [] or obj == "" or obj == {}:
            return self.response_empty(obj)
        return {"status": 200, "response_message":"Success", "response_code":"SUCCESS", "data": obj }
