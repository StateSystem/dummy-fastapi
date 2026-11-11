# dummy-fastapi

- 対象 EV: EV028–031。
- 起動: `python -m pip install -r requirements.txt && sh start.sh`
- デフォルト PORT: 3000。環境変数 `PORT` で変更可能。`0.0.0.0` で待受。
- ブランチ: `main` はルートに Dockerfile あり。`no-docker` は Dockerfile のみを削除した同一アプリ。 デフォルトは `main`。

Python は仮想環境を推奨: `python3 -m venv .venv`、`source .venv/bin/activate` の後、上記起動コマンドを実行する。

## 実行環境と API

Python 3.12 を使用する。`GET /` はアプリ名を含む Hello、`GET /health` は HTTP 200 と次の JSON を返す。

```json
{"ok":true,"app":"dummy-fastapi"}
```

ローカル起動後は `http://localhost:3000/health` で確認する。
公開 URL にも同じパスでアクセスできる。ブラウザーや curl で確認可能。
認証、業務 CRUD、seed、CI は含めない。

## DB 設定

指示書 B56 に従い、起動時に `DATABASE_URL` を読み取る。未設定でも Hello / health は起動可能。
DB の作成・マイグレーション・seed・自動 INSERT は実行しない。health はアプリの生存確認であり DB 接続成功を保証しない。
接続 URL やパスワードはレスポンス・ログに出さない。実値は実行環境に注入し、`.env` を Git に追加しない。
`.env.example` は形式説明のみ。値を環境変数へ設定して起動する。

## Docker

main ブランチで以下を実行する。

```sh
docker build -t dummy-fastapi .
docker run --rm -p 3000:3000 dummy-fastapi
```

ポート変更例: `docker run --rm -e PORT=3100 -p 3100:3100 dummy-fastapi`。
DB 設定を注入する場合は設定済み環境変数を `-e DATABASE_URL` で渡す。
no-docker ブランチでは上記のネイティブ起動コマンドを使用する。
DEParture の no-docker 経路は言語によって既知制限があり、失敗・Dockerfile 推奨案内も EV の確認対象。
ローカルで動くことと DEParture 上のデプロイ成功は別途確認する。

## fail-no-dockerfile

このブランチは EV221 用。アプリは `no-docker` と同じで Dockerfile は置かない。
`railway.json` でビルダーを `DOCKERFILE` に固定しているため、DEParture の再デプロイは Dockerfile 不在で失敗する。
`main` と `no-docker` は変更していない。
