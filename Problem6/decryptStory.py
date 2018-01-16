def decrypt_story():

    cipher = CiphertextMessage(get_story_string())
    return cipher.decrypt_message()
