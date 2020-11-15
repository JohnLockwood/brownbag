aws cloudformation delete-stack --stack-name prod-brownbag
./scripts/upsert_stack.sh prod-brownbag prod/db.yml --capabilities CAPABILITY_AUTO_EXPAND
