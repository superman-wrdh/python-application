fileName=log"-"$(date +%Y%m%d%H%M)".log"
app=app.py
nohup python3 -u $app >$fileName 2>&1 &
echo "Started app"

