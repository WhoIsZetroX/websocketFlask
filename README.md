# websocketFlask
How to use websockets with flask python

1. Rename the .env.example file and edit with the config you prefer 
   ```shell
   cp .env.example .env
   ```
   
2. Create python env
   ```shell
   python3 -m venv my_env
   ```
   
3. Install required packages for python
   ```shell
   # Linux
   my_env/bin/python -m pip install -r requirements.txt
   
   # Windows
   my_env/Scripts/python.exe -m pip install -r requirements.txt
   ```

4. Run main script with the virtual env
   ```shell
   # Linux
   my_env/bin/python server.py
   
   # Windows
   my_env/Scripts/python.exe server.py
   ```