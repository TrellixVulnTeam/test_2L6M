"# test" 

https://stackoverflow.com/questions/66720501/how-to-update-openssl-on-centos-7

https://www.tutorialspoint.com/elasticsearch/elasticsearch_migrations_between_versions.htm

https://www.elastic.co/guide/en/elastic-stack/6.8/upgrading-elastic-stack.html


・（重）修正箇所の画面と操作の記述
・（重）修正箇所のアウトライン図を記述
・詳細設計書レビュー指摘対応
・型定義を外してテスト
・テスト仕様書作成（機能）
・テスト仕様書作成（パフォーマンス）
・パフォーマンステスト観点洗い出し
・コードレビュー時間調整
・コードレビュー実施
・コードレビュー修正
・静的解析
・カバレッジ
・リソースチェック


・カバレッジ取り方
　→ coverage run manage.py runserver --noreload
　traceモジュールは使えるか？
・リスケ計画
・buf監視処理検討
・何の機能かわからないものを確認
・日付範囲追加してよいのかわからない部分の確認
　→ 確認中だが、多分追加してよい
・システム設定値を登録しない方法を検討
　→ writeする箇所でwriteしないようにする
　　 PostgresSQL削除処理なんのためにある？





coverage run manage.py runserver --noreload
coverage run --append test.py
coverage html
coverage combine
coverage run --parallel-mode test.py
