aws lambda invoke \
--invocation-type RequestResponse \
--function-name UrlCopy \
--region us-east-1 \
--log-type Tail \
--payload '{ "url": "https://ftp.ncbi.nlm.nih.gov/README.ftp", "bucket": "omics_metadata", "key": "README.ftp" }' \
outputfile.txt
