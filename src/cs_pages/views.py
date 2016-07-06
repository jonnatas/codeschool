from django.http import HttpResponse
import srvice
import ejudge


@srvice.program
def send_input_block(client, id, source, correct_code, test_inputs, language, **kwargs):
	print("///////////////////")

	ret = ejudge.io.run(correct_code, test_inputs, language, sandbox=False)

	print(ret)

	client.dialog(html="hello world!")
	return 42