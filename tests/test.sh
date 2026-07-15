# #!/bin/bash

# # pytest is baked into the environment image (environment/Dockerfile).
# pytest /tests/test_outputs.py -rA

# if [ $? -eq 0 ]; then
#   echo 1 > /app/reward.txt
# else
#   echo 0 > /app/reward.txt
# fi

#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py -rA --ctrf /logs/verifier/ctrf.json
status=$?

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi

exit 0