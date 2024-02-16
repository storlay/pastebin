FROM postgres:16

ARG POSTGRES_DB

RUN apt-get update \
    && apt-get install -y postgresql-16-cron

RUN mkdir -p /docker-entrypoint-initdb.d

RUN echo "shared_preload_libraries = 'pg_cron'" >> /var/lib/postgresql/data/postgresql.conf \
    && echo "shared_preload_libraries = 'pg_cron'" >> /usr/share/postgresql/postgresql.conf.sample \
    && echo "cron.database_name = '${POSTGRES_DB}'" >> /var/lib/postgresql/data/postgresql.conf \
    && echo "cron.database_name = '${POSTGRES_DB}'" >>  /usr/share/postgresql/postgresql.conf.sample \
    && echo pg_ctl restart  >> /docker-entrypoint-initdb.d/002-setup.sh