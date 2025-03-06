{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"pygments_lexer":"ipython3","nbconvert_exporter":"python","version":"3.6.4","file_extension":".py","codemirror_mode":{"name":"ipython","version":3},"name":"python","mimetype":"text/x-python"},"kaggle":{"accelerator":"none","dataSources":[],"isInternetEnabled":true,"language":"python","sourceType":"notebook","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"from fastapi import FastAPI, UploadFile, File, Response\nimport re\n \ndef add_alt_to_img_tags(html_content: str) -> str:\n    # Regex pour détecter les balises <img> avec src mais sans alt=\"image\"\n    img_pattern = re.compile(r'(<img\\s+[^>]*?src=\"[^\"]+\")(?!\\s+alt=\"image\")', re.IGNORECASE)\n    count = 0  # Compteur d'ajouts\n    # Fonction pour ajouter alt=\"image\" immédiatement après src\n    def add_alt(match):\n        nonlocal count\n        count += 1\n        return f'{match.group(1)} alt=\"image\"'\n    # Remplacement\n    updated_content = img_pattern.sub(add_alt, html_content)\n    print(f'Nombre de balises alt ajoutées : {count}')\n    return updated_content\n \n@app.post(\"/add_alt_to_img_tags\")\nasync def add_alt_to_img_tags_endpoint(file: UploadFile = File(...)):\n    content = await file.read()\n    html_content = content.decode(\"utf-8\")\n    updated_content = add_alt_to_img_tags(html_content)\n    return Response(content=updated_content, media_type=file.content_type)","metadata":{"_uuid":"8f2839f25d086af736a60e9eeb907d3b93b6e0e5","_cell_guid":"b1076dfc-b9ad-4769-8c92-a6c4dae69d19","trusted":true},"outputs":[],"execution_count":null}]}