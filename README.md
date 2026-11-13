# dummy-fastapi

`main` は FastAPI です。このブランチ `ev216` だけ Django です。

EV216 用です。`GET /` は未ログインなら `logged-out`、ログイン後は `logged-in:tester` です。ログインは `GET /login` です。セッションは `SECRET_KEY` で署名します。`SECRET_KEY` と `ALLOWED_HOSTS` はリポジトリに書きません。
