# gold-mule

## FXCM Authentication
For the authentication to the services of FXCM copy the *fxcm-template.cfg* and rename it to *fxcm.cfg*. Create a token at the FXCM platform and enter the token to the previously copied file.


## Start
The service can be started using docker compose:

docker-compose up -d

docker exec -it gold-mule bash

python src/prototype_one.py