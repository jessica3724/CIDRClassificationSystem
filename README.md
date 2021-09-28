# CIDRClassificationSystem
> CIDR classification analysis system (Demo)

## Getting start
 - Python 3.8.10
---
## Install
```shell
git clone https://github.com/jessica3724/CIDRClassificationSystem.git
cd CIDRClassificationSystem
pip install -r requirements.txt
```
## Start project
```
python manage.py runserver 127.0.0.1:8080
``` 
---
### API 
#### `A_group/{IP}`
#### [GET]
- Request
    ```shell
    curl http://127.0.0.1:8080/A_group/{IP}
    ```

- Response
    ```
    # if IP is in A_group, then return "{org}".
    org
    # if IP isn't in A_group, then return "None".
    None
    ```

#### `B_group/{IP}`
##### [GET]
- Request
    ```shell
    curl http://127.0.0.1:8080/B_group/{IP}
    ```
- Response
    ```
    # if IP is in B_group, then return "{org}".
    org
    # if IP isn't in B_group, then return "None".
    None
    ```
