# To start project

```
# To start backend
docker-compose up
# To start requestor app
docker-compose -f docker-compose.requestor.yaml up
```

## Locust result

I've ran backend on gunicorn with 4 workers

```
Type     Name                                                                          # reqs      # fails |    Avg     Min     Max    Med |   req/s  failures/s
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
GET      /api/v1/courses                                                               742993     0(0.00%) |     26       1     375     27 | 1497.81        0.00
--------|----------------------------------------------------------------------------|-------|-------------|-------|-------|-------|-------|--------|-----------
         Aggregated                                                                    742993     0(0.00%) |     26       1     375     27 | 1497.81        0.00

Response time percentiles (approximated)
Type     Name                                                                                  50%    66%    75%    80%    90%    95%    98%    99%  99.9% 99.99%   100% # reqs
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
GET      /api/v1/courses                                                                        27     31     34     37     43     50     60     69    110    250    380 742993
--------|--------------------------------------------------------------------------------|--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated                                                                             27     31     34     37     43     50     60     69    110    250    380 742993
```
