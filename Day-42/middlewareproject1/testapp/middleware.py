class ExecutionFlowMiddleware(object):

    def __init__(self, get_response):
        print('init method execution')
        self.get_response = get_response

    def __call__(self,request):
        print('Pre Processing of request')
        response = self.get_response(request)
        print('post processing of request')

        return response