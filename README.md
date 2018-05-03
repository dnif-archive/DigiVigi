# DigiVigi
________________________________________________________________

Project Description:
	DigiVigi is a 'DNIF Open Source' project which simply tries exhibiting a "How To?" process of analyzing real-time data inside DNIF from start to finish.

__________________________ Product ______________________________

Product in Use: DNIF - Open Big Data Analytics Platform (Free Forever Version)

________________ Other Support Tools/ Software ________________

	- Virtual Box
	- JetBrains: PyCharm Community Edition
	- Ubuntu 16.04 or above
	- Docker

____________________ Project Sketch ________________________

The project execution is carried out in two process-phase. Its just a procedural way based on the diagram from issue #1

PROCESS 1: Refer Issue #1

Stage 1: 
- Select & understand data-set from a domain of interest.

Stage 2: 
- Understand DNIF platform and its capabilities limited to project scope.
- Here's a link to DNIF's complete documentation: https://dnif.it/docs/
	
Stage 3: 
- Get the static data-set inside DNIF platform by following the guidelines mentioned on the website.
- One can use a ready made dataset(json, csv or excel) or create one by scripting it.

Stage 4: 
- Perform analytics, create dashboards, build alerts(for which one will have to configure SMTP in their container)
- Here's how to configure SMTP: https://dnif.it/docs/guides/tutorials/configuring-smtp-in-docker.html

_____

NOTE:Process 1 will ensure you get a good grasp of executing the project on a more fundametal level, before moving on to advanced level.
_____


PROCESS 2: Refer Issue #1

Stage 1:
- Select & understand data-set from a domain of interest. Dataset has to be dynamic this time. Meaning it can update over a period of min(s), hour(s), day(s), week(s) ... This selection should be careful as in later stage this might count when it comes down to your machines processing speed (CPU, RAM, Disk Space) Check out the pre-requisites on https://dnif.it/docs/guides/getting-started/prerequisites.html

Stage 2:
- Understand DNIF platform and its capabilities limited to project scope.
- Here's a link to DNIF's complete documentation: https://dnif.it/docs/

Stage 3:
- Fetch the data continuously from the source selected in stage one and store/ update it in a file (ex; mydata.csv)
- This file will get updated continuously depending on your scheduler/cron job frequency. 
- For this one can write a code to do so or using an existing one from the repo.

Stage 4:
- The data captured needs to be fed to DNIF for it to be analyzed and played with.
- Write a connector/ API which does this job for you. Or use the existing one from the repo.

Stage5: 
- Perform analytics, create dashboards, build alerts(for which one will have to configure SMTP in their container)
- Here's how to configure SMTP: https://dnif.it/docs/guides/tutorials/configuring-smtp-in-docker.html
________________________________________________________________