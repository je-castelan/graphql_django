FROM python:3.7-alpine
LABEL AUTHOR Jose Emanuel Castelan

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt

#Removing jpeg-dev, musl-dev zlib zlib-dev (not using images at this moment)
#RUN apk add --update --no-cache postgresql-client jpeg-dev
#RUN apk add --update --no-cache --virtual .tmp-build-deps \
#	gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
#RUN pip install -r /requirements.txt
#RUN apk del .tmp-build-deps
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
	gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /src
WORKDIR /src
COPY ./src/ /src

# Create media and static directories (not in use)
# RUN mkdir -p /vol/web/media
# RUN mkdir -p /vol/web/static

# Create new user
RUN adduser -D user

#New user will have assigned new directories (not in use)
#RUN chown -R user:user /vol/
#RUN chmod -R 755 /vol/web
USER user