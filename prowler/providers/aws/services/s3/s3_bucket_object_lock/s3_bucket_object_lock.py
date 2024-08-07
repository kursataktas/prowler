from prowler.lib.check.models import Check, Check_Report_AWS
from prowler.providers.aws.services.s3.s3_client import s3_client
import importlib
import sys
import gc 

class s3_bucket_object_lock(Check):
    def execute(self):
        findings = []
        for bucket in s3_client.buckets:
            report = Check_Report_AWS(self.metadata())
            report.region = bucket.region
            report.resource_id = bucket.name
            report.resource_arn = bucket.arn
            report.resource_tags = bucket.tags
            if bucket.object_lock:
                report.status = "PASS"
                report.status_extended = (
                    f"S3 Bucket {bucket.name} has Object Lock enabled."
                )
            else:
                report.status = "FAIL"
                report.status_extended = (
                    f"S3 Bucket {bucket.name} has Object Lock disabled."
                )
            findings.append(report)

        
        del sys.modules['prowler.providers.aws.services.s3.s3_client']
        gc.collect()
        return findings
