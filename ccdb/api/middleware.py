class DeBracketifyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cleaned = request.GET.copy()
        for key in cleaned:
            if key.endswith('[]'):
                val = cleaned.pop(key)
                cleaned_key = key.replace('[]', '')
                cleaned.setlist(cleaned_key, val)
        request.GET = cleaned
        return self.get_response(request)
