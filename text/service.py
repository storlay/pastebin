from drive.message import upload_message
from text.hash_generation import hash_encode
from text.models import Text


def create_message(form, uuid_url):
    message = form.cleaned_data['message']
    message_name = f'{uuid_url}.txt'
    with open(message_name, 'w') as file:
        file.write(message)
    message_id = upload_message(message_name)
    encoded_message_id = hash_encode(message_id)

    Text.objects.create(
        uuid_url=uuid_url,
        drive_id=encoded_message_id,
        is_temporary=form.cleaned_data['is_temporary'],
        datetime_of_deletion=form.cleaned_data['datetime_of_deletion']
    )
