from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    message = []
    for key, value in exc.detail.items():
        message.append(key.capitalize() + ': ' + ', '.join(value))
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['message'] = ' '.join(message)
    return response
