# DigiVigi


Project Description:
	DigiVigi is a 'DNIF Open Source' project which simply tries exhibiting a "How To?" process of analyzing real-time data inside DNIF from start to finish.

___________________________ 
# **Tool** 

DNIF - Open Big Data Analytics Platform (Free Forever Version)

________________ 
# **Other Support Tools/ Software**

	- Virtual Box
	- JetBrains: PyCharm Community Edition
	- Ubuntu 16.04 or above
	- Docker
	- Postman
	- AlwaysUp (Trial Version)

____________________ 
# **Project Sketch** 

The execution of project is carried out in two process-phase. 
Its just a procedural way based on the diagram from issue #1

**PROCESS 1: Refer Issue #1**

Stage 1: 
- Select & understand data-set from a domain of interest.

Stage 2: 
- Understand DNIF platform and its capabilities limited to project scope.
- Here's a link to DNIF's complete documentation: https://dnif.it/docs/
	
Stage 3: 
- Get the static data-set inside DNIF platform by following the guidelines mentioned on the website.
- One can use a ready made dataset(json, csv or excel) or create one by scripting it, like writing a web scrapper code.

Stage 4: 
- Perform analytics, create dashboards, build alerts(for which one will have to configure SMTP in their container)
- Here's how to configure SMTP: https://dnif.it/docs/guides/tutorials/configuring-smtp-in-docker.html



_____

**NOTE:Process 1 will ensure you get a good grasp of executing the project on a more fundametal level, before moving on to advanced level.**
_____

**PROCESS 2: Refer Issue #1**

Stage 1:
- Select & understand data-set from a domain of interest. Dataset has to be dynamic this time. Meaning it can update over a period of min(s), hour(s), day(s), week(s) ... The selection should be careful because in a later stage this might count when it comes down to your machine processing speed (CPU, RAM, Disk Space) - -   - Check out the pre-requisites on https://dnif.it/docs/guides/getting-started/prerequisites.html

Stage 2:
- Understand DNIF platform and its capabilities limited to project scope.
- Here's a link to DNIF's complete documentation: https://dnif.it/docs/

Stage 3:
- Fetch the data continuously from the source selected in stage one and store/ update it in a file (ex; mydata.csv)
- For this one can write a code to do so or using an existing one from the repo.
- This file will get updated continuously depending on your scheduler/cron job frequency or any other way of your choice. 

Stage 4:
- The data captured needs to be fed to DNIF for it to be analyzed and played with.
- Use DNIF API which does this job for you and use the existing unified code from the repo - under Process 2 folder; a file called "SourceToDnif.py".

Stage5: 
- Perform analytics, create dashboards, build alerts(for which one will have to configure SMTP in their container)
- Here's how to configure SMTP: https://dnif.it/docs/guides/tutorials/configuring-smtp-in-docker.html

____________________  
# **Diagrammatic Representation**


**Process 1:**

![process_1_dnif](https://user-images.githubusercontent.com/38049677/39574485-0dad9fae-4ef5-11e8-96c9-2aba1e6ff108.png)

**Process 2:**

![process_2_dnif](https://user-images.githubusercontent.com/38049677/39574484-0d74b900-4ef5-11e8-8bdc-adf3f6f50b12.png)

**Additional Credits to: [SOC18-Genesis](https://github.com/dnif/SOC18-genesis/issues/5)**
![39711316-09db6e06-523d-11e8-8975-175ccc03622d](https://user-images.githubusercontent.com/38049677/40010897-c4011714-57c3-11e8-944f-b3523fd58865.png)

____________________
# **Hey! Do you want to stop coming to the repository & get all the project files on your system?**

There's only one thing you'll need to do. Click on the "clone or download" button and get that ZIP file.

THANKS FOR VISITING