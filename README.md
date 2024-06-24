# clothes-outfit


## How to launch Backend
1. git clone this repo.
2. docker compose up -d
3. need to extract from other data source , before invoking api
   1. entering container virtuak env.
   2. `cd backend`
   3. `docker exec -it container_id bash`
   4. `python3 scrapy.py` , maybe wait for 20 minutes

## look api `http://localhost:8080/api/images`
after launching `docker comppose`, you could open browser, enter `http://localhost:8080/docs` more detail. 


## How to launch App
1. cd `frontend/app` and npm i
2. `npm run build` to generate `dist/`
3. docker compose up -d 
