FROM python:3.10

RUN apt update \
    && apt install libpq-dev -y

COPY bff_requirements.txt ./requirements.txt
RUN pip install --upgrade --no-cache-dir pip setuptools wheel
RUN pip install --no-cache-dir wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/app/src"
CMD [ "uvicorn", "src.bff_gql.main:app", "--host", "0.0.0.0", "--port", "8000" ]