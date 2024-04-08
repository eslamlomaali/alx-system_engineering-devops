postmortem
Learning how to write an Incident Report, also referred to as a Postmortem. This postmortem follows the guidelines used closely by google engineers to file reports. The report is made up of five parts, an issue summary, a timeline, root cause analysis, resolution and recovery, and lastly, corrective and preventative measures. Lets review each of these parts in detail.
Issue Summary:
Duration: April 6, 2024, 10:00 AM — April 7, 2024, 2:00 PM (UTC)
Impact: The online payment service was unavailable for approximately 28 hours, affecting all users. Users experienced errors and were unable to complete transactions during this period.
Root Cause:
The root cause of the issue was a database failure due to a hardware malfunction. One of the storage disks in the database cluster failed, leading to data corruption and an inability to process user transactions.
Timeline:
April 6, 2024, 10:00 AM (UTC): The issue was detected when monitoring systems reported a sudden increase in error rates and a loss of connectivity to the database cluster.
Actions taken: The operations team initiated an investigation to identify the cause of the issue. They focused on the database cluster and reviewed system logs for any potential errors or anomalies.
Misleading investigation/debugging paths: Initially, the team suspected a network issue, as the loss of connectivity pointed towards a possible network misconfiguration. However, further analysis revealed that the network configuration was sound, leading them to investigate the database cluster.
The incident was escalated to the database administration team and the vendor support for the database technology.
April 6, 2024, 4:00 PM (UTC): The root cause was identified as a failed storage disk in the database cluster, causing data corruption and rendering the database inaccessible.
April 6–7, 2024: The database administration team worked with the vendor support to replace the faulty disk and restore the database from the most recent backup.
April 7, 2024, 2:00 PM (UTC): The issue was resolved, and the online payment service was restored to full functionality.
Root Cause and Resolution:
The root cause of the issue was a hardware malfunction, specifically a failed storage disk in the database cluster. The failure resulted in data corruption and prevented the processing of user transactions. To resolve the issue, the faulty disk was replaced, and the database was restored from the most recent backup. This ensured data integrity and allowed the online payment service to resume normal operation.
Corrective and Preventative Measures:
Implement redundant storage solutions: To mitigate the impact of hardware failures, redundancy should be introduced at the storage level, such as using RAID configurations or distributed storage systems.
Enhance monitoring capabilities: Improve the monitoring system to provide early detection of disk failures and other critical hardware issues. This includes setting up alerts for abnormal disk behavior and implementing regular health checks.
Conduct regular hardware maintenance: Establish a preventive maintenance schedule to proactively identify and replace aging or potentially faulty hardware components before they cause service disruptions.
Strengthen disaster recovery procedures: Review and enhance the existing backup and restore procedures to minimize downtime and data loss in the event of similar incidents. Regularly test the recovery process to ensure its effectiveness.
Perform post-incident review: Conduct a thorough review of the incident response and resolution process to identify areas for improvement. Document any lessons learned and share them with relevant teams to enhance their incident management capabilities.
Tasks to Address the Issue:
Replace the faulty storage disk in the database cluster.
Verify and validate the integrity of the restored database.
Update the monitoring system to include disk health checks and alerts.
Review and update the disaster recovery procedures based on lessons learned.
Conduct training and knowledge sharing sessions with the operations team to enhance incident response capabilities.
By implementing these corrective and preventative measures, the company aims to strengthen the resilience of its online payment service and minimize the likelihood and impact of similar incidents in the future.

