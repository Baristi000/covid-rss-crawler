from datetime import datetime

class ResponseDto():
    def Success(self, data:dict):
        return{
            "status":200,
            "time":datetime.now(),
            "data":data
        }
    def Badrequest(self, message:str):
        return{
            "status":400,
            "time":datetime.now(),
            "message":message
        }
    def Create(self, data:dict):
        return{
            "status":201,
            "time":datetime.now(),
            "data":data
        }
    def genExampleResponse(self, succeed_body: dict = None, error_body:dict = None, create_body = None):
        baseResponse = {
            200: {
            "description": "Success",
            "content": {
                "application/json": {
                "examples": {}
                }
            }
            },
        }
        if succeed_body!=None:
            baseResponse[200]["content"]["application/json"]["examples"].update(
            {
                "success":{
                "summary": "success",
                "value":succeed_body
                }
            }
            )
        if error_body!=None:
            baseResponse[200]["content"]["application/json"]["examples"].update(
            {
                "error":{
                "summary": "error",
                "value":error_body
                }
            }
            )  
        if create_body!=None:
            baseResponse[200]["content"]["application/json"]["examples"].update(
            {
                "create":{
                "summary": "create",
                "value": create_body
                }
            }
            ) 
        return baseResponse