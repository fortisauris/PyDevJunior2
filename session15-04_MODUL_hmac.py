import hmac

key = bytes(hashstring_predchadzajuceho_bloku, encoding='utf8')
msg = bytes(str('nejake data'), encoding='utf8')
h = hmac.new(key=key, msg=msg, digestmod='md5')
result = h.hexdigest()
print(result)

