code = [
'Keyword Name\n',
'    Create Session    session    {url}\n',
'    ${headers}=    Create Dictionary\n'
]

headers = ['    ...    Content-Type=multipart/form-data\n    ', '...    Accept=application/json\n    ', '...    Ocp-Apim-Subscription-Key=e4b5521dccb84da587bc4c56648445c0\n    ', '...    Authorization=Bearer 8B4332A33DCF9AC75A21F984991444CA61BCD876C456AC8109F188A6363CCE44\n    ']

indice = 0
while indice < len(headers):
    header_value = headers[indice]
    code.append(header_value)
    indice += 1

code2 = "".join(code)
print(code2)