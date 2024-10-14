from prowler.lib.check.models import Check, Check_Report_AWS
from prowler.providers.aws.services.opensearch.opensearch_client import (
    opensearch_client,
)


class opensearch_domain_master_nodes_fault_tolerant(Check):
    def execute(self):
        findings = []
        for domain in opensearch_client.opensearch_domains:
            if getattr(domain, "dedicated_master_enabled", False):
                report = Check_Report_AWS(self.metadata())
                report.resource_id = domain.name
                report.resource_arn = domain.arn
                report.region = domain.region
                report.resource_tags = domain.tags
                report.status = "PASS"
                report.status_extended = f"Opensearch domain {domain.name} has {domain.dedicated_master_count} dedicated master nodes, which guarantees fault tolerance on the master nodes."

                if domain.dedicated_master_count < 3:
                    report.status = "FAIL"
                    report.status_extended = f"Opensearch domain {domain.name} does not have at least 3 dedicated master nodes."

                findings.append(report)

        return findings
