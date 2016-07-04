from django.http import HttpResponse
import srvice


@srvice.program
def send_input_block(client, id, source, **kwargs):
	print(args, kwargs)
	client.dialog(html="hello world!")
	return 42