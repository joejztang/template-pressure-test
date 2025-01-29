# template for pressure test

This is a complex tool for pressure / performance testing. It comes up with 3 containers that are important:

1. k6 containers.
2. prometheus container.
3. grafana container.

### k6 container

k6 container will contain tests. Some basic tests will be available in `simple_tests` in current skeleton. Modify tests in that folder will work for some simple tests. Folder name is changable of course if you modify accordingly in `docker-compose.yml` as well.

### prometheus container

Initially, k6 doesn't support prometheus as data source, while recently grafana introduces [xk6-output-prometheus-remote](https://github.com/grafana/xk6-output-prometheus-remote) made it possible.

### grafana container

grafana container helps to show dashboard.

## how to use this skeleton to test your service

You will build your service somewhere else and make it runnable first. Ideally you have a docker compose file that instruct how to run the services. Copy that block into `docker-compose.yml` in this repo and modify accordingly to make it right. There can be back and forth. After finish modifying, start the whole services to see the test results.

## entrypoint

`docker compose up`

In NON-detached way, you can see some helpful logs.

## localhost quick access index

* prometheus: localhost:9000
* grafana: localhost:4000

## grafana dashboard

Initially there is no grafana dashboard available in the pod. User will need to build dashboard according their own usecases.

## Reference

* https://medium.com/@rody.bothe/turning-data-into-understandable-insights-with-k6-load-testing-fa24e326e221
* https://community.grafana.com/t/unable-to-send-the-metric-to-prometheus/98914