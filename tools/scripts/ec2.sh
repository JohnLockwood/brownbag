stack=brownbag-ec2
file="prod/ec2.yml"

echo deleting stack if it exists:  "${stack}"
aws cloudformation delete-stack --stack-name "${stack}"

echo waiting for stack to be deleted
aws cloudformation wait stack-delete-complete --stack-name "${stack}"

echo creating stack
./upsert_stack.sh "${stack}" "${file}" --capabilities CAPABILITY_IAM

