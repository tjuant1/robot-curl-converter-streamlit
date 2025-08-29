import re

class GetContent:
    def code(self, url):
        code = [
        'Keyword Name\n',
        f'    Create Session    session    {url}\n\n',
        '    ${headers}=    Create Dictionary\n'
        ]

        return code

    def get_url(self, curl_input):
        url = re.search(r"'([^']+)", curl_input)
        url = url.group().replace("'", "")
        return url

    def get_headers(self, curl_input, header_selected):
        headers = re.findall(fr"{header_selected}\s+'([^:]+):\s*([^']+)'", curl_input)
        headers_len = len(headers)

        indice = 0
        values_list = []

        while indice < headers_len:
            header_tuple = headers[indice]
            robot_format = f"{header_tuple[0]}={header_tuple[1]}"
            indice += 1
            values_list.append(f"    ...    {robot_format}\n")
        return values_list

    def content_formdata(self, curl_input, body_prefix, has_file, header, url):
        indice = 0

        body = re.findall(fr"{body_prefix}\s+'([^']+)'", curl_input)
        image_path = [item for item in body if "=@" in item]

        if has_file == "Yes":
            body = [item for item in body if "=@" not in item]

        body_len = len(body)

        code = self.code(url)

        indice = 0
        while indice < len(header):
            header_value = header[indice]
            code.append(header_value)
            indice += 1

        code.append("\n    ${form_data}=    Create Dictionary\n    ")
        indice = 0
        while indice < body_len:
            body_new = body[indice]
            code.append(f"...    {body_new}\n    ")
            indice += 1

        if has_file == "No":
            code.append("\n    ${response}=    REQUEST On Session    session    /\n    ...    data=${form_data}\n    ...    headers=${headers}")
        else:
            code.append(f"\n    ${{files}}=    Create Dictionary\n    ...    {image_path[0]}\n")
            code.append("\n    ${response}=    REQUEST On Session    session    /\n    ...    files=${files}\n    ...    data=${form_data}\n    ...    headers=${headers}")

        code_retunable = "".join(code)
        return code_retunable

    def content_json(self, curl_input, body_prefix, headers, url):
        body_w_prefix = re.search(fr"{body_prefix}\s+'([^']+)'", curl_input)
        body = body_w_prefix.group(1)
        body = body.replace('\n', "").replace(" ", "")

        code = self.code(url)

        indice = 0
        while indice < len(headers):
            header_value = headers[indice]
            code.append(header_value)
            indice += 1

        code.append(f"\n    ${{body}}=    Set Variable    {body}\n")
        code.append("\n    ${response}=    REQUEST On Session    session    /\n    ...    headers=${headers}\n    ...    json=${body}")

        code_retunable = "".join(code)
        return code_retunable

    def content_urlencoded(self, curl_input, body_prefix, headers, url):
        body_w_prefix = re.findall(fr"{body_prefix}\s+'([^']+)'", curl_input)
        body_len = len(body_w_prefix)

        code = self.code(url)

        indice = 0
        while indice < len(headers):
            header_value = headers[indice]
            code.append(header_value)
            indice += 1

        code.append('\n    &{data}=    Create Dictionary\n    ')
        indice = 0
        while indice < body_len:
            body = body_w_prefix[indice]
            code.append(f"...    {body}\n    ")
            indice += 1

        code.append("\n    ${response}=    REQUEST On Session    session    /\n    ...    headers=${headers}\n    ...    data=${data}")

        code_retunable = "".join(code)
        return code_retunable

    def no_body_requisition(self, headers, url):
        code = self.code(url)

        indice = 0
        while indice < len(headers):
            header_value = headers[indice]
            code.append(header_value)
            indice += 1
        
        code.append("\n    ${response}=    REQUEST On Session    session    /\n    ...    headers=${headers}")                                                                

        code_retunable = "".join(code)
        return code_retunable