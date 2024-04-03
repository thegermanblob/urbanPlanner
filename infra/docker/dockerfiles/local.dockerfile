FROM python:3.10-bullseye
RUN pip install openai
EXPOSE 8000
WORKDIR /appsrc

ENTRYPOINT ["./infra/local.entrypoint.sh"]